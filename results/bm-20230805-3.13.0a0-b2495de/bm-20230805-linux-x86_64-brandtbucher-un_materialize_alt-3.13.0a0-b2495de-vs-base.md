
# Results vs. base

- fork: brandtbucher
- ref: un_materialize_alt
- machine: linux-x86_64
- commit hash: b2495de
- commit date: 2023-08-05
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-16c9415fba4972743f19-3.13.0a0-16c9415 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.64 sec                                                              | 2.65 sec: 1.00x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230807-linux-x86_64-python-16c9415fba4972743f19-3.13.0a0-16c9415 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                | 189 ms: 1.00x faster                                                      |
| float          | 79.8 ms                                                               | 80.2 ms: 1.00x slower                                                     |
| nbody          | 88.3 ms                                                               | 89.2 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230807-linux-x86_64-python-16c9415fba4972743f19-3.13.0a0-16c9415 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 208 ms                                                                | 203 ms: 1.02x faster                                                      |
| regex_compile  | 137 ms                                                                | 136 ms: 1.00x faster                                                      |
| regex_effbot   | 3.44 ms                                                               | 3.53 ms: 1.02x slower                                                     |
| regex_v8       | 21.8 ms                                                               | 22.5 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230807-linux-x86_64-python-16c9415fba4972743f19-3.13.0a0-16c9415 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_list        | 4.96 us                                                               | 4.91 us: 1.01x faster                                                     |
| pickle_pure_python   | 298 us                                                                | 296 us: 1.01x faster                                                      |
| xml_etree_generate   | 83.0 ms                                                               | 83.4 ms: 1.00x slower                                                     |
| json_loads           | 25.4 us                                                               | 25.6 us: 1.01x slower                                                     |
| xml_etree_process    | 57.5 ms                                                               | 58.0 ms: 1.01x slower                                                     |
| pickle               | 10.6 us                                                               | 10.8 us: 1.02x slower                                                     |
| unpickle_pure_python | 211 us                                                                | 215 us: 1.02x slower                                                      |
| pickle_dict          | 31.0 us                                                               | 31.6 us: 1.02x slower                                                     |
| pickle_list          | 4.48 us                                                               | 4.66 us: 1.04x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (5): tomli_loads, json_dumps, xml_etree_iterparse, xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230807-linux-x86_64-python-16c9415fba4972743f19-3.13.0a0-16c9415 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 9.35 ms                                                               | 9.43 ms: 1.01x slower                                                     |
| python_startup_no_site | 6.83 ms                                                               | 6.89 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230807-linux-x86_64-python-16c9415fba4972743f19-3.13.0a0-16c9415 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.8 ms                                                               | 10.7 ms: 1.01x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20230807-linux-x86_64-python-16c9415fba4972743f19-3.13.0a0-16c9415 | bm-20230805-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-b2495de |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                      | 2.65 sec                                                              | 2.54 sec: 1.04x faster                                                    |
| sqlite_synth             | 2.78 us                                                               | 2.71 us: 1.03x faster                                                     |
| regex_dna                | 208 ms                                                                | 203 ms: 1.02x faster                                                      |
| chaos                    | 60.4 ms                                                               | 59.3 ms: 1.02x faster                                                     |
| fannkuch                 | 391 ms                                                                | 386 ms: 1.01x faster                                                      |
| logging_silent           | 102 ns                                                                | 101 ns: 1.01x faster                                                      |
| dask                     | 522 ms                                                                | 516 ms: 1.01x faster                                                      |
| generators               | 28.4 ms                                                               | 28.1 ms: 1.01x faster                                                     |
| unpickle_list            | 4.96 us                                                               | 4.91 us: 1.01x faster                                                     |
| bench_thread_pool        | 828 us                                                                | 820 us: 1.01x faster                                                      |
| richards_super           | 54.4 ms                                                               | 53.9 ms: 1.01x faster                                                     |
| spectral_norm            | 107 ms                                                                | 106 ms: 1.01x faster                                                      |
| logging_simple           | 5.90 us                                                               | 5.86 us: 1.01x faster                                                     |
| mako                     | 10.8 ms                                                               | 10.7 ms: 1.01x faster                                                     |
| sqlglot_normalize        | 105 ms                                                                | 104 ms: 1.01x faster                                                      |
| pprint_safe_repr         | 720 ms                                                                | 715 ms: 1.01x faster                                                      |
| pickle_pure_python       | 298 us                                                                | 296 us: 1.01x faster                                                      |
| coroutines               | 21.5 ms                                                               | 21.3 ms: 1.01x faster                                                     |
| dulwich_log              | 66.6 ms                                                               | 66.2 ms: 1.01x faster                                                     |
| pyflate                  | 446 ms                                                                | 443 ms: 1.01x faster                                                      |
| pprint_pformat           | 1.48 sec                                                              | 1.47 sec: 1.01x faster                                                    |
| deepcopy_memo            | 37.8 us                                                               | 37.6 us: 1.00x faster                                                     |
| regex_compile            | 137 ms                                                                | 136 ms: 1.00x faster                                                      |
| pidigits                 | 189 ms                                                                | 189 ms: 1.00x faster                                                      |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                    |
| hexiom                   | 6.02 ms                                                               | 6.03 ms: 1.00x slower                                                     |
| asyncio_tcp              | 483 ms                                                                | 485 ms: 1.00x slower                                                      |
| docutils                 | 2.64 sec                                                              | 2.65 sec: 1.00x slower                                                    |
| xml_etree_generate       | 83.0 ms                                                               | 83.4 ms: 1.00x slower                                                     |
| float                    | 79.8 ms                                                               | 80.2 ms: 1.00x slower                                                     |
| crypto_pyaes             | 69.5 ms                                                               | 69.9 ms: 1.01x slower                                                     |
| meteor_contest           | 105 ms                                                                | 106 ms: 1.01x slower                                                      |
| deepcopy_reduce          | 3.19 us                                                               | 3.21 us: 1.01x slower                                                     |
| async_generators         | 443 ms                                                                | 447 ms: 1.01x slower                                                      |
| sqlglot_parse            | 1.28 ms                                                               | 1.29 ms: 1.01x slower                                                     |
| json_loads               | 25.4 us                                                               | 25.6 us: 1.01x slower                                                     |
| deepcopy                 | 355 us                                                                | 358 us: 1.01x slower                                                      |
| async_tree_io            | 1.19 sec                                                              | 1.20 sec: 1.01x slower                                                    |
| xml_etree_process        | 57.5 ms                                                               | 58.0 ms: 1.01x slower                                                     |
| python_startup           | 9.35 ms                                                               | 9.43 ms: 1.01x slower                                                     |
| python_startup_no_site   | 6.83 ms                                                               | 6.89 ms: 1.01x slower                                                     |
| go                       | 137 ms                                                                | 138 ms: 1.01x slower                                                      |
| nbody                    | 88.3 ms                                                               | 89.2 ms: 1.01x slower                                                     |
| typing_runtime_protocols | 141 us                                                                | 143 us: 1.01x slower                                                      |
| pathlib                  | 18.6 ms                                                               | 18.8 ms: 1.01x slower                                                     |
| json                     | 4.78 ms                                                               | 4.83 ms: 1.01x slower                                                     |
| scimark_monte_carlo      | 67.7 ms                                                               | 68.5 ms: 1.01x slower                                                     |
| telco                    | 7.86 ms                                                               | 7.97 ms: 1.01x slower                                                     |
| create_gc_cycles         | 1.49 ms                                                               | 1.52 ms: 1.02x slower                                                     |
| pickle                   | 10.6 us                                                               | 10.8 us: 1.02x slower                                                     |
| raytrace                 | 271 ms                                                                | 275 ms: 1.02x slower                                                      |
| scimark_fft              | 350 ms                                                                | 356 ms: 1.02x slower                                                      |
| unpickle_pure_python     | 211 us                                                                | 215 us: 1.02x slower                                                      |
| pickle_dict              | 31.0 us                                                               | 31.6 us: 1.02x slower                                                     |
| comprehensions           | 19.8 us                                                               | 20.2 us: 1.02x slower                                                     |
| regex_effbot             | 3.44 ms                                                               | 3.53 ms: 1.02x slower                                                     |
| scimark_sparse_mat_mult  | 4.77 ms                                                               | 4.91 ms: 1.03x slower                                                     |
| regex_v8                 | 21.8 ms                                                               | 22.5 ms: 1.03x slower                                                     |
| pickle_list              | 4.48 us                                                               | 4.66 us: 1.04x slower                                                     |
| gc_traversal             | 4.06 ms                                                               | 4.34 ms: 1.07x slower                                                     |
| unpack_sequence          | 41.8 ns                                                               | 47.6 ns: 1.14x slower                                                     |
| mypy2                    | 336 ms                                                                | 456 ms: 1.36x slower                                                      |
| Geometric mean           | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (20): richards, tomli_loads, tornado_http, scimark_sor, logging_format, json_dumps, scimark_lu, pycparser, coverage, async_tree_memoization, nqueens, bench_mp_pool, sqlglot_optimize, async_tree_none, deltablue, xml_etree_iterparse, sqlglot_transpile, async_tree_cpu_io_mixed, xml_etree_parse, unpickle
