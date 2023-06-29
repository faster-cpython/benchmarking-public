
# Results vs. base

- fork: brandtbucher
- ref: un_materialize
- machine: linux-x86_64
- commit hash: c5f2067
- commit date: 2023-06-29
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230629-linux-x86_64-python-3c70d467c148875f2ce1-3.13.0a0-3c70d46 | bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 197 ms                                                                | 197 ms: 1.00x slower                                                  |
| nbody          | 87.8 ms                                                               | 90.2 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230629-linux-x86_64-python-3c70d467c148875f2ce1-3.13.0a0-3c70d46 | bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.60 ms                                                               | 3.51 ms: 1.03x faster                                                 |
| regex_dna      | 208 ms                                                                | 207 ms: 1.01x faster                                                  |
| regex_v8       | 21.9 ms                                                               | 22.1 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230629-linux-x86_64-python-3c70d467c148875f2ce1-3.13.0a0-3c70d46 | bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_dict          | 31.8 us                                                               | 31.0 us: 1.03x faster                                                 |
| tomli_loads          | 2.23 sec                                                              | 2.19 sec: 1.02x faster                                                |
| xml_etree_iterparse  | 104 ms                                                                | 102 ms: 1.01x faster                                                  |
| json_loads           | 25.8 us                                                               | 25.5 us: 1.01x faster                                                 |
| unpickle_pure_python | 214 us                                                                | 212 us: 1.01x faster                                                  |
| pickle_pure_python   | 309 us                                                                | 306 us: 1.01x faster                                                  |
| xml_etree_generate   | 83.4 ms                                                               | 82.8 ms: 1.01x faster                                                 |
| pickle               | 10.8 us                                                               | 10.8 us: 1.01x faster                                                 |
| xml_etree_process    | 57.3 ms                                                               | 57.1 ms: 1.00x faster                                                 |
| unpickle_list        | 4.90 us                                                               | 4.93 us: 1.01x slower                                                 |
| xml_etree_parse      | 152 ms                                                                | 153 ms: 1.01x slower                                                  |
| pickle_list          | 4.46 us                                                               | 4.75 us: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (2): json_dumps, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230629-linux-x86_64-python-3c70d467c148875f2ce1-3.13.0a0-3c70d46 | bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.65 ms                                                               | 6.70 ms: 1.01x slower                                                 |
| python_startup         | 9.15 ms                                                               | 9.24 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230629-linux-x86_64-python-3c70d467c148875f2ce1-3.13.0a0-3c70d46 | bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067 |
|-----------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako      | 10.7 ms                                                               | 10.5 ms: 1.02x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20230629-linux-x86_64-python-3c70d467c148875f2ce1-3.13.0a0-3c70d46 | bm-20230629-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-c5f2067 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| scimark_sparse_mat_mult  | 4.78 ms                                                               | 4.57 ms: 1.05x faster                                                 |
| gc_traversal             | 4.06 ms                                                               | 3.91 ms: 1.04x faster                                                 |
| coroutines               | 23.2 ms                                                               | 22.5 ms: 1.03x faster                                                 |
| async_generators         | 450 ms                                                                | 437 ms: 1.03x faster                                                  |
| regex_effbot             | 3.60 ms                                                               | 3.51 ms: 1.03x faster                                                 |
| pickle_dict              | 31.8 us                                                               | 31.0 us: 1.03x faster                                                 |
| logging_silent           | 100 ns                                                                | 97.7 ns: 1.02x faster                                                 |
| logging_format           | 6.52 us                                                               | 6.39 us: 1.02x faster                                                 |
| mako                     | 10.7 ms                                                               | 10.5 ms: 1.02x faster                                                 |
| tomli_loads              | 2.23 sec                                                              | 2.19 sec: 1.02x faster                                                |
| scimark_sor              | 121 ms                                                                | 119 ms: 1.02x faster                                                  |
| json                     | 4.93 ms                                                               | 4.85 ms: 1.02x faster                                                 |
| logging_simple           | 6.01 us                                                               | 5.93 us: 1.01x faster                                                 |
| sqlglot_transpile        | 1.63 ms                                                               | 1.60 ms: 1.01x faster                                                 |
| sqlglot_parse            | 1.31 ms                                                               | 1.29 ms: 1.01x faster                                                 |
| xml_etree_iterparse      | 104 ms                                                                | 102 ms: 1.01x faster                                                  |
| dask                     | 518 ms                                                                | 512 ms: 1.01x faster                                                  |
| pprint_pformat           | 1.47 sec                                                              | 1.45 sec: 1.01x faster                                                |
| json_loads               | 25.8 us                                                               | 25.5 us: 1.01x faster                                                 |
| unpickle_pure_python     | 214 us                                                                | 212 us: 1.01x faster                                                  |
| nqueens                  | 80.9 ms                                                               | 80.1 ms: 1.01x faster                                                 |
| richards                 | 44.2 ms                                                               | 43.8 ms: 1.01x faster                                                 |
| pickle_pure_python       | 309 us                                                                | 306 us: 1.01x faster                                                  |
| xml_etree_generate       | 83.4 ms                                                               | 82.8 ms: 1.01x faster                                                 |
| go                       | 137 ms                                                                | 136 ms: 1.01x faster                                                  |
| scimark_fft              | 361 ms                                                                | 358 ms: 1.01x faster                                                  |
| meteor_contest           | 104 ms                                                                | 103 ms: 1.01x faster                                                  |
| pprint_safe_repr         | 716 ms                                                                | 711 ms: 1.01x faster                                                  |
| hexiom                   | 6.05 ms                                                               | 6.01 ms: 1.01x faster                                                 |
| pickle                   | 10.8 us                                                               | 10.8 us: 1.01x faster                                                 |
| regex_dna                | 208 ms                                                                | 207 ms: 1.01x faster                                                  |
| bench_thread_pool        | 817 us                                                                | 814 us: 1.00x faster                                                  |
| crypto_pyaes             | 76.3 ms                                                               | 76.0 ms: 1.00x faster                                                 |
| xml_etree_process        | 57.3 ms                                                               | 57.1 ms: 1.00x faster                                                 |
| dulwich_log              | 65.6 ms                                                               | 65.4 ms: 1.00x faster                                                 |
| pidigits                 | 197 ms                                                                | 197 ms: 1.00x slower                                                  |
| asyncio_tcp              | 505 ms                                                                | 508 ms: 1.01x slower                                                  |
| unpickle_list            | 4.90 us                                                               | 4.93 us: 1.01x slower                                                 |
| python_startup_no_site   | 6.65 ms                                                               | 6.70 ms: 1.01x slower                                                 |
| regex_v8                 | 21.9 ms                                                               | 22.1 ms: 1.01x slower                                                 |
| xml_etree_parse          | 152 ms                                                                | 153 ms: 1.01x slower                                                  |
| python_startup           | 9.15 ms                                                               | 9.24 ms: 1.01x slower                                                 |
| async_tree_io            | 1.18 sec                                                              | 1.20 sec: 1.01x slower                                                |
| deepcopy_reduce          | 3.15 us                                                               | 3.18 us: 1.01x slower                                                 |
| pyflate                  | 442 ms                                                                | 448 ms: 1.01x slower                                                  |
| chaos                    | 58.1 ms                                                               | 59.0 ms: 1.02x slower                                                 |
| create_gc_cycles         | 1.49 ms                                                               | 1.52 ms: 1.02x slower                                                 |
| typing_runtime_protocols | 140 us                                                                | 142 us: 1.02x slower                                                  |
| deepcopy                 | 348 us                                                                | 355 us: 1.02x slower                                                  |
| pathlib                  | 18.9 ms                                                               | 19.3 ms: 1.02x slower                                                 |
| raytrace                 | 266 ms                                                                | 273 ms: 1.02x slower                                                  |
| comprehensions           | 20.2 us                                                               | 20.7 us: 1.03x slower                                                 |
| nbody                    | 87.8 ms                                                               | 90.2 ms: 1.03x slower                                                 |
| telco                    | 7.11 ms                                                               | 7.31 ms: 1.03x slower                                                 |
| mdp                      | 2.55 sec                                                              | 2.70 sec: 1.06x slower                                                |
| pickle_list              | 4.46 us                                                               | 4.75 us: 1.07x slower                                                 |
| unpack_sequence          | 43.1 ns                                                               | 47.9 ns: 1.11x slower                                                 |
| mypy2                    | 336 ms                                                                | 454 ms: 1.35x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (24): richards_super, deltablue, spectral_norm, deepcopy_memo, scimark_lu, scimark_monte_carlo, regex_compile, async_tree_none, sqlite_synth, pycparser, fannkuch, asyncio_tcp_ssl, bench_mp_pool, json_dumps, async_tree_memoization, docutils, coverage, float, sqlglot_optimize, sqlglot_normalize, async_tree_cpu_io_mixed, tornado_http, generators, unpickle
