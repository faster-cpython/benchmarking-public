# Results vs. 3.10.4

- fork: gpshead
- ref: traceback_timestamps
- machine: windows-amd64
- commit hash: e4f54d4
- commit date: 2025-06-08
- overall geometric mean: 1.162x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.62 sec: 1.19x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                       |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 389 ms: 2.85x faster                                                        |
| async_tree_none         | 435 ms                                                      | 170 ms: 2.56x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 206 ms: 2.55x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 331 ms: 1.93x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.45x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.0 ms: 1.40x faster                                                       |
| nbody          | 71.3 ms                                                     | 62.8 ms: 1.13x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.4 ms: 1.32x faster                                                       |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.53 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.31 ms: 1.45x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 137 us: 1.34x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 212 us: 1.27x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 39.0 ms: 1.14x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 89.7 ms: 1.08x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.1 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.6 ms: 1.26x slower                                                       |
| python_startup         | 20.6 ms                                                     | 26.2 ms: 1.27x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.65 ms: 1.36x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                                       |
| django_template | 28.9 ms                                                     | 24.0 ms: 1.21x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 34.5 ms: 1.19x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.26x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.27x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 389 ms: 2.85x faster                                                        |
| async_tree_none          | 435 ms                                                      | 170 ms: 2.56x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 206 ms: 2.55x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.4 ms: 2.34x faster                                                       |
| mdp                      | 1.78 sec                                                    | 801 ms: 2.22x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 331 ms: 1.93x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.23 ms: 1.88x faster                                                       |
| go                       | 139 ms                                                      | 77.3 ms: 1.80x faster                                                       |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                                        |
| generators               | 32.4 ms                                                     | 19.5 ms: 1.66x faster                                                       |
| richards_super           | 52.2 ms                                                     | 31.5 ms: 1.66x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 18.3 us: 1.57x faster                                                       |
| chaos                    | 61.7 ms                                                     | 39.8 ms: 1.55x faster                                                       |
| richards                 | 42.4 ms                                                     | 27.7 ms: 1.53x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.9 us: 1.52x faster                                                       |
| deepcopy                 | 255 us                                                      | 171 us: 1.50x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 57.4 ms: 1.49x faster                                                       |
| raytrace                 | 273 ms                                                      | 183 ms: 1.49x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.31 ms: 1.45x faster                                                       |
| pyflate                  | 409 ms                                                      | 287 ms: 1.42x faster                                                        |
| scimark_sor              | 106 ms                                                      | 75.2 ms: 1.41x faster                                                       |
| float                    | 61.7 ms                                                     | 44.0 ms: 1.40x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.14 ms: 1.39x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.5 ms: 1.38x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.65 ms: 1.36x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 137 us: 1.34x faster                                                        |
| pycparser                | 930 ms                                                      | 704 ms: 1.32x faster                                                        |
| regex_compile            | 106 ms                                                      | 80.4 ms: 1.32x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 47.6 ms: 1.32x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 60.1 ms: 1.29x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 212 us: 1.27x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.24x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.9 ms: 1.23x faster                                                       |
| sympy_sum                | 107 ms                                                      | 87.4 ms: 1.22x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.0 ms: 1.21x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.84 us: 1.20x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 34.5 ms: 1.19x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.62 sec: 1.19x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.64 us: 1.17x faster                                                       |
| sympy_str                | 194 ms                                                      | 168 ms: 1.16x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.9 ms: 1.15x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.0 ms: 1.14x faster                                                       |
| nbody                    | 71.3 ms                                                     | 62.8 ms: 1.13x faster                                                       |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| regex_v8                 | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                       |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                                        |
| sympy_expand             | 314 ms                                                      | 285 ms: 1.10x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 1.12 sec: 1.09x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.53 ms: 1.08x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 61.6 ms: 1.08x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 89.7 ms: 1.08x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 554 ms: 1.07x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.55 ms: 1.07x faster                                                       |
| scimark_fft              | 187 ms                                                      | 178 ms: 1.05x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 73.4 ms: 1.03x faster                                                       |
| json                     | 3.14 ms                                                     | 3.03 ms: 1.03x faster                                                       |
| json_loads               | 14.0 us                                                     | 14.1 us: 1.01x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.31 us: 1.01x slower                                                       |
| async_generators         | 222 ms                                                      | 232 ms: 1.05x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.57 ms: 1.16x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.6 ms: 1.26x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.2 ms: 1.27x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.17 ms: 1.54x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.66x slower                                                       |
| logging_silent           | 94.6 ns                                                     | 324 ns: 3.42x slower                                                        |
| coverage                 | 39.0 ms                                                     | 291 ms: 7.46x slower                                                        |
| thrift                   | 617 us                                                      | 93.6 ms: 151.57x slower                                                     |
| Geometric mean           | (ref)                                                       | 1.14x faster                                                                |

Benchmark hidden because not significant (5): pidigits, xml_etree_iterparse, fannkuch, xml_etree_generate, logging_format
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250608-3.15.0a0-e4f54d4/bm-20250608-pythonperf1-amd64-gpshead-traceback_timestamps-3.15.0a0-e4f54d4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.162x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown