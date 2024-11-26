# Results vs. 3.10.4

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: windows-amd64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.164x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 227 ms: 1.08x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.3 ms: 1.27x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 220 ms: 1.98x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 564 ms: 1.96x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 279 ms: 1.89x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 383 ms: 1.67x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.87x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 56.0 ms: 1.10x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| nbody          | 71.3 ms                                                     | 79.6 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 91.5 ms: 1.16x faster                                                       |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.67 ms: 1.37x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 153 us: 1.20x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 229 us: 1.18x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 40.5 ms: 1.10x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.60 sec: 1.04x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 93.1 ms: 1.04x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.03x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 57.4 ms: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.6 ms: 1.13x slower                                                       |
| python_startup         | 20.6 ms                                                     | 24.3 ms: 1.18x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.93 ms: 1.30x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 35.1 ms: 1.17x faster                                                       |
| django_template | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.98x faster                                                        |
| async_tree_none          | 435 ms                                                      | 220 ms: 1.98x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 564 ms: 1.96x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 279 ms: 1.89x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.34 ms: 1.79x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 383 ms: 1.67x faster                                                        |
| pylint                   | 350 ms                                                      | 225 ms: 1.56x faster                                                        |
| go                       | 139 ms                                                      | 90.5 ms: 1.54x faster                                                       |
| generators               | 32.4 ms                                                     | 21.7 ms: 1.49x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 64.6 ns: 1.46x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 60.6 ms: 1.42x faster                                                       |
| richards_super           | 52.2 ms                                                     | 37.2 ms: 1.40x faster                                                       |
| chaos                    | 61.7 ms                                                     | 44.8 ms: 1.38x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.0 us: 1.38x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.67 ms: 1.37x faster                                                       |
| raytrace                 | 273 ms                                                      | 200 ms: 1.37x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 21.2 us: 1.36x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 922 us: 1.32x faster                                                        |
| mako                     | 9.03 ms                                                     | 6.93 ms: 1.30x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 48.0 ms: 1.30x faster                                                       |
| deepcopy                 | 255 us                                                      | 196 us: 1.30x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.14 ms: 1.30x faster                                                       |
| richards                 | 42.4 ms                                                     | 32.9 ms: 1.29x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.49 ms: 1.28x faster                                                       |
| pyflate                  | 409 ms                                                      | 322 ms: 1.27x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 40.3 ms: 1.27x faster                                                       |
| pycparser                | 930 ms                                                      | 738 ms: 1.26x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.45 sec: 1.22x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 153 us: 1.20x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 48.0 ms: 1.19x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.3 ms: 1.18x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.6 ms: 1.18x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 229 us: 1.18x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 813 us: 1.18x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 35.1 ms: 1.17x faster                                                       |
| scimark_sor              | 106 ms                                                      | 91.0 ms: 1.17x faster                                                       |
| thrift                   | 617 us                                                      | 530 us: 1.16x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 43.4 ms: 1.16x faster                                                       |
| regex_compile            | 106 ms                                                      | 91.5 ms: 1.16x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 67.8 ms: 1.14x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                      |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| float                    | 61.7 ms                                                     | 56.0 ms: 1.10x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.00 us: 1.10x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 40.5 ms: 1.10x faster                                                       |
| sympy_str                | 194 ms                                                      | 179 ms: 1.09x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 545 ms: 1.09x faster                                                        |
| 2to3                     | 246 ms                                                      | 227 ms: 1.08x faster                                                        |
| json                     | 3.14 ms                                                     | 2.92 ms: 1.07x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 37.2 ms: 1.07x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.60 sec: 1.04x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 93.1 ms: 1.04x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 198 ms: 1.04x faster                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.03x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 65.0 ms: 1.03x faster                                                       |
| sympy_expand             | 314 ms                                                      | 307 ms: 1.03x faster                                                        |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.83 us: 1.01x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.39 us: 1.03x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 78.0 ms: 1.03x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.03x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 57.4 ms: 1.03x slower                                                       |
| scimark_fft              | 187 ms                                                      | 196 ms: 1.04x slower                                                        |
| pathlib                  | 75.7 ms                                                     | 79.1 ms: 1.05x slower                                                       |
| fannkuch                 | 256 ms                                                      | 280 ms: 1.09x slower                                                        |
| nbody                    | 71.3 ms                                                     | 79.6 ms: 1.12x slower                                                       |
| async_generators         | 222 ms                                                      | 248 ms: 1.12x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 17.6 ms: 1.13x slower                                                       |
| python_startup           | 20.6 ms                                                     | 24.3 ms: 1.18x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.2 ms: 1.21x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.81 ms: 1.22x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 83.0 ms: 1.34x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.93 ms: 1.37x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.38 ms: 1.73x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.16x faster                                                                |

Benchmark hidden because not significant (3): scimark_sparse_mat_mult, regex_v8, xml_etree_iterparse
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-pythonperf1-amd64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.164x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown