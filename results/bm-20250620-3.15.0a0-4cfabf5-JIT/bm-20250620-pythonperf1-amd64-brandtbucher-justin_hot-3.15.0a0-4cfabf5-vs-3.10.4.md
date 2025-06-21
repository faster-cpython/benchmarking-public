# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_hot
- machine: windows-amd64
- commit hash: 4cfabf5
- commit date: 2025-06-20
- overall geometric mean: 1.296x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                                   |
| docutils       | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                 |
| html5lib       | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                  |
| Geometric mean | (ref)                                                       | 1.19x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 400 ms: 2.77x faster                                                   |
| async_tree_none         | 435 ms                                                      | 172 ms: 2.53x faster                                                   |
| async_tree_memoization  | 526 ms                                                      | 210 ms: 2.50x faster                                                   |
| async_tree_cpu_io_mixed | 638 ms                                                      | 334 ms: 1.91x faster                                                   |
| Geometric mean          | (ref)                                                       | 2.41x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.2 ms: 1.40x faster                                                  |
| nbody          | 71.3 ms                                                     | 56.4 ms: 1.26x faster                                                  |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                       | 1.21x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.5 ms: 1.33x faster                                                  |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                   |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.08x faster                                                  |
| regex_effbot   | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                       | 1.13x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 112 us: 1.63x faster                                                   |
| json_dumps           | 9.16 ms                                                     | 6.21 ms: 1.47x faster                                                  |
| tomli_loads          | 1.67 sec                                                    | 1.18 sec: 1.42x faster                                                 |
| pickle_pure_python   | 270 us                                                      | 207 us: 1.31x faster                                                   |
| xml_etree_process    | 44.5 ms                                                     | 36.6 ms: 1.21x faster                                                  |
| xml_etree_parse      | 96.8 ms                                                     | 87.9 ms: 1.10x faster                                                  |
| xml_etree_generate   | 55.5 ms                                                     | 52.2 ms: 1.06x faster                                                  |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.3 ms: 1.01x faster                                                  |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                       | 1.23x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                  |
| python_startup_no_site | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                  |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.65 ms: 1.60x faster                                                  |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                  |
| django_template | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                  |
| genshi_xml      | 41.0 ms                                                     | 34.4 ms: 1.19x faster                                                  |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 107 us: 3.15x faster                                                   |
| async_tree_io            | 1.11 sec                                                    | 400 ms: 2.77x faster                                                   |
| async_tree_none          | 435 ms                                                      | 172 ms: 2.53x faster                                                   |
| async_tree_memoization   | 526 ms                                                      | 210 ms: 2.50x faster                                                   |
| pathlib                  | 75.7 ms                                                     | 31.8 ms: 2.38x faster                                                  |
| mdp                      | 1.78 sec                                                    | 820 ms: 2.17x faster                                                   |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 334 ms: 1.91x faster                                                   |
| deltablue                | 4.19 ms                                                     | 2.23 ms: 1.88x faster                                                  |
| go                       | 139 ms                                                      | 78.5 ms: 1.77x faster                                                  |
| pylint                   | 350 ms                                                      | 202 ms: 1.74x faster                                                   |
| richards_super           | 52.2 ms                                                     | 31.5 ms: 1.66x faster                                                  |
| generators               | 32.4 ms                                                     | 19.7 ms: 1.64x faster                                                  |
| unpickle_pure_python     | 183 us                                                      | 112 us: 1.63x faster                                                   |
| mako                     | 9.03 ms                                                     | 5.65 ms: 1.60x faster                                                  |
| deepcopy_memo            | 28.8 us                                                     | 18.4 us: 1.57x faster                                                  |
| chaos                    | 61.7 ms                                                     | 39.5 ms: 1.56x faster                                                  |
| pyflate                  | 409 ms                                                      | 263 ms: 1.55x faster                                                   |
| richards                 | 42.4 ms                                                     | 27.8 ms: 1.52x faster                                                  |
| raytrace                 | 273 ms                                                      | 181 ms: 1.51x faster                                                   |
| deepcopy                 | 255 us                                                      | 171 us: 1.50x faster                                                   |
| comprehensions           | 16.5 us                                                     | 11.2 us: 1.48x faster                                                  |
| json_dumps               | 9.16 ms                                                     | 6.21 ms: 1.47x faster                                                  |
| scimark_lu               | 85.8 ms                                                     | 58.9 ms: 1.46x faster                                                  |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.9 ms: 1.44x faster                                                  |
| tomli_loads              | 1.67 sec                                                    | 1.18 sec: 1.42x faster                                                 |
| scimark_sor              | 106 ms                                                      | 75.9 ms: 1.40x faster                                                  |
| float                    | 61.7 ms                                                     | 44.2 ms: 1.40x faster                                                  |
| hexiom                   | 5.74 ms                                                     | 4.13 ms: 1.39x faster                                                  |
| crypto_pyaes             | 62.5 ms                                                     | 45.9 ms: 1.36x faster                                                  |
| regex_compile            | 106 ms                                                      | 79.5 ms: 1.33x faster                                                  |
| html5lib                 | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                  |
| pycparser                | 930 ms                                                      | 708 ms: 1.31x faster                                                   |
| pickle_pure_python       | 270 us                                                      | 207 us: 1.31x faster                                                   |
| spectral_norm            | 77.3 ms                                                     | 59.3 ms: 1.30x faster                                                  |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                  |
| nbody                    | 71.3 ms                                                     | 56.4 ms: 1.26x faster                                                  |
| thrift                   | 617 us                                                      | 489 us: 1.26x faster                                                   |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.24x faster                                                  |
| dulwich_log              | 50.5 ms                                                     | 41.3 ms: 1.22x faster                                                  |
| sympy_sum                | 107 ms                                                      | 88.1 ms: 1.22x faster                                                  |
| xml_etree_process        | 44.5 ms                                                     | 36.6 ms: 1.21x faster                                                  |
| deepcopy_reduce          | 2.20 us                                                     | 1.82 us: 1.21x faster                                                  |
| sympy_integrate          | 15.3 ms                                                     | 12.7 ms: 1.20x faster                                                  |
| django_template          | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                  |
| scimark_fft              | 187 ms                                                      | 156 ms: 1.20x faster                                                   |
| genshi_xml               | 41.0 ms                                                     | 34.4 ms: 1.19x faster                                                  |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.34 ms: 1.17x faster                                                  |
| pprint_pformat           | 1.22 sec                                                    | 1.05 sec: 1.16x faster                                                 |
| docutils                 | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                 |
| pprint_safe_repr         | 592 ms                                                      | 518 ms: 1.14x faster                                                   |
| sympy_str                | 194 ms                                                      | 172 ms: 1.13x faster                                                   |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                   |
| nqueens                  | 66.6 ms                                                     | 59.4 ms: 1.12x faster                                                  |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                                   |
| coroutines               | 16.0 ms                                                     | 14.5 ms: 1.10x faster                                                  |
| xml_etree_parse          | 96.8 ms                                                     | 87.9 ms: 1.10x faster                                                  |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.08x faster                                                  |
| fannkuch                 | 256 ms                                                      | 236 ms: 1.08x faster                                                   |
| xml_etree_generate       | 55.5 ms                                                     | 52.2 ms: 1.06x faster                                                  |
| sympy_expand             | 314 ms                                                      | 297 ms: 1.06x faster                                                   |
| json                     | 3.14 ms                                                     | 3.00 ms: 1.05x faster                                                  |
| meteor_contest           | 75.9 ms                                                     | 73.3 ms: 1.04x faster                                                  |
| regex_effbot             | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                  |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.3 ms: 1.01x faster                                                  |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                   |
| logging_format           | 6.76 us                                                     | 6.86 us: 1.02x slower                                                  |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                  |
| logging_simple           | 6.22 us                                                     | 6.49 us: 1.04x slower                                                  |
| telco                    | 3.94 ms                                                     | 4.35 ms: 1.11x slower                                                  |
| async_generators         | 222 ms                                                      | 248 ms: 1.12x slower                                                   |
| python_startup           | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                  |
| coverage                 | 39.0 ms                                                     | 49.0 ms: 1.26x slower                                                  |
| python_startup_no_site   | 15.5 ms                                                     | 19.5 ms: 1.26x slower                                                  |
| gc_traversal             | 1.41 ms                                                     | 2.16 ms: 1.53x slower                                                  |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.66x slower                                                  |
| logging_silent           | 94.6 ns                                                     | 319 ns: 3.37x slower                                                   |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                           |
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250620-3.15.0a0-4cfabf5-JIT/bm-20250620-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-4cfabf5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.296x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown