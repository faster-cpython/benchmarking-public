
# Results vs. base

- fork: brandtbucher
- ref: un_materialize
- machine: linux-x86_64
- commit hash: a4e456f
- commit date: 2023-06-22
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230622-linux-x86_64-python-13237a2da846efef9ce9-3.13.0a0-13237a2 | bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 2.62 sec                                                              | 2.67 sec: 1.02x slower                                                |
| tornado_http   | 95.6 ms                                                               | 96.8 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230622-linux-x86_64-python-13237a2da846efef9ce9-3.13.0a0-13237a2 | bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 197 ms                                                                | 192 ms: 1.03x faster                                                  |
| nbody          | 88.1 ms                                                               | 92.8 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230622-linux-x86_64-python-13237a2da846efef9ce9-3.13.0a0-13237a2 | bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 208 ms                                                                | 203 ms: 1.02x faster                                                  |
| regex_v8       | 22.0 ms                                                               | 21.9 ms: 1.01x faster                                                 |
| regex_compile  | 134 ms                                                                | 135 ms: 1.01x slower                                                  |
| regex_effbot   | 3.46 ms                                                               | 3.50 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230622-linux-x86_64-python-13237a2da846efef9ce9-3.13.0a0-13237a2 | bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_list          | 4.66 us                                                               | 4.50 us: 1.04x faster                                                 |
| pickle_pure_python   | 310 us                                                                | 311 us: 1.00x slower                                                  |
| unpickle_pure_python | 213 us                                                                | 214 us: 1.01x slower                                                  |
| pickle               | 10.6 us                                                               | 10.7 us: 1.01x slower                                                 |
| xml_etree_parse      | 153 ms                                                                | 155 ms: 1.01x slower                                                  |
| xml_etree_generate   | 84.1 ms                                                               | 85.2 ms: 1.01x slower                                                 |
| json_dumps           | 9.72 ms                                                               | 9.86 ms: 1.01x slower                                                 |
| unpickle             | 15.0 us                                                               | 15.3 us: 1.02x slower                                                 |
| pickle_dict          | 30.7 us                                                               | 31.2 us: 1.02x slower                                                 |
| xml_etree_process    | 57.6 ms                                                               | 58.7 ms: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (4): json_loads, unpickle_list, xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230622-linux-x86_64-python-13237a2da846efef9ce9-3.13.0a0-13237a2 | bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 9.19 ms                                                               | 9.17 ms: 1.00x faster                                                 |
| python_startup_no_site | 6.68 ms                                                               | 6.67 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20230622-linux-x86_64-python-13237a2da846efef9ce9-3.13.0a0-13237a2 | bm-20230622-linux-x86_64-brandtbucher-un_materialize-3.13.0a0-a4e456f |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                      | 2.69 sec                                                              | 2.53 sec: 1.06x faster                                                |
| unpack_sequence          | 44.2 ns                                                               | 41.8 ns: 1.06x faster                                                 |
| pickle_list              | 4.66 us                                                               | 4.50 us: 1.04x faster                                                 |
| generators               | 30.2 ms                                                               | 29.3 ms: 1.03x faster                                                 |
| pidigits                 | 197 ms                                                                | 192 ms: 1.03x faster                                                  |
| regex_dna                | 208 ms                                                                | 203 ms: 1.02x faster                                                  |
| logging_simple           | 6.01 us                                                               | 5.93 us: 1.01x faster                                                 |
| nqueens                  | 80.5 ms                                                               | 79.5 ms: 1.01x faster                                                 |
| logging_format           | 6.54 us                                                               | 6.49 us: 1.01x faster                                                 |
| async_generators         | 450 ms                                                                | 447 ms: 1.01x faster                                                  |
| sqlglot_normalize        | 106 ms                                                                | 105 ms: 1.01x faster                                                  |
| regex_v8                 | 22.0 ms                                                               | 21.9 ms: 1.01x faster                                                 |
| sqlglot_optimize         | 52.7 ms                                                               | 52.4 ms: 1.00x faster                                                 |
| python_startup           | 9.19 ms                                                               | 9.17 ms: 1.00x faster                                                 |
| python_startup_no_site   | 6.68 ms                                                               | 6.67 ms: 1.00x faster                                                 |
| create_gc_cycles         | 1.51 ms                                                               | 1.51 ms: 1.00x slower                                                 |
| pickle_pure_python       | 310 us                                                                | 311 us: 1.00x slower                                                  |
| asyncio_tcp_ssl          | 1.78 sec                                                              | 1.79 sec: 1.00x slower                                                |
| asyncio_tcp              | 511 ms                                                                | 513 ms: 1.00x slower                                                  |
| regex_compile            | 134 ms                                                                | 135 ms: 1.01x slower                                                  |
| mypy2                    | 335 ms                                                                | 337 ms: 1.01x slower                                                  |
| unpickle_pure_python     | 213 us                                                                | 214 us: 1.01x slower                                                  |
| deepcopy                 | 348 us                                                                | 351 us: 1.01x slower                                                  |
| scimark_sparse_mat_mult  | 4.52 ms                                                               | 4.55 ms: 1.01x slower                                                 |
| go                       | 135 ms                                                                | 136 ms: 1.01x slower                                                  |
| pprint_safe_repr         | 716 ms                                                                | 721 ms: 1.01x slower                                                  |
| dulwich_log              | 65.5 ms                                                               | 66.0 ms: 1.01x slower                                                 |
| bench_thread_pool        | 816 us                                                                | 822 us: 1.01x slower                                                  |
| deltablue                | 3.25 ms                                                               | 3.28 ms: 1.01x slower                                                 |
| deepcopy_memo            | 37.3 us                                                               | 37.6 us: 1.01x slower                                                 |
| scimark_fft              | 348 ms                                                                | 351 ms: 1.01x slower                                                  |
| meteor_contest           | 105 ms                                                                | 106 ms: 1.01x slower                                                  |
| pprint_pformat           | 1.46 sec                                                              | 1.47 sec: 1.01x slower                                                |
| async_tree_memoization   | 583 ms                                                                | 589 ms: 1.01x slower                                                  |
| pyflate                  | 443 ms                                                                | 448 ms: 1.01x slower                                                  |
| async_tree_none          | 477 ms                                                                | 482 ms: 1.01x slower                                                  |
| regex_effbot             | 3.46 ms                                                               | 3.50 ms: 1.01x slower                                                 |
| chaos                    | 58.3 ms                                                               | 58.9 ms: 1.01x slower                                                 |
| async_tree_io            | 1.18 sec                                                              | 1.20 sec: 1.01x slower                                                |
| tornado_http             | 95.6 ms                                                               | 96.8 ms: 1.01x slower                                                 |
| pickle                   | 10.6 us                                                               | 10.7 us: 1.01x slower                                                 |
| xml_etree_parse          | 153 ms                                                                | 155 ms: 1.01x slower                                                  |
| xml_etree_generate       | 84.1 ms                                                               | 85.2 ms: 1.01x slower                                                 |
| json_dumps               | 9.72 ms                                                               | 9.86 ms: 1.01x slower                                                 |
| hexiom                   | 6.03 ms                                                               | 6.12 ms: 1.02x slower                                                 |
| unpickle                 | 15.0 us                                                               | 15.3 us: 1.02x slower                                                 |
| pickle_dict              | 30.7 us                                                               | 31.2 us: 1.02x slower                                                 |
| comprehensions           | 20.4 us                                                               | 20.7 us: 1.02x slower                                                 |
| docutils                 | 2.62 sec                                                              | 2.67 sec: 1.02x slower                                                |
| fannkuch                 | 391 ms                                                                | 398 ms: 1.02x slower                                                  |
| xml_etree_process        | 57.6 ms                                                               | 58.7 ms: 1.02x slower                                                 |
| coroutines               | 21.8 ms                                                               | 22.2 ms: 1.02x slower                                                 |
| telco                    | 6.74 ms                                                               | 6.88 ms: 1.02x slower                                                 |
| deepcopy_reduce          | 3.10 us                                                               | 3.17 us: 1.02x slower                                                 |
| spectral_norm            | 102 ms                                                                | 104 ms: 1.02x slower                                                  |
| raytrace                 | 267 ms                                                                | 273 ms: 1.02x slower                                                  |
| richards_super           | 50.1 ms                                                               | 51.7 ms: 1.03x slower                                                 |
| logging_silent           | 96.1 ns                                                               | 100 ns: 1.04x slower                                                  |
| richards                 | 43.7 ms                                                               | 45.6 ms: 1.04x slower                                                 |
| typing_runtime_protocols | 143 us                                                                | 150 us: 1.04x slower                                                  |
| nbody                    | 88.1 ms                                                               | 92.8 ms: 1.05x slower                                                 |
| gc_traversal             | 3.61 ms                                                               | 4.31 ms: 1.19x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (20): json_loads, json, float, unpickle_list, coverage, pycparser, scimark_monte_carlo, pathlib, mako, sqlglot_transpile, scimark_lu, bench_mp_pool, sqlite_synth, scimark_sor, dask, xml_etree_iterparse, sqlglot_parse, crypto_pyaes, tomli_loads, async_tree_cpu_io_mixed
