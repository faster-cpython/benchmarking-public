# Results vs. 3.10.4

- fork: python
- ref: c5e856a5dc8eed4813ec
- machine: windows-amd64
- commit hash: c5e856a
- commit date: 2025-04-08
- overall geometric mean: 1.301x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 217 ms: 1.13x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                      |
| html5lib       | 51.0 ms                                                     | 38.1 ms: 1.34x faster                                                       |
| Geometric mean | (ref)                                                       | 1.22x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 409 ms: 2.71x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 205 ms: 2.57x faster                                                        |
| async_tree_none         | 435 ms                                                      | 178 ms: 2.44x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 327 ms: 1.95x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.40x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 42.4 ms: 1.45x faster                                                       |
| nbody          | 71.3 ms                                                     | 61.9 ms: 1.15x faster                                                       |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.2 ms: 1.34x faster                                                       |
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.43 ms: 1.16x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.1 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.45 ms: 1.42x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 134 us: 1.37x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 210 us: 1.29x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.34 sec: 1.25x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 39.0 ms: 1.14x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 89.7 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.6 ms: 1.02x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.9 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.16x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.31 ms: 1.43x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.4 ms: 1.28x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 33.9 ms: 1.21x faster                                                       |
| django_template | 28.9 ms                                                     | 24.6 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.23x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 409 ms: 2.71x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 28.5 ms: 2.65x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 205 ms: 2.57x faster                                                        |
| async_tree_none          | 435 ms                                                      | 178 ms: 2.44x faster                                                        |
| mdp                      | 1.78 sec                                                    | 772 ms: 2.31x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.10 ms: 1.99x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 327 ms: 1.95x faster                                                        |
| go                       | 139 ms                                                      | 76.4 ms: 1.82x faster                                                       |
| pylint                   | 350 ms                                                      | 197 ms: 1.78x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 55.3 ns: 1.71x faster                                                       |
| generators               | 32.4 ms                                                     | 19.0 ms: 1.70x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.9 ms: 1.69x faster                                                       |
| chaos                    | 61.7 ms                                                     | 37.8 ms: 1.63x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 17.8 us: 1.62x faster                                                       |
| richards                 | 42.4 ms                                                     | 27.1 ms: 1.57x faster                                                       |
| raytrace                 | 273 ms                                                      | 175 ms: 1.56x faster                                                        |
| deepcopy                 | 255 us                                                      | 167 us: 1.53x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.2 ms: 1.50x faster                                                       |
| scimark_sor              | 106 ms                                                      | 72.2 ms: 1.47x faster                                                       |
| float                    | 61.7 ms                                                     | 42.4 ms: 1.45x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 59.0 ms: 1.45x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.4 us: 1.45x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.97 ms: 1.45x faster                                                       |
| pyflate                  | 409 ms                                                      | 285 ms: 1.43x faster                                                        |
| mako                     | 9.03 ms                                                     | 6.31 ms: 1.43x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.45 ms: 1.42x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 56.2 ms: 1.38x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 45.6 ms: 1.37x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 134 us: 1.37x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 38.1 ms: 1.34x faster                                                       |
| regex_compile            | 106 ms                                                      | 79.2 ms: 1.34x faster                                                       |
| pycparser                | 930 ms                                                      | 706 ms: 1.32x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 210 us: 1.29x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 15.4 ms: 1.28x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.34 sec: 1.25x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.78 us: 1.24x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.1 ms: 1.23x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 997 ms: 1.22x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 487 ms: 1.21x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 33.9 ms: 1.21x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.0 ms: 1.20x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.3 ms: 1.20x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.6 ms: 1.18x faster                                                       |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.43 ms: 1.16x faster                                                       |
| nbody                    | 71.3 ms                                                     | 61.9 ms: 1.15x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 834 us: 1.15x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 39.0 ms: 1.14x faster                                                       |
| 2to3                     | 246 ms                                                      | 217 ms: 1.13x faster                                                        |
| sympy_str                | 194 ms                                                      | 172 ms: 1.13x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 60.2 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.49 ms: 1.10x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.1 ms: 1.09x faster                                                       |
| scimark_fft              | 187 ms                                                      | 174 ms: 1.08x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 89.7 ms: 1.08x faster                                                       |
| sympy_expand             | 314 ms                                                      | 296 ms: 1.06x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 72.2 ms: 1.05x faster                                                       |
| fannkuch                 | 256 ms                                                      | 245 ms: 1.04x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.6 ms: 1.02x faster                                                       |
| json                     | 3.14 ms                                                     | 3.08 ms: 1.02x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.67 us: 1.01x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.15 us: 1.01x faster                                                       |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                        |
| async_generators         | 222 ms                                                      | 228 ms: 1.03x slower                                                        |
| json_loads               | 14.0 us                                                     | 14.9 us: 1.06x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.56 ms: 1.16x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                       |
| coverage                 | 39.0 ms                                                     | 51.2 ms: 1.31x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 86.3 ms: 1.39x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.01 ms: 1.43x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.52x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.29x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_generate
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250408-3.14.0a7+-c5e856a/bm-20250408-pythonperf1-amd64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.301x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown