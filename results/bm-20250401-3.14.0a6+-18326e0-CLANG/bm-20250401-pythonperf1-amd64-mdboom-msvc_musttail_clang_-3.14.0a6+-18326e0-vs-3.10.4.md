# Results vs. 3.10.4

- fork: mdboom
- ref: msvc_musttail_clang_
- machine: windows-amd64
- commit hash: 18326e0
- commit date: 2025-04-01
- overall geometric mean: 1.479x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 207 ms: 1.19x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.56 sec: 1.23x faster                                                      |
| html5lib       | 51.0 ms                                                     | 34.9 ms: 1.46x faster                                                       |
| Geometric mean | (ref)                                                       | 1.29x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 353 ms: 3.14x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 187 ms: 2.81x faster                                                        |
| async_tree_none         | 435 ms                                                      | 159 ms: 2.74x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 313 ms: 2.04x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.65x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 36.9 ms: 1.67x faster                                                       |
| nbody          | 71.3 ms                                                     | 49.1 ms: 1.45x faster                                                       |
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.36x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 69.8 ms: 1.52x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.0 ms: 1.19x faster                                                       |
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 107 us: 1.71x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 5.66 ms: 1.62x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 173 us: 1.56x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.09 sec: 1.54x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 34.0 ms: 1.31x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 49.1 ms: 1.13x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 89.4 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.5 ms: 1.06x faster                                                       |
| Geometric mean       | (ref)                                                       | 1.31x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.4 ms: 1.28x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 20.9 ms: 1.35x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 11.9 ms: 1.66x faster                                                       |
| mako            | 9.03 ms                                                     | 5.83 ms: 1.55x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 29.0 ms: 1.41x faster                                                       |
| django_template | 28.9 ms                                                     | 21.3 ms: 1.36x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.49x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 87.6 us: 3.84x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 353 ms: 3.14x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 187 ms: 2.81x faster                                                        |
| async_tree_none          | 435 ms                                                      | 159 ms: 2.74x faster                                                        |
| mdp                      | 1.78 sec                                                    | 682 ms: 2.61x faster                                                        |
| deltablue                | 4.19 ms                                                     | 1.64 ms: 2.55x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 30.7 ms: 2.47x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 41.1 ns: 2.30x faster                                                       |
| go                       | 139 ms                                                      | 61.5 ms: 2.26x faster                                                       |
| generators               | 32.4 ms                                                     | 14.8 ms: 2.19x faster                                                       |
| scimark_sor              | 106 ms                                                      | 49.3 ms: 2.15x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 14.0 us: 2.06x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 313 ms: 2.04x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 28.6 ms: 2.00x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 43.5 ms: 1.97x faster                                                       |
| chaos                    | 61.7 ms                                                     | 31.4 ms: 1.96x faster                                                       |
| raytrace                 | 273 ms                                                      | 142 ms: 1.92x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 2.98 ms: 1.92x faster                                                       |
| comprehensions           | 16.5 us                                                     | 8.64 us: 1.91x faster                                                       |
| pylint                   | 350 ms                                                      | 188 ms: 1.86x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 42.8 ms: 1.80x faster                                                       |
| deepcopy                 | 255 us                                                      | 144 us: 1.77x faster                                                        |
| pyflate                  | 409 ms                                                      | 234 ms: 1.74x faster                                                        |
| richards_super           | 52.2 ms                                                     | 30.2 ms: 1.73x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 107 us: 1.71x faster                                                        |
| float                    | 61.7 ms                                                     | 36.9 ms: 1.67x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 11.9 ms: 1.66x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.66 ms: 1.62x faster                                                       |
| richards                 | 42.4 ms                                                     | 26.3 ms: 1.62x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 39.9 ms: 1.57x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 173 us: 1.56x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.83 ms: 1.55x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.09 sec: 1.54x faster                                                      |
| regex_compile            | 106 ms                                                      | 69.8 ms: 1.52x faster                                                       |
| coroutines               | 16.0 ms                                                     | 10.7 ms: 1.49x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 835 ms: 1.46x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 34.9 ms: 1.46x faster                                                       |
| nbody                    | 71.3 ms                                                     | 49.1 ms: 1.45x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.52 us: 1.45x faster                                                       |
| pycparser                | 930 ms                                                      | 647 ms: 1.44x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 415 ms: 1.43x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 29.0 ms: 1.41x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 1.99 ms: 1.37x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 11.2 ms: 1.36x faster                                                       |
| django_template          | 28.9 ms                                                     | 21.3 ms: 1.36x faster                                                       |
| sympy_sum                | 107 ms                                                      | 79.2 ms: 1.35x faster                                                       |
| scimark_fft              | 187 ms                                                      | 139 ms: 1.34x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 49.8 ms: 1.34x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 38.0 ms: 1.33x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 34.0 ms: 1.31x faster                                                       |
| sympy_str                | 194 ms                                                      | 149 ms: 1.31x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.51 us: 1.27x faster                                                       |
| fannkuch                 | 256 ms                                                      | 207 ms: 1.24x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.56 sec: 1.23x faster                                                      |
| sympy_expand             | 314 ms                                                      | 256 ms: 1.23x faster                                                        |
| regex_v8                 | 15.4 ms                                                     | 13.0 ms: 1.19x faster                                                       |
| 2to3                     | 246 ms                                                      | 207 ms: 1.19x faster                                                        |
| async_generators         | 222 ms                                                      | 187 ms: 1.18x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 823 us: 1.16x faster                                                        |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 66.8 ms: 1.14x faster                                                       |
| logging_format           | 6.76 us                                                     | 5.96 us: 1.13x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 49.1 ms: 1.13x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.55 us: 1.12x faster                                                       |
| json                     | 3.14 ms                                                     | 2.81 ms: 1.11x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 89.4 ms: 1.08x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.5 ms: 1.06x faster                                                       |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                        |
| coverage                 | 39.0 ms                                                     | 39.8 ms: 1.02x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.25 ms: 1.08x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.4 ms: 1.28x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.9 ms: 1.35x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.6 ms: 1.43x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.36 ms: 1.70x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.76 ms: 1.95x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.47x faster                                                                |

Benchmark hidden because not significant (1): json_loads
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250401-3.14.0a6+-18326e0-CLANG/bm-20250401-pythonperf1-amd64-mdboom-msvc_musttail_clang_-3.14.0a6+-18326e0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.479x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.34x

# Memory
- memory change: unknown