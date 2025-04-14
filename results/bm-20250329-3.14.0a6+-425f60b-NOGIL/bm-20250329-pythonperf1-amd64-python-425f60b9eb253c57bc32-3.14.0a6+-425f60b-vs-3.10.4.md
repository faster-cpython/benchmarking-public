# Results vs. 3.10.4

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-amd64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.117x faster
- HPT reliability: 99.24%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 235 ms: 1.05x faster                                                        |
| docutils       | 1.92 sec                                                    | 2.99 sec: 1.56x slower                                                      |
| html5lib       | 51.0 ms                                                     | 42.5 ms: 1.20x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 378 ms: 2.93x faster                                                        |
| async_tree_none         | 435 ms                                                      | 181 ms: 2.40x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 228 ms: 2.31x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 339 ms: 1.88x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.35x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 48.1 ms: 1.28x faster                                                       |
| pidigits       | 149 ms                                                      | 138 ms: 1.08x faster                                                        |
| nbody          | 71.3 ms                                                     | 92.0 ms: 1.29x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 111 ms: 1.22x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 13.1 ms: 1.18x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.45 ms: 1.15x faster                                                       |
| regex_compile  | 106 ms                                                      | 97.2 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 7.62 ms: 1.20x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 238 us: 1.13x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 165 us: 1.11x faster                                                        |
| xml_etree_iterparse  | 65.0 ms                                                     | 59.6 ms: 1.09x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 90.1 ms: 1.07x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 45.9 ms: 1.03x slower                                                       |
| unpickle             | 9.09 us                                                     | 9.86 us: 1.09x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 63.6 ms: 1.15x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 20.4 us: 1.19x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.33 us: 1.21x slower                                                       |
| pickle               | 6.85 us                                                     | 8.39 us: 1.22x slower                                                       |
| json_loads           | 14.0 us                                                     | 17.4 us: 1.24x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 3.37 us: 1.24x slower                                                       |
| tomli_loads          | 1.67 sec                                                    | 2.89 sec: 1.73x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 27.3 ms: 1.32x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 21.0 ms: 1.35x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.34x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 41.0 ms                                                     | 39.1 ms: 1.05x faster                                                       |
| django_template | 28.9 ms                                                     | 27.5 ms: 1.05x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 19.3 ms: 1.02x faster                                                       |
| mako            | 9.03 ms                                                     | 9.96 ms: 1.10x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io            | 1.11 sec                                                    | 378 ms: 2.93x faster                                                        |
| typing_runtime_protocols | 336 us                                                      | 133 us: 2.52x faster                                                        |
| async_tree_none          | 435 ms                                                      | 181 ms: 2.40x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.1 ms: 2.36x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 228 ms: 2.31x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 339 ms: 1.88x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.51 ms: 1.67x faster                                                       |
| pylint                   | 350 ms                                                      | 216 ms: 1.62x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.14 sec: 1.57x faster                                                      |
| generators               | 32.4 ms                                                     | 21.2 ms: 1.53x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 64.3 ns: 1.47x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.33 us: 1.44x faster                                                       |
| go                       | 139 ms                                                      | 100 ms: 1.38x faster                                                        |
| asyncio_tcp              | 732 ms                                                      | 555 ms: 1.32x faster                                                        |
| richards_super           | 52.2 ms                                                     | 40.3 ms: 1.30x faster                                                       |
| float                    | 61.7 ms                                                     | 48.1 ms: 1.28x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 67.1 ms: 1.28x faster                                                       |
| pycparser                | 930 ms                                                      | 728 ms: 1.28x faster                                                        |
| chaos                    | 61.7 ms                                                     | 48.4 ms: 1.27x faster                                                       |
| raytrace                 | 273 ms                                                      | 217 ms: 1.26x faster                                                        |
| richards                 | 42.4 ms                                                     | 34.2 ms: 1.24x faster                                                       |
| pyflate                  | 409 ms                                                      | 333 ms: 1.23x faster                                                        |
| gc_traversal             | 1.41 ms                                                     | 1.15 ms: 1.23x faster                                                       |
| regex_dna                | 136 ms                                                      | 111 ms: 1.22x faster                                                        |
| deepcopy                 | 255 us                                                      | 211 us: 1.21x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 23.8 us: 1.21x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.2 ms: 1.21x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 7.62 ms: 1.20x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 42.5 ms: 1.20x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.81 ms: 1.20x faster                                                       |
| comprehensions           | 16.5 us                                                     | 13.8 us: 1.19x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.3 ms: 1.19x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.1 ms: 1.18x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.45 ms: 1.15x faster                                                       |
| scimark_sor              | 106 ms                                                      | 93.2 ms: 1.14x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 238 us: 1.13x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 165 us: 1.11x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 70.2 ms: 1.10x faster                                                       |
| regex_compile            | 106 ms                                                      | 97.2 ms: 1.09x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 59.6 ms: 1.09x faster                                                       |
| pidigits                 | 149 ms                                                      | 138 ms: 1.08x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 90.1 ms: 1.07x faster                                                       |
| sympy_sum                | 107 ms                                                      | 101 ms: 1.06x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 59.3 ms: 1.05x faster                                                       |
| thrift                   | 617 us                                                      | 586 us: 1.05x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 39.1 ms: 1.05x faster                                                       |
| django_template          | 28.9 ms                                                     | 27.5 ms: 1.05x faster                                                       |
| 2to3                     | 246 ms                                                      | 235 ms: 1.05x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 55.6 ms: 1.03x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 14.9 ms: 1.03x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 19.3 ms: 1.02x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 604 ms: 1.02x slower                                                        |
| xml_etree_process        | 44.5 ms                                                     | 45.9 ms: 1.03x slower                                                       |
| json                     | 3.14 ms                                                     | 3.31 ms: 1.06x slower                                                       |
| sympy_expand             | 314 ms                                                      | 333 ms: 1.06x slower                                                        |
| unpickle                 | 9.09 us                                                     | 9.86 us: 1.09x slower                                                       |
| logging_format           | 6.76 us                                                     | 7.41 us: 1.10x slower                                                       |
| mako                     | 9.03 ms                                                     | 9.96 ms: 1.10x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.89 us: 1.11x slower                                                       |
| async_generators         | 222 ms                                                      | 250 ms: 1.13x slower                                                        |
| nqueens                  | 66.6 ms                                                     | 75.3 ms: 1.13x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 45.4 ns: 1.14x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 63.6 ms: 1.15x slower                                                       |
| scimark_fft              | 187 ms                                                      | 217 ms: 1.16x slower                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 3.17 ms: 1.17x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 89.4 ms: 1.18x slower                                                       |
| bench_thread_pool        | 958 us                                                      | 1.13 ms: 1.18x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 20.4 us: 1.19x slower                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.52 sec: 1.19x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 967 us: 1.21x slower                                                        |
| pickle_list              | 2.75 us                                                     | 3.33 us: 1.21x slower                                                       |
| pickle                   | 6.85 us                                                     | 8.39 us: 1.22x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 76.9 ms: 1.24x slower                                                       |
| json_loads               | 14.0 us                                                     | 17.4 us: 1.24x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 3.37 us: 1.24x slower                                                       |
| fannkuch                 | 256 ms                                                      | 328 ms: 1.28x slower                                                        |
| nbody                    | 71.3 ms                                                     | 92.0 ms: 1.29x slower                                                       |
| python_startup           | 20.6 ms                                                     | 27.3 ms: 1.32x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 21.0 ms: 1.35x slower                                                       |
| telco                    | 3.94 ms                                                     | 5.60 ms: 1.42x slower                                                       |
| docutils                 | 1.92 sec                                                    | 2.99 sec: 1.56x slower                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.98 sec: 1.62x slower                                                      |
| coverage                 | 39.0 ms                                                     | 67.2 ms: 1.72x slower                                                       |
| tomli_loads              | 1.67 sec                                                    | 2.89 sec: 1.73x slower                                                      |
| Geometric mean           | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (2): deepcopy_reduce, sympy_str
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-425f60b-NOGIL/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.117x faster

# HPT report

- Reliability score: 99.24% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown