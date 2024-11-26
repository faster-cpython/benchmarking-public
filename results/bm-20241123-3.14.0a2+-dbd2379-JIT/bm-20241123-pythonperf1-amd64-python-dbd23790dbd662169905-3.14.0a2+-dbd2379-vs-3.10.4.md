# Results vs. 3.10.4

- fork: python
- ref: dbd23790dbd662169905
- machine: windows-amd64
- commit hash: dbd2379
- commit date: 2024-11-23
- overall geometric mean: 1.233x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 225 ms: 1.09x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.79 sec: 1.07x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 435 ms                                                      | 209 ms: 2.09x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 279 ms: 1.89x faster                                                        |
| async_tree_io           | 1.11 sec                                                    | 588 ms: 1.88x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 401 ms: 1.59x faster                                                        |
| Geometric mean          | (ref)                                                       | 1.85x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 52.4 ms: 1.36x faster                                                       |
| float          | 61.7 ms                                                     | 47.2 ms: 1.31x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.22x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 85.1 ms: 1.25x faster                                                       |
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.49 ms: 1.11x faster                                                       |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 108 us: 1.70x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.26 sec: 1.33x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 211 us: 1.28x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 35.8 ms: 1.24x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 50.7 ms: 1.10x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 93.7 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.22x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.1 ms: 1.11x slower                                                       |
| python_startup         | 20.6 ms                                                     | 23.2 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.12x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.15 ms: 1.76x faster                                                       |
| django_template | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 18.4 ms: 1.08x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 44.3 ms: 1.08x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 3.01x faster                                                        |
| async_tree_none          | 435 ms                                                      | 209 ms: 2.09x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 279 ms: 1.89x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 588 ms: 1.88x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 15.8 us: 1.83x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.34 ms: 1.79x faster                                                       |
| mako                     | 9.03 ms                                                     | 5.15 ms: 1.76x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 108 us: 1.70x faster                                                        |
| pylint                   | 350 ms                                                      | 207 ms: 1.70x faster                                                        |
| scimark_sor              | 106 ms                                                      | 64.1 ms: 1.66x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 57.5 ns: 1.65x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 401 ms: 1.59x faster                                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 36.4 ms: 1.57x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 55.2 ms: 1.56x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 40.4 ms: 1.55x faster                                                       |
| chaos                    | 61.7 ms                                                     | 40.5 ms: 1.52x faster                                                       |
| go                       | 139 ms                                                      | 91.7 ms: 1.52x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                                       |
| generators               | 32.4 ms                                                     | 22.2 ms: 1.46x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 53.3 ms: 1.45x faster                                                       |
| pyflate                  | 409 ms                                                      | 284 ms: 1.44x faster                                                        |
| richards_super           | 52.2 ms                                                     | 37.3 ms: 1.40x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.8 us: 1.40x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 878 us: 1.38x faster                                                        |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                        |
| nbody                    | 71.3 ms                                                     | 52.4 ms: 1.36x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.26 sec: 1.33x faster                                                      |
| pycparser                | 930 ms                                                      | 705 ms: 1.32x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 39.0 ms: 1.31x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.13 ms: 1.31x faster                                                       |
| float                    | 61.7 ms                                                     | 47.2 ms: 1.31x faster                                                       |
| raytrace                 | 273 ms                                                      | 209 ms: 1.31x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 211 us: 1.28x faster                                                        |
| richards                 | 42.4 ms                                                     | 33.3 ms: 1.27x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 970 ms: 1.26x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 473 ms: 1.25x faster                                                        |
| regex_compile            | 106 ms                                                      | 85.1 ms: 1.25x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.8 ms: 1.24x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.7 ms: 1.24x faster                                                       |
| scimark_fft              | 187 ms                                                      | 153 ms: 1.23x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.24 ms: 1.22x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 806 us: 1.19x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.50 sec: 1.18x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.17x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.88 us: 1.17x faster                                                       |
| thrift                   | 617 us                                                      | 530 us: 1.17x faster                                                        |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.66 us: 1.15x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.99 ms: 1.15x faster                                                       |
| sympy_sum                | 107 ms                                                      | 93.7 ms: 1.14x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.49 ms: 1.11x faster                                                       |
| django_template          | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.9 ms: 1.10x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 50.7 ms: 1.10x faster                                                       |
| 2to3                     | 246 ms                                                      | 225 ms: 1.09x faster                                                        |
| sympy_str                | 194 ms                                                      | 179 ms: 1.09x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 18.4 ms: 1.08x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.79 sec: 1.07x faster                                                      |
| json                     | 3.14 ms                                                     | 2.97 ms: 1.05x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 63.4 ms: 1.05x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 37.9 ms: 1.05x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 72.4 ms: 1.05x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.53 us: 1.04x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 93.7 ms: 1.03x faster                                                       |
| sympy_expand             | 314 ms                                                      | 307 ms: 1.02x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.10 us: 1.02x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 205 ms: 1.00x faster                                                        |
| fannkuch                 | 256 ms                                                      | 258 ms: 1.01x slower                                                        |
| pathlib                  | 75.7 ms                                                     | 76.5 ms: 1.01x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.02x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 44.3 ms: 1.08x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.33 ms: 1.10x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.1 ms: 1.11x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.2 ms: 1.13x slower                                                       |
| async_generators         | 222 ms                                                      | 264 ms: 1.19x slower                                                        |
| coverage                 | 39.0 ms                                                     | 47.0 ms: 1.21x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.85 ms: 1.31x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 82.2 ms: 1.32x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.31 ms: 1.64x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                                |

Benchmark hidden because not significant (1): regex_v8
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241123-3.14.0a2+-dbd2379-JIT/bm-20241123-pythonperf1-amd64-python-dbd23790dbd662169905-3.14.0a2+-dbd2379.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.233x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown