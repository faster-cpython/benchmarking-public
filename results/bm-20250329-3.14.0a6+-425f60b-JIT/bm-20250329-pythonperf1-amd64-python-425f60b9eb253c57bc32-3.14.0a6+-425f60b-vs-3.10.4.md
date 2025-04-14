# Results vs. 3.10.4

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-amd64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.260x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.72 sec: 1.12x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.5 ms: 1.29x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 420 ms: 2.64x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 218 ms: 2.42x faster                                                        |
| async_tree_none         | 435 ms                                                      | 186 ms: 2.34x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 338 ms: 1.89x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 47.0 ms: 1.31x faster                                                       |
| nbody          | 71.3 ms                                                     | 60.9 ms: 1.17x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 83.4 ms: 1.27x faster                                                       |
| regex_dna      | 136 ms                                                      | 120 ms: 1.14x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 122 us: 1.50x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 6.79 ms: 1.35x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.25 sec: 1.34x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 219 us: 1.23x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 37.8 ms: 1.18x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 87.4 ms: 1.11x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 52.0 ms: 1.07x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.1 ms: 1.05x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.80 us: 1.03x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.80 us: 1.03x slower                                                       |
| json_loads           | 14.0 us                                                     | 15.0 us: 1.07x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 20.3 us: 1.18x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.33 us: 1.21x slower                                                       |
| pickle               | 6.85 us                                                     | 8.56 us: 1.25x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 20.4 ms: 1.31x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.66 ms: 1.60x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.4 ms: 1.21x faster                                                       |
| django_template | 28.9 ms                                                     | 25.2 ms: 1.14x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 36.5 ms: 1.12x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.26x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 3.00x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 420 ms: 2.64x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 218 ms: 2.42x faster                                                        |
| async_tree_none          | 435 ms                                                      | 186 ms: 2.34x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.7 ms: 2.32x faster                                                       |
| mdp                      | 1.78 sec                                                    | 792 ms: 2.25x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 338 ms: 1.89x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.35 ms: 1.78x faster                                                       |
| generators               | 32.4 ms                                                     | 18.3 ms: 1.77x faster                                                       |
| pylint                   | 350 ms                                                      | 206 ms: 1.70x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 58.1 ns: 1.63x faster                                                       |
| go                       | 139 ms                                                      | 85.7 ms: 1.62x faster                                                       |
| richards_super           | 52.2 ms                                                     | 32.4 ms: 1.61x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.66 ms: 1.60x faster                                                       |
| pyflate                  | 409 ms                                                      | 265 ms: 1.54x faster                                                        |
| raytrace                 | 273 ms                                                      | 180 ms: 1.52x faster                                                        |
| chaos                    | 61.7 ms                                                     | 40.8 ms: 1.51x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 122 us: 1.50x faster                                                        |
| richards                 | 42.4 ms                                                     | 28.7 ms: 1.48x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.44 sec: 1.46x faster                                                      |
| scimark_lu               | 85.8 ms                                                     | 60.5 ms: 1.42x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 517 ms: 1.42x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 20.9 us: 1.37x faster                                                       |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                        |
| comprehensions           | 16.5 us                                                     | 12.2 us: 1.36x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.79 ms: 1.35x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.25 sec: 1.34x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.2 ms: 1.32x faster                                                       |
| float                    | 61.7 ms                                                     | 47.0 ms: 1.31x faster                                                       |
| scimark_sor              | 106 ms                                                      | 81.4 ms: 1.30x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 59.4 ms: 1.30x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.5 ms: 1.29x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.13 ms: 1.28x faster                                                       |
| regex_compile            | 106 ms                                                      | 83.4 ms: 1.27x faster                                                       |
| pycparser                | 930 ms                                                      | 738 ms: 1.26x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 46.2 ms: 1.24x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.24x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 219 us: 1.23x faster                                                        |
| scimark_fft              | 187 ms                                                      | 154 ms: 1.21x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 4.73 ms: 1.21x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.4 ms: 1.21x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.4 ms: 1.19x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.03 sec: 1.19x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 37.8 ms: 1.18x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.9 ms: 1.18x faster                                                       |
| nbody                    | 71.3 ms                                                     | 60.9 ms: 1.17x faster                                                       |
| sympy_sum                | 107 ms                                                      | 92.2 ms: 1.16x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 511 ms: 1.16x faster                                                        |
| django_template          | 28.9 ms                                                     | 25.2 ms: 1.14x faster                                                       |
| regex_dna                | 136 ms                                                      | 120 ms: 1.14x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.5 ms: 1.12x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.72 sec: 1.12x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.99 us: 1.11x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 87.4 ms: 1.11x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 872 us: 1.10x faster                                                        |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 62.1 ms: 1.07x faster                                                       |
| sympy_str                | 194 ms                                                      | 182 ms: 1.07x faster                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 52.0 ms: 1.07x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.1 ms: 1.05x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.80 us: 1.03x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 38.5 ns: 1.03x faster                                                       |
| json                     | 3.14 ms                                                     | 3.10 ms: 1.01x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 76.7 ms: 1.01x slower                                                       |
| sympy_expand             | 314 ms                                                      | 319 ms: 1.01x slower                                                        |
| logging_format           | 6.76 us                                                     | 6.95 us: 1.03x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.80 us: 1.03x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.48 us: 1.04x slower                                                       |
| json_loads               | 14.0 us                                                     | 15.0 us: 1.07x slower                                                       |
| async_generators         | 222 ms                                                      | 244 ms: 1.10x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.55 ms: 1.15x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 20.3 us: 1.18x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.33 us: 1.21x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.7 ms: 1.25x slower                                                       |
| pickle                   | 6.85 us                                                     | 8.56 us: 1.25x slower                                                       |
| coverage                 | 39.0 ms                                                     | 49.4 ms: 1.27x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.4 ms: 1.31x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 89.0 ms: 1.43x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.05 ms: 1.45x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.25 ms: 1.57x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                                |

Benchmark hidden because not significant (2): fannkuch, pidigits
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.260x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown