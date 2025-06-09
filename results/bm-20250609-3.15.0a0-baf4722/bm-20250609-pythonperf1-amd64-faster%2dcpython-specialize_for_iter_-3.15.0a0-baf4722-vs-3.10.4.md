# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: windows-amd64
- commit hash: baf4722
- commit date: 2025-06-09
- overall geometric mean: 1.171x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 219 ms: 1.12x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                               |
| html5lib       | 51.0 ms                                                     | 39.1 ms: 1.30x faster                                                                |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 394 ms: 2.81x faster                                                                 |
| async_tree_none         | 435 ms                                                      | 169 ms: 2.57x faster                                                                 |
| async_tree_memoization  | 526 ms                                                      | 206 ms: 2.56x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 326 ms: 1.95x faster                                                                 |
| Geometric mean          | (ref)                                                       | 2.45x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.8 ms: 1.41x faster                                                                |
| nbody          | 71.3 ms                                                     | 63.8 ms: 1.12x faster                                                                |
| pidigits       | 149 ms                                                      | 148 ms: 1.00x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.8 ms: 1.30x faster                                                                |
| regex_dna      | 136 ms                                                      | 121 ms: 1.12x faster                                                                 |
| regex_v8       | 15.4 ms                                                     | 14.1 ms: 1.09x faster                                                                |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                                |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.22 ms: 1.47x faster                                                                |
| unpickle_pure_python | 183 us                                                      | 136 us: 1.35x faster                                                                 |
| pickle_pure_python   | 270 us                                                      | 212 us: 1.27x faster                                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                               |
| xml_etree_process    | 44.5 ms                                                     | 38.9 ms: 1.14x faster                                                                |
| xml_etree_parse      | 96.8 ms                                                     | 87.2 ms: 1.11x faster                                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.7 ms: 1.04x faster                                                                |
| xml_etree_generate   | 55.5 ms                                                     | 56.2 ms: 1.01x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.17x faster                                                                         |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.5 ms: 1.25x slower                                                                |
| python_startup         | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.55 ms: 1.38x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 33.2 ms: 1.24x faster                                                                |
| django_template | 28.9 ms                                                     | 23.8 ms: 1.21x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.28x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 101 us: 3.34x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 394 ms: 2.81x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 169 ms: 2.57x faster                                                                 |
| async_tree_memoization   | 526 ms                                                      | 206 ms: 2.56x faster                                                                 |
| pathlib                  | 75.7 ms                                                     | 31.8 ms: 2.38x faster                                                                |
| mdp                      | 1.78 sec                                                    | 802 ms: 2.22x faster                                                                 |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 326 ms: 1.95x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.24 ms: 1.87x faster                                                                |
| go                       | 139 ms                                                      | 76.2 ms: 1.82x faster                                                                |
| pylint                   | 350 ms                                                      | 197 ms: 1.78x faster                                                                 |
| richards_super           | 52.2 ms                                                     | 31.1 ms: 1.68x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 17.4 us: 1.66x faster                                                                |
| generators               | 32.4 ms                                                     | 19.8 ms: 1.64x faster                                                                |
| chaos                    | 61.7 ms                                                     | 39.1 ms: 1.58x faster                                                                |
| richards                 | 42.4 ms                                                     | 27.3 ms: 1.56x faster                                                                |
| comprehensions           | 16.5 us                                                     | 10.8 us: 1.53x faster                                                                |
| deepcopy                 | 255 us                                                      | 170 us: 1.51x faster                                                                 |
| raytrace                 | 273 ms                                                      | 183 ms: 1.50x faster                                                                 |
| json_dumps               | 9.16 ms                                                     | 6.22 ms: 1.47x faster                                                                |
| pyflate                  | 409 ms                                                      | 278 ms: 1.47x faster                                                                 |
| scimark_lu               | 85.8 ms                                                     | 58.8 ms: 1.46x faster                                                                |
| scimark_sor              | 106 ms                                                      | 74.1 ms: 1.43x faster                                                                |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.3 ms: 1.42x faster                                                                |
| hexiom                   | 5.74 ms                                                     | 4.06 ms: 1.41x faster                                                                |
| float                    | 61.7 ms                                                     | 43.8 ms: 1.41x faster                                                                |
| mako                     | 9.03 ms                                                     | 6.55 ms: 1.38x faster                                                                |
| unpickle_pure_python     | 183 us                                                      | 136 us: 1.35x faster                                                                 |
| spectral_norm            | 77.3 ms                                                     | 57.6 ms: 1.34x faster                                                                |
| crypto_pyaes             | 62.5 ms                                                     | 46.7 ms: 1.34x faster                                                                |
| pycparser                | 930 ms                                                      | 705 ms: 1.32x faster                                                                 |
| genshi_text              | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                                |
| html5lib                 | 51.0 ms                                                     | 39.1 ms: 1.30x faster                                                                |
| regex_compile            | 106 ms                                                      | 81.8 ms: 1.30x faster                                                                |
| pickle_pure_python       | 270 us                                                      | 212 us: 1.27x faster                                                                 |
| genshi_xml               | 41.0 ms                                                     | 33.2 ms: 1.24x faster                                                                |
| sympy_sum                | 107 ms                                                      | 87.0 ms: 1.23x faster                                                                |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.23x faster                                                                |
| tomli_loads              | 1.67 sec                                                    | 1.36 sec: 1.23x faster                                                               |
| deepcopy_reduce          | 2.20 us                                                     | 1.80 us: 1.22x faster                                                                |
| django_template          | 28.9 ms                                                     | 23.8 ms: 1.21x faster                                                                |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                                |
| dulwich_log              | 50.5 ms                                                     | 41.8 ms: 1.21x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.61 sec: 1.19x faster                                                               |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.15x faster                                                                |
| sympy_str                | 194 ms                                                      | 169 ms: 1.15x faster                                                                 |
| xml_etree_process        | 44.5 ms                                                     | 38.9 ms: 1.14x faster                                                                |
| 2to3                     | 246 ms                                                      | 219 ms: 1.12x faster                                                                 |
| regex_dna                | 136 ms                                                      | 121 ms: 1.12x faster                                                                 |
| nbody                    | 71.3 ms                                                     | 63.8 ms: 1.12x faster                                                                |
| xml_etree_parse          | 96.8 ms                                                     | 87.2 ms: 1.11x faster                                                                |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                                               |
| nqueens                  | 66.6 ms                                                     | 60.5 ms: 1.10x faster                                                                |
| pprint_safe_repr         | 592 ms                                                      | 538 ms: 1.10x faster                                                                 |
| sympy_expand             | 314 ms                                                      | 286 ms: 1.10x faster                                                                 |
| regex_v8                 | 15.4 ms                                                     | 14.1 ms: 1.09x faster                                                                |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.50 ms: 1.09x faster                                                                |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                                |
| scimark_fft              | 187 ms                                                      | 176 ms: 1.06x faster                                                                 |
| meteor_contest           | 75.9 ms                                                     | 71.8 ms: 1.06x faster                                                                |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.7 ms: 1.04x faster                                                                |
| json                     | 3.14 ms                                                     | 3.02 ms: 1.04x faster                                                                |
| fannkuch                 | 256 ms                                                      | 252 ms: 1.01x faster                                                                 |
| pidigits                 | 149 ms                                                      | 148 ms: 1.00x faster                                                                 |
| xml_etree_generate       | 55.5 ms                                                     | 56.2 ms: 1.01x slower                                                                |
| async_generators         | 222 ms                                                      | 231 ms: 1.04x slower                                                                 |
| telco                    | 3.94 ms                                                     | 4.64 ms: 1.18x slower                                                                |
| python_startup_no_site   | 15.5 ms                                                     | 19.5 ms: 1.25x slower                                                                |
| python_startup           | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                                |
| gc_traversal             | 1.41 ms                                                     | 2.14 ms: 1.52x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.65x slower                                                                |
| logging_silent           | 94.6 ns                                                     | 318 ns: 3.36x slower                                                                 |
| coverage                 | 39.0 ms                                                     | 290 ms: 7.44x slower                                                                 |
| thrift                   | 617 us                                                      | 93.6 ms: 151.61x slower                                                              |
| Geometric mean           | (ref)                                                       | 1.15x faster                                                                         |

Benchmark hidden because not significant (3): logging_format, json_loads, logging_simple
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250609-3.15.0a0-baf4722/bm-20250609-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-baf4722.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.171x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown