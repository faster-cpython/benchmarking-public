# Results vs. 3.10.4

- fork: python
- ref: 844596c09fc812a58ac1
- machine: windows-amd64
- commit hash: 844596c
- commit date: 2025-04-14
- overall geometric mean: 1.286x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                      |
| html5lib       | 51.0 ms                                                     | 37.6 ms: 1.36x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 409 ms: 2.71x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 204 ms: 2.58x faster                                                        |
| async_tree_none         | 435 ms                                                      | 178 ms: 2.45x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 329 ms: 1.94x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.40x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 42.9 ms: 1.44x faster                                                       |
| nbody          | 71.3 ms                                                     | 61.3 ms: 1.16x faster                                                       |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.5 ms: 1.33x faster                                                       |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.49 ms: 1.11x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 133 us: 1.37x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 6.79 ms: 1.35x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 210 us: 1.28x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 39.9 ms: 1.12x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 89.8 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.0 ms: 1.01x faster                                                       |
| json_loads           | 14.0 us                                                     | 15.5 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.4 ms: 1.28x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 20.9 ms: 1.35x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.62 ms: 1.36x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                       |
| django_template | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.25x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 106 us: 3.18x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 409 ms: 2.71x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 204 ms: 2.58x faster                                                        |
| async_tree_none          | 435 ms                                                      | 178 ms: 2.45x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.3 ms: 2.34x faster                                                       |
| mdp                      | 1.78 sec                                                    | 813 ms: 2.19x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.10 ms: 1.99x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 329 ms: 1.94x faster                                                        |
| go                       | 139 ms                                                      | 76.4 ms: 1.82x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 54.2 ns: 1.74x faster                                                       |
| pylint                   | 350 ms                                                      | 201 ms: 1.74x faster                                                        |
| richards_super           | 52.2 ms                                                     | 31.0 ms: 1.68x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 17.7 us: 1.63x faster                                                       |
| chaos                    | 61.7 ms                                                     | 37.9 ms: 1.63x faster                                                       |
| generators               | 32.4 ms                                                     | 20.6 ms: 1.57x faster                                                       |
| raytrace                 | 273 ms                                                      | 174 ms: 1.57x faster                                                        |
| richards                 | 42.4 ms                                                     | 27.5 ms: 1.54x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 56.6 ms: 1.52x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.3 ms: 1.49x faster                                                       |
| deepcopy                 | 255 us                                                      | 171 us: 1.49x faster                                                        |
| comprehensions           | 16.5 us                                                     | 11.2 us: 1.47x faster                                                       |
| pyflate                  | 409 ms                                                      | 279 ms: 1.46x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 3.94 ms: 1.46x faster                                                       |
| float                    | 61.7 ms                                                     | 42.9 ms: 1.44x faster                                                       |
| scimark_sor              | 106 ms                                                      | 74.5 ms: 1.43x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 133 us: 1.37x faster                                                        |
| mako                     | 9.03 ms                                                     | 6.62 ms: 1.36x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 37.6 ms: 1.36x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.79 ms: 1.35x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 46.4 ms: 1.35x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 57.5 ms: 1.34x faster                                                       |
| regex_compile            | 106 ms                                                      | 79.5 ms: 1.33x faster                                                       |
| pycparser                | 930 ms                                                      | 717 ms: 1.30x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 210 us: 1.28x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.80 us: 1.23x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.00 sec: 1.21x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 41.7 ms: 1.21x faster                                                       |
| sympy_sum                | 107 ms                                                      | 88.7 ms: 1.21x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.3 ms: 1.20x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 494 ms: 1.20x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                      |
| nbody                    | 71.3 ms                                                     | 61.3 ms: 1.16x faster                                                       |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                        |
| sympy_str                | 194 ms                                                      | 172 ms: 1.13x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 39.9 ms: 1.12x faster                                                       |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.45 ms: 1.11x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.49 ms: 1.11x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 882 us: 1.09x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 89.8 ms: 1.08x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 61.9 ms: 1.08x faster                                                       |
| scimark_fft              | 187 ms                                                      | 174 ms: 1.07x faster                                                        |
| sympy_expand             | 314 ms                                                      | 295 ms: 1.06x faster                                                        |
| regex_v8                 | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 73.1 ms: 1.04x faster                                                       |
| fannkuch                 | 256 ms                                                      | 246 ms: 1.04x faster                                                        |
| json                     | 3.14 ms                                                     | 3.04 ms: 1.03x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.0 ms: 1.01x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.84 us: 1.01x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.31 us: 1.01x slower                                                       |
| async_generators         | 222 ms                                                      | 228 ms: 1.03x slower                                                        |
| json_loads               | 14.0 us                                                     | 15.5 us: 1.11x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.64 ms: 1.18x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.4 ms: 1.28x slower                                                       |
| coverage                 | 39.0 ms                                                     | 50.4 ms: 1.29x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.9 ms: 1.35x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 89.0 ms: 1.43x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.07 ms: 1.47x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.26 ms: 1.57x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.28x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_generate, pidigits
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250414-3.14.0a7+-844596c/bm-20250414-pythonperf1-amd64-python-844596c09fc812a58ac1-3.14.0a7+-844596c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.286x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown