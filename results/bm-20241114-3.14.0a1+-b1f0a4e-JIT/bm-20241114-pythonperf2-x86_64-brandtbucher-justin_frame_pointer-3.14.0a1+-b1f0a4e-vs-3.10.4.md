# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_frame_pointer
- machine: linux-x86_64
- commit hash: b1f0a4e
- commit date: 2024-11-14
- overall geometric mean: 1.219x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 330 ms: 1.06x faster                                                               |
| docutils       | 3.41 sec                                                     | 3.24 sec: 1.05x faster                                                             |
| html5lib       | 94.6 ms                                                      | 72.2 ms: 1.31x faster                                                              |
| Geometric mean | (ref)                                                        | 1.14x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 345 ms: 2.01x faster                                                               |
| async_tree_memoization  | 819 ms                                                       | 424 ms: 1.93x faster                                                               |
| async_tree_io           | 1.60 sec                                                     | 861 ms: 1.86x faster                                                               |
| async_tree_cpu_io_mixed | 936 ms                                                       | 588 ms: 1.59x faster                                                               |
| Geometric mean          | (ref)                                                        | 1.84x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 91.2 ms: 1.47x faster                                                              |
| float          | 111 ms                                                       | 81.1 ms: 1.37x faster                                                              |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                               |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 153 ms: 1.24x faster                                                               |
| regex_dna      | 261 ms                                                       | 257 ms: 1.02x faster                                                               |
| regex_v8       | 27.2 ms                                                      | 26.8 ms: 1.01x faster                                                              |
| regex_effbot   | 3.09 ms                                                      | 3.70 ms: 1.20x slower                                                              |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 228 us: 1.37x faster                                                               |
| tomli_loads          | 2.92 sec                                                     | 2.22 sec: 1.31x faster                                                             |
| pickle_pure_python   | 455 us                                                       | 351 us: 1.30x faster                                                               |
| json_dumps           | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                              |
| json_loads           | 30.3 us                                                      | 24.5 us: 1.24x faster                                                              |
| xml_etree_process    | 75.9 ms                                                      | 61.3 ms: 1.24x faster                                                              |
| xml_etree_parse      | 160 ms                                                       | 147 ms: 1.09x faster                                                               |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.08x faster                                                               |
| xml_etree_generate   | 92.3 ms                                                      | 86.3 ms: 1.07x faster                                                              |
| Geometric mean       | (ref)                                                        | 1.21x faster                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.08 ms: 1.24x slower                                                              |
| python_startup         | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                              |
| Geometric mean         | (ref)                                                        | 1.32x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                              |
| django_template | 50.2 ms                                                      | 44.0 ms: 1.14x faster                                                              |
| genshi_text     | 31.4 ms                                                      | 30.7 ms: 1.03x faster                                                              |
| genshi_xml      | 63.3 ms                                                      | 67.6 ms: 1.07x slower                                                              |
| Geometric mean  | (ref)                                                        | 1.12x faster                                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 186 us: 2.89x faster                                                               |
| deltablue                | 7.50 ms                                                      | 3.55 ms: 2.11x faster                                                              |
| async_tree_none          | 692 ms                                                       | 345 ms: 2.01x faster                                                               |
| async_tree_memoization   | 819 ms                                                       | 424 ms: 1.93x faster                                                               |
| async_tree_io            | 1.60 sec                                                     | 861 ms: 1.86x faster                                                               |
| logging_silent           | 167 ns                                                       | 100 ns: 1.67x faster                                                               |
| scimark_lu               | 167 ms                                                       | 102 ms: 1.64x faster                                                               |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 588 ms: 1.59x faster                                                               |
| go                       | 262 ms                                                       | 165 ms: 1.58x faster                                                               |
| richards_super           | 90.6 ms                                                      | 58.6 ms: 1.55x faster                                                              |
| raytrace                 | 489 ms                                                       | 318 ms: 1.54x faster                                                               |
| scimark_sor              | 180 ms                                                       | 117 ms: 1.54x faster                                                               |
| chaos                    | 109 ms                                                       | 70.9 ms: 1.53x faster                                                              |
| crypto_pyaes             | 119 ms                                                       | 78.1 ms: 1.52x faster                                                              |
| richards                 | 75.1 ms                                                      | 50.8 ms: 1.48x faster                                                              |
| deepcopy_memo            | 49.8 us                                                      | 33.8 us: 1.47x faster                                                              |
| nbody                    | 134 ms                                                       | 91.2 ms: 1.47x faster                                                              |
| sqlglot_parse            | 2.24 ms                                                      | 1.53 ms: 1.47x faster                                                              |
| scimark_monte_carlo      | 107 ms                                                       | 73.8 ms: 1.46x faster                                                              |
| mako                     | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                              |
| pylint                   | 566 ms                                                       | 392 ms: 1.44x faster                                                               |
| deepcopy                 | 468 us                                                       | 325 us: 1.44x faster                                                               |
| pyflate                  | 733 ms                                                       | 511 ms: 1.43x faster                                                               |
| coroutines               | 30.3 ms                                                      | 21.5 ms: 1.41x faster                                                              |
| spectral_norm            | 139 ms                                                       | 101 ms: 1.38x faster                                                               |
| unpickle_pure_python     | 312 us                                                       | 228 us: 1.37x faster                                                               |
| float                    | 111 ms                                                       | 81.1 ms: 1.37x faster                                                              |
| sqlglot_transpile        | 2.68 ms                                                      | 2.03 ms: 1.32x faster                                                              |
| generators               | 57.3 ms                                                      | 43.4 ms: 1.32x faster                                                              |
| logging_format           | 9.64 us                                                      | 7.31 us: 1.32x faster                                                              |
| pathlib                  | 21.4 ms                                                      | 16.3 ms: 1.31x faster                                                              |
| html5lib                 | 94.6 ms                                                      | 72.2 ms: 1.31x faster                                                              |
| tomli_loads              | 2.92 sec                                                     | 2.22 sec: 1.31x faster                                                             |
| logging_simple           | 8.88 us                                                      | 6.78 us: 1.31x faster                                                              |
| pickle_pure_python       | 455 us                                                       | 351 us: 1.30x faster                                                               |
| pycparser                | 1.67 sec                                                     | 1.29 sec: 1.30x faster                                                             |
| thrift                   | 1.18 ms                                                      | 909 us: 1.29x faster                                                               |
| deepcopy_reduce          | 4.01 us                                                      | 3.17 us: 1.26x faster                                                              |
| json_dumps               | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                              |
| pprint_safe_repr         | 1.05 sec                                                     | 837 ms: 1.25x faster                                                               |
| pprint_pformat           | 2.15 sec                                                     | 1.73 sec: 1.25x faster                                                             |
| regex_compile            | 190 ms                                                       | 153 ms: 1.24x faster                                                               |
| json_loads               | 30.3 us                                                      | 24.5 us: 1.24x faster                                                              |
| xml_etree_process        | 75.9 ms                                                      | 61.3 ms: 1.24x faster                                                              |
| comprehensions           | 26.7 us                                                      | 21.7 us: 1.23x faster                                                              |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.8 ms: 1.21x faster                                                              |
| dulwich_log              | 81.1 ms                                                      | 67.6 ms: 1.20x faster                                                              |
| fannkuch                 | 483 ms                                                       | 403 ms: 1.20x faster                                                               |
| hexiom                   | 9.42 ms                                                      | 7.96 ms: 1.18x faster                                                              |
| bench_thread_pool        | 1.14 ms                                                      | 998 us: 1.14x faster                                                               |
| django_template          | 50.2 ms                                                      | 44.0 ms: 1.14x faster                                                              |
| mdp                      | 3.01 sec                                                     | 2.65 sec: 1.14x faster                                                             |
| json                     | 5.86 ms                                                      | 5.21 ms: 1.12x faster                                                              |
| sqlalchemy_declarative   | 190 ms                                                       | 170 ms: 1.12x faster                                                               |
| scimark_fft              | 361 ms                                                       | 326 ms: 1.11x faster                                                               |
| sympy_expand             | 600 ms                                                       | 548 ms: 1.10x faster                                                               |
| xml_etree_parse          | 160 ms                                                       | 147 ms: 1.09x faster                                                               |
| xml_etree_iterparse      | 110 ms                                                       | 102 ms: 1.08x faster                                                               |
| sympy_str                | 360 ms                                                       | 332 ms: 1.08x faster                                                               |
| pidigits                 | 271 ms                                                       | 252 ms: 1.08x faster                                                               |
| xml_etree_generate       | 92.3 ms                                                      | 86.3 ms: 1.07x faster                                                              |
| sympy_sum                | 193 ms                                                       | 181 ms: 1.07x faster                                                               |
| 2to3                     | 350 ms                                                       | 330 ms: 1.06x faster                                                               |
| docutils                 | 3.41 sec                                                     | 3.24 sec: 1.05x faster                                                             |
| nqueens                  | 115 ms                                                       | 110 ms: 1.05x faster                                                               |
| sqlite_synth             | 2.99 us                                                      | 2.85 us: 1.05x faster                                                              |
| genshi_text              | 31.4 ms                                                      | 30.7 ms: 1.03x faster                                                              |
| meteor_contest           | 138 ms                                                       | 135 ms: 1.02x faster                                                               |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.00 ms: 1.02x faster                                                              |
| regex_dna                | 261 ms                                                       | 257 ms: 1.02x faster                                                               |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                               |
| regex_v8                 | 27.2 ms                                                      | 26.8 ms: 1.01x faster                                                              |
| sqlglot_optimize         | 70.1 ms                                                      | 74.3 ms: 1.06x slower                                                              |
| genshi_xml               | 63.3 ms                                                      | 67.6 ms: 1.07x slower                                                              |
| telco                    | 7.23 ms                                                      | 7.89 ms: 1.09x slower                                                              |
| async_generators         | 421 ms                                                       | 479 ms: 1.14x slower                                                               |
| regex_effbot             | 3.09 ms                                                      | 3.70 ms: 1.20x slower                                                              |
| python_startup_no_site   | 7.33 ms                                                      | 9.08 ms: 1.24x slower                                                              |
| coverage                 | 63.3 ms                                                      | 78.8 ms: 1.25x slower                                                              |
| python_startup           | 11.5 ms                                                      | 16.1 ms: 1.40x slower                                                              |
| create_gc_cycles         | 1.76 ms                                                      | 2.90 ms: 1.65x slower                                                              |
| gc_traversal             | 3.42 ms                                                      | 6.29 ms: 1.84x slower                                                              |
| bench_mp_pool            | 6.37 ms                                                      | 1.37 sec: 215.48x slower                                                           |
| Geometric mean           | (ref)                                                        | 1.15x faster                                                                       |

Benchmark hidden because not significant (2): sympy_integrate, sqlglot_normalize
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241114-3.14.0a1+-b1f0a4e-JIT/bm-20241114-pythonperf2-x86_64-brandtbucher-justin_frame_pointer-3.14.0a1+-b1f0a4e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.219x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.35x