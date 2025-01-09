# Results vs. 3.10.4

- fork: python
- ref: 0cafa97932c6574734bb
- machine: windows-amd64
- commit hash: 0cafa97
- commit date: 2025-01-04
- overall geometric mean: 1.167x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 235 ms: 1.05x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.76 sec: 1.09x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.3 ms: 1.30x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 388 ms: 2.86x faster                                                        |
| async_tree_none         | 435 ms                                                      | 174 ms: 2.50x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 215 ms: 2.45x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 372 ms: 1.71x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.34x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 52.8 ms: 1.17x faster                                                       |
| nbody          | 71.3 ms                                                     | 67.5 ms: 1.06x faster                                                       |
| pidigits       | 149 ms                                                      | 156 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 87.9 ms: 1.21x faster                                                       |
| regex_dna      | 136 ms                                                      | 130 ms: 1.05x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.88 ms: 1.13x slower                                                       |
| regex_v8       | 15.4 ms                                                     | 23.4 ms: 1.51x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 270 us                                                      | 222 us: 1.21x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 154 us: 1.19x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 7.84 ms: 1.17x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 45.7 ms: 1.03x slower                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 103 ms: 1.06x slower                                                        |
| xml_etree_iterparse  | 65.0 ms                                                     | 69.5 ms: 1.07x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 66.0 ms: 1.19x slower                                                       |
| json_loads           | 14.0 us                                                     | 19.3 us: 1.38x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.6 ms: 1.20x slower                                                       |
| python_startup         | 20.6 ms                                                     | 25.6 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 16.0 ms: 1.24x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                       |
| django_template | 28.9 ms                                                     | 24.8 ms: 1.16x faster                                                       |
| mako            | 9.03 ms                                                     | 8.22 ms: 1.10x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 115 us: 2.91x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 388 ms: 2.86x faster                                                        |
| async_tree_none          | 435 ms                                                      | 174 ms: 2.50x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 215 ms: 2.45x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.02 ms: 2.08x faster                                                       |
| generators               | 32.4 ms                                                     | 17.2 ms: 1.88x faster                                                       |
| go                       | 139 ms                                                      | 78.2 ms: 1.78x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 372 ms: 1.71x faster                                                        |
| pylint                   | 350 ms                                                      | 205 ms: 1.71x faster                                                        |
| raytrace                 | 273 ms                                                      | 177 ms: 1.55x faster                                                        |
| richards_super           | 52.2 ms                                                     | 33.9 ms: 1.54x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 845 us: 1.44x faster                                                        |
| richards                 | 42.4 ms                                                     | 30.1 ms: 1.41x faster                                                       |
| chaos                    | 61.7 ms                                                     | 43.9 ms: 1.41x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 67.3 ns: 1.41x faster                                                       |
| deepcopy                 | 255 us                                                      | 184 us: 1.39x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 20.7 us: 1.39x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.07 ms: 1.38x faster                                                       |
| scimark_sor              | 106 ms                                                      | 79.2 ms: 1.34x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.5 us: 1.32x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.37 ms: 1.31x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 44.0 ms: 1.30x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.3 ms: 1.30x faster                                                       |
| pyflate                  | 409 ms                                                      | 316 ms: 1.30x faster                                                        |
| pycparser                | 930 ms                                                      | 730 ms: 1.28x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 67.7 ms: 1.27x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.0 ms: 1.24x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 222 us: 1.21x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                                      |
| regex_compile            | 106 ms                                                      | 87.9 ms: 1.21x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.2 ms: 1.20x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 154 us: 1.19x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.17x faster                                                       |
| sympy_sum                | 107 ms                                                      | 91.5 ms: 1.17x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 7.84 ms: 1.17x faster                                                       |
| float                    | 61.7 ms                                                     | 52.8 ms: 1.17x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.8 ms: 1.16x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.07 sec: 1.14x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.93 us: 1.14x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 54.8 ms: 1.14x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 849 us: 1.13x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 68.9 ms: 1.12x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 529 ms: 1.12x faster                                                        |
| thrift                   | 617 us                                                      | 561 us: 1.10x faster                                                        |
| mako                     | 9.03 ms                                                     | 8.22 ms: 1.10x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.75 us: 1.09x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.76 sec: 1.09x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 36.6 ms: 1.09x faster                                                       |
| sympy_str                | 194 ms                                                      | 180 ms: 1.08x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.67 sec: 1.06x faster                                                      |
| nbody                    | 71.3 ms                                                     | 67.5 ms: 1.06x faster                                                       |
| regex_dna                | 136 ms                                                      | 130 ms: 1.05x faster                                                        |
| 2to3                     | 246 ms                                                      | 235 ms: 1.05x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 63.7 ms: 1.05x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 197 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.63 ms: 1.04x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 73.6 ms: 1.03x faster                                                       |
| sympy_expand             | 314 ms                                                      | 308 ms: 1.02x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.68 us: 1.01x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 45.7 ms: 1.03x slower                                                       |
| scimark_fft              | 187 ms                                                      | 195 ms: 1.04x slower                                                        |
| pidigits                 | 149 ms                                                      | 156 ms: 1.04x slower                                                        |
| pathlib                  | 75.7 ms                                                     | 79.6 ms: 1.05x slower                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 103 ms: 1.06x slower                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 69.5 ms: 1.07x slower                                                       |
| fannkuch                 | 256 ms                                                      | 283 ms: 1.11x slower                                                        |
| async_generators         | 222 ms                                                      | 251 ms: 1.13x slower                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.88 ms: 1.13x slower                                                       |
| json                     | 3.14 ms                                                     | 3.61 ms: 1.15x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 66.0 ms: 1.19x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.6 ms: 1.20x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.6 ms: 1.24x slower                                                       |
| coverage                 | 39.0 ms                                                     | 50.1 ms: 1.29x slower                                                       |
| telco                    | 3.94 ms                                                     | 5.24 ms: 1.33x slower                                                       |
| json_loads               | 14.0 us                                                     | 19.3 us: 1.38x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 23.4 ms: 1.51x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 93.9 ms: 1.51x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.35 ms: 1.68x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.54 ms: 1.80x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                                |

Benchmark hidden because not significant (1): logging_simple
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250104-3.14.0a3+-0cafa97-CLANG/bm-20250104-pythonperf1-amd64-python-0cafa97932c6574734bb-3.14.0a3+-0cafa97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.167x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: unknown