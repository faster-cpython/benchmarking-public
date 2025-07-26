# Results vs. 3.10.4

- fork: python
- ref: 1e69cd1634e4f0f8c375
- machine: windows-amd64
- commit hash: 1e69cd1
- commit date: 2025-07-25
- overall geometric mean: 1.307x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                     |
| html5lib       | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 398 ms: 2.79x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 203 ms: 2.59x faster                                                       |
| async_tree_none         | 435 ms                                                      | 177 ms: 2.46x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 337 ms: 1.89x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.41x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.4 ms: 1.39x faster                                                      |
| nbody          | 71.3 ms                                                     | 56.7 ms: 1.26x faster                                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.0 ms: 1.33x faster                                                      |
| regex_dna      | 136 ms                                                      | 121 ms: 1.12x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.9 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.12x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 105 us: 1.75x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.11 sec: 1.51x faster                                                     |
| json_dumps           | 9.16 ms                                                     | 6.31 ms: 1.45x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 207 us: 1.30x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 35.2 ms: 1.26x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 49.8 ms: 1.12x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 89.2 ms: 1.09x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.25x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.9 ms: 1.28x slower                                                      |
| python_startup         | 20.6 ms                                                     | 26.7 ms: 1.29x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.40 ms: 1.67x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 16.1 ms: 1.23x faster                                                      |
| django_template | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 35.2 ms: 1.17x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 102 us: 3.28x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 398 ms: 2.79x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 203 ms: 2.59x faster                                                       |
| async_tree_none          | 435 ms                                                      | 177 ms: 2.46x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 33.5 ms: 2.26x faster                                                      |
| mdp                      | 1.78 sec                                                    | 808 ms: 2.20x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.19 ms: 1.91x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 337 ms: 1.89x faster                                                       |
| go                       | 139 ms                                                      | 77.0 ms: 1.81x faster                                                      |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 105 us: 1.75x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 54.3 ns: 1.74x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.40 ms: 1.67x faster                                                      |
| richards_super           | 52.2 ms                                                     | 31.6 ms: 1.66x faster                                                      |
| pyflate                  | 409 ms                                                      | 249 ms: 1.64x faster                                                       |
| generators               | 32.4 ms                                                     | 20.1 ms: 1.61x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.0 us: 1.60x faster                                                      |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.56x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.8 ms: 1.53x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.11 sec: 1.51x faster                                                     |
| deepcopy                 | 255 us                                                      | 170 us: 1.50x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.3 ms: 1.49x faster                                                      |
| raytrace                 | 273 ms                                                      | 183 ms: 1.49x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 58.2 ms: 1.47x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.31 ms: 1.45x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.3 ms: 1.42x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.05 ms: 1.42x faster                                                      |
| float                    | 61.7 ms                                                     | 44.4 ms: 1.39x faster                                                      |
| scimark_sor              | 106 ms                                                      | 77.9 ms: 1.36x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 46.2 ms: 1.35x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 906 ms: 1.35x faster                                                       |
| pycparser                | 930 ms                                                      | 695 ms: 1.34x faster                                                       |
| regex_compile            | 106 ms                                                      | 80.0 ms: 1.33x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 452 ms: 1.31x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 207 us: 1.30x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.2 ms: 1.26x faster                                                      |
| thrift                   | 617 us                                                      | 491 us: 1.26x faster                                                       |
| nbody                    | 71.3 ms                                                     | 56.7 ms: 1.26x faster                                                      |
| fannkuch                 | 256 ms                                                      | 207 ms: 1.23x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.1 ms: 1.23x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 41.2 ms: 1.22x faster                                                      |
| django_template          | 28.9 ms                                                     | 23.9 ms: 1.21x faster                                                      |
| sympy_sum                | 107 ms                                                      | 88.7 ms: 1.21x faster                                                      |
| scimark_fft              | 187 ms                                                      | 155 ms: 1.21x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.84 us: 1.20x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.19x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.0 ms: 1.18x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 35.2 ms: 1.17x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.34 ms: 1.17x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                     |
| spectral_norm            | 77.3 ms                                                     | 67.0 ms: 1.15x faster                                                      |
| sympy_str                | 194 ms                                                      | 172 ms: 1.13x faster                                                       |
| regex_dna                | 136 ms                                                      | 121 ms: 1.12x faster                                                       |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 49.8 ms: 1.12x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 60.6 ms: 1.10x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.6 ms: 1.09x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 89.2 ms: 1.09x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.97 us: 1.04x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.52 us: 1.04x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.9 ms: 1.04x faster                                                      |
| sympy_expand             | 314 ms                                                      | 304 ms: 1.04x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 73.4 ms: 1.03x faster                                                      |
| json                     | 3.14 ms                                                     | 3.04 ms: 1.03x faster                                                      |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.01x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.32 ms: 1.10x slower                                                      |
| async_generators         | 222 ms                                                      | 253 ms: 1.14x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.9 ms: 1.28x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.7 ms: 1.29x slower                                                      |
| coverage                 | 39.0 ms                                                     | 50.5 ms: 1.29x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.24 ms: 1.59x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.37 ms: 1.71x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.30x faster                                                               |

Benchmark hidden because not significant (3): regex_effbot, xml_etree_iterparse, pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250725-3.15.0a0-1e69cd1-JIT/bm-20250725-pythonperf1-amd64-python-1e69cd1634e4f0f8c375-3.15.0a0-1e69cd1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.307x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown