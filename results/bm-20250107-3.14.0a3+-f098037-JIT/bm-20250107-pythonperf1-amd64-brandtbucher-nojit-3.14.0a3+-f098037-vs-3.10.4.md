# Results vs. 3.10.4

- fork: brandtbucher
- ref: nojit
- machine: windows-amd64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.263x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                               |
| docutils       | 1.92 sec                                                    | 1.72 sec: 1.11x faster                                             |
| html5lib       | 51.0 ms                                                     | 38.0 ms: 1.34x faster                                              |
| Geometric mean | (ref)                                                       | 1.19x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 399 ms: 2.78x faster                                               |
| async_tree_none         | 435 ms                                                      | 182 ms: 2.40x faster                                               |
| async_tree_memoization  | 526 ms                                                      | 220 ms: 2.39x faster                                               |
| async_tree_cpu_io_mixed | 638 ms                                                      | 352 ms: 1.81x faster                                               |
| Geometric mean          | (ref)                                                       | 2.32x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 39.5 ms: 1.56x faster                                              |
| nbody          | 71.3 ms                                                     | 54.2 ms: 1.32x faster                                              |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                       | 1.28x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.5 ms: 1.32x faster                                              |
| regex_dna      | 136 ms                                                      | 113 ms: 1.20x faster                                               |
| regex_effbot   | 1.66 ms                                                     | 1.41 ms: 1.18x faster                                              |
| regex_v8       | 15.4 ms                                                     | 14.6 ms: 1.06x faster                                              |
| Geometric mean | (ref)                                                       | 1.19x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 109 us: 1.68x faster                                               |
| json_dumps           | 9.16 ms                                                     | 6.42 ms: 1.43x faster                                              |
| tomli_loads          | 1.67 sec                                                    | 1.19 sec: 1.41x faster                                             |
| pickle_pure_python   | 270 us                                                      | 207 us: 1.30x faster                                               |
| xml_etree_process    | 44.5 ms                                                     | 35.9 ms: 1.24x faster                                              |
| xml_etree_generate   | 55.5 ms                                                     | 49.6 ms: 1.12x faster                                              |
| xml_etree_parse      | 96.8 ms                                                     | 87.4 ms: 1.11x faster                                              |
| xml_etree_iterparse  | 65.0 ms                                                     | 59.1 ms: 1.10x faster                                              |
| Geometric mean       | (ref)                                                       | 1.25x faster                                                       |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.0 ms: 1.10x slower                                              |
| python_startup         | 20.6 ms                                                     | 23.1 ms: 1.12x slower                                              |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.16 ms: 1.75x faster                                              |
| django_template | 28.9 ms                                                     | 26.0 ms: 1.11x faster                                              |
| genshi_text     | 19.8 ms                                                     | 18.6 ms: 1.07x faster                                              |
| genshi_xml      | 41.0 ms                                                     | 44.9 ms: 1.09x slower                                              |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 116 us: 2.91x faster                                               |
| async_tree_io            | 1.11 sec                                                    | 399 ms: 2.78x faster                                               |
| async_tree_none          | 435 ms                                                      | 182 ms: 2.40x faster                                               |
| async_tree_memoization   | 526 ms                                                      | 220 ms: 2.39x faster                                               |
| deltablue                | 4.19 ms                                                     | 2.25 ms: 1.86x faster                                              |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 352 ms: 1.81x faster                                               |
| deepcopy_memo            | 28.8 us                                                     | 16.0 us: 1.79x faster                                              |
| scimark_sor              | 106 ms                                                      | 59.7 ms: 1.78x faster                                              |
| mako                     | 9.03 ms                                                     | 5.16 ms: 1.75x faster                                              |
| logging_silent           | 94.6 ns                                                     | 55.7 ns: 1.70x faster                                              |
| unpickle_pure_python     | 183 us                                                      | 109 us: 1.68x faster                                               |
| pylint                   | 350 ms                                                      | 208 ms: 1.68x faster                                               |
| scimark_lu               | 85.8 ms                                                     | 53.2 ms: 1.61x faster                                              |
| scimark_monte_carlo      | 57.3 ms                                                     | 35.7 ms: 1.60x faster                                              |
| go                       | 139 ms                                                      | 88.6 ms: 1.57x faster                                              |
| float                    | 61.7 ms                                                     | 39.5 ms: 1.56x faster                                              |
| spectral_norm            | 77.3 ms                                                     | 49.6 ms: 1.56x faster                                              |
| crypto_pyaes             | 62.5 ms                                                     | 40.9 ms: 1.53x faster                                              |
| chaos                    | 61.7 ms                                                     | 41.8 ms: 1.48x faster                                              |
| pyflate                  | 409 ms                                                      | 277 ms: 1.48x faster                                               |
| sqlglot_parse            | 1.22 ms                                                     | 824 us: 1.47x faster                                               |
| json_dumps               | 9.16 ms                                                     | 6.42 ms: 1.43x faster                                              |
| comprehensions           | 16.5 us                                                     | 11.6 us: 1.42x faster                                              |
| tomli_loads              | 1.67 sec                                                    | 1.19 sec: 1.41x faster                                             |
| generators               | 32.4 ms                                                     | 23.1 ms: 1.40x faster                                              |
| sqlglot_transpile        | 1.48 ms                                                     | 1.07 ms: 1.38x faster                                              |
| richards_super           | 52.2 ms                                                     | 38.4 ms: 1.36x faster                                              |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                               |
| html5lib                 | 51.0 ms                                                     | 38.0 ms: 1.34x faster                                              |
| raytrace                 | 273 ms                                                      | 205 ms: 1.33x faster                                               |
| scimark_fft              | 187 ms                                                      | 142 ms: 1.32x faster                                               |
| regex_compile            | 106 ms                                                      | 80.5 ms: 1.32x faster                                              |
| nbody                    | 71.3 ms                                                     | 54.2 ms: 1.32x faster                                              |
| pycparser                | 930 ms                                                      | 707 ms: 1.32x faster                                               |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.08 ms: 1.31x faster                                              |
| pickle_pure_python       | 270 us                                                      | 207 us: 1.30x faster                                               |
| pprint_pformat           | 1.22 sec                                                    | 955 ms: 1.28x faster                                               |
| dulwich_log              | 50.5 ms                                                     | 39.9 ms: 1.26x faster                                              |
| pprint_safe_repr         | 592 ms                                                      | 472 ms: 1.25x faster                                               |
| richards                 | 42.4 ms                                                     | 34.2 ms: 1.24x faster                                              |
| xml_etree_process        | 44.5 ms                                                     | 35.9 ms: 1.24x faster                                              |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                              |
| regex_dna                | 136 ms                                                      | 113 ms: 1.20x faster                                               |
| deepcopy_reduce          | 2.20 us                                                     | 1.87 us: 1.18x faster                                              |
| thrift                   | 617 us                                                      | 523 us: 1.18x faster                                               |
| regex_effbot             | 1.66 ms                                                     | 1.41 ms: 1.18x faster                                              |
| coroutines               | 16.0 ms                                                     | 13.7 ms: 1.17x faster                                              |
| mdp                      | 1.78 sec                                                    | 1.52 sec: 1.17x faster                                             |
| sympy_sum                | 107 ms                                                      | 91.8 ms: 1.17x faster                                              |
| bench_thread_pool        | 958 us                                                      | 829 us: 1.16x faster                                               |
| hexiom                   | 5.74 ms                                                     | 5.04 ms: 1.14x faster                                              |
| sympy_integrate          | 15.3 ms                                                     | 13.6 ms: 1.12x faster                                              |
| xml_etree_generate       | 55.5 ms                                                     | 49.6 ms: 1.12x faster                                              |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                               |
| docutils                 | 1.92 sec                                                    | 1.72 sec: 1.11x faster                                             |
| django_template          | 28.9 ms                                                     | 26.0 ms: 1.11x faster                                              |
| xml_etree_parse          | 96.8 ms                                                     | 87.4 ms: 1.11x faster                                              |
| sympy_str                | 194 ms                                                      | 176 ms: 1.10x faster                                               |
| xml_etree_iterparse      | 65.0 ms                                                     | 59.1 ms: 1.10x faster                                              |
| json                     | 3.14 ms                                                     | 2.90 ms: 1.08x faster                                              |
| fannkuch                 | 256 ms                                                      | 238 ms: 1.08x faster                                               |
| genshi_text              | 19.8 ms                                                     | 18.6 ms: 1.07x faster                                              |
| sqlglot_optimize         | 39.8 ms                                                     | 37.6 ms: 1.06x faster                                              |
| regex_v8                 | 15.4 ms                                                     | 14.6 ms: 1.06x faster                                              |
| sympy_expand             | 314 ms                                                      | 300 ms: 1.05x faster                                               |
| meteor_contest           | 75.9 ms                                                     | 72.6 ms: 1.05x faster                                              |
| nqueens                  | 66.6 ms                                                     | 65.1 ms: 1.02x faster                                              |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                               |
| logging_format           | 6.76 us                                                     | 6.68 us: 1.01x faster                                              |
| sqlglot_normalize        | 205 ms                                                      | 203 ms: 1.01x faster                                               |
| genshi_xml               | 41.0 ms                                                     | 44.9 ms: 1.09x slower                                              |
| python_startup_no_site   | 15.5 ms                                                     | 17.0 ms: 1.10x slower                                              |
| telco                    | 3.94 ms                                                     | 4.35 ms: 1.10x slower                                              |
| python_startup           | 20.6 ms                                                     | 23.1 ms: 1.12x slower                                              |
| mypy2                    | 555 ms                                                      | 641 ms: 1.15x slower                                               |
| async_generators         | 222 ms                                                      | 259 ms: 1.17x slower                                               |
| coverage                 | 39.0 ms                                                     | 46.5 ms: 1.19x slower                                              |
| bench_mp_pool            | 62.0 ms                                                     | 82.0 ms: 1.32x slower                                              |
| gc_traversal             | 1.41 ms                                                     | 1.96 ms: 1.39x slower                                              |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.51x slower                                              |
| Geometric mean           | (ref)                                                       | 1.26x faster                                                       |

Benchmark hidden because not significant (3): logging_simple, json_loads, pathlib
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250107-3.14.0a3+-f098037-JIT/bm-20250107-pythonperf1-amd64-brandtbucher-nojit-3.14.0a3+-f098037.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.263x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown