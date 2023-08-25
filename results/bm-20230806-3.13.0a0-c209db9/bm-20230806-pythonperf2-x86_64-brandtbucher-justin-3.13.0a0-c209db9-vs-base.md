
# Results vs. base

- fork: brandtbucher
- ref: justin
- machine: linux-x86_64
- commit hash: c209db9
- commit date: 2023-08-06
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 2.93 sec                                                                    | 3.03 sec: 1.03x slower                                              |
| tornado_http   | 121 ms                                                                      | 123 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 260 ms                                                                      | 260 ms: 1.00x faster                                                |
| float          | 81.2 ms                                                                     | 85.3 ms: 1.05x slower                                               |
| nbody          | 87.3 ms                                                                     | 94.7 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                                       | 1.04x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.68 ms                                                                     | 3.55 ms: 1.03x faster                                               |
| regex_dna      | 246 ms                                                                      | 244 ms: 1.01x faster                                                |
| regex_v8       | 23.6 ms                                                                     | 24.4 ms: 1.03x slower                                               |
| regex_compile  | 152 ms                                                                      | 160 ms: 1.06x slower                                                |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle             | 15.3 us                                                                     | 14.7 us: 1.04x faster                                               |
| xml_etree_parse      | 152 ms                                                                      | 149 ms: 1.02x faster                                                |
| unpickle_list        | 4.73 us                                                                     | 4.68 us: 1.01x faster                                               |
| json_loads           | 25.4 us                                                                     | 25.7 us: 1.01x slower                                               |
| json_dumps           | 10.4 ms                                                                     | 10.5 ms: 1.01x slower                                               |
| pickle_dict          | 31.8 us                                                                     | 32.3 us: 1.02x slower                                               |
| xml_etree_iterparse  | 107 ms                                                                      | 109 ms: 1.02x slower                                                |
| pickle_pure_python   | 317 us                                                                      | 324 us: 1.02x slower                                                |
| xml_etree_process    | 60.3 ms                                                                     | 61.8 ms: 1.02x slower                                               |
| pickle               | 9.96 us                                                                     | 10.2 us: 1.03x slower                                               |
| xml_etree_generate   | 86.1 ms                                                                     | 89.2 ms: 1.04x slower                                               |
| unpickle_pure_python | 224 us                                                                      | 237 us: 1.06x slower                                                |
| pickle_list          | 4.17 us                                                                     | 4.45 us: 1.07x slower                                               |
| tomli_loads          | 2.39 sec                                                                    | 2.68 sec: 1.12x slower                                              |
| Geometric mean       | (ref)                                                                       | 1.02x slower                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 11.6 ms                                                                     | 11.6 ms: 1.00x slower                                               |
| python_startup_no_site | 8.63 ms                                                                     | 8.68 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|-----------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 10.4 ms                                                                     | 11.5 ms: 1.11x slower                                               |

All benchmarks:
===============

| Benchmark                | bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|--------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle                 | 15.3 us                                                                     | 14.7 us: 1.04x faster                                               |
| richards_super           | 62.4 ms                                                                     | 60.2 ms: 1.04x faster                                               |
| regex_effbot             | 3.68 ms                                                                     | 3.55 ms: 1.03x faster                                               |
| create_gc_cycles         | 1.63 ms                                                                     | 1.59 ms: 1.03x faster                                               |
| xml_etree_parse          | 152 ms                                                                      | 149 ms: 1.02x faster                                                |
| coverage                 | 92.3 ms                                                                     | 90.3 ms: 1.02x faster                                               |
| unpickle_list            | 4.73 us                                                                     | 4.68 us: 1.01x faster                                               |
| regex_dna                | 246 ms                                                                      | 244 ms: 1.01x faster                                                |
| deepcopy_reduce          | 3.53 us                                                                     | 3.50 us: 1.01x faster                                               |
| pidigits                 | 260 ms                                                                      | 260 ms: 1.00x faster                                                |
| python_startup           | 11.6 ms                                                                     | 11.6 ms: 1.00x slower                                               |
| python_startup_no_site   | 8.63 ms                                                                     | 8.68 ms: 1.01x slower                                               |
| json                     | 5.17 ms                                                                     | 5.20 ms: 1.01x slower                                               |
| sqlite_synth             | 2.76 us                                                                     | 2.78 us: 1.01x slower                                               |
| json_loads               | 25.4 us                                                                     | 25.7 us: 1.01x slower                                               |
| dulwich_log              | 68.6 ms                                                                     | 69.4 ms: 1.01x slower                                               |
| dask                     | 590 ms                                                                      | 597 ms: 1.01x slower                                                |
| async_generators         | 406 ms                                                                      | 411 ms: 1.01x slower                                                |
| json_dumps               | 10.4 ms                                                                     | 10.5 ms: 1.01x slower                                               |
| pickle_dict              | 31.8 us                                                                     | 32.3 us: 1.02x slower                                               |
| logging_silent           | 98.7 ns                                                                     | 100 ns: 1.02x slower                                                |
| tornado_http             | 121 ms                                                                      | 123 ms: 1.02x slower                                                |
| generators               | 37.0 ms                                                                     | 37.6 ms: 1.02x slower                                               |
| async_tree_io            | 1.08 sec                                                                    | 1.10 sec: 1.02x slower                                              |
| xml_etree_iterparse      | 107 ms                                                                      | 109 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed  | 716 ms                                                                      | 731 ms: 1.02x slower                                                |
| scimark_sor              | 147 ms                                                                      | 150 ms: 1.02x slower                                                |
| pickle_pure_python       | 317 us                                                                      | 324 us: 1.02x slower                                                |
| xml_etree_process        | 60.3 ms                                                                     | 61.8 ms: 1.02x slower                                               |
| async_tree_none          | 468 ms                                                                      | 481 ms: 1.03x slower                                                |
| pickle                   | 9.96 us                                                                     | 10.2 us: 1.03x slower                                               |
| async_tree_memoization   | 567 ms                                                                      | 585 ms: 1.03x slower                                                |
| bench_thread_pool        | 963 us                                                                      | 993 us: 1.03x slower                                                |
| docutils                 | 2.93 sec                                                                    | 3.03 sec: 1.03x slower                                              |
| regex_v8                 | 23.6 ms                                                                     | 24.4 ms: 1.03x slower                                               |
| sqlglot_parse            | 1.44 ms                                                                     | 1.49 ms: 1.03x slower                                               |
| sqlglot_transpile        | 1.84 ms                                                                     | 1.90 ms: 1.03x slower                                               |
| sqlglot_normalize        | 118 ms                                                                      | 122 ms: 1.03x slower                                                |
| unpack_sequence          | 54.5 ns                                                                     | 56.4 ns: 1.03x slower                                               |
| mypy2                    | 372 ms                                                                      | 385 ms: 1.03x slower                                                |
| pycparser                | 1.32 sec                                                                    | 1.37 sec: 1.04x slower                                              |
| logging_simple           | 6.80 us                                                                     | 7.04 us: 1.04x slower                                               |
| xml_etree_generate       | 86.1 ms                                                                     | 89.2 ms: 1.04x slower                                               |
| scimark_monte_carlo      | 67.9 ms                                                                     | 70.6 ms: 1.04x slower                                               |
| logging_format           | 7.34 us                                                                     | 7.66 us: 1.04x slower                                               |
| pprint_safe_repr         | 825 ms                                                                      | 861 ms: 1.04x slower                                                |
| pyflate                  | 514 ms                                                                      | 537 ms: 1.04x slower                                                |
| sqlglot_optimize         | 59.1 ms                                                                     | 61.8 ms: 1.05x slower                                               |
| pathlib                  | 19.2 ms                                                                     | 20.1 ms: 1.05x slower                                               |
| pprint_pformat           | 1.69 sec                                                                    | 1.77 sec: 1.05x slower                                              |
| float                    | 81.2 ms                                                                     | 85.3 ms: 1.05x slower                                               |
| regex_compile            | 152 ms                                                                      | 160 ms: 1.06x slower                                                |
| typing_runtime_protocols | 151 us                                                                      | 160 us: 1.06x slower                                                |
| unpickle_pure_python     | 224 us                                                                      | 237 us: 1.06x slower                                                |
| deltablue                | 3.66 ms                                                                     | 3.89 ms: 1.06x slower                                               |
| mdp                      | 2.57 sec                                                                    | 2.74 sec: 1.06x slower                                              |
| crypto_pyaes             | 72.9 ms                                                                     | 77.6 ms: 1.06x slower                                               |
| pickle_list              | 4.17 us                                                                     | 4.45 us: 1.07x slower                                               |
| raytrace                 | 275 ms                                                                      | 294 ms: 1.07x slower                                                |
| deepcopy_memo            | 38.9 us                                                                     | 41.6 us: 1.07x slower                                               |
| chaos                    | 63.0 ms                                                                     | 67.4 ms: 1.07x slower                                               |
| go                       | 173 ms                                                                      | 186 ms: 1.07x slower                                                |
| scimark_lu               | 98.5 ms                                                                     | 106 ms: 1.08x slower                                                |
| meteor_contest           | 133 ms                                                                      | 143 ms: 1.08x slower                                                |
| spectral_norm            | 94.9 ms                                                                     | 103 ms: 1.08x slower                                                |
| nbody                    | 87.3 ms                                                                     | 94.7 ms: 1.08x slower                                               |
| gc_traversal             | 3.58 ms                                                                     | 3.95 ms: 1.10x slower                                               |
| mako                     | 10.4 ms                                                                     | 11.5 ms: 1.11x slower                                               |
| scimark_fft              | 306 ms                                                                      | 339 ms: 1.11x slower                                                |
| tomli_loads              | 2.39 sec                                                                    | 2.68 sec: 1.12x slower                                              |
| nqueens                  | 91.5 ms                                                                     | 109 ms: 1.20x slower                                                |
| fannkuch                 | 389 ms                                                                      | 471 ms: 1.21x slower                                                |
| comprehensions           | 21.9 us                                                                     | 27.2 us: 1.24x slower                                               |
| hexiom                   | 6.47 ms                                                                     | 8.05 ms: 1.24x slower                                               |
| scimark_sparse_mat_mult  | 4.17 ms                                                                     | 5.65 ms: 1.35x slower                                               |
| Geometric mean           | (ref)                                                                       | 1.04x slower                                                        |

Benchmark hidden because not significant (7): bench_mp_pool, richards, asyncio_tcp, asyncio_tcp_ssl, coroutines, deepcopy, telco


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x
