# Results vs. 3.10.4

- fork: brandtbucher
- ref: hack_night
- machine: linux-x86_64
- commit hash: b856d47
- commit date: 2025-02-22
- overall geometric mean: 1.332x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 291 ms: 1.20x faster                                                    |
| docutils       | 3.41 sec                                                     | 2.96 sec: 1.15x faster                                                  |
| html5lib       | 94.6 ms                                                      | 68.5 ms: 1.38x faster                                                   |
| Geometric mean | (ref)                                                        | 1.24x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 640 ms: 2.50x faster                                                    |
| async_tree_none         | 692 ms                                                       | 291 ms: 2.37x faster                                                    |
| async_tree_memoization  | 819 ms                                                       | 353 ms: 2.32x faster                                                    |
| async_tree_cpu_io_mixed | 936 ms                                                       | 524 ms: 1.79x faster                                                    |
| Geometric mean          | (ref)                                                        | 2.23x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 111 ms                                                       | 69.5 ms: 1.60x faster                                                   |
| nbody          | 134 ms                                                       | 100.0 ms: 1.34x faster                                                  |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                        | 1.32x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 136 ms: 1.40x faster                                                    |
| regex_dna      | 261 ms                                                       | 238 ms: 1.10x faster                                                    |
| regex_v8       | 27.2 ms                                                      | 25.5 ms: 1.07x faster                                                   |
| regex_effbot   | 3.09 ms                                                      | 3.13 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.13x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 206 us: 1.51x faster                                                    |
| tomli_loads          | 2.92 sec                                                     | 2.02 sec: 1.44x faster                                                  |
| xml_etree_process    | 75.9 ms                                                      | 55.9 ms: 1.36x faster                                                   |
| pickle_pure_python   | 455 us                                                       | 337 us: 1.35x faster                                                    |
| json_dumps           | 14.5 ms                                                      | 11.8 ms: 1.24x faster                                                   |
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                    |
| xml_etree_generate   | 92.3 ms                                                      | 79.8 ms: 1.16x faster                                                   |
| xml_etree_iterparse  | 110 ms                                                       | 96.6 ms: 1.14x faster                                                   |
| json_loads           | 30.3 us                                                      | 26.6 us: 1.14x faster                                                   |
| Geometric mean       | (ref)                                                        | 1.27x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                   |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.61 ms: 1.53x faster                                                   |
| django_template | 50.2 ms                                                      | 36.3 ms: 1.38x faster                                                   |
| genshi_text     | 31.4 ms                                                      | 25.0 ms: 1.26x faster                                                   |
| genshi_xml      | 63.3 ms                                                      | 58.3 ms: 1.09x faster                                                   |
| Geometric mean  | (ref)                                                        | 1.30x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 177 us: 3.03x faster                                                    |
| async_tree_io            | 1.60 sec                                                     | 640 ms: 2.50x faster                                                    |
| async_tree_none          | 692 ms                                                       | 291 ms: 2.37x faster                                                    |
| async_tree_memoization   | 819 ms                                                       | 353 ms: 2.32x faster                                                    |
| deltablue                | 7.50 ms                                                      | 3.44 ms: 2.18x faster                                                   |
| generators               | 57.3 ms                                                      | 28.9 ms: 1.98x faster                                                   |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 524 ms: 1.79x faster                                                    |
| richards_super           | 90.6 ms                                                      | 51.0 ms: 1.78x faster                                                   |
| pylint                   | 566 ms                                                       | 321 ms: 1.76x faster                                                    |
| scimark_monte_carlo      | 107 ms                                                       | 61.1 ms: 1.76x faster                                                   |
| go                       | 262 ms                                                       | 149 ms: 1.76x faster                                                    |
| chaos                    | 109 ms                                                       | 62.1 ms: 1.75x faster                                                   |
| pyflate                  | 733 ms                                                       | 425 ms: 1.73x faster                                                    |
| deepcopy_memo            | 49.8 us                                                      | 28.9 us: 1.72x faster                                                   |
| logging_silent           | 167 ns                                                       | 97.3 ns: 1.72x faster                                                   |
| scimark_lu               | 167 ms                                                       | 97.7 ms: 1.71x faster                                                   |
| spectral_norm            | 139 ms                                                       | 82.4 ms: 1.69x faster                                                   |
| scimark_sor              | 180 ms                                                       | 107 ms: 1.69x faster                                                    |
| deepcopy                 | 468 us                                                       | 280 us: 1.67x faster                                                    |
| richards                 | 75.1 ms                                                      | 45.1 ms: 1.67x faster                                                   |
| raytrace                 | 489 ms                                                       | 295 ms: 1.66x faster                                                    |
| sqlglot_parse            | 2.24 ms                                                      | 1.38 ms: 1.62x faster                                                   |
| float                    | 111 ms                                                       | 69.5 ms: 1.60x faster                                                   |
| crypto_pyaes             | 119 ms                                                       | 76.7 ms: 1.55x faster                                                   |
| mako                     | 14.7 ms                                                      | 9.61 ms: 1.53x faster                                                   |
| unpickle_pure_python     | 312 us                                                       | 206 us: 1.51x faster                                                    |
| sqlglot_transpile        | 2.68 ms                                                      | 1.78 ms: 1.50x faster                                                   |
| tomli_loads              | 2.92 sec                                                     | 2.02 sec: 1.44x faster                                                  |
| coroutines               | 30.3 ms                                                      | 21.1 ms: 1.44x faster                                                   |
| comprehensions           | 26.7 us                                                      | 19.0 us: 1.40x faster                                                   |
| regex_compile            | 190 ms                                                       | 136 ms: 1.40x faster                                                    |
| logging_format           | 9.64 us                                                      | 6.91 us: 1.39x faster                                                   |
| logging_simple           | 8.88 us                                                      | 6.37 us: 1.39x faster                                                   |
| django_template          | 50.2 ms                                                      | 36.3 ms: 1.38x faster                                                   |
| html5lib                 | 94.6 ms                                                      | 68.5 ms: 1.38x faster                                                   |
| deepcopy_reduce          | 4.01 us                                                      | 2.93 us: 1.37x faster                                                   |
| xml_etree_process        | 75.9 ms                                                      | 55.9 ms: 1.36x faster                                                   |
| pickle_pure_python       | 455 us                                                       | 337 us: 1.35x faster                                                    |
| thrift                   | 1.18 ms                                                      | 873 us: 1.35x faster                                                    |
| nbody                    | 134 ms                                                       | 100.0 ms: 1.34x faster                                                  |
| hexiom                   | 9.42 ms                                                      | 7.04 ms: 1.34x faster                                                   |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.32x faster                                                  |
| sqlalchemy_declarative   | 190 ms                                                       | 146 ms: 1.30x faster                                                    |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.30x faster                                                  |
| pprint_safe_repr         | 1.05 sec                                                     | 813 ms: 1.29x faster                                                    |
| pathlib                  | 21.4 ms                                                      | 16.6 ms: 1.29x faster                                                   |
| fannkuch                 | 483 ms                                                       | 382 ms: 1.26x faster                                                    |
| genshi_text              | 31.4 ms                                                      | 25.0 ms: 1.26x faster                                                   |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.1 ms: 1.26x faster                                                   |
| json_dumps               | 14.5 ms                                                      | 11.8 ms: 1.24x faster                                                   |
| sympy_sum                | 193 ms                                                       | 157 ms: 1.23x faster                                                    |
| scimark_fft              | 361 ms                                                       | 295 ms: 1.22x faster                                                    |
| dulwich_log              | 81.1 ms                                                      | 67.4 ms: 1.20x faster                                                   |
| sqlglot_normalize        | 144 ms                                                       | 120 ms: 1.20x faster                                                    |
| 2to3                     | 350 ms                                                       | 291 ms: 1.20x faster                                                    |
| sympy_str                | 360 ms                                                       | 300 ms: 1.20x faster                                                    |
| sympy_integrate          | 28.2 ms                                                      | 23.7 ms: 1.19x faster                                                   |
| bench_thread_pool        | 1.14 ms                                                      | 965 us: 1.18x faster                                                    |
| mdp                      | 3.01 sec                                                     | 2.57 sec: 1.17x faster                                                  |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                    |
| sympy_expand             | 600 ms                                                       | 515 ms: 1.16x faster                                                    |
| sqlglot_optimize         | 70.1 ms                                                      | 60.3 ms: 1.16x faster                                                   |
| nqueens                  | 115 ms                                                       | 99.3 ms: 1.16x faster                                                   |
| xml_etree_generate       | 92.3 ms                                                      | 79.8 ms: 1.16x faster                                                   |
| docutils                 | 3.41 sec                                                     | 2.96 sec: 1.15x faster                                                  |
| xml_etree_iterparse      | 110 ms                                                       | 96.6 ms: 1.14x faster                                                   |
| json_loads               | 30.3 us                                                      | 26.6 us: 1.14x faster                                                   |
| regex_dna                | 261 ms                                                       | 238 ms: 1.10x faster                                                    |
| genshi_xml               | 63.3 ms                                                      | 58.3 ms: 1.09x faster                                                   |
| json                     | 5.86 ms                                                      | 5.41 ms: 1.08x faster                                                   |
| sqlite_synth             | 2.99 us                                                      | 2.78 us: 1.08x faster                                                   |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.73 ms: 1.07x faster                                                   |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                    |
| regex_v8                 | 27.2 ms                                                      | 25.5 ms: 1.07x faster                                                   |
| meteor_contest           | 138 ms                                                       | 133 ms: 1.04x faster                                                    |
| regex_effbot             | 3.09 ms                                                      | 3.13 ms: 1.01x slower                                                   |
| async_generators         | 421 ms                                                       | 434 ms: 1.03x slower                                                    |
| telco                    | 7.23 ms                                                      | 7.58 ms: 1.05x slower                                                   |
| coverage                 | 63.3 ms                                                      | 77.8 ms: 1.23x slower                                                   |
| python_startup_no_site   | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                   |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                   |
| create_gc_cycles         | 1.76 ms                                                      | 2.68 ms: 1.52x slower                                                   |
| gc_traversal             | 3.42 ms                                                      | 6.33 ms: 1.85x slower                                                   |
| bench_mp_pool            | 6.37 ms                                                      | 1.64 sec: 257.00x slower                                                |
| Geometric mean           | (ref)                                                        | 1.25x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250222-3.14.0a5-b856d47-JIT/bm-20250222-pythonperf2-x86_64-brandtbucher-hack_night-3.14.0a5-b856d47.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.332x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.29x