# Results vs. 3.10.4

- fork: python
- ref: 275056a7fdcbe36aaac4
- machine: windows-amd64
- commit hash: 275056a
- commit date: 2025-04-03
- overall geometric mean: 1.513x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 203 ms: 1.21x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.54 sec: 1.25x faster                                                      |
| html5lib       | 51.0 ms                                                     | 34.0 ms: 1.50x faster                                                       |
| Geometric mean | (ref)                                                       | 1.32x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 342 ms: 3.24x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 182 ms: 2.89x faster                                                        |
| async_tree_none         | 435 ms                                                      | 155 ms: 2.81x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 310 ms: 2.05x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.71x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 35.5 ms: 1.74x faster                                                       |
| nbody          | 71.3 ms                                                     | 50.4 ms: 1.41x faster                                                       |
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.36x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 67.8 ms: 1.57x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.3 ms: 1.16x faster                                                       |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 102 us: 1.79x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.01 sec: 1.65x faster                                                      |
| json_dumps           | 9.16 ms                                                     | 5.59 ms: 1.64x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 165 us: 1.64x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 33.0 ms: 1.35x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 48.1 ms: 1.16x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 88.4 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.1 ms: 1.08x faster                                                       |
| json_loads           | 14.0 us                                                     | 13.5 us: 1.04x faster                                                       |
| Geometric mean       | (ref)                                                       | 1.35x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.5 ms: 1.29x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 21.0 ms: 1.35x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 11.2 ms: 1.77x faster                                                       |
| mako            | 9.03 ms                                                     | 5.66 ms: 1.59x faster                                                       |
| django_template | 28.9 ms                                                     | 19.5 ms: 1.49x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 28.1 ms: 1.46x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.57x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 85.9 us: 3.91x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 342 ms: 3.24x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 182 ms: 2.89x faster                                                        |
| async_tree_none          | 435 ms                                                      | 155 ms: 2.81x faster                                                        |
| deltablue                | 4.19 ms                                                     | 1.52 ms: 2.76x faster                                                       |
| mdp                      | 1.78 sec                                                    | 669 ms: 2.66x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 30.9 ms: 2.45x faster                                                       |
| go                       | 139 ms                                                      | 58.2 ms: 2.39x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 41.0 ns: 2.31x faster                                                       |
| scimark_sor              | 106 ms                                                      | 47.8 ms: 2.22x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 13.1 us: 2.19x faster                                                       |
| generators               | 32.4 ms                                                     | 15.0 ms: 2.16x faster                                                       |
| richards_super           | 52.2 ms                                                     | 24.3 ms: 2.15x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 27.3 ms: 2.10x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 310 ms: 2.05x faster                                                        |
| richards                 | 42.4 ms                                                     | 20.7 ms: 2.05x faster                                                       |
| raytrace                 | 273 ms                                                      | 135 ms: 2.03x faster                                                        |
| chaos                    | 61.7 ms                                                     | 30.7 ms: 2.01x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 2.91 ms: 1.98x faster                                                       |
| comprehensions           | 16.5 us                                                     | 8.36 us: 1.97x faster                                                       |
| pylint                   | 350 ms                                                      | 184 ms: 1.90x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 45.1 ms: 1.90x faster                                                       |
| deepcopy                 | 255 us                                                      | 138 us: 1.85x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 102 us: 1.79x faster                                                        |
| pyflate                  | 409 ms                                                      | 229 ms: 1.79x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 11.2 ms: 1.77x faster                                                       |
| float                    | 61.7 ms                                                     | 35.5 ms: 1.74x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 46.8 ms: 1.65x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.01 sec: 1.65x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 5.59 ms: 1.64x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 165 us: 1.64x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 38.9 ms: 1.61x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.66 ms: 1.59x faster                                                       |
| regex_compile            | 106 ms                                                      | 67.8 ms: 1.57x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 393 ms: 1.51x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 34.0 ms: 1.50x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.48 us: 1.49x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 817 ms: 1.49x faster                                                        |
| django_template          | 28.9 ms                                                     | 19.5 ms: 1.49x faster                                                       |
| coroutines               | 16.0 ms                                                     | 10.9 ms: 1.47x faster                                                       |
| pycparser                | 930 ms                                                      | 636 ms: 1.46x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 28.1 ms: 1.46x faster                                                       |
| nbody                    | 71.3 ms                                                     | 50.4 ms: 1.41x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 11.2 ms: 1.36x faster                                                       |
| sympy_sum                | 107 ms                                                      | 78.6 ms: 1.36x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 33.0 ms: 1.35x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 49.6 ms: 1.34x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 37.8 ms: 1.34x faster                                                       |
| fannkuch                 | 256 ms                                                      | 192 ms: 1.33x faster                                                        |
| scimark_fft              | 187 ms                                                      | 141 ms: 1.33x faster                                                        |
| sympy_str                | 194 ms                                                      | 149 ms: 1.31x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.49 us: 1.28x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.15 ms: 1.27x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.54 sec: 1.25x faster                                                      |
| sympy_expand             | 314 ms                                                      | 257 ms: 1.22x faster                                                        |
| 2to3                     | 246 ms                                                      | 203 ms: 1.21x faster                                                        |
| async_generators         | 222 ms                                                      | 186 ms: 1.19x faster                                                        |
| regex_v8                 | 15.4 ms                                                     | 13.3 ms: 1.16x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 48.1 ms: 1.16x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 831 us: 1.15x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 66.3 ms: 1.14x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.00 us: 1.13x faster                                                       |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| logging_simple           | 6.22 us                                                     | 5.53 us: 1.13x faster                                                       |
| json                     | 3.14 ms                                                     | 2.84 ms: 1.10x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 88.4 ms: 1.10x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.1 ms: 1.08x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                       |
| json_loads               | 14.0 us                                                     | 13.5 us: 1.04x faster                                                       |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                        |
| coverage                 | 39.0 ms                                                     | 39.5 ms: 1.01x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.16 ms: 1.06x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.5 ms: 1.29x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 21.0 ms: 1.35x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 87.8 ms: 1.41x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.66x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.79 ms: 1.98x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.50x faster                                                                |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250403-3.14.0a6+-275056a-CLANG/bm-20250403-pythonperf1-amd64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.513x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.43x
- 95% likely to have a speedup of 1.40x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: unknown