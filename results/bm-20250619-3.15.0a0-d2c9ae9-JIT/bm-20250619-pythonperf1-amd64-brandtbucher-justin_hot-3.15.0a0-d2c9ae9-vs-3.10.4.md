# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_hot
- machine: windows-amd64
- commit hash: d2c9ae9
- commit date: 2025-06-19
- overall geometric mean: 1.299x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                   |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                 |
| html5lib       | 51.0 ms                                                     | 38.2 ms: 1.34x faster                                                  |
| Geometric mean | (ref)                                                       | 1.20x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 398 ms: 2.79x faster                                                   |
| async_tree_none         | 435 ms                                                      | 171 ms: 2.54x faster                                                   |
| async_tree_memoization  | 526 ms                                                      | 207 ms: 2.54x faster                                                   |
| async_tree_cpu_io_mixed | 638 ms                                                      | 333 ms: 1.91x faster                                                   |
| Geometric mean          | (ref)                                                       | 2.42x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.0 ms: 1.40x faster                                                  |
| nbody          | 71.3 ms                                                     | 62.4 ms: 1.14x faster                                                  |
| Geometric mean | (ref)                                                       | 1.17x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.9 ms: 1.34x faster                                                  |
| regex_dna      | 136 ms                                                      | 120 ms: 1.13x faster                                                   |
| regex_v8       | 15.4 ms                                                     | 14.4 ms: 1.07x faster                                                  |
| regex_effbot   | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                       | 1.13x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 114 us: 1.61x faster                                                   |
| tomli_loads          | 1.67 sec                                                    | 1.16 sec: 1.45x faster                                                 |
| json_dumps           | 9.16 ms                                                     | 6.47 ms: 1.42x faster                                                  |
| pickle_pure_python   | 270 us                                                      | 205 us: 1.32x faster                                                   |
| xml_etree_process    | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                  |
| xml_etree_parse      | 96.8 ms                                                     | 88.1 ms: 1.10x faster                                                  |
| xml_etree_generate   | 55.5 ms                                                     | 50.7 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.8 ms: 1.03x faster                                                  |
| json_loads           | 14.0 us                                                     | 14.6 us: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                       | 1.23x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                  |
| python_startup         | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                  |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.47 ms: 1.65x faster                                                  |
| genshi_text     | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                  |
| django_template | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                  |
| genshi_xml      | 41.0 ms                                                     | 35.1 ms: 1.17x faster                                                  |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.26x faster                                                   |
| async_tree_io            | 1.11 sec                                                    | 398 ms: 2.79x faster                                                   |
| async_tree_none          | 435 ms                                                      | 171 ms: 2.54x faster                                                   |
| async_tree_memoization   | 526 ms                                                      | 207 ms: 2.54x faster                                                   |
| pathlib                  | 75.7 ms                                                     | 31.8 ms: 2.38x faster                                                  |
| mdp                      | 1.78 sec                                                    | 795 ms: 2.24x faster                                                   |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 333 ms: 1.91x faster                                                   |
| deltablue                | 4.19 ms                                                     | 2.24 ms: 1.87x faster                                                  |
| go                       | 139 ms                                                      | 77.5 ms: 1.79x faster                                                  |
| pylint                   | 350 ms                                                      | 201 ms: 1.74x faster                                                   |
| richards_super           | 52.2 ms                                                     | 30.7 ms: 1.70x faster                                                  |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                  |
| mako                     | 9.03 ms                                                     | 5.47 ms: 1.65x faster                                                  |
| unpickle_pure_python     | 183 us                                                      | 114 us: 1.61x faster                                                   |
| deepcopy_memo            | 28.8 us                                                     | 18.2 us: 1.58x faster                                                  |
| richards                 | 42.4 ms                                                     | 27.2 ms: 1.56x faster                                                  |
| pyflate                  | 409 ms                                                      | 263 ms: 1.55x faster                                                   |
| chaos                    | 61.7 ms                                                     | 40.4 ms: 1.53x faster                                                  |
| comprehensions           | 16.5 us                                                     | 10.8 us: 1.53x faster                                                  |
| deepcopy                 | 255 us                                                      | 169 us: 1.51x faster                                                   |
| raytrace                 | 273 ms                                                      | 182 ms: 1.50x faster                                                   |
| scimark_lu               | 85.8 ms                                                     | 58.9 ms: 1.46x faster                                                  |
| tomli_loads              | 1.67 sec                                                    | 1.16 sec: 1.45x faster                                                 |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.2 ms: 1.43x faster                                                  |
| json_dumps               | 9.16 ms                                                     | 6.47 ms: 1.42x faster                                                  |
| float                    | 61.7 ms                                                     | 44.0 ms: 1.40x faster                                                  |
| hexiom                   | 5.74 ms                                                     | 4.12 ms: 1.40x faster                                                  |
| scimark_sor              | 106 ms                                                      | 77.0 ms: 1.38x faster                                                  |
| crypto_pyaes             | 62.5 ms                                                     | 46.5 ms: 1.35x faster                                                  |
| regex_compile            | 106 ms                                                      | 78.9 ms: 1.34x faster                                                  |
| html5lib                 | 51.0 ms                                                     | 38.2 ms: 1.34x faster                                                  |
| pycparser                | 930 ms                                                      | 700 ms: 1.33x faster                                                   |
| pickle_pure_python       | 270 us                                                      | 205 us: 1.32x faster                                                   |
| genshi_text              | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                  |
| thrift                   | 617 us                                                      | 492 us: 1.26x faster                                                   |
| spectral_norm            | 77.3 ms                                                     | 61.7 ms: 1.25x faster                                                  |
| deepcopy_reduce          | 2.20 us                                                     | 1.79 us: 1.23x faster                                                  |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.22x faster                                                  |
| sympy_sum                | 107 ms                                                      | 87.5 ms: 1.22x faster                                                  |
| xml_etree_process        | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                                  |
| dulwich_log              | 50.5 ms                                                     | 41.5 ms: 1.22x faster                                                  |
| django_template          | 28.9 ms                                                     | 24.0 ms: 1.20x faster                                                  |
| sympy_integrate          | 15.3 ms                                                     | 12.8 ms: 1.19x faster                                                  |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.29 ms: 1.19x faster                                                  |
| pprint_pformat           | 1.22 sec                                                    | 1.03 sec: 1.18x faster                                                 |
| genshi_xml               | 41.0 ms                                                     | 35.1 ms: 1.17x faster                                                  |
| pprint_safe_repr         | 592 ms                                                      | 507 ms: 1.17x faster                                                   |
| scimark_fft              | 187 ms                                                      | 161 ms: 1.16x faster                                                   |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                 |
| nbody                    | 71.3 ms                                                     | 62.4 ms: 1.14x faster                                                  |
| nqueens                  | 66.6 ms                                                     | 58.4 ms: 1.14x faster                                                  |
| regex_dna                | 136 ms                                                      | 120 ms: 1.13x faster                                                   |
| sympy_str                | 194 ms                                                      | 172 ms: 1.13x faster                                                   |
| coroutines               | 16.0 ms                                                     | 14.3 ms: 1.12x faster                                                  |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                   |
| fannkuch                 | 256 ms                                                      | 232 ms: 1.10x faster                                                   |
| xml_etree_parse          | 96.8 ms                                                     | 88.1 ms: 1.10x faster                                                  |
| xml_etree_generate       | 55.5 ms                                                     | 50.7 ms: 1.09x faster                                                  |
| regex_v8                 | 15.4 ms                                                     | 14.4 ms: 1.07x faster                                                  |
| sympy_expand             | 314 ms                                                      | 297 ms: 1.06x faster                                                   |
| meteor_contest           | 75.9 ms                                                     | 71.8 ms: 1.06x faster                                                  |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.8 ms: 1.03x faster                                                  |
| json                     | 3.14 ms                                                     | 3.07 ms: 1.02x faster                                                  |
| logging_format           | 6.76 us                                                     | 6.64 us: 1.02x faster                                                  |
| regex_effbot             | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                  |
| logging_simple           | 6.22 us                                                     | 6.27 us: 1.01x slower                                                  |
| json_loads               | 14.0 us                                                     | 14.6 us: 1.04x slower                                                  |
| async_generators         | 222 ms                                                      | 243 ms: 1.09x slower                                                   |
| telco                    | 3.94 ms                                                     | 4.41 ms: 1.12x slower                                                  |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                  |
| python_startup           | 20.6 ms                                                     | 25.8 ms: 1.25x slower                                                  |
| coverage                 | 39.0 ms                                                     | 50.2 ms: 1.29x slower                                                  |
| gc_traversal             | 1.41 ms                                                     | 2.17 ms: 1.54x slower                                                  |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.65x slower                                                  |
| logging_silent           | 94.6 ns                                                     | 314 ns: 3.31x slower                                                   |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                           |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250619-3.15.0a0-d2c9ae9-JIT/bm-20250619-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.299x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown