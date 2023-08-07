
# Results vs. base

- fork: brandtbucher
- ref: justin
- machine: linux-x86_64
- commit hash: c209db9
- commit date: 2023-08-06
- overall geometric mean: 1.04x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 2.92 sec                                                                    | 3.03 sec: 1.04x slower                                              |
| tornado_http   | 120 ms                                                                      | 123 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                                       | 1.03x slower                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 259 ms                                                                      | 260 ms: 1.00x slower                                                |
| float          | 81.4 ms                                                                     | 85.3 ms: 1.05x slower                                               |
| nbody          | 87.7 ms                                                                     | 94.7 ms: 1.08x slower                                               |
| Geometric mean | (ref)                                                                       | 1.04x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 24.0 ms                                                                     | 24.4 ms: 1.02x slower                                               |
| regex_dna      | 238 ms                                                                      | 244 ms: 1.03x slower                                                |
| regex_effbot   | 3.42 ms                                                                     | 3.55 ms: 1.04x slower                                               |
| regex_compile  | 151 ms                                                                      | 160 ms: 1.06x slower                                                |
| Geometric mean | (ref)                                                                       | 1.04x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_list        | 4.87 us                                                                     | 4.68 us: 1.04x faster                                               |
| xml_etree_parse      | 153 ms                                                                      | 149 ms: 1.03x faster                                                |
| unpickle_pure_python | 239 us                                                                      | 237 us: 1.01x faster                                                |
| json_loads           | 25.6 us                                                                     | 25.7 us: 1.00x slower                                               |
| pickle_dict          | 31.9 us                                                                     | 32.3 us: 1.01x slower                                               |
| json_dumps           | 10.3 ms                                                                     | 10.5 ms: 1.02x slower                                               |
| xml_etree_process    | 60.3 ms                                                                     | 61.8 ms: 1.02x slower                                               |
| pickle               | 9.96 us                                                                     | 10.2 us: 1.03x slower                                               |
| xml_etree_generate   | 86.6 ms                                                                     | 89.2 ms: 1.03x slower                                               |
| pickle_list          | 4.25 us                                                                     | 4.45 us: 1.05x slower                                               |
| tomli_loads          | 2.42 sec                                                                    | 2.68 sec: 1.11x slower                                              |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                        |

Benchmark hidden because not significant (3): unpickle, xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 11.6 ms                                                                     | 11.6 ms: 1.00x slower                                               |
| python_startup_no_site | 8.62 ms                                                                     | 8.68 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|-----------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 10.3 ms                                                                     | 11.5 ms: 1.12x slower                                               |

All benchmarks:
===============

| Benchmark                | bm-20230806-pythonperf2-x86_64-python-9564e31cbc95a723f241-3.13.0a0-9564e31 | bm-20230806-pythonperf2-x86_64-brandtbucher-justin-3.13.0a0-c209db9 |
|--------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_list            | 4.87 us                                                                     | 4.68 us: 1.04x faster                                               |
| richards_super           | 62.5 ms                                                                     | 60.2 ms: 1.04x faster                                               |
| xml_etree_parse          | 153 ms                                                                      | 149 ms: 1.03x faster                                                |
| richards                 | 56.1 ms                                                                     | 55.0 ms: 1.02x faster                                               |
| create_gc_cycles         | 1.62 ms                                                                     | 1.59 ms: 1.02x faster                                               |
| json                     | 5.26 ms                                                                     | 5.20 ms: 1.01x faster                                               |
| unpickle_pure_python     | 239 us                                                                      | 237 us: 1.01x faster                                                |
| pidigits                 | 259 ms                                                                      | 260 ms: 1.00x slower                                                |
| python_startup           | 11.6 ms                                                                     | 11.6 ms: 1.00x slower                                               |
| json_loads               | 25.6 us                                                                     | 25.7 us: 1.00x slower                                               |
| logging_simple           | 7.00 us                                                                     | 7.04 us: 1.01x slower                                               |
| generators               | 37.4 ms                                                                     | 37.6 ms: 1.01x slower                                               |
| python_startup_no_site   | 8.62 ms                                                                     | 8.68 ms: 1.01x slower                                               |
| telco                    | 7.99 ms                                                                     | 8.04 ms: 1.01x slower                                               |
| coroutines               | 23.7 ms                                                                     | 23.9 ms: 1.01x slower                                               |
| deepcopy                 | 388 us                                                                      | 392 us: 1.01x slower                                                |
| coverage                 | 89.3 ms                                                                     | 90.3 ms: 1.01x slower                                               |
| pickle_dict              | 31.9 us                                                                     | 32.3 us: 1.01x slower                                               |
| async_tree_io            | 1.08 sec                                                                    | 1.10 sec: 1.01x slower                                              |
| pycparser                | 1.35 sec                                                                    | 1.37 sec: 1.01x slower                                              |
| dask                     | 588 ms                                                                      | 597 ms: 1.02x slower                                                |
| async_tree_cpu_io_mixed  | 719 ms                                                                      | 731 ms: 1.02x slower                                                |
| dulwich_log              | 68.2 ms                                                                     | 69.4 ms: 1.02x slower                                               |
| pathlib                  | 19.8 ms                                                                     | 20.1 ms: 1.02x slower                                               |
| regex_v8                 | 24.0 ms                                                                     | 24.4 ms: 1.02x slower                                               |
| json_dumps               | 10.3 ms                                                                     | 10.5 ms: 1.02x slower                                               |
| sqlite_synth             | 2.72 us                                                                     | 2.78 us: 1.02x slower                                               |
| async_tree_none          | 471 ms                                                                      | 481 ms: 1.02x slower                                                |
| scimark_monte_carlo      | 69.0 ms                                                                     | 70.6 ms: 1.02x slower                                               |
| xml_etree_process        | 60.3 ms                                                                     | 61.8 ms: 1.02x slower                                               |
| sqlglot_transpile        | 1.86 ms                                                                     | 1.90 ms: 1.02x slower                                               |
| async_tree_memoization   | 570 ms                                                                      | 585 ms: 1.03x slower                                                |
| tornado_http             | 120 ms                                                                      | 123 ms: 1.03x slower                                                |
| regex_dna                | 238 ms                                                                      | 244 ms: 1.03x slower                                                |
| pickle                   | 9.96 us                                                                     | 10.2 us: 1.03x slower                                               |
| sqlglot_parse            | 1.44 ms                                                                     | 1.49 ms: 1.03x slower                                               |
| xml_etree_generate       | 86.6 ms                                                                     | 89.2 ms: 1.03x slower                                               |
| scimark_sor              | 145 ms                                                                      | 150 ms: 1.03x slower                                                |
| mypy2                    | 374 ms                                                                      | 385 ms: 1.03x slower                                                |
| logging_silent           | 97.2 ns                                                                     | 100 ns: 1.03x slower                                                |
| sqlglot_normalize        | 118 ms                                                                      | 122 ms: 1.03x slower                                                |
| pyflate                  | 519 ms                                                                      | 537 ms: 1.03x slower                                                |
| docutils                 | 2.92 sec                                                                    | 3.03 sec: 1.04x slower                                              |
| raytrace                 | 283 ms                                                                      | 294 ms: 1.04x slower                                                |
| bench_thread_pool        | 956 us                                                                      | 993 us: 1.04x slower                                                |
| regex_effbot             | 3.42 ms                                                                     | 3.55 ms: 1.04x slower                                               |
| sqlglot_optimize         | 59.1 ms                                                                     | 61.8 ms: 1.05x slower                                               |
| typing_runtime_protocols | 153 us                                                                      | 160 us: 1.05x slower                                                |
| pickle_list              | 4.25 us                                                                     | 4.45 us: 1.05x slower                                               |
| async_generators         | 392 ms                                                                      | 411 ms: 1.05x slower                                                |
| float                    | 81.4 ms                                                                     | 85.3 ms: 1.05x slower                                               |
| spectral_norm            | 97.7 ms                                                                     | 103 ms: 1.05x slower                                                |
| mdp                      | 2.60 sec                                                                    | 2.74 sec: 1.05x slower                                              |
| go                       | 177 ms                                                                      | 186 ms: 1.05x slower                                                |
| crypto_pyaes             | 73.2 ms                                                                     | 77.6 ms: 1.06x slower                                               |
| regex_compile            | 151 ms                                                                      | 160 ms: 1.06x slower                                                |
| pprint_safe_repr         | 811 ms                                                                      | 861 ms: 1.06x slower                                                |
| deltablue                | 3.66 ms                                                                     | 3.89 ms: 1.06x slower                                               |
| pprint_pformat           | 1.65 sec                                                                    | 1.77 sec: 1.07x slower                                              |
| scimark_lu               | 98.5 ms                                                                     | 106 ms: 1.08x slower                                                |
| chaos                    | 62.5 ms                                                                     | 67.4 ms: 1.08x slower                                               |
| nbody                    | 87.7 ms                                                                     | 94.7 ms: 1.08x slower                                               |
| meteor_contest           | 131 ms                                                                      | 143 ms: 1.09x slower                                                |
| deepcopy_memo            | 38.1 us                                                                     | 41.6 us: 1.09x slower                                               |
| scimark_fft              | 308 ms                                                                      | 339 ms: 1.10x slower                                                |
| tomli_loads              | 2.42 sec                                                                    | 2.68 sec: 1.11x slower                                              |
| mako                     | 10.3 ms                                                                     | 11.5 ms: 1.12x slower                                               |
| gc_traversal             | 3.50 ms                                                                     | 3.95 ms: 1.13x slower                                               |
| nqueens                  | 91.3 ms                                                                     | 109 ms: 1.20x slower                                                |
| fannkuch                 | 392 ms                                                                      | 471 ms: 1.20x slower                                                |
| unpack_sequence          | 46.5 ns                                                                     | 56.4 ns: 1.21x slower                                               |
| comprehensions           | 22.0 us                                                                     | 27.2 us: 1.24x slower                                               |
| hexiom                   | 6.42 ms                                                                     | 8.05 ms: 1.25x slower                                               |
| scimark_sparse_mat_mult  | 4.29 ms                                                                     | 5.65 ms: 1.32x slower                                               |
| Geometric mean           | (ref)                                                                       | 1.04x slower                                                        |

Benchmark hidden because not significant (8): logging_format, unpickle, asyncio_tcp_ssl, deepcopy_reduce, asyncio_tcp, xml_etree_iterparse, pickle_pure_python, bench_mp_pool
