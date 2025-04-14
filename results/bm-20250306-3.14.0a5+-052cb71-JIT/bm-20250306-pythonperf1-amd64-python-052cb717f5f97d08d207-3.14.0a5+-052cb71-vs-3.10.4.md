# Results vs. 3.10.4

- fork: python
- ref: 052cb717f5f97d08d207
- machine: windows-amd64
- commit hash: 052cb71
- commit date: 2025-03-06
- overall geometric mean: 1.239x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.74 sec: 1.11x faster                                                      |
| html5lib       | 51.0 ms                                                     | 41.3 ms: 1.24x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 419 ms: 2.64x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 220 ms: 2.39x faster                                                        |
| async_tree_none         | 435 ms                                                      | 188 ms: 2.32x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 344 ms: 1.85x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.28x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 41.3 ms: 1.49x faster                                                       |
| nbody          | 71.3 ms                                                     | 59.7 ms: 1.19x faster                                                       |
| pidigits       | 149 ms                                                      | 153 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 85.2 ms: 1.24x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                       |
| regex_dna      | 136 ms                                                      | 126 ms: 1.08x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 15.3 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 116 us: 1.58x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.24 sec: 1.35x faster                                                      |
| json_dumps           | 9.16 ms                                                     | 6.88 ms: 1.33x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 219 us: 1.23x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 37.4 ms: 1.19x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 52.7 ms: 1.05x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 92.1 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.8 ms: 1.02x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.6 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 20.2 ms: 1.30x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.35 ms: 1.69x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                       |
| django_template | 28.9 ms                                                     | 25.9 ms: 1.11x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 37.5 ms: 1.10x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.24x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 110 us: 3.06x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 419 ms: 2.64x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 220 ms: 2.39x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.2 ms: 2.35x faster                                                       |
| async_tree_none          | 435 ms                                                      | 188 ms: 2.32x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 344 ms: 1.85x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.28 ms: 1.83x faster                                                       |
| pylint                   | 350 ms                                                      | 205 ms: 1.71x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.35 ms: 1.69x faster                                                       |
| generators               | 32.4 ms                                                     | 20.3 ms: 1.60x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 116 us: 1.58x faster                                                        |
| go                       | 139 ms                                                      | 91.5 ms: 1.52x faster                                                       |
| richards_super           | 52.2 ms                                                     | 34.7 ms: 1.50x faster                                                       |
| float                    | 61.7 ms                                                     | 41.3 ms: 1.49x faster                                                       |
| chaos                    | 61.7 ms                                                     | 42.2 ms: 1.46x faster                                                       |
| pyflate                  | 409 ms                                                      | 281 ms: 1.46x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 66.0 ns: 1.43x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.5 us: 1.43x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 20.1 us: 1.43x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 853 us: 1.42x faster                                                        |
| raytrace                 | 273 ms                                                      | 194 ms: 1.41x faster                                                        |
| richards                 | 42.4 ms                                                     | 30.6 ms: 1.38x faster                                                       |
| deepcopy                 | 255 us                                                      | 189 us: 1.35x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.24 sec: 1.35x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.10 ms: 1.34x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.88 ms: 1.33x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 65.0 ms: 1.32x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 48.1 ms: 1.30x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.46 ms: 1.29x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 45.6 ms: 1.25x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 974 ms: 1.25x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.18 ms: 1.25x faster                                                       |
| regex_compile            | 106 ms                                                      | 85.2 ms: 1.24x faster                                                       |
| pycparser                | 930 ms                                                      | 750 ms: 1.24x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 41.3 ms: 1.24x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.24x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 62.5 ms: 1.24x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 219 us: 1.23x faster                                                        |
| scimark_sor              | 106 ms                                                      | 87.4 ms: 1.21x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 488 ms: 1.21x faster                                                        |
| scimark_fft              | 187 ms                                                      | 156 ms: 1.20x faster                                                        |
| nbody                    | 71.3 ms                                                     | 59.7 ms: 1.19x faster                                                       |
| thrift                   | 617 us                                                      | 517 us: 1.19x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 37.4 ms: 1.19x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.3 ms: 1.18x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.16x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 43.7 ms: 1.16x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.13x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.58 sec: 1.13x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 858 us: 1.12x faster                                                        |
| django_template          | 28.9 ms                                                     | 25.9 ms: 1.11x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.99 us: 1.11x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.74 sec: 1.11x faster                                                      |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 37.5 ms: 1.10x faster                                                       |
| sympy_str                | 194 ms                                                      | 178 ms: 1.09x faster                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 36.9 ms: 1.08x faster                                                       |
| regex_dna                | 136 ms                                                      | 126 ms: 1.08x faster                                                        |
| json                     | 3.14 ms                                                     | 2.96 ms: 1.06x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 62.9 ms: 1.06x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 52.7 ms: 1.05x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 92.1 ms: 1.05x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 199 ms: 1.03x faster                                                        |
| fannkuch                 | 256 ms                                                      | 250 ms: 1.02x faster                                                        |
| sympy_expand             | 314 ms                                                      | 308 ms: 1.02x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.8 ms: 1.02x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 15.3 ms: 1.01x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 76.7 ms: 1.01x slower                                                       |
| pidigits                 | 149 ms                                                      | 153 ms: 1.03x slower                                                        |
| json_loads               | 14.0 us                                                     | 14.6 us: 1.04x slower                                                       |
| logging_format           | 6.76 us                                                     | 7.07 us: 1.05x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.62 us: 1.06x slower                                                       |
| async_generators         | 222 ms                                                      | 240 ms: 1.08x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.39 ms: 1.11x slower                                                       |
| coverage                 | 39.0 ms                                                     | 48.9 ms: 1.25x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.1 ms: 1.27x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.2 ms: 1.30x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 87.3 ms: 1.41x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.09 ms: 1.48x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.24 ms: 1.55x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                                |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250306-3.14.0a5+-052cb71-JIT/bm-20250306-pythonperf1-amd64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.239x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown