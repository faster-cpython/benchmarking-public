# Results vs. 3.10.4

- fork: JelleZijlstra
- ref: sunder_io
- machine: windows-amd64
- commit hash: dac50cc
- commit date: 2025-04-25
- overall geometric mean: 1.277x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                    |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                  |
| html5lib       | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                   |
| Geometric mean | (ref)                                                       | 1.19x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 413 ms: 2.68x faster                                                    |
| async_tree_memoization  | 526 ms                                                      | 207 ms: 2.54x faster                                                    |
| async_tree_none         | 435 ms                                                      | 183 ms: 2.38x faster                                                    |
| async_tree_cpu_io_mixed | 638 ms                                                      | 330 ms: 1.93x faster                                                    |
| Geometric mean          | (ref)                                                       | 2.37x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 42.8 ms: 1.44x faster                                                   |
| nbody          | 71.3 ms                                                     | 63.0 ms: 1.13x faster                                                   |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                       | 1.18x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.5 ms: 1.30x faster                                                   |
| regex_dna      | 136 ms                                                      | 117 ms: 1.17x faster                                                    |
| regex_effbot   | 1.66 ms                                                     | 1.43 ms: 1.16x faster                                                   |
| regex_v8       | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                   |
| Geometric mean | (ref)                                                       | 1.18x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 135 us: 1.35x faster                                                    |
| json_dumps           | 9.16 ms                                                     | 6.90 ms: 1.33x faster                                                   |
| pickle_pure_python   | 270 us                                                      | 210 us: 1.28x faster                                                    |
| tomli_loads          | 1.67 sec                                                    | 1.42 sec: 1.18x faster                                                  |
| xml_etree_process    | 44.5 ms                                                     | 40.0 ms: 1.11x faster                                                   |
| xml_etree_parse      | 96.8 ms                                                     | 88.9 ms: 1.09x faster                                                   |
| xml_etree_iterparse  | 65.0 ms                                                     | 64.3 ms: 1.01x faster                                                   |
| json_loads           | 14.0 us                                                     | 15.4 us: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                            |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                   |
| python_startup         | 20.6 ms                                                     | 26.6 ms: 1.29x slower                                                   |
| Geometric mean         | (ref)                                                       | 1.27x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.68 ms: 1.35x faster                                                   |
| genshi_text     | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                   |
| django_template | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                   |
| genshi_xml      | 41.0 ms                                                     | 34.4 ms: 1.19x faster                                                   |
| Geometric mean  | (ref)                                                       | 1.25x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 107 us: 3.14x faster                                                    |
| async_tree_io            | 1.11 sec                                                    | 413 ms: 2.68x faster                                                    |
| async_tree_memoization   | 526 ms                                                      | 207 ms: 2.54x faster                                                    |
| async_tree_none          | 435 ms                                                      | 183 ms: 2.38x faster                                                    |
| pathlib                  | 75.7 ms                                                     | 32.5 ms: 2.33x faster                                                   |
| mdp                      | 1.78 sec                                                    | 789 ms: 2.26x faster                                                    |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 330 ms: 1.93x faster                                                    |
| deltablue                | 4.19 ms                                                     | 2.19 ms: 1.91x faster                                                   |
| go                       | 139 ms                                                      | 79.0 ms: 1.76x faster                                                   |
| pylint                   | 350 ms                                                      | 200 ms: 1.75x faster                                                    |
| logging_silent           | 94.6 ns                                                     | 55.1 ns: 1.72x faster                                                   |
| generators               | 32.4 ms                                                     | 19.1 ms: 1.69x faster                                                   |
| richards_super           | 52.2 ms                                                     | 31.5 ms: 1.66x faster                                                   |
| chaos                    | 61.7 ms                                                     | 38.6 ms: 1.60x faster                                                   |
| raytrace                 | 273 ms                                                      | 175 ms: 1.56x faster                                                    |
| deepcopy_memo            | 28.8 us                                                     | 18.6 us: 1.55x faster                                                   |
| richards                 | 42.4 ms                                                     | 27.7 ms: 1.53x faster                                                   |
| comprehensions           | 16.5 us                                                     | 11.2 us: 1.47x faster                                                   |
| deepcopy                 | 255 us                                                      | 175 us: 1.46x faster                                                    |
| scimark_lu               | 85.8 ms                                                     | 59.1 ms: 1.45x faster                                                   |
| float                    | 61.7 ms                                                     | 42.8 ms: 1.44x faster                                                   |
| pyflate                  | 409 ms                                                      | 285 ms: 1.43x faster                                                    |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.3 ms: 1.42x faster                                                   |
| hexiom                   | 5.74 ms                                                     | 4.13 ms: 1.39x faster                                                   |
| scimark_sor              | 106 ms                                                      | 78.1 ms: 1.36x faster                                                   |
| unpickle_pure_python     | 183 us                                                      | 135 us: 1.35x faster                                                    |
| mako                     | 9.03 ms                                                     | 6.68 ms: 1.35x faster                                                   |
| spectral_norm            | 77.3 ms                                                     | 57.8 ms: 1.34x faster                                                   |
| json_dumps               | 9.16 ms                                                     | 6.90 ms: 1.33x faster                                                   |
| html5lib                 | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                   |
| crypto_pyaes             | 62.5 ms                                                     | 47.7 ms: 1.31x faster                                                   |
| pycparser                | 930 ms                                                      | 714 ms: 1.30x faster                                                    |
| regex_compile            | 106 ms                                                      | 81.5 ms: 1.30x faster                                                   |
| pickle_pure_python       | 270 us                                                      | 210 us: 1.28x faster                                                    |
| genshi_text              | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                   |
| deepcopy_reduce          | 2.20 us                                                     | 1.80 us: 1.22x faster                                                   |
| sympy_integrate          | 15.3 ms                                                     | 12.6 ms: 1.21x faster                                                   |
| sympy_sum                | 107 ms                                                      | 88.3 ms: 1.21x faster                                                   |
| pprint_pformat           | 1.22 sec                                                    | 1.01 sec: 1.21x faster                                                  |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                   |
| django_template          | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                   |
| genshi_xml               | 41.0 ms                                                     | 34.4 ms: 1.19x faster                                                   |
| pprint_safe_repr         | 592 ms                                                      | 499 ms: 1.19x faster                                                    |
| dulwich_log              | 50.5 ms                                                     | 42.6 ms: 1.18x faster                                                   |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.18x faster                                                   |
| tomli_loads              | 1.67 sec                                                    | 1.42 sec: 1.18x faster                                                  |
| regex_dna                | 136 ms                                                      | 117 ms: 1.17x faster                                                    |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                  |
| regex_effbot             | 1.66 ms                                                     | 1.43 ms: 1.16x faster                                                   |
| sympy_str                | 194 ms                                                      | 172 ms: 1.13x faster                                                    |
| nbody                    | 71.3 ms                                                     | 63.0 ms: 1.13x faster                                                   |
| xml_etree_process        | 44.5 ms                                                     | 40.0 ms: 1.11x faster                                                   |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                    |
| regex_v8                 | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                   |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.49 ms: 1.09x faster                                                   |
| xml_etree_parse          | 96.8 ms                                                     | 88.9 ms: 1.09x faster                                                   |
| nqueens                  | 66.6 ms                                                     | 61.5 ms: 1.08x faster                                                   |
| bench_thread_pool        | 958 us                                                      | 894 us: 1.07x faster                                                    |
| sympy_expand             | 314 ms                                                      | 295 ms: 1.07x faster                                                    |
| scimark_fft              | 187 ms                                                      | 176 ms: 1.06x faster                                                    |
| meteor_contest           | 75.9 ms                                                     | 74.1 ms: 1.02x faster                                                   |
| json                     | 3.14 ms                                                     | 3.06 ms: 1.02x faster                                                   |
| xml_etree_iterparse      | 65.0 ms                                                     | 64.3 ms: 1.01x faster                                                   |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                    |
| logging_format           | 6.76 us                                                     | 6.81 us: 1.01x slower                                                   |
| logging_simple           | 6.22 us                                                     | 6.32 us: 1.02x slower                                                   |
| async_generators         | 222 ms                                                      | 230 ms: 1.04x slower                                                    |
| json_loads               | 14.0 us                                                     | 15.4 us: 1.10x slower                                                   |
| telco                    | 3.94 ms                                                     | 4.60 ms: 1.17x slower                                                   |
| python_startup_no_site   | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                   |
| python_startup           | 20.6 ms                                                     | 26.6 ms: 1.29x slower                                                   |
| coverage                 | 39.0 ms                                                     | 51.5 ms: 1.32x slower                                                   |
| bench_mp_pool            | 62.0 ms                                                     | 89.4 ms: 1.44x slower                                                   |
| gc_traversal             | 1.41 ms                                                     | 2.07 ms: 1.47x slower                                                   |
| create_gc_cycles         | 800 us                                                      | 1.24 ms: 1.55x slower                                                   |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                            |

Benchmark hidden because not significant (2): fannkuch, xml_etree_generate
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250425-3.14.0a7+-dac50cc/bm-20250425-pythonperf1-amd64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.277x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown