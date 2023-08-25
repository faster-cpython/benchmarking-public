
# Results vs. base

- fork: brandtbucher
- ref: uops_enabled
- machine: linux-x86_64
- commit hash: 9016d52
- commit date: 2023-08-06
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 2.64 sec                                                              | 2.75 sec: 1.04x slower                                              |
| tornado_http   | 95.2 ms                                                               | 97.3 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 201 ms                                                                | 201 ms: 1.00x slower                                                |
| float          | 79.3 ms                                                               | 84.5 ms: 1.07x slower                                               |
| nbody          | 88.0 ms                                                               | 96.6 ms: 1.10x slower                                               |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 22.6 ms                                                               | 22.3 ms: 1.01x faster                                               |
| regex_effbot   | 3.52 ms                                                               | 3.51 ms: 1.00x faster                                               |
| regex_dna      | 204 ms                                                                | 211 ms: 1.03x slower                                                |
| regex_compile  | 136 ms                                                                | 152 ms: 1.12x slower                                                |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads           | 25.4 us                                                               | 25.5 us: 1.01x slower                                               |
| pickle_dict          | 31.9 us                                                               | 32.1 us: 1.01x slower                                               |
| pickle_pure_python   | 297 us                                                                | 300 us: 1.01x slower                                                |
| pickle_list          | 4.55 us                                                               | 4.60 us: 1.01x slower                                               |
| xml_etree_iterparse  | 103 ms                                                                | 106 ms: 1.03x slower                                                |
| xml_etree_process    | 57.8 ms                                                               | 59.7 ms: 1.03x slower                                               |
| pickle               | 10.3 us                                                               | 10.6 us: 1.03x slower                                               |
| json_dumps           | 9.64 ms                                                               | 9.98 ms: 1.04x slower                                               |
| xml_etree_generate   | 83.6 ms                                                               | 86.6 ms: 1.04x slower                                               |
| unpickle_pure_python | 212 us                                                                | 224 us: 1.06x slower                                                |
| tomli_loads          | 2.29 sec                                                              | 2.66 sec: 1.16x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                        |

Benchmark hidden because not significant (3): unpickle, xml_etree_parse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.87 ms                                                               | 6.88 ms: 1.00x slower                                               |
| python_startup         | 9.38 ms                                                               | 9.42 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|-----------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 10.8 ms                                                               | 12.0 ms: 1.12x slower                                               |

All benchmarks:
===============

| Benchmark                | bm-20230806-linux-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-linux-x86_64-brandtbucher-uops_enabled-3.13.0a0-9016d52 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| coverage                 | 95.2 ms                                                               | 92.3 ms: 1.03x faster                                               |
| logging_silent           | 105 ns                                                                | 103 ns: 1.02x faster                                                |
| regex_v8                 | 22.6 ms                                                               | 22.3 ms: 1.01x faster                                               |
| regex_effbot             | 3.52 ms                                                               | 3.51 ms: 1.00x faster                                               |
| create_gc_cycles         | 1.52 ms                                                               | 1.51 ms: 1.00x faster                                               |
| pidigits                 | 201 ms                                                                | 201 ms: 1.00x slower                                                |
| python_startup_no_site   | 6.87 ms                                                               | 6.88 ms: 1.00x slower                                               |
| python_startup           | 9.38 ms                                                               | 9.42 ms: 1.00x slower                                               |
| deepcopy                 | 357 us                                                                | 360 us: 1.01x slower                                                |
| asyncio_tcp_ssl          | 1.79 sec                                                              | 1.80 sec: 1.01x slower                                              |
| json_loads               | 25.4 us                                                               | 25.5 us: 1.01x slower                                               |
| pickle_dict              | 31.9 us                                                               | 32.1 us: 1.01x slower                                               |
| pickle_pure_python       | 297 us                                                                | 300 us: 1.01x slower                                                |
| pickle_list              | 4.55 us                                                               | 4.60 us: 1.01x slower                                               |
| async_tree_io            | 1.19 sec                                                              | 1.20 sec: 1.01x slower                                              |
| richards                 | 48.4 ms                                                               | 48.9 ms: 1.01x slower                                               |
| json                     | 4.77 ms                                                               | 4.83 ms: 1.01x slower                                               |
| scimark_monte_carlo      | 67.8 ms                                                               | 68.9 ms: 1.02x slower                                               |
| async_tree_memoization   | 584 ms                                                                | 594 ms: 1.02x slower                                                |
| telco                    | 7.79 ms                                                               | 7.93 ms: 1.02x slower                                               |
| logging_simple           | 5.94 us                                                               | 6.06 us: 1.02x slower                                               |
| async_tree_none          | 479 ms                                                                | 489 ms: 1.02x slower                                                |
| tornado_http             | 95.2 ms                                                               | 97.3 ms: 1.02x slower                                               |
| sqlite_synth             | 2.75 us                                                               | 2.81 us: 1.02x slower                                               |
| gc_traversal             | 3.84 ms                                                               | 3.93 ms: 1.02x slower                                               |
| logging_format           | 6.48 us                                                               | 6.66 us: 1.03x slower                                               |
| dask                     | 518 ms                                                                | 532 ms: 1.03x slower                                                |
| asyncio_tcp              | 476 ms                                                                | 489 ms: 1.03x slower                                                |
| richards_super           | 54.2 ms                                                               | 55.8 ms: 1.03x slower                                               |
| xml_etree_iterparse      | 103 ms                                                                | 106 ms: 1.03x slower                                                |
| dulwich_log              | 65.5 ms                                                               | 67.6 ms: 1.03x slower                                               |
| xml_etree_process        | 57.8 ms                                                               | 59.7 ms: 1.03x slower                                               |
| regex_dna                | 204 ms                                                                | 211 ms: 1.03x slower                                                |
| pickle                   | 10.3 us                                                               | 10.6 us: 1.03x slower                                               |
| sqlglot_transpile        | 1.60 ms                                                               | 1.65 ms: 1.03x slower                                               |
| json_dumps               | 9.64 ms                                                               | 9.98 ms: 1.04x slower                                               |
| scimark_sor              | 120 ms                                                                | 125 ms: 1.04x slower                                                |
| mypy2                    | 334 ms                                                                | 346 ms: 1.04x slower                                                |
| mdp                      | 2.63 sec                                                              | 2.73 sec: 1.04x slower                                              |
| scimark_lu               | 113 ms                                                                | 117 ms: 1.04x slower                                                |
| xml_etree_generate       | 83.6 ms                                                               | 86.6 ms: 1.04x slower                                               |
| sqlglot_parse            | 1.28 ms                                                               | 1.33 ms: 1.04x slower                                               |
| pathlib                  | 18.4 ms                                                               | 19.2 ms: 1.04x slower                                               |
| async_generators         | 443 ms                                                                | 462 ms: 1.04x slower                                                |
| pprint_safe_repr         | 713 ms                                                                | 744 ms: 1.04x slower                                                |
| typing_runtime_protocols | 143 us                                                                | 150 us: 1.04x slower                                                |
| docutils                 | 2.64 sec                                                              | 2.75 sec: 1.04x slower                                              |
| pycparser                | 1.16 sec                                                              | 1.21 sec: 1.04x slower                                              |
| bench_thread_pool        | 823 us                                                                | 859 us: 1.04x slower                                                |
| sqlglot_normalize        | 105 ms                                                                | 110 ms: 1.05x slower                                                |
| pprint_pformat           | 1.46 sec                                                              | 1.53 sec: 1.05x slower                                              |
| sqlglot_optimize         | 52.7 ms                                                               | 55.2 ms: 1.05x slower                                               |
| raytrace                 | 271 ms                                                                | 283 ms: 1.05x slower                                                |
| spectral_norm            | 105 ms                                                                | 110 ms: 1.05x slower                                                |
| unpickle_pure_python     | 212 us                                                                | 224 us: 1.06x slower                                                |
| coroutines               | 21.7 ms                                                               | 23.0 ms: 1.06x slower                                               |
| float                    | 79.3 ms                                                               | 84.5 ms: 1.07x slower                                               |
| crypto_pyaes             | 70.2 ms                                                               | 74.9 ms: 1.07x slower                                               |
| go                       | 139 ms                                                                | 149 ms: 1.07x slower                                                |
| deepcopy_memo            | 38.6 us                                                               | 41.8 us: 1.08x slower                                               |
| scimark_fft              | 353 ms                                                                | 382 ms: 1.08x slower                                                |
| meteor_contest           | 107 ms                                                                | 116 ms: 1.09x slower                                                |
| unpack_sequence          | 45.5 ns                                                               | 49.8 ns: 1.09x slower                                               |
| nbody                    | 88.0 ms                                                               | 96.6 ms: 1.10x slower                                               |
| pyflate                  | 450 ms                                                                | 498 ms: 1.11x slower                                                |
| mako                     | 10.8 ms                                                               | 12.0 ms: 1.12x slower                                               |
| regex_compile            | 136 ms                                                                | 152 ms: 1.12x slower                                                |
| chaos                    | 59.3 ms                                                               | 66.3 ms: 1.12x slower                                               |
| deltablue                | 3.19 ms                                                               | 3.63 ms: 1.14x slower                                               |
| tomli_loads              | 2.29 sec                                                              | 2.66 sec: 1.16x slower                                              |
| fannkuch                 | 388 ms                                                                | 455 ms: 1.17x slower                                                |
| comprehensions           | 20.2 us                                                               | 24.6 us: 1.22x slower                                               |
| nqueens                  | 79.6 ms                                                               | 98.8 ms: 1.24x slower                                               |
| hexiom                   | 6.07 ms                                                               | 7.60 ms: 1.25x slower                                               |
| scimark_sparse_mat_mult  | 4.62 ms                                                               | 5.84 ms: 1.26x slower                                               |
| Geometric mean           | (ref)                                                                 | 1.05x slower                                                        |

Benchmark hidden because not significant (7): unpickle, xml_etree_parse, deepcopy_reduce, bench_mp_pool, unpickle_list, generators, async_tree_cpu_io_mixed


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x
