# Results vs. 3.10.4

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-amd64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.489x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 203 ms: 1.21x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.53 sec: 1.25x faster                                                      |
| html5lib       | 51.0 ms                                                     | 35.4 ms: 1.44x faster                                                       |
| Geometric mean | (ref)                                                       | 1.30x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 350 ms: 3.17x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 189 ms: 2.79x faster                                                        |
| async_tree_none         | 435 ms                                                      | 157 ms: 2.78x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 312 ms: 2.05x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.66x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 36.9 ms: 1.67x faster                                                       |
| nbody          | 71.3 ms                                                     | 48.0 ms: 1.48x faster                                                       |
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.37x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 69.1 ms: 1.53x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 12.4 ms: 1.24x faster                                                       |
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.50 ms: 1.10x faster                                                       |
| Geometric mean | (ref)                                                       | 1.25x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 106 us: 1.73x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 5.50 ms: 1.66x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 174 us: 1.55x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.09 sec: 1.54x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 34.2 ms: 1.30x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 49.0 ms: 1.13x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 91.0 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.6 ms: 1.06x faster                                                       |
| json_loads           | 14.0 us                                                     | 13.8 us: 1.01x faster                                                       |
| Geometric mean       | (ref)                                                       | 1.31x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.6 ms: 1.29x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 20.3 ms: 1.31x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 12.3 ms: 1.61x faster                                                       |
| mako            | 9.03 ms                                                     | 5.80 ms: 1.56x faster                                                       |
| django_template | 28.9 ms                                                     | 20.5 ms: 1.41x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 29.8 ms: 1.38x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.49x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 87.6 us: 3.83x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 350 ms: 3.17x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 189 ms: 2.79x faster                                                        |
| async_tree_none          | 435 ms                                                      | 157 ms: 2.78x faster                                                        |
| mdp                      | 1.78 sec                                                    | 671 ms: 2.65x faster                                                        |
| deltablue                | 4.19 ms                                                     | 1.62 ms: 2.58x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 31.2 ms: 2.43x faster                                                       |
| go                       | 139 ms                                                      | 60.7 ms: 2.29x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 41.8 ns: 2.26x faster                                                       |
| scimark_sor              | 106 ms                                                      | 50.0 ms: 2.12x faster                                                       |
| generators               | 32.4 ms                                                     | 15.3 ms: 2.12x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 14.0 us: 2.06x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 312 ms: 2.05x faster                                                        |
| richards_super           | 52.2 ms                                                     | 25.7 ms: 2.03x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 43.5 ms: 1.97x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 29.1 ms: 1.97x faster                                                       |
| chaos                    | 61.7 ms                                                     | 31.4 ms: 1.96x faster                                                       |
| raytrace                 | 273 ms                                                      | 140 ms: 1.95x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 2.96 ms: 1.94x faster                                                       |
| comprehensions           | 16.5 us                                                     | 8.60 us: 1.92x faster                                                       |
| richards                 | 42.4 ms                                                     | 22.2 ms: 1.91x faster                                                       |
| pylint                   | 350 ms                                                      | 185 ms: 1.89x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 42.8 ms: 1.81x faster                                                       |
| deepcopy                 | 255 us                                                      | 143 us: 1.79x faster                                                        |
| pyflate                  | 409 ms                                                      | 229 ms: 1.78x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 106 us: 1.73x faster                                                        |
| float                    | 61.7 ms                                                     | 36.9 ms: 1.67x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.50 ms: 1.66x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 12.3 ms: 1.61x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 39.2 ms: 1.60x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.80 ms: 1.56x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 174 us: 1.55x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.09 sec: 1.54x faster                                                      |
| regex_compile            | 106 ms                                                      | 69.1 ms: 1.53x faster                                                       |
| coroutines               | 16.0 ms                                                     | 10.7 ms: 1.50x faster                                                       |
| nbody                    | 71.3 ms                                                     | 48.0 ms: 1.48x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 828 ms: 1.47x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 405 ms: 1.46x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 35.4 ms: 1.44x faster                                                       |
| pycparser                | 930 ms                                                      | 645 ms: 1.44x faster                                                        |
| django_template          | 28.9 ms                                                     | 20.5 ms: 1.41x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.57 us: 1.41x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 29.8 ms: 1.38x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 48.4 ms: 1.38x faster                                                       |
| sympy_sum                | 107 ms                                                      | 78.7 ms: 1.36x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.01 ms: 1.36x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 11.3 ms: 1.35x faster                                                       |
| scimark_fft              | 187 ms                                                      | 139 ms: 1.35x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 38.2 ms: 1.32x faster                                                       |
| fannkuch                 | 256 ms                                                      | 196 ms: 1.31x faster                                                        |
| sympy_str                | 194 ms                                                      | 149 ms: 1.31x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 34.2 ms: 1.30x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.49 us: 1.29x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.53 sec: 1.25x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 12.4 ms: 1.24x faster                                                       |
| sympy_expand             | 314 ms                                                      | 257 ms: 1.22x faster                                                        |
| async_generators         | 222 ms                                                      | 183 ms: 1.21x faster                                                        |
| 2to3                     | 246 ms                                                      | 203 ms: 1.21x faster                                                        |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 825 us: 1.16x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 65.9 ms: 1.15x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 49.0 ms: 1.13x faster                                                       |
| json                     | 3.14 ms                                                     | 2.78 ms: 1.13x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.04 us: 1.12x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.62 us: 1.11x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.50 ms: 1.10x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 91.0 ms: 1.06x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.6 ms: 1.06x faster                                                       |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                        |
| json_loads               | 14.0 us                                                     | 13.8 us: 1.01x faster                                                       |
| telco                    | 3.94 ms                                                     | 4.33 ms: 1.10x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.0 ms: 1.20x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.6 ms: 1.29x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.3 ms: 1.31x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.8 ms: 1.43x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.36 ms: 1.70x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.73 ms: 1.93x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.48x faster                                                                |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-425f60b-CLANG/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.489x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.40x
- 95% likely to have a speedup of 1.38x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: unknown