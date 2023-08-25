
# Results vs. base

- fork: brandtbucher
- ref: un_materialize_alt
- machine: linux-x86_64
- commit hash: 25202d9
- commit date: 2023-07-16
- overall geometric mean: 1.00x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230716-linux-x86_64-python-main-3.13.0a0-8c17729 | bm-20230716-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9 |
|----------------|:-----------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.65 sec                                              | 2.66 sec: 1.00x slower                                                    |
| Geometric mean | (ref)                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230716-linux-x86_64-python-main-3.13.0a0-8c17729 | bm-20230716-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9 |
|----------------|:-----------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 80.7 ms                                               | 79.1 ms: 1.02x faster                                                     |
| pidigits       | 196 ms                                                | 198 ms: 1.01x slower                                                      |
| nbody          | 89.3 ms                                               | 93.8 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                 | 1.01x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230716-linux-x86_64-python-main-3.13.0a0-8c17729 | bm-20230716-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9 |
|----------------|:-----------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                               | 3.52 ms: 1.04x faster                                                     |
| regex_v8       | 22.3 ms                                               | 22.1 ms: 1.01x faster                                                     |
| regex_compile  | 138 ms                                                | 137 ms: 1.01x faster                                                      |
| regex_dna      | 207 ms                                                | 214 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                 | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230716-linux-x86_64-python-main-3.13.0a0-8c17729 | bm-20230716-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9 |
|----------------------|:-----------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_list        | 5.14 us                                               | 4.95 us: 1.04x faster                                                     |
| json_loads           | 26.1 us                                               | 25.5 us: 1.03x faster                                                     |
| pickle_list          | 4.70 us                                               | 4.59 us: 1.02x faster                                                     |
| xml_etree_generate   | 84.6 ms                                               | 83.1 ms: 1.02x faster                                                     |
| xml_etree_process    | 58.5 ms                                               | 57.5 ms: 1.02x faster                                                     |
| unpickle_pure_python | 214 us                                                | 211 us: 1.01x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                | 102 ms: 1.01x faster                                                      |
| xml_etree_parse      | 154 ms                                                | 153 ms: 1.01x faster                                                      |
| pickle_pure_python   | 298 us                                                | 296 us: 1.01x faster                                                      |
| tomli_loads          | 2.33 sec                                              | 2.32 sec: 1.01x faster                                                    |
| pickle               | 10.6 us                                               | 10.6 us: 1.01x slower                                                     |
| pickle_dict          | 31.7 us                                               | 32.5 us: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (2): json_dumps, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230716-linux-x86_64-python-main-3.13.0a0-8c17729 | bm-20230716-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9 |
|------------------------|:-----------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 9.25 ms                                               | 9.18 ms: 1.01x faster                                                     |
| python_startup_no_site | 6.71 ms                                               | 6.67 ms: 1.01x faster                                                     |
| Geometric mean         | (ref)                                                 | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230716-linux-x86_64-python-main-3.13.0a0-8c17729 | bm-20230716-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9 |
|-----------|:-----------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.9 ms                                               | 10.7 ms: 1.02x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20230716-linux-x86_64-python-main-3.13.0a0-8c17729 | bm-20230716-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-25202d9 |
|--------------------------|:-----------------------------------------------------:|:-------------------------------------------------------------------------:|
| spectral_norm            | 109 ms                                                | 103 ms: 1.05x faster                                                      |
| typing_runtime_protocols | 148 us                                                | 141 us: 1.05x faster                                                      |
| regex_effbot             | 3.67 ms                                               | 3.52 ms: 1.04x faster                                                     |
| unpickle_list            | 5.14 us                                               | 4.95 us: 1.04x faster                                                     |
| crypto_pyaes             | 71.1 ms                                               | 69.3 ms: 1.03x faster                                                     |
| json_loads               | 26.1 us                                               | 25.5 us: 1.03x faster                                                     |
| pickle_list              | 4.70 us                                               | 4.59 us: 1.02x faster                                                     |
| create_gc_cycles         | 1.52 ms                                               | 1.49 ms: 1.02x faster                                                     |
| async_generators         | 454 ms                                                | 445 ms: 1.02x faster                                                      |
| mako                     | 10.9 ms                                               | 10.7 ms: 1.02x faster                                                     |
| float                    | 80.7 ms                                               | 79.1 ms: 1.02x faster                                                     |
| xml_etree_generate       | 84.6 ms                                               | 83.1 ms: 1.02x faster                                                     |
| xml_etree_process        | 58.5 ms                                               | 57.5 ms: 1.02x faster                                                     |
| pprint_pformat           | 1.51 sec                                              | 1.49 sec: 1.02x faster                                                    |
| hexiom                   | 6.11 ms                                               | 6.00 ms: 1.02x faster                                                     |
| logging_simple           | 5.90 us                                               | 5.81 us: 1.01x faster                                                     |
| deepcopy_memo            | 37.7 us                                               | 37.2 us: 1.01x faster                                                     |
| telco                    | 7.28 ms                                               | 7.18 ms: 1.01x faster                                                     |
| logging_format           | 6.54 us                                               | 6.45 us: 1.01x faster                                                     |
| unpickle_pure_python     | 214 us                                                | 211 us: 1.01x faster                                                      |
| coroutines               | 22.6 ms                                               | 22.3 ms: 1.01x faster                                                     |
| json                     | 4.96 ms                                               | 4.90 ms: 1.01x faster                                                     |
| regex_v8                 | 22.3 ms                                               | 22.1 ms: 1.01x faster                                                     |
| fannkuch                 | 397 ms                                                | 393 ms: 1.01x faster                                                      |
| scimark_monte_carlo      | 68.5 ms                                               | 67.7 ms: 1.01x faster                                                     |
| dulwich_log              | 66.4 ms                                               | 65.7 ms: 1.01x faster                                                     |
| coverage                 | 94.1 ms                                               | 93.1 ms: 1.01x faster                                                     |
| xml_etree_iterparse      | 103 ms                                                | 102 ms: 1.01x faster                                                      |
| xml_etree_parse          | 154 ms                                                | 153 ms: 1.01x faster                                                      |
| pathlib                  | 18.8 ms                                               | 18.6 ms: 1.01x faster                                                     |
| logging_silent           | 103 ns                                                | 102 ns: 1.01x faster                                                      |
| deepcopy                 | 356 us                                                | 353 us: 1.01x faster                                                      |
| nqueens                  | 80.2 ms                                               | 79.5 ms: 1.01x faster                                                     |
| regex_compile            | 138 ms                                                | 137 ms: 1.01x faster                                                      |
| python_startup           | 9.25 ms                                               | 9.18 ms: 1.01x faster                                                     |
| scimark_sor              | 121 ms                                                | 120 ms: 1.01x faster                                                      |
| scimark_lu               | 111 ms                                                | 111 ms: 1.01x faster                                                      |
| pickle_pure_python       | 298 us                                                | 296 us: 1.01x faster                                                      |
| python_startup_no_site   | 6.71 ms                                               | 6.67 ms: 1.01x faster                                                     |
| asyncio_tcp_ssl          | 1.79 sec                                              | 1.78 sec: 1.01x faster                                                    |
| tomli_loads              | 2.33 sec                                              | 2.32 sec: 1.01x faster                                                    |
| bench_thread_pool        | 820 us                                                | 815 us: 1.01x faster                                                      |
| generators               | 28.7 ms                                               | 28.5 ms: 1.01x faster                                                     |
| chaos                    | 59.8 ms                                               | 59.5 ms: 1.00x faster                                                     |
| sqlglot_normalize        | 105 ms                                                | 105 ms: 1.00x faster                                                      |
| docutils                 | 2.65 sec                                              | 2.66 sec: 1.00x slower                                                    |
| deepcopy_reduce          | 3.15 us                                               | 3.16 us: 1.01x slower                                                     |
| pickle                   | 10.6 us                                               | 10.6 us: 1.01x slower                                                     |
| sqlglot_optimize         | 52.5 ms                                               | 52.8 ms: 1.01x slower                                                     |
| go                       | 138 ms                                                | 139 ms: 1.01x slower                                                      |
| raytrace                 | 268 ms                                                | 270 ms: 1.01x slower                                                      |
| pidigits                 | 196 ms                                                | 198 ms: 1.01x slower                                                      |
| sqlite_synth             | 2.75 us                                               | 2.78 us: 1.01x slower                                                     |
| async_tree_io            | 1.18 sec                                              | 1.19 sec: 1.01x slower                                                    |
| mdp                      | 2.56 sec                                              | 2.59 sec: 1.01x slower                                                    |
| richards                 | 48.1 ms                                               | 49.0 ms: 1.02x slower                                                     |
| pickle_dict              | 31.7 us                                               | 32.5 us: 1.03x slower                                                     |
| regex_dna                | 207 ms                                                | 214 ms: 1.04x slower                                                      |
| nbody                    | 89.3 ms                                               | 93.8 ms: 1.05x slower                                                     |
| gc_traversal             | 3.94 ms                                               | 4.30 ms: 1.09x slower                                                     |
| unpack_sequence          | 42.3 ns                                               | 47.9 ns: 1.13x slower                                                     |
| mypy2                    | 336 ms                                                | 453 ms: 1.35x slower                                                      |
| Geometric mean           | (ref)                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (20): async_tree_cpu_io_mixed, scimark_fft, dask, deltablue, pyflate, pycparser, tornado_http, async_tree_memoization, pprint_safe_repr, comprehensions, meteor_contest, async_tree_none, scimark_sparse_mat_mult, bench_mp_pool, richards_super, asyncio_tcp, sqlglot_parse, sqlglot_transpile, json_dumps, unpickle


# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
