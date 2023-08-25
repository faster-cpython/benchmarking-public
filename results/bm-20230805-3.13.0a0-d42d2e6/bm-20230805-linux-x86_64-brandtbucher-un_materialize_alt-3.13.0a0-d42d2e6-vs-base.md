
# Results vs. base

- fork: brandtbucher
- ref: un_materialize_alt
- machine: linux-x86_64
- commit hash: d42d2e6
- commit date: 2023-08-05
- overall geometric mean: 1.00x slower
- HPT reliability: 67.39%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-16c9415fba4972743f19-3.13.0a0-16c9415 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                               | 87.6 ms: 1.01x faster                                                     |
| pidigits       | 189 ms                                                                | 189 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230807-linux-x86_64-python-16c9415fba4972743f19-3.13.0a0-16c9415 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 208 ms                                                                | 204 ms: 1.02x faster                                                      |
| regex_compile  | 137 ms                                                                | 136 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230807-linux-x86_64-python-16c9415fba4972743f19-3.13.0a0-16c9415 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle               | 10.6 us                                                               | 10.4 us: 1.02x faster                                                     |
| tomli_loads          | 2.32 sec                                                              | 2.31 sec: 1.01x faster                                                    |
| xml_etree_process    | 57.5 ms                                                               | 57.3 ms: 1.00x faster                                                     |
| unpickle_pure_python | 211 us                                                                | 213 us: 1.01x slower                                                      |
| unpickle_list        | 4.96 us                                                               | 5.04 us: 1.02x slower                                                     |
| pickle_dict          | 31.0 us                                                               | 31.5 us: 1.02x slower                                                     |
| pickle_list          | 4.48 us                                                               | 4.59 us: 1.02x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (7): json_dumps, json_loads, pickle_pure_python, xml_etree_iterparse, xml_etree_generate, xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230807-linux-x86_64-python-16c9415fba4972743f19-3.13.0a0-16c9415 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.83 ms                                                               | 6.85 ms: 1.00x slower                                                     |
| python_startup         | 9.35 ms                                                               | 9.37 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230807-linux-x86_64-python-16c9415fba4972743f19-3.13.0a0-16c9415 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6 |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.8 ms                                                               | 10.7 ms: 1.01x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20230807-linux-x86_64-python-16c9415fba4972743f19-3.13.0a0-16c9415 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d42d2e6 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| gc_traversal             | 4.06 ms                                                               | 3.84 ms: 1.06x faster                                                     |
| spectral_norm            | 107 ms                                                                | 103 ms: 1.04x faster                                                      |
| pickle                   | 10.6 us                                                               | 10.4 us: 1.02x faster                                                     |
| sqlite_synth             | 2.78 us                                                               | 2.72 us: 1.02x faster                                                     |
| async_tree_memoization   | 585 ms                                                                | 574 ms: 1.02x faster                                                      |
| regex_dna                | 208 ms                                                                | 204 ms: 1.02x faster                                                      |
| deepcopy_reduce          | 3.19 us                                                               | 3.13 us: 1.02x faster                                                     |
| richards                 | 48.5 ms                                                               | 47.6 ms: 1.02x faster                                                     |
| dask                     | 522 ms                                                                | 515 ms: 1.02x faster                                                      |
| dulwich_log              | 66.6 ms                                                               | 65.6 ms: 1.01x faster                                                     |
| async_tree_none          | 483 ms                                                                | 476 ms: 1.01x faster                                                      |
| pathlib                  | 18.6 ms                                                               | 18.3 ms: 1.01x faster                                                     |
| richards_super           | 54.4 ms                                                               | 53.7 ms: 1.01x faster                                                     |
| scimark_sor              | 121 ms                                                                | 119 ms: 1.01x faster                                                      |
| mako                     | 10.8 ms                                                               | 10.7 ms: 1.01x faster                                                     |
| chaos                    | 60.4 ms                                                               | 59.7 ms: 1.01x faster                                                     |
| async_tree_io            | 1.19 sec                                                              | 1.18 sec: 1.01x faster                                                    |
| create_gc_cycles         | 1.49 ms                                                               | 1.48 ms: 1.01x faster                                                     |
| telco                    | 7.86 ms                                                               | 7.79 ms: 1.01x faster                                                     |
| nbody                    | 88.3 ms                                                               | 87.6 ms: 1.01x faster                                                     |
| regex_compile            | 137 ms                                                                | 136 ms: 1.01x faster                                                      |
| tomli_loads              | 2.32 sec                                                              | 2.31 sec: 1.01x faster                                                    |
| xml_etree_process        | 57.5 ms                                                               | 57.3 ms: 1.00x faster                                                     |
| pidigits                 | 189 ms                                                                | 189 ms: 1.00x faster                                                      |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                    |
| python_startup_no_site   | 6.83 ms                                                               | 6.85 ms: 1.00x slower                                                     |
| python_startup           | 9.35 ms                                                               | 9.37 ms: 1.00x slower                                                     |
| fannkuch                 | 391 ms                                                                | 392 ms: 1.00x slower                                                      |
| sqlglot_optimize         | 52.6 ms                                                               | 52.9 ms: 1.01x slower                                                     |
| pycparser                | 1.15 sec                                                              | 1.15 sec: 1.01x slower                                                    |
| go                       | 137 ms                                                                | 138 ms: 1.01x slower                                                      |
| scimark_monte_carlo      | 67.7 ms                                                               | 68.2 ms: 1.01x slower                                                     |
| raytrace                 | 271 ms                                                                | 273 ms: 1.01x slower                                                      |
| sqlglot_parse            | 1.28 ms                                                               | 1.29 ms: 1.01x slower                                                     |
| unpickle_pure_python     | 211 us                                                                | 213 us: 1.01x slower                                                      |
| nqueens                  | 79.1 ms                                                               | 79.9 ms: 1.01x slower                                                     |
| async_generators         | 443 ms                                                                | 448 ms: 1.01x slower                                                      |
| deepcopy_memo            | 37.8 us                                                               | 38.2 us: 1.01x slower                                                     |
| json                     | 4.78 ms                                                               | 4.83 ms: 1.01x slower                                                     |
| scimark_fft              | 350 ms                                                                | 356 ms: 1.02x slower                                                      |
| unpickle_list            | 4.96 us                                                               | 5.04 us: 1.02x slower                                                     |
| pickle_dict              | 31.0 us                                                               | 31.5 us: 1.02x slower                                                     |
| coroutines               | 21.5 ms                                                               | 21.9 ms: 1.02x slower                                                     |
| pickle_list              | 4.48 us                                                               | 4.59 us: 1.02x slower                                                     |
| typing_runtime_protocols | 141 us                                                                | 145 us: 1.03x slower                                                      |
| mdp                      | 2.65 sec                                                              | 2.73 sec: 1.03x slower                                                    |
| unpack_sequence          | 41.8 ns                                                               | 43.2 ns: 1.03x slower                                                     |
| comprehensions           | 19.8 us                                                               | 20.5 us: 1.04x slower                                                     |
| mypy2                    | 336 ms                                                                | 453 ms: 1.35x slower                                                      |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (33): async_tree_cpu_io_mixed, json_dumps, regex_effbot, tornado_http, logging_simple, json_loads, docutils, pickle_pure_python, bench_thread_pool, pyflate, xml_etree_iterparse, xml_etree_generate, meteor_contest, bench_mp_pool, logging_silent, pprint_safe_repr, sqlglot_normalize, scimark_lu, float, asyncio_tcp, hexiom, regex_v8, deltablue, coverage, deepcopy, logging_format, pprint_pformat, crypto_pyaes, sqlglot_transpile, generators, scimark_sparse_mat_mult, xml_etree_parse, unpickle


# HPT report

- Reliability score: 67.39% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
