# Results vs. 3.10.4

- fork: python
- ref: 85bc489b649fe261f962
- machine: windows-amd64
- commit hash: 85bc489
- commit date: 2025-04-05
- overall geometric mean: 1.517x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.37x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 202 ms: 1.22x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.54 sec: 1.25x faster                                                      |
| html5lib       | 51.0 ms                                                     | 33.3 ms: 1.53x faster                                                       |
| Geometric mean | (ref)                                                       | 1.33x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 339 ms: 3.27x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 183 ms: 2.88x faster                                                        |
| async_tree_none         | 435 ms                                                      | 153 ms: 2.84x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 308 ms: 2.07x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.73x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 35.8 ms: 1.73x faster                                                       |
| nbody          | 71.3 ms                                                     | 51.9 ms: 1.37x faster                                                       |
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.35x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 67.6 ms: 1.57x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.2 ms: 1.17x faster                                                       |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 105 us: 1.74x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.01 sec: 1.66x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 164 us: 1.64x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 5.59 ms: 1.64x faster                                                       |
| pickle_dict          | 17.2 us                                                     | 11.7 us: 1.47x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 32.4 ms: 1.37x faster                                                       |
| pickle_list          | 2.75 us                                                     | 2.12 us: 1.30x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.09 us: 1.30x faster                                                       |
| unpickle             | 9.09 us                                                     | 7.38 us: 1.23x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 46.9 ms: 1.18x faster                                                       |
| pickle               | 6.85 us                                                     | 6.15 us: 1.11x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 89.5 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.1 ms: 1.06x faster                                                       |
| json_loads           | 14.0 us                                                     | 13.6 us: 1.03x faster                                                       |
| Geometric mean       | (ref)                                                       | 1.32x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.6 ms: 1.29x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 20.9 ms: 1.35x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 11.3 ms: 1.75x faster                                                       |
| mako            | 9.03 ms                                                     | 5.72 ms: 1.58x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 27.3 ms: 1.50x faster                                                       |
| django_template | 28.9 ms                                                     | 19.4 ms: 1.49x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.58x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 84.1 us: 3.99x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 339 ms: 3.27x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 183 ms: 2.88x faster                                                        |
| async_tree_none          | 435 ms                                                      | 153 ms: 2.84x faster                                                        |
| deltablue                | 4.19 ms                                                     | 1.51 ms: 2.77x faster                                                       |
| mdp                      | 1.78 sec                                                    | 661 ms: 2.70x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 30.7 ms: 2.47x faster                                                       |
| go                       | 139 ms                                                      | 57.9 ms: 2.40x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 41.9 ns: 2.26x faster                                                       |
| scimark_sor              | 106 ms                                                      | 47.1 ms: 2.25x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 13.0 us: 2.21x faster                                                       |
| richards_super           | 52.2 ms                                                     | 23.9 ms: 2.19x faster                                                       |
| generators               | 32.4 ms                                                     | 15.2 ms: 2.13x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 26.9 ms: 2.13x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 308 ms: 2.07x faster                                                        |
| richards                 | 42.4 ms                                                     | 20.7 ms: 2.05x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 2.88 ms: 1.99x faster                                                       |
| comprehensions           | 16.5 us                                                     | 8.35 us: 1.98x faster                                                       |
| chaos                    | 61.7 ms                                                     | 31.2 ms: 1.97x faster                                                       |
| raytrace                 | 273 ms                                                      | 143 ms: 1.92x faster                                                        |
| deepcopy                 | 255 us                                                      | 133 us: 1.92x faster                                                        |
| pylint                   | 350 ms                                                      | 183 ms: 1.91x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 45.2 ms: 1.90x faster                                                       |
| pyflate                  | 409 ms                                                      | 233 ms: 1.75x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 11.3 ms: 1.75x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 105 us: 1.74x faster                                                        |
| float                    | 61.7 ms                                                     | 35.8 ms: 1.73x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 46.5 ms: 1.66x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.01 sec: 1.66x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 164 us: 1.64x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 5.59 ms: 1.64x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 39.2 ms: 1.59x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.72 ms: 1.58x faster                                                       |
| regex_compile            | 106 ms                                                      | 67.6 ms: 1.57x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.41 us: 1.56x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 379 ms: 1.56x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 785 ms: 1.55x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 33.3 ms: 1.53x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 27.3 ms: 1.50x faster                                                       |
| django_template          | 28.9 ms                                                     | 19.4 ms: 1.49x faster                                                       |
| coroutines               | 16.0 ms                                                     | 10.8 ms: 1.47x faster                                                       |
| pickle_dict              | 17.2 us                                                     | 11.7 us: 1.47x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.45 sec: 1.46x faster                                                      |
| asyncio_tcp              | 732 ms                                                      | 504 ms: 1.45x faster                                                        |
| pycparser                | 930 ms                                                      | 641 ms: 1.45x faster                                                        |
| unpack_sequence          | 39.6 ns                                                     | 28.3 ns: 1.40x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 47.8 ms: 1.39x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 11.1 ms: 1.38x faster                                                       |
| nbody                    | 71.3 ms                                                     | 51.9 ms: 1.37x faster                                                       |
| sympy_sum                | 107 ms                                                      | 77.9 ms: 1.37x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 32.4 ms: 1.37x faster                                                       |
| scimark_fft              | 187 ms                                                      | 138 ms: 1.36x faster                                                        |
| fannkuch                 | 256 ms                                                      | 190 ms: 1.34x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 37.6 ms: 1.34x faster                                                       |
| sympy_str                | 194 ms                                                      | 147 ms: 1.32x faster                                                        |
| pickle_list              | 2.75 us                                                     | 2.12 us: 1.30x faster                                                       |
| unpickle_list            | 2.71 us                                                     | 2.09 us: 1.30x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.50 us: 1.28x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.14 ms: 1.27x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.54 sec: 1.25x faster                                                      |
| sympy_expand             | 314 ms                                                      | 252 ms: 1.25x faster                                                        |
| unpickle                 | 9.09 us                                                     | 7.38 us: 1.23x faster                                                       |
| 2to3                     | 246 ms                                                      | 202 ms: 1.22x faster                                                        |
| async_generators         | 222 ms                                                      | 183 ms: 1.21x faster                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 46.9 ms: 1.18x faster                                                       |
| logging_format           | 6.76 us                                                     | 5.73 us: 1.18x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 813 us: 1.18x faster                                                        |
| regex_v8                 | 15.4 ms                                                     | 13.2 ms: 1.17x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.38 us: 1.16x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 66.2 ms: 1.15x faster                                                       |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| pickle                   | 6.85 us                                                     | 6.15 us: 1.11x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 89.5 ms: 1.08x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.1 ms: 1.06x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                       |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                        |
| json_loads               | 14.0 us                                                     | 13.6 us: 1.03x faster                                                       |
| json                     | 3.14 ms                                                     | 3.08 ms: 1.02x faster                                                       |
| telco                    | 3.94 ms                                                     | 4.00 ms: 1.02x slower                                                       |
| coverage                 | 39.0 ms                                                     | 40.5 ms: 1.04x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.6 ms: 1.29x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.9 ms: 1.35x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 87.9 ms: 1.42x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.38 ms: 1.73x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.81 ms: 2.00x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.49x faster                                                                |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (16) of results/bm-20250405-3.14.0a6+-85bc489-CLANG/bm-20250405-pythonperf1-amd64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.517x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.42x
- 95% likely to have a speedup of 1.40x
- 99% likely to have a speedup of 1.37x

# Memory
- memory change: unknown