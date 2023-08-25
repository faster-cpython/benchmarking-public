
# Results vs. base

- fork: gvanrossum
- ref: optim_exec
- machine: linux-x86_64
- commit hash: 6b23e0f
- commit date: 2023-06-19
- overall geometric mean: 1.00x slower
- HPT reliability: 55.79%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230619-linux-x86_64-python-1858db7cbdbf41aa600c-3.13.0a0-1858db7 | bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| tornado_http   | 97.5 ms                                                               | 96.4 ms: 1.01x faster                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230619-linux-x86_64-python-1858db7cbdbf41aa600c-3.13.0a0-1858db7 | bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 89.8 ms                                                               | 89.0 ms: 1.01x faster                                           |
| pidigits       | 197 ms                                                                | 196 ms: 1.00x faster                                            |
| float          | 79.5 ms                                                               | 80.5 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230619-linux-x86_64-python-1858db7cbdbf41aa600c-3.13.0a0-1858db7 | bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 3.50 ms                                                               | 3.38 ms: 1.04x faster                                           |
| regex_dna      | 208 ms                                                                | 201 ms: 1.03x faster                                            |
| regex_v8       | 22.0 ms                                                               | 21.7 ms: 1.01x faster                                           |
| regex_compile  | 136 ms                                                                | 137 ms: 1.00x slower                                            |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230619-linux-x86_64-python-1858db7cbdbf41aa600c-3.13.0a0-1858db7 | bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_list          | 4.69 us                                                               | 4.51 us: 1.04x faster                                           |
| unpickle_pure_python | 216 us                                                                | 212 us: 1.02x faster                                            |
| unpickle_list        | 4.95 us                                                               | 4.87 us: 1.02x faster                                           |
| pickle_pure_python   | 308 us                                                                | 306 us: 1.01x faster                                            |
| pickle_dict          | 31.5 us                                                               | 31.5 us: 1.00x faster                                           |
| xml_etree_iterparse  | 104 ms                                                                | 104 ms: 1.01x slower                                            |
| xml_etree_process    | 57.7 ms                                                               | 58.2 ms: 1.01x slower                                           |
| xml_etree_generate   | 84.5 ms                                                               | 85.3 ms: 1.01x slower                                           |
| pickle               | 10.6 us                                                               | 10.7 us: 1.01x slower                                           |
| json_loads           | 25.0 us                                                               | 25.3 us: 1.01x slower                                           |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                    |

Benchmark hidden because not significant (4): xml_etree_parse, tomli_loads, json_dumps, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230619-linux-x86_64-python-1858db7cbdbf41aa600c-3.13.0a0-1858db7 | bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 9.20 ms                                                               | 9.20 ms: 1.00x slower                                           |
| python_startup_no_site | 6.68 ms                                                               | 6.68 ms: 1.00x slower                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230619-linux-x86_64-python-1858db7cbdbf41aa600c-3.13.0a0-1858db7 | bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f |
|-----------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 10.9 ms                                                               | 10.8 ms: 1.01x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20230619-linux-x86_64-python-1858db7cbdbf41aa600c-3.13.0a0-1858db7 | bm-20230619-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-6b23e0f |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| logging_silent           | 101 ns                                                                | 94.3 ns: 1.07x faster                                           |
| gc_traversal             | 3.93 ms                                                               | 3.74 ms: 1.05x faster                                           |
| pickle_list              | 4.69 us                                                               | 4.51 us: 1.04x faster                                           |
| regex_effbot             | 3.50 ms                                                               | 3.38 ms: 1.04x faster                                           |
| regex_dna                | 208 ms                                                                | 201 ms: 1.03x faster                                            |
| pprint_safe_repr         | 729 ms                                                                | 713 ms: 1.02x faster                                            |
| logging_simple           | 6.09 us                                                               | 5.96 us: 1.02x faster                                           |
| scimark_sor              | 120 ms                                                                | 117 ms: 1.02x faster                                            |
| pyflate                  | 452 ms                                                                | 444 ms: 1.02x faster                                            |
| unpickle_pure_python     | 216 us                                                                | 212 us: 1.02x faster                                            |
| scimark_monte_carlo      | 71.2 ms                                                               | 70.0 ms: 1.02x faster                                           |
| unpickle_list            | 4.95 us                                                               | 4.87 us: 1.02x faster                                           |
| telco                    | 6.91 ms                                                               | 6.81 ms: 1.02x faster                                           |
| coroutines               | 22.5 ms                                                               | 22.2 ms: 1.01x faster                                           |
| deepcopy_reduce          | 3.17 us                                                               | 3.13 us: 1.01x faster                                           |
| deepcopy                 | 356 us                                                                | 351 us: 1.01x faster                                            |
| regex_v8                 | 22.0 ms                                                               | 21.7 ms: 1.01x faster                                           |
| mako                     | 10.9 ms                                                               | 10.8 ms: 1.01x faster                                           |
| raytrace                 | 294 ms                                                                | 290 ms: 1.01x faster                                            |
| sqlglot_parse            | 1.32 ms                                                               | 1.30 ms: 1.01x faster                                           |
| tornado_http             | 97.5 ms                                                               | 96.4 ms: 1.01x faster                                           |
| sqlglot_optimize         | 53.1 ms                                                               | 52.6 ms: 1.01x faster                                           |
| pprint_pformat           | 1.48 sec                                                              | 1.47 sec: 1.01x faster                                          |
| logging_format           | 6.57 us                                                               | 6.50 us: 1.01x faster                                           |
| sqlglot_transpile        | 1.63 ms                                                               | 1.62 ms: 1.01x faster                                           |
| mypy2                    | 339 ms                                                                | 336 ms: 1.01x faster                                            |
| nbody                    | 89.8 ms                                                               | 89.0 ms: 1.01x faster                                           |
| dulwich_log              | 65.4 ms                                                               | 64.9 ms: 1.01x faster                                           |
| sqlglot_normalize        | 107 ms                                                                | 106 ms: 1.01x faster                                            |
| chaos                    | 61.8 ms                                                               | 61.4 ms: 1.01x faster                                           |
| scimark_lu               | 110 ms                                                                | 110 ms: 1.01x faster                                            |
| pickle_pure_python       | 308 us                                                                | 306 us: 1.01x faster                                            |
| pidigits                 | 197 ms                                                                | 196 ms: 1.00x faster                                            |
| asyncio_tcp              | 507 ms                                                                | 506 ms: 1.00x faster                                            |
| pickle_dict              | 31.5 us                                                               | 31.5 us: 1.00x faster                                           |
| python_startup           | 9.20 ms                                                               | 9.20 ms: 1.00x slower                                           |
| python_startup_no_site   | 6.68 ms                                                               | 6.68 ms: 1.00x slower                                           |
| async_tree_io            | 1.20 sec                                                              | 1.20 sec: 1.00x slower                                          |
| regex_compile            | 136 ms                                                                | 137 ms: 1.00x slower                                            |
| xml_etree_iterparse      | 104 ms                                                                | 104 ms: 1.01x slower                                            |
| generators               | 29.6 ms                                                               | 29.8 ms: 1.01x slower                                           |
| xml_etree_process        | 57.7 ms                                                               | 58.2 ms: 1.01x slower                                           |
| xml_etree_generate       | 84.5 ms                                                               | 85.3 ms: 1.01x slower                                           |
| pickle                   | 10.6 us                                                               | 10.7 us: 1.01x slower                                           |
| float                    | 79.5 ms                                                               | 80.5 ms: 1.01x slower                                           |
| json_loads               | 25.0 us                                                               | 25.3 us: 1.01x slower                                           |
| mdp                      | 2.53 sec                                                              | 2.56 sec: 1.01x slower                                          |
| bench_thread_pool        | 821 us                                                                | 833 us: 1.02x slower                                            |
| deepcopy_memo            | 37.7 us                                                               | 38.2 us: 1.02x slower                                           |
| async_generators         | 458 ms                                                                | 465 ms: 1.02x slower                                            |
| fannkuch                 | 394 ms                                                                | 401 ms: 1.02x slower                                            |
| json                     | 4.80 ms                                                               | 4.90 ms: 1.02x slower                                           |
| scimark_fft              | 344 ms                                                                | 351 ms: 1.02x slower                                            |
| hexiom                   | 6.09 ms                                                               | 6.22 ms: 1.02x slower                                           |
| crypto_pyaes             | 76.7 ms                                                               | 78.5 ms: 1.02x slower                                           |
| sqlite_synth             | 2.71 us                                                               | 2.78 us: 1.02x slower                                           |
| pathlib                  | 18.8 ms                                                               | 19.3 ms: 1.03x slower                                           |
| meteor_contest           | 104 ms                                                                | 108 ms: 1.03x slower                                            |
| comprehensions           | 20.7 us                                                               | 21.4 us: 1.03x slower                                           |
| nqueens                  | 79.2 ms                                                               | 82.5 ms: 1.04x slower                                           |
| typing_runtime_protocols | 141 us                                                                | 147 us: 1.04x slower                                            |
| spectral_norm            | 104 ms                                                                | 109 ms: 1.05x slower                                            |
| unpack_sequence          | 43.3 ns                                                               | 46.8 ns: 1.08x slower                                           |
| scimark_sparse_mat_mult  | 4.63 ms                                                               | 5.07 ms: 1.09x slower                                           |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                    |

Benchmark hidden because not significant (18): dask, async_tree_memoization, go, pycparser, create_gc_cycles, richards_super, bench_mp_pool, xml_etree_parse, asyncio_tcp_ssl, tomli_loads, richards, docutils, json_dumps, async_tree_cpu_io_mixed, async_tree_none, coverage, deltablue, unpickle


# HPT report

- Reliability score: 55.79% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
