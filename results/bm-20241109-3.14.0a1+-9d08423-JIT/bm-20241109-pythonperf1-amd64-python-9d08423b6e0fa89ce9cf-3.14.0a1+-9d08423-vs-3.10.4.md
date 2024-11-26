# Results vs. 3.10.4

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: windows-amd64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.208x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 251 ms: 1.02x slower                                                        |
| docutils       | 1.92 sec                                                    | 1.88 sec: 1.02x faster                                                      |
| html5lib       | 51.0 ms                                                     | 38.9 ms: 1.31x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 210 ms: 2.07x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 546 ms: 2.03x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 262 ms: 2.01x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 391 ms: 1.63x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.93x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 53.2 ms: 1.34x faster                                                       |
| float          | 61.7 ms                                                     | 47.4 ms: 1.30x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 90.9 ms: 1.17x faster                                                       |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.42 ms: 1.43x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.27 sec: 1.32x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 207 us: 1.30x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 144 us: 1.28x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.0 ms: 1.24x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 51.0 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.2 ms: 1.03x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 94.4 ms: 1.03x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 24.9 ms: 1.21x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 18.8 ms: 1.21x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.21x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.04 ms: 1.79x faster                                                       |
| django_template | 28.9 ms                                                     | 26.7 ms: 1.08x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 19.2 ms: 1.03x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 45.5 ms: 1.11x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.94x faster                                                        |
| async_tree_none          | 435 ms                                                      | 210 ms: 2.07x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 546 ms: 2.03x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 262 ms: 2.01x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.33 ms: 1.79x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.04 ms: 1.79x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.6 us: 1.74x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 56.3 ns: 1.68x faster                                                       |
| scimark_sor              | 106 ms                                                      | 64.3 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 391 ms: 1.63x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 54.7 ms: 1.57x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 39.9 ms: 1.57x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 37.4 ms: 1.53x faster                                                       |
| go                       | 139 ms                                                      | 90.7 ms: 1.53x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.2 ms: 1.50x faster                                                       |
| pylint                   | 350 ms                                                      | 243 ms: 1.44x faster                                                        |
| generators               | 32.4 ms                                                     | 22.5 ms: 1.44x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.42 ms: 1.43x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.7 us: 1.41x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 54.9 ms: 1.41x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 880 us: 1.38x faster                                                        |
| pyflate                  | 409 ms                                                      | 296 ms: 1.38x faster                                                        |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                        |
| nbody                    | 71.3 ms                                                     | 53.2 ms: 1.34x faster                                                       |
| richards_super           | 52.2 ms                                                     | 39.0 ms: 1.34x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 918 ms: 1.33x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.27 sec: 1.32x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.9 ms: 1.31x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 453 ms: 1.31x faster                                                        |
| float                    | 61.7 ms                                                     | 47.4 ms: 1.30x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 207 us: 1.30x faster                                                        |
| pycparser                | 930 ms                                                      | 721 ms: 1.29x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 144 us: 1.28x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 39.6 ms: 1.28x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.17 ms: 1.26x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.0 ms: 1.24x faster                                                       |
| raytrace                 | 273 ms                                                      | 222 ms: 1.23x faster                                                        |
| scimark_fft              | 187 ms                                                      | 153 ms: 1.23x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                       |
| richards                 | 42.4 ms                                                     | 34.9 ms: 1.21x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.21x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.25 ms: 1.21x faster                                                       |
| thrift                   | 617 us                                                      | 524 us: 1.18x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.17x faster                                                       |
| regex_compile            | 106 ms                                                      | 90.9 ms: 1.17x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.53 sec: 1.16x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 827 us: 1.16x faster                                                        |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 5.16 ms: 1.11x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 51.0 ms: 1.09x faster                                                       |
| django_template          | 28.9 ms                                                     | 26.7 ms: 1.08x faster                                                       |
| json                     | 3.14 ms                                                     | 2.93 ms: 1.07x faster                                                       |
| sympy_sum                | 107 ms                                                      | 101 ms: 1.06x faster                                                        |
| fannkuch                 | 256 ms                                                      | 242 ms: 1.06x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 64.3 ms: 1.04x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 73.5 ms: 1.03x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 19.2 ms: 1.03x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.61 ms: 1.03x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.2 ms: 1.03x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 94.4 ms: 1.03x faster                                                       |
| sympy_str                | 194 ms                                                      | 190 ms: 1.02x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.88 sec: 1.02x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.66 us: 1.01x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 208 ms: 1.01x slower                                                        |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                       |
| sympy_integrate          | 15.3 ms                                                     | 15.6 ms: 1.02x slower                                                       |
| 2to3                     | 246 ms                                                      | 251 ms: 1.02x slower                                                        |
| sympy_expand             | 314 ms                                                      | 321 ms: 1.02x slower                                                        |
| pathlib                  | 75.7 ms                                                     | 79.0 ms: 1.04x slower                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 42.6 ms: 1.07x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.29 ms: 1.09x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 45.5 ms: 1.11x slower                                                       |
| async_generators         | 222 ms                                                      | 259 ms: 1.17x slower                                                        |
| python_startup           | 20.6 ms                                                     | 24.9 ms: 1.21x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.8 ms: 1.21x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.4 ms: 1.22x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.93 ms: 1.37x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 93.3 ms: 1.50x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.37 ms: 1.72x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (2): logging_simple, regex_v8
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.208x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown