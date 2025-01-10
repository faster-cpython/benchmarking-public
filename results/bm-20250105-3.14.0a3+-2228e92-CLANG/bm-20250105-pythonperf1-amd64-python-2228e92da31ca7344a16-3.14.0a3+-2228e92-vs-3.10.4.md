# Results vs. 3.10.4

- fork: python
- ref: 2228e92da31ca7344a16
- machine: windows-amd64
- commit hash: 2228e92
- commit date: 2025-01-05
- overall geometric mean: 1.138x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 239 ms: 1.03x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.79 sec: 1.07x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.8 ms: 1.28x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 401 ms: 2.76x faster                                                        |
| async_tree_none         | 435 ms                                                      | 177 ms: 2.45x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 218 ms: 2.42x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 373 ms: 1.71x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 55.1 ms: 1.12x faster                                                       |
| nbody          | 71.3 ms                                                     | 68.8 ms: 1.04x faster                                                       |
| pidigits       | 149 ms                                                      | 155 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 91.0 ms: 1.17x faster                                                       |
| regex_dna      | 136 ms                                                      | 142 ms: 1.04x slower                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.98 ms: 1.19x slower                                                       |
| regex_v8       | 15.4 ms                                                     | 26.6 ms: 1.73x slower                                                       |
| Geometric mean | (ref)                                                       | 1.16x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.67 sec                                                    | 1.40 sec: 1.19x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 228 us: 1.18x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 7.79 ms: 1.18x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 159 us: 1.15x faster                                                        |
| xml_etree_parse      | 96.8 ms                                                     | 102 ms: 1.05x slower                                                        |
| xml_etree_process    | 44.5 ms                                                     | 47.3 ms: 1.06x slower                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 71.0 ms: 1.09x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 67.6 ms: 1.22x slower                                                       |
| json_loads           | 14.0 us                                                     | 19.6 us: 1.40x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.0 ms: 1.22x slower                                                       |
| python_startup         | 20.6 ms                                                     | 25.6 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.23x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 16.2 ms: 1.22x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 34.1 ms: 1.20x faster                                                       |
| django_template | 28.9 ms                                                     | 25.7 ms: 1.12x faster                                                       |
| mako            | 9.03 ms                                                     | 8.55 ms: 1.06x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 115 us: 2.91x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 401 ms: 2.76x faster                                                        |
| async_tree_none          | 435 ms                                                      | 177 ms: 2.45x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 218 ms: 2.42x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.15 ms: 1.95x faster                                                       |
| generators               | 32.4 ms                                                     | 17.3 ms: 1.88x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 373 ms: 1.71x faster                                                        |
| pylint                   | 350 ms                                                      | 206 ms: 1.70x faster                                                        |
| go                       | 139 ms                                                      | 82.7 ms: 1.68x faster                                                       |
| raytrace                 | 273 ms                                                      | 182 ms: 1.50x faster                                                        |
| richards_super           | 52.2 ms                                                     | 35.3 ms: 1.48x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 871 us: 1.39x faster                                                        |
| deepcopy                 | 255 us                                                      | 185 us: 1.38x faster                                                        |
| chaos                    | 61.7 ms                                                     | 45.2 ms: 1.36x faster                                                       |
| richards                 | 42.4 ms                                                     | 31.1 ms: 1.36x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 70.2 ns: 1.35x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.10 ms: 1.34x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.7 us: 1.32x faster                                                       |
| scimark_sor              | 106 ms                                                      | 82.5 ms: 1.29x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.9 us: 1.28x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.8 ms: 1.28x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 45.7 ms: 1.25x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.59 ms: 1.25x faster                                                       |
| pycparser                | 930 ms                                                      | 753 ms: 1.24x faster                                                        |
| pyflate                  | 409 ms                                                      | 332 ms: 1.23x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 16.2 ms: 1.22x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 34.1 ms: 1.20x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.40 sec: 1.19x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 42.3 ms: 1.19x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 72.3 ms: 1.19x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 228 us: 1.18x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 7.79 ms: 1.18x faster                                                       |
| regex_compile            | 106 ms                                                      | 91.0 ms: 1.17x faster                                                       |
| sympy_sum                | 107 ms                                                      | 92.0 ms: 1.16x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 159 us: 1.15x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.95 us: 1.13x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.7 ms: 1.12x faster                                                       |
| float                    | 61.7 ms                                                     | 55.1 ms: 1.12x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.7 ms: 1.11x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.72 us: 1.11x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                                      |
| coroutines               | 16.0 ms                                                     | 14.6 ms: 1.09x faster                                                       |
| thrift                   | 617 us                                                      | 565 us: 1.09x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 878 us: 1.09x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 57.7 ms: 1.08x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 549 ms: 1.08x faster                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 37.0 ms: 1.07x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.79 sec: 1.07x faster                                                      |
| sympy_str                | 194 ms                                                      | 182 ms: 1.07x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.68 sec: 1.06x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 73.1 ms: 1.06x faster                                                       |
| mako                     | 9.03 ms                                                     | 8.55 ms: 1.06x faster                                                       |
| nbody                    | 71.3 ms                                                     | 68.8 ms: 1.04x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 64.8 ms: 1.03x faster                                                       |
| 2to3                     | 246 ms                                                      | 239 ms: 1.03x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 201 ms: 1.02x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 75.4 ms: 1.01x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.82 us: 1.01x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.76 ms: 1.01x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.41 us: 1.03x slower                                                       |
| scimark_fft              | 187 ms                                                      | 194 ms: 1.03x slower                                                        |
| regex_dna                | 136 ms                                                      | 142 ms: 1.04x slower                                                        |
| pidigits                 | 149 ms                                                      | 155 ms: 1.04x slower                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 102 ms: 1.05x slower                                                        |
| pathlib                  | 75.7 ms                                                     | 79.8 ms: 1.05x slower                                                       |
| xml_etree_process        | 44.5 ms                                                     | 47.3 ms: 1.06x slower                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 71.0 ms: 1.09x slower                                                       |
| fannkuch                 | 256 ms                                                      | 291 ms: 1.14x slower                                                        |
| async_generators         | 222 ms                                                      | 254 ms: 1.15x slower                                                        |
| json                     | 3.14 ms                                                     | 3.67 ms: 1.17x slower                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.98 ms: 1.19x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 67.6 ms: 1.22x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.0 ms: 1.22x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.6 ms: 1.24x slower                                                       |
| telco                    | 3.94 ms                                                     | 5.18 ms: 1.31x slower                                                       |
| coverage                 | 39.0 ms                                                     | 53.1 ms: 1.36x slower                                                       |
| json_loads               | 14.0 us                                                     | 19.6 us: 1.40x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 93.5 ms: 1.51x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.36 ms: 1.70x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 26.6 ms: 1.73x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.54 ms: 1.80x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (1): sympy_expand
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250105-3.14.0a3+-2228e92-CLANG/bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.138x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown