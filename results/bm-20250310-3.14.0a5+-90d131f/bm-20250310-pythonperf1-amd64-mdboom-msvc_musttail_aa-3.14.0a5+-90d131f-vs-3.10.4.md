# Results vs. 3.10.4

- fork: mdboom
- ref: msvc_musttail_aa
- machine: windows-amd64
- commit hash: 90d131f
- commit date: 2025-03-10
- overall geometric mean: 1.167x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 309 ms: 1.26x slower                                                    |
| docutils       | 1.92 sec                                                    | 2.31 sec: 1.20x slower                                                  |
| html5lib       | 51.0 ms                                                     | 52.5 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                       | 1.16x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 570 ms: 1.95x faster                                                    |
| async_tree_memoization  | 526 ms                                                      | 313 ms: 1.68x faster                                                    |
| async_tree_none         | 435 ms                                                      | 267 ms: 1.63x faster                                                    |
| async_tree_cpu_io_mixed | 638 ms                                                      | 455 ms: 1.40x faster                                                    |
| Geometric mean          | (ref)                                                       | 1.65x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 149 ms                                                      | 156 ms: 1.05x slower                                                    |
| float          | 61.7 ms                                                     | 78.0 ms: 1.26x slower                                                   |
| nbody          | 71.3 ms                                                     | 103 ms: 1.45x slower                                                    |
| Geometric mean | (ref)                                                       | 1.24x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 123 ms: 1.11x faster                                                    |
| regex_effbot   | 1.66 ms                                                     | 1.87 ms: 1.13x slower                                                   |
| regex_v8       | 15.4 ms                                                     | 17.5 ms: 1.13x slower                                                   |
| regex_compile  | 106 ms                                                      | 130 ms: 1.22x slower                                                    |
| Geometric mean | (ref)                                                       | 1.09x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 9.44 ms: 1.03x slower                                                   |
| xml_etree_parse      | 96.8 ms                                                     | 112 ms: 1.16x slower                                                    |
| tomli_loads          | 1.67 sec                                                    | 2.07 sec: 1.24x slower                                                  |
| pickle_pure_python   | 270 us                                                      | 364 us: 1.35x slower                                                    |
| xml_etree_iterparse  | 65.0 ms                                                     | 94.3 ms: 1.45x slower                                                   |
| xml_etree_process    | 44.5 ms                                                     | 66.9 ms: 1.50x slower                                                   |
| unpickle_pure_python | 183 us                                                      | 284 us: 1.55x slower                                                    |
| json_loads           | 14.0 us                                                     | 23.3 us: 1.66x slower                                                   |
| xml_etree_generate   | 55.5 ms                                                     | 92.6 ms: 1.67x slower                                                   |
| Geometric mean       | (ref)                                                       | 1.39x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 22.0 ms: 1.42x slower                                                   |
| python_startup         | 20.6 ms                                                     | 29.5 ms: 1.43x slower                                                   |
| Geometric mean         | (ref)                                                       | 1.43x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 23.9 ms: 1.21x slower                                                   |
| genshi_xml      | 41.0 ms                                                     | 50.4 ms: 1.23x slower                                                   |
| django_template | 28.9 ms                                                     | 38.0 ms: 1.31x slower                                                   |
| mako            | 9.03 ms                                                     | 12.1 ms: 1.34x slower                                                   |
| Geometric mean  | (ref)                                                       | 1.27x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 154 us: 2.18x faster                                                    |
| pathlib                  | 75.7 ms                                                     | 37.5 ms: 2.02x faster                                                   |
| async_tree_io            | 1.11 sec                                                    | 570 ms: 1.95x faster                                                    |
| async_tree_memoization   | 526 ms                                                      | 313 ms: 1.68x faster                                                    |
| async_tree_none          | 435 ms                                                      | 267 ms: 1.63x faster                                                    |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 455 ms: 1.40x faster                                                    |
| pylint                   | 350 ms                                                      | 269 ms: 1.30x faster                                                    |
| regex_dna                | 136 ms                                                      | 123 ms: 1.11x faster                                                    |
| deltablue                | 4.19 ms                                                     | 4.22 ms: 1.01x slower                                                   |
| go                       | 139 ms                                                      | 140 ms: 1.01x slower                                                    |
| sqlite_synth             | 1.91 us                                                     | 1.96 us: 1.02x slower                                                   |
| html5lib                 | 51.0 ms                                                     | 52.5 ms: 1.03x slower                                                   |
| json_dumps               | 9.16 ms                                                     | 9.44 ms: 1.03x slower                                                   |
| dulwich_log              | 50.5 ms                                                     | 52.4 ms: 1.04x slower                                                   |
| pidigits                 | 149 ms                                                      | 156 ms: 1.05x slower                                                    |
| mdp                      | 1.78 sec                                                    | 1.89 sec: 1.06x slower                                                  |
| deepcopy                 | 255 us                                                      | 278 us: 1.09x slower                                                    |
| pycparser                | 930 ms                                                      | 1.01 sec: 1.09x slower                                                  |
| generators               | 32.4 ms                                                     | 35.6 ms: 1.10x slower                                                   |
| chaos                    | 61.7 ms                                                     | 69.3 ms: 1.12x slower                                                   |
| regex_effbot             | 1.66 ms                                                     | 1.87 ms: 1.13x slower                                                   |
| regex_v8                 | 15.4 ms                                                     | 17.5 ms: 1.13x slower                                                   |
| raytrace                 | 273 ms                                                      | 313 ms: 1.14x slower                                                    |
| thrift                   | 617 us                                                      | 710 us: 1.15x slower                                                    |
| sympy_sum                | 107 ms                                                      | 123 ms: 1.15x slower                                                    |
| xml_etree_parse          | 96.8 ms                                                     | 112 ms: 1.16x slower                                                    |
| pyflate                  | 409 ms                                                      | 477 ms: 1.17x slower                                                    |
| deepcopy_memo            | 28.8 us                                                     | 34.0 us: 1.18x slower                                                   |
| docutils                 | 1.92 sec                                                    | 2.31 sec: 1.20x slower                                                  |
| sympy_integrate          | 15.3 ms                                                     | 18.4 ms: 1.21x slower                                                   |
| genshi_text              | 19.8 ms                                                     | 23.9 ms: 1.21x slower                                                   |
| comprehensions           | 16.5 us                                                     | 20.1 us: 1.22x slower                                                   |
| regex_compile            | 106 ms                                                      | 130 ms: 1.22x slower                                                    |
| genshi_xml               | 41.0 ms                                                     | 50.4 ms: 1.23x slower                                                   |
| tomli_loads              | 1.67 sec                                                    | 2.07 sec: 1.24x slower                                                  |
| 2to3                     | 246 ms                                                      | 309 ms: 1.26x slower                                                    |
| float                    | 61.7 ms                                                     | 78.0 ms: 1.26x slower                                                   |
| sympy_str                | 194 ms                                                      | 247 ms: 1.27x slower                                                    |
| crypto_pyaes             | 62.5 ms                                                     | 80.1 ms: 1.28x slower                                                   |
| richards_super           | 52.2 ms                                                     | 67.7 ms: 1.30x slower                                                   |
| hexiom                   | 5.74 ms                                                     | 7.44 ms: 1.30x slower                                                   |
| json                     | 3.14 ms                                                     | 4.07 ms: 1.30x slower                                                   |
| deepcopy_reduce          | 2.20 us                                                     | 2.86 us: 1.30x slower                                                   |
| scimark_sor              | 106 ms                                                      | 139 ms: 1.31x slower                                                    |
| meteor_contest           | 75.9 ms                                                     | 99.5 ms: 1.31x slower                                                   |
| logging_silent           | 94.6 ns                                                     | 124 ns: 1.31x slower                                                    |
| django_template          | 28.9 ms                                                     | 38.0 ms: 1.31x slower                                                   |
| spectral_norm            | 77.3 ms                                                     | 102 ms: 1.32x slower                                                    |
| scimark_monte_carlo      | 57.3 ms                                                     | 75.8 ms: 1.32x slower                                                   |
| sympy_expand             | 314 ms                                                      | 419 ms: 1.33x slower                                                    |
| bench_thread_pool        | 958 us                                                      | 1.28 ms: 1.33x slower                                                   |
| mako                     | 9.03 ms                                                     | 12.1 ms: 1.34x slower                                                   |
| pickle_pure_python       | 270 us                                                      | 364 us: 1.35x slower                                                    |
| pprint_pformat           | 1.22 sec                                                    | 1.66 sec: 1.36x slower                                                  |
| richards                 | 42.4 ms                                                     | 59.0 ms: 1.39x slower                                                   |
| scimark_lu               | 85.8 ms                                                     | 119 ms: 1.39x slower                                                    |
| pprint_safe_repr         | 592 ms                                                      | 825 ms: 1.39x slower                                                    |
| coroutines               | 16.0 ms                                                     | 22.4 ms: 1.40x slower                                                   |
| python_startup_no_site   | 15.5 ms                                                     | 22.0 ms: 1.42x slower                                                   |
| python_startup           | 20.6 ms                                                     | 29.5 ms: 1.43x slower                                                   |
| nbody                    | 71.3 ms                                                     | 103 ms: 1.45x slower                                                    |
| xml_etree_iterparse      | 65.0 ms                                                     | 94.3 ms: 1.45x slower                                                   |
| nqueens                  | 66.6 ms                                                     | 96.9 ms: 1.45x slower                                                   |
| logging_format           | 6.76 us                                                     | 9.92 us: 1.47x slower                                                   |
| scimark_fft              | 187 ms                                                      | 276 ms: 1.47x slower                                                    |
| logging_simple           | 6.22 us                                                     | 9.30 us: 1.49x slower                                                   |
| xml_etree_process        | 44.5 ms                                                     | 66.9 ms: 1.50x slower                                                   |
| unpickle_pure_python     | 183 us                                                      | 284 us: 1.55x slower                                                    |
| async_generators         | 222 ms                                                      | 348 ms: 1.57x slower                                                    |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 4.43 ms: 1.63x slower                                                   |
| bench_mp_pool            | 62.0 ms                                                     | 101 ms: 1.63x slower                                                    |
| coverage                 | 39.0 ms                                                     | 63.7 ms: 1.63x slower                                                   |
| fannkuch                 | 256 ms                                                      | 418 ms: 1.63x slower                                                    |
| json_loads               | 14.0 us                                                     | 23.3 us: 1.66x slower                                                   |
| telco                    | 3.94 ms                                                     | 6.56 ms: 1.67x slower                                                   |
| xml_etree_generate       | 55.5 ms                                                     | 92.6 ms: 1.67x slower                                                   |
| create_gc_cycles         | 800 us                                                      | 1.42 ms: 1.77x slower                                                   |
| gc_traversal             | 1.41 ms                                                     | 3.25 ms: 2.31x slower                                                   |
| Geometric mean           | (ref)                                                       | 1.21x slower                                                            |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250310-3.14.0a5+-90d131f/bm-20250310-pythonperf1-amd64-mdboom-msvc_musttail_aa-3.14.0a5+-90d131f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.167x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.18x
- 95% likely to have a slowdown of 1.17x
- 99% likely to have a slowdown of 1.15x

# Memory
- memory change: unknown