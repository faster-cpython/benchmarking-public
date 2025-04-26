# Results vs. 3.10.4

- fork: mdboom
- ref: python_startup_time
- machine: windows-amd64
- commit hash: 9fc1238
- commit date: 2025-04-25
- overall geometric mean: 1.282x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                     |
| html5lib       | 51.0 ms                                                     | 37.9 ms: 1.35x faster                                                      |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 408 ms: 2.72x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 205 ms: 2.57x faster                                                       |
| async_tree_none         | 435 ms                                                      | 178 ms: 2.44x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 331 ms: 1.93x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.40x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 42.6 ms: 1.45x faster                                                      |
| nbody          | 71.3 ms                                                     | 62.2 ms: 1.15x faster                                                      |
| pidigits       | 149 ms                                                      | 150 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.6 ms: 1.32x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.47 ms: 1.13x faster                                                      |
| regex_dna      | 136 ms                                                      | 121 ms: 1.12x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.69 ms: 1.37x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 136 us: 1.35x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 210 us: 1.28x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 39.9 ms: 1.11x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 88.5 ms: 1.09x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 56.3 ms: 1.01x slower                                                      |
| json_loads           | 14.0 us                                                     | 14.9 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.2 ms: 1.27x slower                                                      |
| python_startup_no_site | 15.5 ms                                                     | 19.9 ms: 1.28x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.65 ms: 1.36x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 33.8 ms: 1.21x faster                                                      |
| django_template | 28.9 ms                                                     | 24.2 ms: 1.20x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.26x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.21x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 408 ms: 2.72x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 205 ms: 2.57x faster                                                       |
| async_tree_none          | 435 ms                                                      | 178 ms: 2.44x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 32.0 ms: 2.37x faster                                                      |
| mdp                      | 1.78 sec                                                    | 781 ms: 2.28x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 331 ms: 1.93x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.17 ms: 1.93x faster                                                      |
| go                       | 139 ms                                                      | 77.3 ms: 1.80x faster                                                      |
| pylint                   | 350 ms                                                      | 200 ms: 1.75x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 54.8 ns: 1.73x faster                                                      |
| generators               | 32.4 ms                                                     | 19.2 ms: 1.69x faster                                                      |
| richards_super           | 52.2 ms                                                     | 32.4 ms: 1.61x faster                                                      |
| chaos                    | 61.7 ms                                                     | 38.4 ms: 1.61x faster                                                      |
| raytrace                 | 273 ms                                                      | 173 ms: 1.58x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 18.5 us: 1.56x faster                                                      |
| deepcopy                 | 255 us                                                      | 171 us: 1.49x faster                                                       |
| richards                 | 42.4 ms                                                     | 28.4 ms: 1.49x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 58.5 ms: 1.47x faster                                                      |
| pyflate                  | 409 ms                                                      | 281 ms: 1.46x faster                                                       |
| float                    | 61.7 ms                                                     | 42.6 ms: 1.45x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.4 us: 1.45x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 54.7 ms: 1.41x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.07 ms: 1.41x faster                                                      |
| scimark_sor              | 106 ms                                                      | 76.2 ms: 1.39x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.3 ms: 1.39x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.69 ms: 1.37x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.65 ms: 1.36x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 136 us: 1.35x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 37.9 ms: 1.35x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.4 ms: 1.32x faster                                                      |
| pycparser                | 930 ms                                                      | 707 ms: 1.32x faster                                                       |
| regex_compile            | 106 ms                                                      | 80.6 ms: 1.32x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 210 us: 1.28x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.79 us: 1.23x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 33.8 ms: 1.21x faster                                                      |
| sympy_sum                | 107 ms                                                      | 88.5 ms: 1.21x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                     |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 41.9 ms: 1.20x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.2 ms: 1.20x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.02 sec: 1.19x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 504 ms: 1.17x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                     |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                      |
| nbody                    | 71.3 ms                                                     | 62.2 ms: 1.15x faster                                                      |
| sympy_str                | 194 ms                                                      | 170 ms: 1.14x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.47 ms: 1.13x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 59.2 ms: 1.12x faster                                                      |
| regex_dna                | 136 ms                                                      | 121 ms: 1.12x faster                                                       |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.9 ms: 1.11x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 862 us: 1.11x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.48 ms: 1.10x faster                                                      |
| scimark_fft              | 187 ms                                                      | 171 ms: 1.10x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 88.5 ms: 1.09x faster                                                      |
| sympy_expand             | 314 ms                                                      | 293 ms: 1.07x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                      |
| json                     | 3.14 ms                                                     | 3.08 ms: 1.02x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 74.8 ms: 1.01x faster                                                      |
| fannkuch                 | 256 ms                                                      | 255 ms: 1.00x faster                                                       |
| pidigits                 | 149 ms                                                      | 150 ms: 1.00x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 56.3 ms: 1.01x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.9 us: 1.06x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.61 ms: 1.17x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.2 ms: 1.27x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.9 ms: 1.28x slower                                                      |
| coverage                 | 39.0 ms                                                     | 51.7 ms: 1.32x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 89.0 ms: 1.43x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.08 ms: 1.48x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.26 ms: 1.57x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                               |

Benchmark hidden because not significant (4): xml_etree_iterparse, logging_format, async_generators, logging_simple
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250425-3.14.0a7+-9fc1238/bm-20250425-pythonperf1-amd64-mdboom-python_startup_time-3.14.0a7+-9fc1238.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.282x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown