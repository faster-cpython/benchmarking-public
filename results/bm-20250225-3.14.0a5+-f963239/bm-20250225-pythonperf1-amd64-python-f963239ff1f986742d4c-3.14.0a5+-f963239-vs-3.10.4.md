# Results vs. 3.10.4

- fork: python
- ref: f963239ff1f986742d4c
- machine: windows-amd64
- commit hash: f963239
- commit date: 2025-02-25
- overall geometric mean: 1.207x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.8 ms: 1.25x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 423 ms: 2.62x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 224 ms: 2.35x faster                                                        |
| async_tree_none         | 435 ms                                                      | 187 ms: 2.33x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 339 ms: 1.88x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.28x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 47.8 ms: 1.29x faster                                                       |
| pidigits       | 149 ms                                                      | 152 ms: 1.02x slower                                                        |
| nbody          | 71.3 ms                                                     | 74.1 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 112 ms: 1.21x faster                                                        |
| regex_compile  | 106 ms                                                      | 88.2 ms: 1.20x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.42 ms: 1.17x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.5 ms: 1.14x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 7.05 ms: 1.30x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 155 us: 1.18x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.47 sec: 1.14x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 237 us: 1.14x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 41.5 ms: 1.07x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 91.2 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.7 ms: 1.02x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.7 us: 1.05x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 58.7 ms: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.1 ms: 1.26x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 19.8 ms: 1.28x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.86 ms: 1.32x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.5 ms: 1.20x faster                                                       |
| django_template | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 36.3 ms: 1.13x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 106 us: 3.17x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 423 ms: 2.62x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.1 ms: 2.36x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 224 ms: 2.35x faster                                                        |
| async_tree_none          | 435 ms                                                      | 187 ms: 2.33x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 339 ms: 1.88x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.29 ms: 1.82x faster                                                       |
| pylint                   | 350 ms                                                      | 201 ms: 1.74x faster                                                        |
| generators               | 32.4 ms                                                     | 19.3 ms: 1.68x faster                                                       |
| go                       | 139 ms                                                      | 88.6 ms: 1.57x faster                                                       |
| richards_super           | 52.2 ms                                                     | 35.1 ms: 1.49x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.3 us: 1.46x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 65.2 ns: 1.45x faster                                                       |
| raytrace                 | 273 ms                                                      | 191 ms: 1.43x faster                                                        |
| chaos                    | 61.7 ms                                                     | 43.6 ms: 1.41x faster                                                       |
| richards                 | 42.4 ms                                                     | 30.7 ms: 1.38x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.0 us: 1.37x faster                                                       |
| deepcopy                 | 255 us                                                      | 190 us: 1.35x faster                                                        |
| mako                     | 9.03 ms                                                     | 6.86 ms: 1.32x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.38 ms: 1.31x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 7.05 ms: 1.30x faster                                                       |
| pyflate                  | 409 ms                                                      | 315 ms: 1.30x faster                                                        |
| float                    | 61.7 ms                                                     | 47.8 ms: 1.29x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 66.9 ms: 1.28x faster                                                       |
| pycparser                | 930 ms                                                      | 738 ms: 1.26x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 61.5 ms: 1.26x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 40.8 ms: 1.25x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 50.0 ms: 1.25x faster                                                       |
| thrift                   | 617 us                                                      | 507 us: 1.22x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 47.1 ms: 1.22x faster                                                       |
| regex_dna                | 136 ms                                                      | 112 ms: 1.21x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                       |
| regex_compile            | 106 ms                                                      | 88.2 ms: 1.20x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.5 ms: 1.20x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.19x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.5 ms: 1.18x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 155 us: 1.18x faster                                                        |
| scimark_sor              | 106 ms                                                      | 91.0 ms: 1.17x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.42 ms: 1.17x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 43.4 ms: 1.16x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 13.5 ms: 1.14x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.47 sec: 1.14x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 237 us: 1.14x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.94 us: 1.14x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.3 ms: 1.13x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 864 us: 1.11x faster                                                        |
| sympy_str                | 194 ms                                                      | 176 ms: 1.10x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.64 sec: 1.09x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.13 sec: 1.08x faster                                                      |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 41.5 ms: 1.07x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 91.2 ms: 1.06x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 558 ms: 1.06x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 63.6 ms: 1.05x faster                                                       |
| sympy_expand             | 314 ms                                                      | 302 ms: 1.04x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.7 ms: 1.02x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 76.9 ms: 1.01x slower                                                       |
| pidigits                 | 149 ms                                                      | 152 ms: 1.02x slower                                                        |
| async_generators         | 222 ms                                                      | 226 ms: 1.02x slower                                                        |
| scimark_fft              | 187 ms                                                      | 192 ms: 1.03x slower                                                        |
| nbody                    | 71.3 ms                                                     | 74.1 ms: 1.04x slower                                                       |
| logging_format           | 6.76 us                                                     | 7.03 us: 1.04x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.53 us: 1.05x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.7 us: 1.05x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 58.7 ms: 1.06x slower                                                       |
| fannkuch                 | 256 ms                                                      | 296 ms: 1.16x slower                                                        |
| coverage                 | 39.0 ms                                                     | 46.8 ms: 1.20x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.89 ms: 1.24x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.1 ms: 1.26x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.8 ms: 1.28x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.7 ms: 1.43x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.06 ms: 1.46x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.25 ms: 1.56x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (2): scimark_sparse_mat_mult, json
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250225-3.14.0a5+-f963239/bm-20250225-pythonperf1-amd64-python-f963239ff1f986742d4c-3.14.0a5+-f963239.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.207x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown