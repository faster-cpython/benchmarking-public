# Results vs. 3.10.4

- fork: python
- ref: f72977b2f4a29063ae30
- machine: windows-amd64
- commit hash: f72977b
- commit date: 2025-02-09
- overall geometric mean: 1.261x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 223 ms: 1.10x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.72 sec: 1.12x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.8 ms: 1.28x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 408 ms: 2.71x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 220 ms: 2.39x faster                                                        |
| async_tree_none         | 435 ms                                                      | 183 ms: 2.38x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 337 ms: 1.89x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.0 ms: 1.34x faster                                                       |
| nbody          | 71.3 ms                                                     | 59.4 ms: 1.20x faster                                                       |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.8 ms: 1.30x faster                                                       |
| regex_dna      | 136 ms                                                      | 113 ms: 1.21x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.42 ms: 1.16x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 113 us: 1.62x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.19 sec: 1.40x faster                                                      |
| json_dumps           | 9.16 ms                                                     | 6.57 ms: 1.40x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 208 us: 1.30x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 35.8 ms: 1.24x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 49.7 ms: 1.12x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 88.7 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.2 ms: 1.08x faster                                                       |
| json_loads           | 14.0 us                                                     | 15.2 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.22x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.3 ms: 1.23x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.25 ms: 1.72x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.9 ms: 1.24x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 35.3 ms: 1.16x faster                                                       |
| django_template | 28.9 ms                                                     | 25.3 ms: 1.14x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.30x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 110 us: 3.05x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 408 ms: 2.71x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 220 ms: 2.39x faster                                                        |
| async_tree_none          | 435 ms                                                      | 183 ms: 2.38x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 337 ms: 1.89x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.29 ms: 1.83x faster                                                       |
| pylint                   | 350 ms                                                      | 201 ms: 1.74x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.25 ms: 1.72x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 58.0 ns: 1.63x faster                                                       |
| generators               | 32.4 ms                                                     | 19.8 ms: 1.63x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 113 us: 1.62x faster                                                        |
| go                       | 139 ms                                                      | 85.9 ms: 1.62x faster                                                       |
| richards_super           | 52.2 ms                                                     | 32.7 ms: 1.60x faster                                                       |
| pyflate                  | 409 ms                                                      | 273 ms: 1.50x faster                                                        |
| richards                 | 42.4 ms                                                     | 28.5 ms: 1.49x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.4 ms: 1.49x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.1 us: 1.49x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 838 us: 1.45x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 20.2 us: 1.43x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 60.6 ms: 1.42x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.19 sec: 1.40x faster                                                      |
| raytrace                 | 273 ms                                                      | 196 ms: 1.40x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.57 ms: 1.40x faster                                                       |
| deepcopy                 | 255 us                                                      | 184 us: 1.39x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.06 ms: 1.39x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 45.6 ms: 1.37x faster                                                       |
| float                    | 61.7 ms                                                     | 46.0 ms: 1.34x faster                                                       |
| pycparser                | 930 ms                                                      | 703 ms: 1.32x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 58.4 ms: 1.32x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.38 ms: 1.31x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 43.9 ms: 1.31x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 58.1 ms: 1.30x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 208 us: 1.30x faster                                                        |
| regex_compile            | 106 ms                                                      | 81.8 ms: 1.30x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.10 ms: 1.30x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.8 ms: 1.28x faster                                                       |
| scimark_fft              | 187 ms                                                      | 147 ms: 1.28x faster                                                        |
| scimark_sor              | 106 ms                                                      | 83.6 ms: 1.27x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.53 us: 1.25x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.9 ms: 1.24x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.8 ms: 1.24x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 987 ms: 1.24x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.1 ms: 1.22x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 41.5 ms: 1.22x faster                                                       |
| regex_dna                | 136 ms                                                      | 113 ms: 1.21x faster                                                        |
| thrift                   | 617 us                                                      | 513 us: 1.20x faster                                                        |
| nbody                    | 71.3 ms                                                     | 59.4 ms: 1.20x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.5 ms: 1.20x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 505 ms: 1.17x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 35.3 ms: 1.16x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.42 ms: 1.16x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.3 ms: 1.14x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 841 us: 1.14x faster                                                        |
| fannkuch                 | 256 ms                                                      | 228 ms: 1.12x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.97 us: 1.12x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.59 sec: 1.12x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 49.7 ms: 1.12x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.72 sec: 1.12x faster                                                      |
| sympy_str                | 194 ms                                                      | 175 ms: 1.11x faster                                                        |
| 2to3                     | 246 ms                                                      | 223 ms: 1.10x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 88.7 ms: 1.09x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 61.1 ms: 1.09x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.2 ms: 1.08x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 37.0 ms: 1.08x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                       |
| sympy_expand             | 314 ms                                                      | 304 ms: 1.03x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 200 ms: 1.03x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 74.9 ms: 1.01x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.68 us: 1.01x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.27 us: 1.01x slower                                                       |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                        |
| async_generators         | 222 ms                                                      | 238 ms: 1.08x slower                                                        |
| json_loads               | 14.0 us                                                     | 15.2 us: 1.09x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.49 ms: 1.14x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.4 ms: 1.21x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.3 ms: 1.23x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.97 ms: 1.40x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 87.7 ms: 1.41x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.52x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.25x faster                                                                |

Benchmark hidden because not significant (1): json
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250209-3.14.0a4+-f72977b-JIT/bm-20250209-pythonperf1-amd64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.261x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown