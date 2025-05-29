# Results vs. 3.10.4

- fork: python
- ref: 4f18916c5c28321f363e
- machine: windows-amd64
- commit hash: 4f18916
- commit date: 2025-04-26
- overall geometric mean: 1.507x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 201 ms: 1.22x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.54 sec: 1.24x faster                                                      |
| html5lib       | 51.0 ms                                                     | 34.6 ms: 1.47x faster                                                       |
| Geometric mean | (ref)                                                       | 1.31x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 345 ms: 3.21x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 184 ms: 2.86x faster                                                        |
| async_tree_none         | 435 ms                                                      | 156 ms: 2.79x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 313 ms: 2.04x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.69x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 35.9 ms: 1.72x faster                                                       |
| nbody          | 71.3 ms                                                     | 54.1 ms: 1.32x faster                                                       |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 67.2 ms: 1.58x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 12.7 ms: 1.22x faster                                                       |
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.50 ms: 1.11x faster                                                       |
| Geometric mean | (ref)                                                       | 1.25x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 102 us: 1.80x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 164 us: 1.64x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.03 sec: 1.63x faster                                                      |
| json_dumps           | 9.16 ms                                                     | 5.87 ms: 1.56x faster                                                       |
| pickle_dict          | 17.2 us                                                     | 11.5 us: 1.49x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 32.7 ms: 1.36x faster                                                       |
| pickle_list          | 2.75 us                                                     | 2.05 us: 1.34x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.18 us: 1.24x faster                                                       |
| unpickle             | 9.09 us                                                     | 7.41 us: 1.23x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 46.9 ms: 1.18x faster                                                       |
| pickle               | 6.85 us                                                     | 6.02 us: 1.14x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 90.4 ms: 1.07x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 68.1 ms: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.31x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.8 ms: 1.34x slower                                                       |
| python_startup         | 20.6 ms                                                     | 27.9 ms: 1.35x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.35x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 11.2 ms: 1.77x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 26.6 ms: 1.54x faster                                                       |
| mako            | 9.03 ms                                                     | 5.98 ms: 1.51x faster                                                       |
| django_template | 28.9 ms                                                     | 19.8 ms: 1.46x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.57x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 88.9 us: 3.78x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 345 ms: 3.21x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 184 ms: 2.86x faster                                                        |
| async_tree_none          | 435 ms                                                      | 156 ms: 2.79x faster                                                        |
| deltablue                | 4.19 ms                                                     | 1.53 ms: 2.74x faster                                                       |
| mdp                      | 1.78 sec                                                    | 672 ms: 2.65x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 31.0 ms: 2.44x faster                                                       |
| go                       | 139 ms                                                      | 58.1 ms: 2.39x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 40.9 ns: 2.31x faster                                                       |
| scimark_sor              | 106 ms                                                      | 47.2 ms: 2.25x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 13.0 us: 2.21x faster                                                       |
| richards_super           | 52.2 ms                                                     | 24.1 ms: 2.17x faster                                                       |
| generators               | 32.4 ms                                                     | 15.0 ms: 2.16x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 26.8 ms: 2.14x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 313 ms: 2.04x faster                                                        |
| richards                 | 42.4 ms                                                     | 21.0 ms: 2.02x faster                                                       |
| chaos                    | 61.7 ms                                                     | 30.7 ms: 2.01x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 2.87 ms: 2.00x faster                                                       |
| raytrace                 | 273 ms                                                      | 139 ms: 1.96x faster                                                        |
| comprehensions           | 16.5 us                                                     | 8.45 us: 1.95x faster                                                       |
| deepcopy                 | 255 us                                                      | 135 us: 1.89x faster                                                        |
| pylint                   | 350 ms                                                      | 186 ms: 1.88x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 46.8 ms: 1.83x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 102 us: 1.80x faster                                                        |
| pyflate                  | 409 ms                                                      | 228 ms: 1.79x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 11.2 ms: 1.77x faster                                                       |
| float                    | 61.7 ms                                                     | 35.9 ms: 1.72x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 46.2 ms: 1.67x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 164 us: 1.64x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.03 sec: 1.63x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 39.3 ms: 1.59x faster                                                       |
| regex_compile            | 106 ms                                                      | 67.2 ms: 1.58x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.87 ms: 1.56x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 26.6 ms: 1.54x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 793 ms: 1.54x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.44 us: 1.53x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.98 ms: 1.51x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 394 ms: 1.50x faster                                                        |
| pickle_dict              | 17.2 us                                                     | 11.5 us: 1.49x faster                                                       |
| pycparser                | 930 ms                                                      | 630 ms: 1.48x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 34.6 ms: 1.47x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.44 sec: 1.46x faster                                                      |
| coroutines               | 16.0 ms                                                     | 11.0 ms: 1.46x faster                                                       |
| django_template          | 28.9 ms                                                     | 19.8 ms: 1.46x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 46.2 ms: 1.44x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 516 ms: 1.42x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 10.9 ms: 1.40x faster                                                       |
| sympy_sum                | 107 ms                                                      | 77.5 ms: 1.38x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 32.7 ms: 1.36x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 29.5 ns: 1.34x faster                                                       |
| pickle_list              | 2.75 us                                                     | 2.05 us: 1.34x faster                                                       |
| sympy_str                | 194 ms                                                      | 146 ms: 1.33x faster                                                        |
| scimark_fft              | 187 ms                                                      | 142 ms: 1.32x faster                                                        |
| nbody                    | 71.3 ms                                                     | 54.1 ms: 1.32x faster                                                       |
| fannkuch                 | 256 ms                                                      | 194 ms: 1.32x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 38.4 ms: 1.31x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.49 us: 1.28x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.15 ms: 1.27x faster                                                       |
| sympy_expand             | 314 ms                                                      | 252 ms: 1.25x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.54 sec: 1.24x faster                                                      |
| unpickle_list            | 2.71 us                                                     | 2.18 us: 1.24x faster                                                       |
| unpickle                 | 9.09 us                                                     | 7.41 us: 1.23x faster                                                       |
| 2to3                     | 246 ms                                                      | 201 ms: 1.22x faster                                                        |
| regex_v8                 | 15.4 ms                                                     | 12.7 ms: 1.22x faster                                                       |
| async_generators         | 222 ms                                                      | 187 ms: 1.19x faster                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 46.9 ms: 1.18x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 64.6 ms: 1.18x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 834 us: 1.15x faster                                                        |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                                        |
| logging_format           | 6.76 us                                                     | 5.93 us: 1.14x faster                                                       |
| pickle                   | 6.85 us                                                     | 6.02 us: 1.14x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.54 us: 1.12x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.50 ms: 1.11x faster                                                       |
| json                     | 3.14 ms                                                     | 2.88 ms: 1.09x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 90.4 ms: 1.07x faster                                                       |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                        |
| telco                    | 3.94 ms                                                     | 4.08 ms: 1.04x slower                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 68.1 ms: 1.05x slower                                                       |
| coverage                 | 39.0 ms                                                     | 41.5 ms: 1.07x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.8 ms: 1.34x slower                                                       |
| python_startup           | 20.6 ms                                                     | 27.9 ms: 1.35x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 89.5 ms: 1.44x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.37 ms: 1.72x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.80 ms: 1.99x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.48x faster                                                                |

Benchmark hidden because not significant (1): json_loads
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (16) of results/bm-20250426-3.14.0a7+-4f18916-CLANG/bm-20250426-pythonperf1-amd64-python-4f18916c5c28321f363e-3.14.0a7+-4f18916.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.507x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.43x
- 95% likely to have a speedup of 1.40x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: unknown