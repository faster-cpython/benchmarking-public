# Results vs. 3.10.4

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: windows-amd64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.248x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.73 sec: 1.11x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 406 ms: 2.73x faster                                                        |
| async_tree_none         | 435 ms                                                      | 183 ms: 2.38x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 224 ms: 2.34x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 353 ms: 1.81x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.29x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 54.3 ms: 1.31x faster                                                       |
| float          | 61.7 ms                                                     | 47.3 ms: 1.31x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.0 ms: 1.33x faster                                                       |
| regex_dna      | 136 ms                                                      | 115 ms: 1.18x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.44 ms: 1.15x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 18.4 ms: 1.19x slower                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 110 us: 1.67x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 6.29 ms: 1.46x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.18 sec: 1.41x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 205 us: 1.31x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 35.9 ms: 1.24x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 87.3 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 58.8 ms: 1.10x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 50.3 ms: 1.10x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.25x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                       |
| python_startup         | 20.6 ms                                                     | 23.4 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.11 ms: 1.77x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 18.3 ms: 1.08x faster                                                       |
| django_template | 28.9 ms                                                     | 26.8 ms: 1.08x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 47.5 ms: 1.16x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 2.99x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 406 ms: 2.73x faster                                                        |
| async_tree_none          | 435 ms                                                      | 183 ms: 2.38x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 224 ms: 2.34x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.25 ms: 1.86x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 353 ms: 1.81x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.11 ms: 1.77x faster                                                       |
| scimark_sor              | 106 ms                                                      | 61.5 ms: 1.73x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.9 us: 1.70x faster                                                       |
| pylint                   | 350 ms                                                      | 208 ms: 1.68x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 110 us: 1.67x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 57.5 ns: 1.65x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 48.6 ms: 1.59x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 54.5 ms: 1.58x faster                                                       |
| go                       | 139 ms                                                      | 88.8 ms: 1.56x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 36.7 ms: 1.56x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 41.1 ms: 1.52x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.4 ms: 1.49x faster                                                       |
| pyflate                  | 409 ms                                                      | 279 ms: 1.47x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.29 ms: 1.46x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 844 us: 1.44x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.18 sec: 1.41x faster                                                      |
| comprehensions           | 16.5 us                                                     | 11.9 us: 1.39x faster                                                       |
| richards_super           | 52.2 ms                                                     | 37.7 ms: 1.38x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.09 ms: 1.35x faster                                                       |
| deepcopy                 | 255 us                                                      | 190 us: 1.34x faster                                                        |
| generators               | 32.4 ms                                                     | 24.2 ms: 1.34x faster                                                       |
| regex_compile            | 106 ms                                                      | 80.0 ms: 1.33x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 205 us: 1.31x faster                                                        |
| nbody                    | 71.3 ms                                                     | 54.3 ms: 1.31x faster                                                       |
| float                    | 61.7 ms                                                     | 47.3 ms: 1.31x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.12 ms: 1.28x faster                                                       |
| raytrace                 | 273 ms                                                      | 213 ms: 1.28x faster                                                        |
| scimark_fft              | 187 ms                                                      | 147 ms: 1.27x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 40.1 ms: 1.27x faster                                                       |
| pycparser                | 930 ms                                                      | 735 ms: 1.27x faster                                                        |
| richards                 | 42.4 ms                                                     | 33.6 ms: 1.26x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.5 ms: 1.25x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.9 ms: 1.24x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 985 ms: 1.24x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.58 us: 1.21x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 495 ms: 1.20x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.85 us: 1.19x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.18x faster                                                       |
| regex_dna                | 136 ms                                                      | 115 ms: 1.18x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 816 us: 1.17x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.52 sec: 1.17x faster                                                      |
| sympy_sum                | 107 ms                                                      | 91.7 ms: 1.17x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.44 ms: 1.15x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 5.01 ms: 1.15x faster                                                       |
| thrift                   | 617 us                                                      | 544 us: 1.14x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                       |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.73 sec: 1.11x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 87.3 ms: 1.11x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 58.8 ms: 1.10x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 50.3 ms: 1.10x faster                                                       |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 18.3 ms: 1.08x faster                                                       |
| django_template          | 28.9 ms                                                     | 26.8 ms: 1.08x faster                                                       |
| json                     | 3.14 ms                                                     | 2.91 ms: 1.08x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 37.8 ms: 1.05x faster                                                       |
| fannkuch                 | 256 ms                                                      | 243 ms: 1.05x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 63.3 ms: 1.05x faster                                                       |
| sympy_expand             | 314 ms                                                      | 305 ms: 1.03x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 74.3 ms: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.71 us: 1.01x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.26 us: 1.01x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.03x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.30 ms: 1.09x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.4 ms: 1.12x slower                                                       |
| async_generators         | 222 ms                                                      | 251 ms: 1.13x slower                                                        |
| python_startup           | 20.6 ms                                                     | 23.4 ms: 1.13x slower                                                       |
| mypy2                    | 555 ms                                                      | 635 ms: 1.14x slower                                                        |
| genshi_xml               | 41.0 ms                                                     | 47.5 ms: 1.16x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 18.4 ms: 1.19x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.6 ms: 1.19x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 82.6 ms: 1.33x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.98 ms: 1.40x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.52x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                                |

Benchmark hidden because not significant (2): sqlglot_normalize, pathlib
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-pythonperf1-amd64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.248x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown