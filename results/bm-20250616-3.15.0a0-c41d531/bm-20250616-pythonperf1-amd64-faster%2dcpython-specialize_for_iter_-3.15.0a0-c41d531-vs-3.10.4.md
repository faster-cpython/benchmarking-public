# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: windows-amd64
- commit hash: c41d531
- commit date: 2025-06-16
- overall geometric mean: 1.153x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                                                 |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                               |
| html5lib       | 51.0 ms                                                     | 38.8 ms: 1.32x faster                                                                |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 400 ms: 2.77x faster                                                                 |
| async_tree_memoization  | 526 ms                                                      | 208 ms: 2.53x faster                                                                 |
| async_tree_none         | 435 ms                                                      | 172 ms: 2.53x faster                                                                 |
| async_tree_cpu_io_mixed | 638 ms                                                      | 326 ms: 1.95x faster                                                                 |
| Geometric mean          | (ref)                                                       | 2.42x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 45.6 ms: 1.35x faster                                                                |
| nbody          | 71.3 ms                                                     | 65.7 ms: 1.09x faster                                                                |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 82.2 ms: 1.29x faster                                                                |
| regex_dna      | 136 ms                                                      | 121 ms: 1.12x faster                                                                 |
| regex_effbot   | 1.66 ms                                                     | 1.51 ms: 1.10x faster                                                                |
| regex_v8       | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                                |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.29 ms: 1.46x faster                                                                |
| unpickle_pure_python | 183 us                                                      | 139 us: 1.32x faster                                                                 |
| pickle_pure_python   | 270 us                                                      | 215 us: 1.26x faster                                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                               |
| xml_etree_process    | 44.5 ms                                                     | 39.4 ms: 1.13x faster                                                                |
| xml_etree_parse      | 96.8 ms                                                     | 89.1 ms: 1.09x faster                                                                |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.7 ms: 1.02x faster                                                                |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                                |
| xml_etree_generate   | 55.5 ms                                                     | 57.2 ms: 1.03x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.6 ms: 1.24x slower                                                                |
| python_startup_no_site | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.67 ms: 1.35x faster                                                                |
| genshi_text     | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                                                |
| genshi_xml      | 41.0 ms                                                     | 34.0 ms: 1.21x faster                                                                |
| django_template | 28.9 ms                                                     | 24.4 ms: 1.19x faster                                                                |
| Geometric mean  | (ref)                                                       | 1.26x faster                                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.26x faster                                                                 |
| async_tree_io            | 1.11 sec                                                    | 400 ms: 2.77x faster                                                                 |
| async_tree_memoization   | 526 ms                                                      | 208 ms: 2.53x faster                                                                 |
| async_tree_none          | 435 ms                                                      | 172 ms: 2.53x faster                                                                 |
| pathlib                  | 75.7 ms                                                     | 32.3 ms: 2.34x faster                                                                |
| mdp                      | 1.78 sec                                                    | 826 ms: 2.16x faster                                                                 |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 326 ms: 1.95x faster                                                                 |
| deltablue                | 4.19 ms                                                     | 2.23 ms: 1.88x faster                                                                |
| go                       | 139 ms                                                      | 77.3 ms: 1.80x faster                                                                |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                                 |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                                |
| richards_super           | 52.2 ms                                                     | 31.7 ms: 1.65x faster                                                                |
| chaos                    | 61.7 ms                                                     | 39.0 ms: 1.58x faster                                                                |
| richards                 | 42.4 ms                                                     | 27.9 ms: 1.52x faster                                                                |
| deepcopy_memo            | 28.8 us                                                     | 19.0 us: 1.51x faster                                                                |
| deepcopy                 | 255 us                                                      | 172 us: 1.48x faster                                                                 |
| comprehensions           | 16.5 us                                                     | 11.2 us: 1.47x faster                                                                |
| raytrace                 | 273 ms                                                      | 186 ms: 1.47x faster                                                                 |
| pyflate                  | 409 ms                                                      | 280 ms: 1.46x faster                                                                 |
| json_dumps               | 9.16 ms                                                     | 6.29 ms: 1.46x faster                                                                |
| scimark_lu               | 85.8 ms                                                     | 59.3 ms: 1.45x faster                                                                |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.9 ms: 1.40x faster                                                                |
| hexiom                   | 5.74 ms                                                     | 4.14 ms: 1.39x faster                                                                |
| mako                     | 9.03 ms                                                     | 6.67 ms: 1.35x faster                                                                |
| float                    | 61.7 ms                                                     | 45.6 ms: 1.35x faster                                                                |
| scimark_sor              | 106 ms                                                      | 79.1 ms: 1.34x faster                                                                |
| crypto_pyaes             | 62.5 ms                                                     | 47.3 ms: 1.32x faster                                                                |
| unpickle_pure_python     | 183 us                                                      | 139 us: 1.32x faster                                                                 |
| html5lib                 | 51.0 ms                                                     | 38.8 ms: 1.32x faster                                                                |
| spectral_norm            | 77.3 ms                                                     | 59.4 ms: 1.30x faster                                                                |
| pycparser                | 930 ms                                                      | 716 ms: 1.30x faster                                                                 |
| regex_compile            | 106 ms                                                      | 82.2 ms: 1.29x faster                                                                |
| genshi_text              | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                                                |
| pickle_pure_python       | 270 us                                                      | 215 us: 1.26x faster                                                                 |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.23x faster                                                                |
| sympy_sum                | 107 ms                                                      | 87.7 ms: 1.22x faster                                                                |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.21x faster                                                                |
| dulwich_log              | 50.5 ms                                                     | 41.7 ms: 1.21x faster                                                                |
| genshi_xml               | 41.0 ms                                                     | 34.0 ms: 1.21x faster                                                                |
| tomli_loads              | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                               |
| django_template          | 28.9 ms                                                     | 24.4 ms: 1.19x faster                                                                |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.18x faster                                                               |
| deepcopy_reduce          | 2.20 us                                                     | 1.88 us: 1.18x faster                                                                |
| sympy_str                | 194 ms                                                      | 170 ms: 1.15x faster                                                                 |
| coroutines               | 16.0 ms                                                     | 14.0 ms: 1.14x faster                                                                |
| xml_etree_process        | 44.5 ms                                                     | 39.4 ms: 1.13x faster                                                                |
| regex_dna                | 136 ms                                                      | 121 ms: 1.12x faster                                                                 |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                                                 |
| regex_effbot             | 1.66 ms                                                     | 1.51 ms: 1.10x faster                                                                |
| sympy_expand             | 314 ms                                                      | 287 ms: 1.10x faster                                                                 |
| xml_etree_parse          | 96.8 ms                                                     | 89.1 ms: 1.09x faster                                                                |
| nbody                    | 71.3 ms                                                     | 65.7 ms: 1.09x faster                                                                |
| pprint_pformat           | 1.22 sec                                                    | 1.13 sec: 1.08x faster                                                               |
| pprint_safe_repr         | 592 ms                                                      | 553 ms: 1.07x faster                                                                 |
| nqueens                  | 66.6 ms                                                     | 62.8 ms: 1.06x faster                                                                |
| json                     | 3.14 ms                                                     | 3.00 ms: 1.05x faster                                                                |
| scimark_fft              | 187 ms                                                      | 179 ms: 1.04x faster                                                                 |
| regex_v8                 | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                                |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.66 ms: 1.02x faster                                                                |
| meteor_contest           | 75.9 ms                                                     | 74.3 ms: 1.02x faster                                                                |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.7 ms: 1.02x faster                                                                |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                                 |
| fannkuch                 | 256 ms                                                      | 257 ms: 1.00x slower                                                                 |
| logging_simple           | 6.22 us                                                     | 6.30 us: 1.01x slower                                                                |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                                |
| xml_etree_generate       | 55.5 ms                                                     | 57.2 ms: 1.03x slower                                                                |
| async_generators         | 222 ms                                                      | 234 ms: 1.06x slower                                                                 |
| telco                    | 3.94 ms                                                     | 4.62 ms: 1.17x slower                                                                |
| python_startup           | 20.6 ms                                                     | 25.6 ms: 1.24x slower                                                                |
| python_startup_no_site   | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                                |
| gc_traversal             | 1.41 ms                                                     | 2.18 ms: 1.54x slower                                                                |
| create_gc_cycles         | 800 us                                                      | 1.33 ms: 1.66x slower                                                                |
| logging_silent           | 94.6 ns                                                     | 317 ns: 3.35x slower                                                                 |
| coverage                 | 39.0 ms                                                     | 293 ms: 7.50x slower                                                                 |
| thrift                   | 617 us                                                      | 97.5 ms: 157.93x slower                                                              |
| Geometric mean           | (ref)                                                       | 1.13x faster                                                                         |

Benchmark hidden because not significant (1): logging_format
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250616-3.15.0a0-c41d531/bm-20250616-pythonperf1-amd64-faster%2dcpython-specialize_for_iter_-3.15.0a0-c41d531.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.153x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown