
# Results vs. base

- fork: brandtbucher
- ref: un_materialize_alt
- machine: linux-x86_64
- commit hash: d00eefe
- commit date: 2023-07-07
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230707-linux-x86_64-python-80b9b3a51757ebb1e354-3.13.0a0-80b9b3a | bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.66 sec                                                              | 2.64 sec: 1.00x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230707-linux-x86_64-python-80b9b3a51757ebb1e354-3.13.0a0-80b9b3a | bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 196 ms                                                                | 197 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230707-linux-x86_64-python-80b9b3a51757ebb1e354-3.13.0a0-80b9b3a | bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 22.3 ms                                                               | 21.9 ms: 1.02x faster                                                     |
| regex_effbot   | 3.56 ms                                                               | 3.51 ms: 1.02x faster                                                     |
| regex_compile  | 136 ms                                                                | 136 ms: 1.00x faster                                                      |
| regex_dna      | 211 ms                                                                | 213 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230707-linux-x86_64-python-80b9b3a51757ebb1e354-3.13.0a0-80b9b3a | bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_list         | 4.72 us                                                               | 4.55 us: 1.04x faster                                                     |
| pickle_pure_python  | 312 us                                                                | 302 us: 1.03x faster                                                      |
| xml_etree_generate  | 84.3 ms                                                               | 83.3 ms: 1.01x faster                                                     |
| json_dumps          | 9.86 ms                                                               | 9.75 ms: 1.01x faster                                                     |
| unpickle_list       | 5.06 us                                                               | 5.00 us: 1.01x faster                                                     |
| pickle              | 10.7 us                                                               | 10.6 us: 1.01x faster                                                     |
| xml_etree_parse     | 153 ms                                                                | 152 ms: 1.01x faster                                                      |
| xml_etree_iterparse | 104 ms                                                                | 103 ms: 1.01x faster                                                      |
| json_loads          | 25.8 us                                                               | 25.7 us: 1.00x faster                                                     |
| xml_etree_process   | 57.8 ms                                                               | 57.5 ms: 1.00x faster                                                     |
| pickle_dict         | 30.8 us                                                               | 30.8 us: 1.00x faster                                                     |
| unpickle            | 14.9 us                                                               | 15.1 us: 1.01x slower                                                     |
| Geometric mean      | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (2): unpickle_pure_python, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230707-linux-x86_64-python-80b9b3a51757ebb1e354-3.13.0a0-80b9b3a | bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.67 ms                                                               | 6.73 ms: 1.01x slower                                                     |
| python_startup         | 9.18 ms                                                               | 9.26 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20230707-linux-x86_64-python-80b9b3a51757ebb1e354-3.13.0a0-80b9b3a | bm-20230707-linux-x86_64-brandtbucher-un_materialize_alt-3.13.0a0-d00eefe |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| gc_traversal             | 4.30 ms                                                               | 3.56 ms: 1.21x faster                                                     |
| unpack_sequence          | 46.7 ns                                                               | 43.1 ns: 1.08x faster                                                     |
| spectral_norm            | 110 ms                                                                | 104 ms: 1.05x faster                                                      |
| pickle_list              | 4.72 us                                                               | 4.55 us: 1.04x faster                                                     |
| pickle_pure_python       | 312 us                                                                | 302 us: 1.03x faster                                                      |
| logging_format           | 6.68 us                                                               | 6.50 us: 1.03x faster                                                     |
| coroutines               | 23.1 ms                                                               | 22.5 ms: 1.02x faster                                                     |
| chaos                    | 59.9 ms                                                               | 58.9 ms: 1.02x faster                                                     |
| regex_v8                 | 22.3 ms                                                               | 21.9 ms: 1.02x faster                                                     |
| regex_effbot             | 3.56 ms                                                               | 3.51 ms: 1.02x faster                                                     |
| logging_simple           | 5.99 us                                                               | 5.90 us: 1.01x faster                                                     |
| sqlite_synth             | 2.78 us                                                               | 2.74 us: 1.01x faster                                                     |
| crypto_pyaes             | 78.9 ms                                                               | 77.9 ms: 1.01x faster                                                     |
| xml_etree_generate       | 84.3 ms                                                               | 83.3 ms: 1.01x faster                                                     |
| telco                    | 7.19 ms                                                               | 7.10 ms: 1.01x faster                                                     |
| async_generators         | 453 ms                                                                | 447 ms: 1.01x faster                                                      |
| hexiom                   | 6.13 ms                                                               | 6.06 ms: 1.01x faster                                                     |
| json_dumps               | 9.86 ms                                                               | 9.75 ms: 1.01x faster                                                     |
| unpickle_list            | 5.06 us                                                               | 5.00 us: 1.01x faster                                                     |
| richards_super           | 53.1 ms                                                               | 52.5 ms: 1.01x faster                                                     |
| json                     | 4.95 ms                                                               | 4.91 ms: 1.01x faster                                                     |
| dask                     | 521 ms                                                                | 517 ms: 1.01x faster                                                      |
| fannkuch                 | 394 ms                                                                | 391 ms: 1.01x faster                                                      |
| scimark_fft              | 353 ms                                                                | 351 ms: 1.01x faster                                                      |
| dulwich_log              | 66.1 ms                                                               | 65.6 ms: 1.01x faster                                                     |
| pickle                   | 10.7 us                                                               | 10.6 us: 1.01x faster                                                     |
| xml_etree_parse          | 153 ms                                                                | 152 ms: 1.01x faster                                                      |
| xml_etree_iterparse      | 104 ms                                                                | 103 ms: 1.01x faster                                                      |
| async_tree_io            | 1.20 sec                                                              | 1.20 sec: 1.01x faster                                                    |
| bench_thread_pool        | 821 us                                                                | 817 us: 1.01x faster                                                      |
| docutils                 | 2.66 sec                                                              | 2.64 sec: 1.00x faster                                                    |
| json_loads               | 25.8 us                                                               | 25.7 us: 1.00x faster                                                     |
| xml_etree_process        | 57.8 ms                                                               | 57.5 ms: 1.00x faster                                                     |
| regex_compile            | 136 ms                                                                | 136 ms: 1.00x faster                                                      |
| sqlglot_parse            | 1.33 ms                                                               | 1.33 ms: 1.00x faster                                                     |
| meteor_contest           | 105 ms                                                                | 104 ms: 1.00x faster                                                      |
| pickle_dict              | 30.8 us                                                               | 30.8 us: 1.00x faster                                                     |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.79 sec: 1.00x faster                                                    |
| pidigits                 | 196 ms                                                                | 197 ms: 1.00x slower                                                      |
| go                       | 138 ms                                                                | 139 ms: 1.00x slower                                                      |
| pyflate                  | 444 ms                                                                | 446 ms: 1.01x slower                                                      |
| scimark_lu               | 110 ms                                                                | 110 ms: 1.01x slower                                                      |
| generators               | 28.4 ms                                                               | 28.6 ms: 1.01x slower                                                     |
| python_startup_no_site   | 6.67 ms                                                               | 6.73 ms: 1.01x slower                                                     |
| python_startup           | 9.18 ms                                                               | 9.26 ms: 1.01x slower                                                     |
| regex_dna                | 211 ms                                                                | 213 ms: 1.01x slower                                                      |
| pprint_safe_repr         | 713 ms                                                                | 720 ms: 1.01x slower                                                      |
| typing_runtime_protocols | 143 us                                                                | 144 us: 1.01x slower                                                      |
| comprehensions           | 20.4 us                                                               | 20.6 us: 1.01x slower                                                     |
| raytrace                 | 268 ms                                                                | 271 ms: 1.01x slower                                                      |
| unpickle                 | 14.9 us                                                               | 15.1 us: 1.01x slower                                                     |
| pprint_pformat           | 1.46 sec                                                              | 1.48 sec: 1.02x slower                                                    |
| create_gc_cycles         | 1.48 ms                                                               | 1.50 ms: 1.02x slower                                                     |
| nqueens                  | 79.7 ms                                                               | 81.6 ms: 1.02x slower                                                     |
| coverage                 | 93.2 ms                                                               | 95.6 ms: 1.03x slower                                                     |
| deepcopy_reduce          | 3.12 us                                                               | 3.21 us: 1.03x slower                                                     |
| mdp                      | 2.53 sec                                                              | 2.70 sec: 1.06x slower                                                    |
| mypy2                    | 337 ms                                                                | 455 ms: 1.35x slower                                                      |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (24): scimark_sparse_mat_mult, sqlglot_transpile, float, nbody, async_tree_memoization, tornado_http, richards, scimark_sor, scimark_monte_carlo, unpickle_pure_python, async_tree_none, deepcopy_memo, sqlglot_normalize, bench_mp_pool, tomli_loads, mako, deepcopy, deltablue, asyncio_tcp, async_tree_cpu_io_mixed, pycparser, sqlglot_optimize, pathlib, logging_silent
