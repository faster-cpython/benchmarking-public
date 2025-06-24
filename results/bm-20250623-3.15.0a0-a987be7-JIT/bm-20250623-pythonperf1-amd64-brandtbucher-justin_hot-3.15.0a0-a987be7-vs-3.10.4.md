# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_hot
- machine: windows-amd64
- commit hash: a987be7
- commit date: 2025-06-23
- overall geometric mean: 1.313x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 219 ms: 1.12x faster                                                   |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                 |
| html5lib       | 51.0 ms                                                     | 38.9 ms: 1.31x faster                                                  |
| Geometric mean | (ref)                                                       | 1.19x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|-------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 393 ms: 2.82x faster                                                   |
| async_tree_none         | 435 ms                                                      | 169 ms: 2.58x faster                                                   |
| async_tree_memoization  | 526 ms                                                      | 206 ms: 2.56x faster                                                   |
| async_tree_cpu_io_mixed | 638 ms                                                      | 330 ms: 1.93x faster                                                   |
| Geometric mean          | (ref)                                                       | 2.45x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.7 ms: 1.38x faster                                                  |
| nbody          | 71.3 ms                                                     | 55.3 ms: 1.29x faster                                                  |
| Geometric mean | (ref)                                                       | 1.21x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.3 ms: 1.35x faster                                                  |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                                   |
| regex_v8       | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                  |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                       | 1.16x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 109 us: 1.67x faster                                                   |
| json_dumps           | 9.16 ms                                                     | 6.16 ms: 1.49x faster                                                  |
| tomli_loads          | 1.67 sec                                                    | 1.15 sec: 1.46x faster                                                 |
| pickle_pure_python   | 270 us                                                      | 202 us: 1.34x faster                                                   |
| xml_etree_process    | 44.5 ms                                                     | 35.5 ms: 1.25x faster                                                  |
| xml_etree_generate   | 55.5 ms                                                     | 50.3 ms: 1.10x faster                                                  |
| xml_etree_parse      | 96.8 ms                                                     | 88.3 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.0 ms: 1.03x faster                                                  |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                       | 1.25x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                  |
| python_startup         | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                                  |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.40 ms: 1.67x faster                                                  |
| genshi_text     | 19.8 ms                                                     | 15.3 ms: 1.30x faster                                                  |
| django_template | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                  |
| genshi_xml      | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                  |
| Geometric mean  | (ref)                                                       | 1.33x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 106 us: 3.18x faster                                                   |
| async_tree_io            | 1.11 sec                                                    | 393 ms: 2.82x faster                                                   |
| async_tree_none          | 435 ms                                                      | 169 ms: 2.58x faster                                                   |
| async_tree_memoization   | 526 ms                                                      | 206 ms: 2.56x faster                                                   |
| pathlib                  | 75.7 ms                                                     | 31.8 ms: 2.38x faster                                                  |
| mdp                      | 1.78 sec                                                    | 807 ms: 2.21x faster                                                   |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 330 ms: 1.93x faster                                                   |
| deltablue                | 4.19 ms                                                     | 2.22 ms: 1.89x faster                                                  |
| go                       | 139 ms                                                      | 75.5 ms: 1.84x faster                                                  |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                   |
| richards_super           | 52.2 ms                                                     | 30.5 ms: 1.71x faster                                                  |
| unpickle_pure_python     | 183 us                                                      | 109 us: 1.67x faster                                                   |
| mako                     | 9.03 ms                                                     | 5.40 ms: 1.67x faster                                                  |
| generators               | 32.4 ms                                                     | 19.7 ms: 1.64x faster                                                  |
| deepcopy_memo            | 28.8 us                                                     | 17.8 us: 1.62x faster                                                  |
| pyflate                  | 409 ms                                                      | 256 ms: 1.60x faster                                                   |
| richards                 | 42.4 ms                                                     | 26.9 ms: 1.58x faster                                                  |
| comprehensions           | 16.5 us                                                     | 10.6 us: 1.55x faster                                                  |
| chaos                    | 61.7 ms                                                     | 40.4 ms: 1.53x faster                                                  |
| deepcopy                 | 255 us                                                      | 170 us: 1.50x faster                                                   |
| raytrace                 | 273 ms                                                      | 182 ms: 1.50x faster                                                   |
| json_dumps               | 9.16 ms                                                     | 6.16 ms: 1.49x faster                                                  |
| tomli_loads              | 1.67 sec                                                    | 1.15 sec: 1.46x faster                                                 |
| hexiom                   | 5.74 ms                                                     | 4.05 ms: 1.42x faster                                                  |
| scimark_sor              | 106 ms                                                      | 75.9 ms: 1.40x faster                                                  |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.2 ms: 1.39x faster                                                  |
| float                    | 61.7 ms                                                     | 44.7 ms: 1.38x faster                                                  |
| scimark_lu               | 85.8 ms                                                     | 62.8 ms: 1.37x faster                                                  |
| crypto_pyaes             | 62.5 ms                                                     | 45.9 ms: 1.36x faster                                                  |
| regex_compile            | 106 ms                                                      | 78.3 ms: 1.35x faster                                                  |
| pickle_pure_python       | 270 us                                                      | 202 us: 1.34x faster                                                   |
| pycparser                | 930 ms                                                      | 701 ms: 1.33x faster                                                   |
| html5lib                 | 51.0 ms                                                     | 38.9 ms: 1.31x faster                                                  |
| genshi_text              | 19.8 ms                                                     | 15.3 ms: 1.30x faster                                                  |
| spectral_norm            | 77.3 ms                                                     | 59.9 ms: 1.29x faster                                                  |
| nbody                    | 71.3 ms                                                     | 55.3 ms: 1.29x faster                                                  |
| xml_etree_process        | 44.5 ms                                                     | 35.5 ms: 1.25x faster                                                  |
| thrift                   | 617 us                                                      | 497 us: 1.24x faster                                                   |
| deepcopy_reduce          | 2.20 us                                                     | 1.78 us: 1.24x faster                                                  |
| dulwich_log              | 50.5 ms                                                     | 40.9 ms: 1.23x faster                                                  |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.23x faster                                                  |
| sympy_sum                | 107 ms                                                      | 87.1 ms: 1.23x faster                                                  |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.23 ms: 1.22x faster                                                  |
| sympy_integrate          | 15.3 ms                                                     | 12.6 ms: 1.21x faster                                                  |
| pprint_pformat           | 1.22 sec                                                    | 1.01 sec: 1.21x faster                                                 |
| scimark_fft              | 187 ms                                                      | 157 ms: 1.20x faster                                                   |
| django_template          | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                  |
| genshi_xml               | 41.0 ms                                                     | 34.3 ms: 1.20x faster                                                  |
| fannkuch                 | 256 ms                                                      | 215 ms: 1.19x faster                                                   |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                 |
| pprint_safe_repr         | 592 ms                                                      | 512 ms: 1.16x faster                                                   |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                                   |
| sympy_str                | 194 ms                                                      | 170 ms: 1.14x faster                                                   |
| coroutines               | 16.0 ms                                                     | 14.0 ms: 1.14x faster                                                  |
| 2to3                     | 246 ms                                                      | 219 ms: 1.12x faster                                                   |
| regex_v8                 | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                                  |
| nqueens                  | 66.6 ms                                                     | 60.1 ms: 1.11x faster                                                  |
| xml_etree_generate       | 55.5 ms                                                     | 50.3 ms: 1.10x faster                                                  |
| xml_etree_parse          | 96.8 ms                                                     | 88.3 ms: 1.10x faster                                                  |
| sympy_expand             | 314 ms                                                      | 294 ms: 1.07x faster                                                   |
| meteor_contest           | 75.9 ms                                                     | 72.1 ms: 1.05x faster                                                  |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.04x faster                                                  |
| json                     | 3.14 ms                                                     | 3.01 ms: 1.04x faster                                                  |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.0 ms: 1.03x faster                                                  |
| logging_format           | 6.76 us                                                     | 6.59 us: 1.03x faster                                                  |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                  |
| telco                    | 3.94 ms                                                     | 4.27 ms: 1.08x slower                                                  |
| async_generators         | 222 ms                                                      | 247 ms: 1.11x slower                                                   |
| coverage                 | 39.0 ms                                                     | 48.3 ms: 1.24x slower                                                  |
| python_startup_no_site   | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                  |
| python_startup           | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                                  |
| gc_traversal             | 1.41 ms                                                     | 2.12 ms: 1.51x slower                                                  |
| create_gc_cycles         | 800 us                                                      | 1.33 ms: 1.66x slower                                                  |
| logging_silent           | 94.6 ns                                                     | 316 ns: 3.34x slower                                                   |
| Geometric mean           | (ref)                                                       | 1.28x faster                                                           |

Benchmark hidden because not significant (2): pidigits, logging_simple
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250623-3.15.0a0-a987be7-JIT/bm-20250623-pythonperf1-amd64-brandtbucher-justin_hot-3.15.0a0-a987be7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.313x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown