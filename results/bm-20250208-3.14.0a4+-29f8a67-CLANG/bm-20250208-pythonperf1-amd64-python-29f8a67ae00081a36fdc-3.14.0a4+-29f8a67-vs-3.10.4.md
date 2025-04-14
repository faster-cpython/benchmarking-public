# Results vs. 3.10.4

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: windows-amd64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.207x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 232 ms: 1.06x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.74 sec: 1.11x faster                                                      |
| html5lib       | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 400 ms: 2.77x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 213 ms: 2.47x faster                                                        |
| async_tree_none         | 435 ms                                                      | 179 ms: 2.42x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 358 ms: 1.78x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.2 ms: 1.39x faster                                                       |
| nbody          | 71.3 ms                                                     | 60.5 ms: 1.18x faster                                                       |
| pidigits       | 149 ms                                                      | 155 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 83.6 ms: 1.27x faster                                                       |
| regex_dna      | 136 ms                                                      | 130 ms: 1.05x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 16.7 ms: 1.08x slower                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.94 ms: 1.17x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 270 us                                                      | 211 us: 1.28x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.32 sec: 1.26x faster                                                      |
| unpickle_pure_python | 183 us                                                      | 146 us: 1.26x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 7.62 ms: 1.20x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 44.8 ms: 1.01x slower                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 102 ms: 1.05x slower                                                        |
| xml_etree_iterparse  | 65.0 ms                                                     | 69.4 ms: 1.07x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 64.3 ms: 1.16x slower                                                       |
| json_loads           | 14.0 us                                                     | 19.3 us: 1.38x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 20.4 ms: 1.31x slower                                                       |
| python_startup         | 20.6 ms                                                     | 27.4 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 14.5 ms: 1.36x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 31.7 ms: 1.29x faster                                                       |
| mako            | 9.03 ms                                                     | 7.56 ms: 1.20x faster                                                       |
| django_template | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.26x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 109 us: 3.08x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 400 ms: 2.77x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 213 ms: 2.47x faster                                                        |
| async_tree_none          | 435 ms                                                      | 179 ms: 2.42x faster                                                        |
| deltablue                | 4.19 ms                                                     | 1.93 ms: 2.17x faster                                                       |
| generators               | 32.4 ms                                                     | 17.0 ms: 1.90x faster                                                       |
| go                       | 139 ms                                                      | 73.8 ms: 1.88x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 358 ms: 1.78x faster                                                        |
| pylint                   | 350 ms                                                      | 203 ms: 1.72x faster                                                        |
| richards_super           | 52.2 ms                                                     | 33.0 ms: 1.58x faster                                                       |
| raytrace                 | 273 ms                                                      | 173 ms: 1.58x faster                                                        |
| chaos                    | 61.7 ms                                                     | 39.4 ms: 1.57x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 18.9 us: 1.52x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 62.9 ns: 1.50x faster                                                       |
| deepcopy                 | 255 us                                                      | 172 us: 1.49x faster                                                        |
| richards                 | 42.4 ms                                                     | 28.8 ms: 1.47x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 831 us: 1.46x faster                                                        |
| scimark_sor              | 106 ms                                                      | 74.0 ms: 1.43x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.5 us: 1.43x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.04 ms: 1.42x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.5 ms: 1.41x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.07 ms: 1.41x faster                                                       |
| pyflate                  | 409 ms                                                      | 293 ms: 1.40x faster                                                        |
| float                    | 61.7 ms                                                     | 44.2 ms: 1.39x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 14.5 ms: 1.36x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                       |
| pycparser                | 930 ms                                                      | 711 ms: 1.31x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 59.7 ms: 1.29x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 31.7 ms: 1.29x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 211 us: 1.28x faster                                                        |
| regex_compile            | 106 ms                                                      | 83.6 ms: 1.27x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 67.7 ms: 1.27x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.32 sec: 1.26x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 146 us: 1.26x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 62.1 ms: 1.22x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 51.6 ms: 1.21x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.0 ms: 1.20x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 7.62 ms: 1.20x faster                                                       |
| mako                     | 9.03 ms                                                     | 7.56 ms: 1.20x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.62 us: 1.18x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.6 ms: 1.18x faster                                                       |
| nbody                    | 71.3 ms                                                     | 60.5 ms: 1.18x faster                                                       |
| sympy_sum                | 107 ms                                                      | 91.5 ms: 1.17x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.89 us: 1.17x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.05 sec: 1.16x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 517 ms: 1.14x faster                                                        |
| thrift                   | 617 us                                                      | 543 us: 1.14x faster                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 35.4 ms: 1.12x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.74 sec: 1.11x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 874 us: 1.10x faster                                                        |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 188 ms: 1.09x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 62.1 ms: 1.07x faster                                                       |
| 2to3                     | 246 ms                                                      | 232 ms: 1.06x faster                                                        |
| regex_dna                | 136 ms                                                      | 130 ms: 1.05x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 72.5 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.60 ms: 1.05x faster                                                       |
| sympy_expand             | 314 ms                                                      | 302 ms: 1.04x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.72 sec: 1.04x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.67 us: 1.01x faster                                                       |
| scimark_fft              | 187 ms                                                      | 189 ms: 1.01x slower                                                        |
| xml_etree_process        | 44.5 ms                                                     | 44.8 ms: 1.01x slower                                                       |
| async_generators         | 222 ms                                                      | 229 ms: 1.03x slower                                                        |
| pidigits                 | 149 ms                                                      | 155 ms: 1.04x slower                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 102 ms: 1.05x slower                                                        |
| fannkuch                 | 256 ms                                                      | 273 ms: 1.07x slower                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 69.4 ms: 1.07x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 16.7 ms: 1.08x slower                                                       |
| json                     | 3.14 ms                                                     | 3.58 ms: 1.14x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 64.3 ms: 1.16x slower                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.94 ms: 1.17x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.4 ms: 1.31x slower                                                       |
| telco                    | 3.94 ms                                                     | 5.22 ms: 1.32x slower                                                       |
| python_startup           | 20.6 ms                                                     | 27.4 ms: 1.33x slower                                                       |
| json_loads               | 14.0 us                                                     | 19.3 us: 1.38x slower                                                       |
| coverage                 | 39.0 ms                                                     | 54.1 ms: 1.39x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 95.8 ms: 1.54x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.36 ms: 1.70x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.82 ms: 2.00x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (1): logging_simple
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-pythonperf1-amd64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.207x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown