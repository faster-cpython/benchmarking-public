# Results vs. 3.10.4

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: linux-x86_64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.189x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.66x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 320 ms: 1.09x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| html5lib       | 94.6 ms                                                      | 71.3 ms: 1.33x faster                                                       |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 569 ms: 2.81x faster                                                        |
| async_tree_none         | 692 ms                                                       | 269 ms: 2.57x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 330 ms: 2.48x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 504 ms: 1.86x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.40x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 71.6 ms: 1.55x faster                                                       |
| pidigits       | 271 ms                                                       | 249 ms: 1.09x faster                                                        |
| nbody          | 134 ms                                                       | 130 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 154 ms: 1.23x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 22.7 ms: 1.19x faster                                                       |
| regex_dna      | 261 ms                                                       | 223 ms: 1.17x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.40 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 237 us: 1.31x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.31 sec: 1.26x faster                                                      |
| xml_etree_iterparse  | 110 ms                                                       | 88.4 ms: 1.25x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 369 us: 1.23x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 12.1 ms: 1.20x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 138 ms: 1.16x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 70.2 ms: 1.08x faster                                                       |
| json_loads           | 30.3 us                                                      | 28.2 us: 1.07x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 97.7 ms: 1.06x slower                                                       |
| unpickle_list        | 4.65 us                                                      | 5.51 us: 1.19x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 36.2 us: 1.23x slower                                                       |
| unpickle             | 13.5 us                                                      | 16.7 us: 1.24x slower                                                       |
| pickle_list          | 4.12 us                                                      | 5.20 us: 1.26x slower                                                       |
| pickle               | 9.89 us                                                      | 12.5 us: 1.26x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                       |
| python_startup         | 11.5 ms                                                      | 19.7 ms: 1.71x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.66x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 44.3 ms: 1.13x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 30.4 ms: 1.03x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 66.8 ms: 1.06x slower                                                       |
| mako            | 14.7 ms                                                      | 17.5 ms: 1.19x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 569 ms: 2.81x faster                                                        |
| typing_runtime_protocols | 537 us                                                       | 207 us: 2.59x faster                                                        |
| async_tree_none          | 692 ms                                                       | 269 ms: 2.57x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 330 ms: 2.48x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.46 sec: 2.06x faster                                                      |
| asyncio_tcp              | 779 ms                                                       | 386 ms: 2.02x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.72 ms: 2.01x faster                                                       |
| go                       | 262 ms                                                       | 140 ms: 1.87x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 504 ms: 1.86x faster                                                        |
| generators               | 57.3 ms                                                      | 31.5 ms: 1.82x faster                                                       |
| logging_silent           | 167 ns                                                       | 99.5 ns: 1.68x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.87 sec: 1.66x faster                                                      |
| pylint                   | 566 ms                                                       | 348 ms: 1.63x faster                                                        |
| chaos                    | 109 ms                                                       | 66.7 ms: 1.63x faster                                                       |
| float                    | 111 ms                                                       | 71.6 ms: 1.55x faster                                                       |
| pyflate                  | 733 ms                                                       | 475 ms: 1.54x faster                                                        |
| gc_traversal             | 3.42 ms                                                      | 2.24 ms: 1.53x faster                                                       |
| raytrace                 | 489 ms                                                       | 323 ms: 1.52x faster                                                        |
| scimark_sor              | 180 ms                                                       | 120 ms: 1.51x faster                                                        |
| comprehensions           | 26.7 us                                                      | 18.2 us: 1.47x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 34.5 us: 1.44x faster                                                       |
| deepcopy                 | 468 us                                                       | 325 us: 1.44x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.66 ms: 1.41x faster                                                       |
| scimark_lu               | 167 ms                                                       | 118 ms: 1.41x faster                                                        |
| richards_super           | 90.6 ms                                                      | 64.6 ms: 1.40x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 79.3 ms: 1.35x faster                                                       |
| spectral_norm            | 139 ms                                                       | 103 ms: 1.35x faster                                                        |
| coroutines               | 30.3 ms                                                      | 22.6 ms: 1.34x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 71.3 ms: 1.33x faster                                                       |
| richards                 | 75.1 ms                                                      | 56.6 ms: 1.33x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                                      |
| dulwich_log              | 81.1 ms                                                      | 61.6 ms: 1.32x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 237 us: 1.31x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.89 us: 1.29x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 93.7 ms: 1.27x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.31 sec: 1.26x faster                                                      |
| logging_format           | 9.64 us                                                      | 7.70 us: 1.25x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 88.4 ms: 1.25x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 17.2 ms: 1.24x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 369 us: 1.23x faster                                                        |
| regex_compile            | 190 ms                                                       | 154 ms: 1.23x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 12.1 ms: 1.20x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 22.7 ms: 1.19x faster                                                       |
| thrift                   | 1.18 ms                                                      | 984 us: 1.19x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 882 ms: 1.19x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.82 sec: 1.18x faster                                                      |
| docutils                 | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| regex_dna                | 261 ms                                                       | 223 ms: 1.17x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 138 ms: 1.16x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.60 us: 1.15x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.53 us: 1.14x faster                                                       |
| django_template          | 50.2 ms                                                      | 44.3 ms: 1.13x faster                                                       |
| sympy_sum                | 193 ms                                                       | 172 ms: 1.12x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 25.3 ms: 1.11x faster                                                       |
| 2to3                     | 350 ms                                                       | 320 ms: 1.09x faster                                                        |
| sympy_str                | 360 ms                                                       | 329 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 249 ms: 1.09x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 70.2 ms: 1.08x faster                                                       |
| json_loads               | 30.3 us                                                      | 28.2 us: 1.07x faster                                                       |
| unpack_sequence          | 59.9 ns                                                      | 55.9 ns: 1.07x faster                                                       |
| fannkuch                 | 483 ms                                                       | 450 ms: 1.07x faster                                                        |
| sympy_expand             | 600 ms                                                       | 561 ms: 1.07x faster                                                        |
| nqueens                  | 115 ms                                                       | 108 ms: 1.07x faster                                                        |
| json                     | 5.86 ms                                                      | 5.56 ms: 1.05x faster                                                       |
| nbody                    | 134 ms                                                       | 130 ms: 1.03x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 30.4 ms: 1.03x faster                                                       |
| scimark_fft              | 361 ms                                                       | 358 ms: 1.01x faster                                                        |
| meteor_contest           | 138 ms                                                       | 145 ms: 1.05x slower                                                        |
| genshi_xml               | 63.3 ms                                                      | 66.8 ms: 1.06x slower                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 97.7 ms: 1.06x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.40 ms: 1.10x slower                                                       |
| async_generators         | 421 ms                                                       | 465 ms: 1.11x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 1.97 ms: 1.12x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.91 ms: 1.16x slower                                                       |
| unpickle_list            | 4.65 us                                                      | 5.51 us: 1.19x slower                                                       |
| mako                     | 14.7 ms                                                      | 17.5 ms: 1.19x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 36.2 us: 1.23x slower                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 1.41 ms: 1.24x slower                                                       |
| unpickle                 | 13.5 us                                                      | 16.7 us: 1.24x slower                                                       |
| pickle_list              | 4.12 us                                                      | 5.20 us: 1.26x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.5 us: 1.26x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                       |
| python_startup           | 11.5 ms                                                      | 19.7 ms: 1.71x slower                                                       |
| coverage                 | 63.3 ms                                                      | 117 ms: 1.84x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 56.9 ms: 8.93x slower                                                       |
| telco                    | 7.23 ms                                                      | 175 ms: 24.17x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.15x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.189x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.66x