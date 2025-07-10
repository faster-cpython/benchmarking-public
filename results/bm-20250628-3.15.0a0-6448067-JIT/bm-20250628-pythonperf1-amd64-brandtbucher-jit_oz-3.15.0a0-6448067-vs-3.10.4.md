# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_oz
- machine: windows-amd64
- commit hash: 6448067
- commit date: 2025-06-28
- overall geometric mean: 1.310x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 218 ms: 1.13x faster                                               |
| docutils       | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                             |
| html5lib       | 51.0 ms                                                     | 37.9 ms: 1.35x faster                                              |
| Geometric mean | (ref)                                                       | 1.21x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|-------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 391 ms: 2.84x faster                                               |
| async_tree_none         | 435 ms                                                      | 170 ms: 2.55x faster                                               |
| async_tree_memoization  | 526 ms                                                      | 207 ms: 2.55x faster                                               |
| async_tree_cpu_io_mixed | 638 ms                                                      | 332 ms: 1.92x faster                                               |
| Geometric mean          | (ref)                                                       | 2.44x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.9 ms: 1.38x faster                                              |
| nbody          | 71.3 ms                                                     | 56.2 ms: 1.27x faster                                              |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                       | 1.21x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.5 ms: 1.35x faster                                              |
| regex_dna      | 136 ms                                                      | 117 ms: 1.17x faster                                               |
| regex_v8       | 15.4 ms                                                     | 13.4 ms: 1.15x faster                                              |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                              |
| Geometric mean | (ref)                                                       | 1.18x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 110 us: 1.67x faster                                               |
| json_dumps           | 9.16 ms                                                     | 6.19 ms: 1.48x faster                                              |
| tomli_loads          | 1.67 sec                                                    | 1.24 sec: 1.35x faster                                             |
| pickle_pure_python   | 270 us                                                      | 207 us: 1.30x faster                                               |
| xml_etree_process    | 44.5 ms                                                     | 35.5 ms: 1.25x faster                                              |
| xml_etree_parse      | 96.8 ms                                                     | 86.5 ms: 1.12x faster                                              |
| xml_etree_generate   | 55.5 ms                                                     | 50.3 ms: 1.10x faster                                              |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.3 ms: 1.04x faster                                              |
| json_loads           | 14.0 us                                                     | 14.7 us: 1.05x slower                                              |
| Geometric mean       | (ref)                                                       | 1.24x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.1 ms: 1.23x slower                                              |
| python_startup         | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                              |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.57 ms: 1.62x faster                                              |
| genshi_text     | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                              |
| genshi_xml      | 41.0 ms                                                     | 34.0 ms: 1.21x faster                                              |
| django_template | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                              |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.21x faster                                               |
| async_tree_io            | 1.11 sec                                                    | 391 ms: 2.84x faster                                               |
| pathlib                  | 75.7 ms                                                     | 28.7 ms: 2.64x faster                                              |
| async_tree_none          | 435 ms                                                      | 170 ms: 2.55x faster                                               |
| async_tree_memoization   | 526 ms                                                      | 207 ms: 2.55x faster                                               |
| mdp                      | 1.78 sec                                                    | 795 ms: 2.24x faster                                               |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 332 ms: 1.92x faster                                               |
| deltablue                | 4.19 ms                                                     | 2.21 ms: 1.89x faster                                              |
| go                       | 139 ms                                                      | 77.8 ms: 1.79x faster                                              |
| pylint                   | 350 ms                                                      | 198 ms: 1.77x faster                                               |
| logging_silent           | 94.6 ns                                                     | 54.8 ns: 1.73x faster                                              |
| richards_super           | 52.2 ms                                                     | 30.7 ms: 1.70x faster                                              |
| unpickle_pure_python     | 183 us                                                      | 110 us: 1.67x faster                                               |
| generators               | 32.4 ms                                                     | 19.5 ms: 1.66x faster                                              |
| deepcopy_memo            | 28.8 us                                                     | 17.6 us: 1.64x faster                                              |
| mako                     | 9.03 ms                                                     | 5.57 ms: 1.62x faster                                              |
| pyflate                  | 409 ms                                                      | 258 ms: 1.58x faster                                               |
| richards                 | 42.4 ms                                                     | 27.0 ms: 1.57x faster                                              |
| raytrace                 | 273 ms                                                      | 178 ms: 1.53x faster                                               |
| deepcopy                 | 255 us                                                      | 170 us: 1.50x faster                                               |
| chaos                    | 61.7 ms                                                     | 41.2 ms: 1.50x faster                                              |
| comprehensions           | 16.5 us                                                     | 11.0 us: 1.50x faster                                              |
| json_dumps               | 9.16 ms                                                     | 6.19 ms: 1.48x faster                                              |
| scimark_lu               | 85.8 ms                                                     | 58.6 ms: 1.46x faster                                              |
| hexiom                   | 5.74 ms                                                     | 4.17 ms: 1.38x faster                                              |
| float                    | 61.7 ms                                                     | 44.9 ms: 1.38x faster                                              |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.7 ms: 1.37x faster                                              |
| tomli_loads              | 1.67 sec                                                    | 1.24 sec: 1.35x faster                                             |
| regex_compile            | 106 ms                                                      | 78.5 ms: 1.35x faster                                              |
| pycparser                | 930 ms                                                      | 691 ms: 1.35x faster                                               |
| html5lib                 | 51.0 ms                                                     | 37.9 ms: 1.35x faster                                              |
| scimark_sor              | 106 ms                                                      | 79.2 ms: 1.34x faster                                              |
| crypto_pyaes             | 62.5 ms                                                     | 46.7 ms: 1.34x faster                                              |
| pickle_pure_python       | 270 us                                                      | 207 us: 1.30x faster                                               |
| pprint_pformat           | 1.22 sec                                                    | 941 ms: 1.30x faster                                               |
| pprint_safe_repr         | 592 ms                                                      | 460 ms: 1.29x faster                                               |
| genshi_text              | 19.8 ms                                                     | 15.5 ms: 1.28x faster                                              |
| nbody                    | 71.3 ms                                                     | 56.2 ms: 1.27x faster                                              |
| xml_etree_process        | 44.5 ms                                                     | 35.5 ms: 1.25x faster                                              |
| dulwich_log              | 50.5 ms                                                     | 40.3 ms: 1.25x faster                                              |
| thrift                   | 617 us                                                      | 496 us: 1.24x faster                                               |
| sympy_sum                | 107 ms                                                      | 86.9 ms: 1.23x faster                                              |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.23x faster                                              |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.23 ms: 1.22x faster                                              |
| sympy_integrate          | 15.3 ms                                                     | 12.6 ms: 1.21x faster                                              |
| genshi_xml               | 41.0 ms                                                     | 34.0 ms: 1.21x faster                                              |
| spectral_norm            | 77.3 ms                                                     | 64.5 ms: 1.20x faster                                              |
| deepcopy_reduce          | 2.20 us                                                     | 1.84 us: 1.20x faster                                              |
| django_template          | 28.9 ms                                                     | 24.4 ms: 1.18x faster                                              |
| docutils                 | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                             |
| regex_dna                | 136 ms                                                      | 117 ms: 1.17x faster                                               |
| scimark_fft              | 187 ms                                                      | 161 ms: 1.16x faster                                               |
| regex_v8                 | 15.4 ms                                                     | 13.4 ms: 1.15x faster                                              |
| sympy_str                | 194 ms                                                      | 169 ms: 1.15x faster                                               |
| 2to3                     | 246 ms                                                      | 218 ms: 1.13x faster                                               |
| xml_etree_parse          | 96.8 ms                                                     | 86.5 ms: 1.12x faster                                              |
| xml_etree_generate       | 55.5 ms                                                     | 50.3 ms: 1.10x faster                                              |
| coroutines               | 16.0 ms                                                     | 14.5 ms: 1.10x faster                                              |
| nqueens                  | 66.6 ms                                                     | 60.8 ms: 1.10x faster                                              |
| regex_effbot             | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                              |
| sympy_expand             | 314 ms                                                      | 292 ms: 1.08x faster                                               |
| meteor_contest           | 75.9 ms                                                     | 71.0 ms: 1.07x faster                                              |
| fannkuch                 | 256 ms                                                      | 242 ms: 1.05x faster                                               |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.3 ms: 1.04x faster                                              |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                               |
| json                     | 3.14 ms                                                     | 3.26 ms: 1.04x slower                                              |
| json_loads               | 14.0 us                                                     | 14.7 us: 1.05x slower                                              |
| telco                    | 3.94 ms                                                     | 4.36 ms: 1.11x slower                                              |
| async_generators         | 222 ms                                                      | 248 ms: 1.12x slower                                               |
| python_startup_no_site   | 15.5 ms                                                     | 19.1 ms: 1.23x slower                                              |
| python_startup           | 20.6 ms                                                     | 26.0 ms: 1.26x slower                                              |
| coverage                 | 39.0 ms                                                     | 49.7 ms: 1.27x slower                                              |
| gc_traversal             | 1.41 ms                                                     | 2.09 ms: 1.48x slower                                              |
| create_gc_cycles         | 800 us                                                      | 1.30 ms: 1.63x slower                                              |
| Geometric mean           | (ref)                                                       | 1.31x faster                                                       |

Benchmark hidden because not significant (2): logging_format, logging_simple
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250628-3.15.0a0-6448067-JIT/bm-20250628-pythonperf1-amd64-brandtbucher-jit_oz-3.15.0a0-6448067.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.310x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown