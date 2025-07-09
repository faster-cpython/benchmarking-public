# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_targets
- machine: windows-amd64
- commit hash: 997a858
- commit date: 2025-07-08
- overall geometric mean: 1.317x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 220 ms: 1.12x faster                                                    |
| docutils       | 1.92 sec                                                    | 1.63 sec: 1.17x faster                                                  |
| html5lib       | 51.0 ms                                                     | 37.9 ms: 1.35x faster                                                   |
| Geometric mean | (ref)                                                       | 1.21x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 394 ms: 2.81x faster                                                    |
| async_tree_none         | 435 ms                                                      | 165 ms: 2.63x faster                                                    |
| async_tree_memoization  | 526 ms                                                      | 203 ms: 2.59x faster                                                    |
| async_tree_cpu_io_mixed | 638 ms                                                      | 331 ms: 1.93x faster                                                    |
| Geometric mean          | (ref)                                                       | 2.46x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.0 ms: 1.40x faster                                                   |
| nbody          | 71.3 ms                                                     | 53.2 ms: 1.34x faster                                                   |
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                       | 1.25x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.7 ms: 1.35x faster                                                   |
| regex_dna      | 136 ms                                                      | 121 ms: 1.12x faster                                                    |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.08x faster                                                   |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                       | 1.15x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 106 us: 1.73x faster                                                    |
| tomli_loads          | 1.67 sec                                                    | 1.12 sec: 1.50x faster                                                  |
| json_dumps           | 9.16 ms                                                     | 6.30 ms: 1.45x faster                                                   |
| pickle_pure_python   | 270 us                                                      | 203 us: 1.33x faster                                                    |
| xml_etree_process    | 44.5 ms                                                     | 35.2 ms: 1.26x faster                                                   |
| xml_etree_generate   | 55.5 ms                                                     | 49.7 ms: 1.12x faster                                                   |
| xml_etree_parse      | 96.8 ms                                                     | 87.5 ms: 1.11x faster                                                   |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                                   |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                       | 1.26x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                   |
| python_startup         | 20.6 ms                                                     | 26.1 ms: 1.26x slower                                                   |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.40 ms: 1.67x faster                                                   |
| genshi_text     | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                   |
| genshi_xml      | 41.0 ms                                                     | 34.8 ms: 1.18x faster                                                   |
| django_template | 28.9 ms                                                     | 24.6 ms: 1.18x faster                                                   |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.25x faster                                                    |
| async_tree_io            | 1.11 sec                                                    | 394 ms: 2.81x faster                                                    |
| pathlib                  | 75.7 ms                                                     | 28.6 ms: 2.65x faster                                                   |
| async_tree_none          | 435 ms                                                      | 165 ms: 2.63x faster                                                    |
| async_tree_memoization   | 526 ms                                                      | 203 ms: 2.59x faster                                                    |
| mdp                      | 1.78 sec                                                    | 809 ms: 2.20x faster                                                    |
| deltablue                | 4.19 ms                                                     | 2.17 ms: 1.93x faster                                                   |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 331 ms: 1.93x faster                                                    |
| go                       | 139 ms                                                      | 75.8 ms: 1.83x faster                                                   |
| pylint                   | 350 ms                                                      | 197 ms: 1.78x faster                                                    |
| logging_silent           | 94.6 ns                                                     | 54.0 ns: 1.75x faster                                                   |
| richards_super           | 52.2 ms                                                     | 30.2 ms: 1.73x faster                                                   |
| unpickle_pure_python     | 183 us                                                      | 106 us: 1.73x faster                                                    |
| mako                     | 9.03 ms                                                     | 5.40 ms: 1.67x faster                                                   |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.65x faster                                                   |
| pyflate                  | 409 ms                                                      | 250 ms: 1.64x faster                                                    |
| deepcopy_memo            | 28.8 us                                                     | 17.9 us: 1.61x faster                                                   |
| richards                 | 42.4 ms                                                     | 26.4 ms: 1.61x faster                                                   |
| comprehensions           | 16.5 us                                                     | 10.4 us: 1.58x faster                                                   |
| raytrace                 | 273 ms                                                      | 180 ms: 1.52x faster                                                    |
| tomli_loads              | 1.67 sec                                                    | 1.12 sec: 1.50x faster                                                  |
| deepcopy                 | 255 us                                                      | 171 us: 1.50x faster                                                    |
| chaos                    | 61.7 ms                                                     | 41.3 ms: 1.49x faster                                                   |
| json_dumps               | 9.16 ms                                                     | 6.30 ms: 1.45x faster                                                   |
| hexiom                   | 5.74 ms                                                     | 4.09 ms: 1.41x faster                                                   |
| float                    | 61.7 ms                                                     | 44.0 ms: 1.40x faster                                                   |
| scimark_sor              | 106 ms                                                      | 76.5 ms: 1.39x faster                                                   |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.5 ms: 1.38x faster                                                   |
| pprint_pformat           | 1.22 sec                                                    | 895 ms: 1.36x faster                                                    |
| crypto_pyaes             | 62.5 ms                                                     | 46.1 ms: 1.36x faster                                                   |
| pprint_safe_repr         | 592 ms                                                      | 437 ms: 1.35x faster                                                    |
| html5lib                 | 51.0 ms                                                     | 37.9 ms: 1.35x faster                                                   |
| regex_compile            | 106 ms                                                      | 78.7 ms: 1.35x faster                                                   |
| nbody                    | 71.3 ms                                                     | 53.2 ms: 1.34x faster                                                   |
| pycparser                | 930 ms                                                      | 695 ms: 1.34x faster                                                    |
| scimark_lu               | 85.8 ms                                                     | 64.5 ms: 1.33x faster                                                   |
| pickle_pure_python       | 270 us                                                      | 203 us: 1.33x faster                                                    |
| thrift                   | 617 us                                                      | 483 us: 1.28x faster                                                    |
| genshi_text              | 19.8 ms                                                     | 15.6 ms: 1.27x faster                                                   |
| xml_etree_process        | 44.5 ms                                                     | 35.2 ms: 1.26x faster                                                   |
| dulwich_log              | 50.5 ms                                                     | 40.1 ms: 1.26x faster                                                   |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.22x faster                                                   |
| sympy_sum                | 107 ms                                                      | 87.9 ms: 1.22x faster                                                   |
| scimark_fft              | 187 ms                                                      | 154 ms: 1.22x faster                                                    |
| sympy_integrate          | 15.3 ms                                                     | 12.6 ms: 1.21x faster                                                   |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.28 ms: 1.20x faster                                                   |
| deepcopy_reduce          | 2.20 us                                                     | 1.85 us: 1.19x faster                                                   |
| genshi_xml               | 41.0 ms                                                     | 34.8 ms: 1.18x faster                                                   |
| django_template          | 28.9 ms                                                     | 24.6 ms: 1.18x faster                                                   |
| docutils                 | 1.92 sec                                                    | 1.63 sec: 1.17x faster                                                  |
| sympy_str                | 194 ms                                                      | 171 ms: 1.14x faster                                                    |
| regex_dna                | 136 ms                                                      | 121 ms: 1.12x faster                                                    |
| fannkuch                 | 256 ms                                                      | 228 ms: 1.12x faster                                                    |
| xml_etree_generate       | 55.5 ms                                                     | 49.7 ms: 1.12x faster                                                   |
| 2to3                     | 246 ms                                                      | 220 ms: 1.12x faster                                                    |
| xml_etree_parse          | 96.8 ms                                                     | 87.5 ms: 1.11x faster                                                   |
| nqueens                  | 66.6 ms                                                     | 60.3 ms: 1.11x faster                                                   |
| spectral_norm            | 77.3 ms                                                     | 70.3 ms: 1.10x faster                                                   |
| coroutines               | 16.0 ms                                                     | 14.6 ms: 1.09x faster                                                   |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.08x faster                                                   |
| meteor_contest           | 75.9 ms                                                     | 70.6 ms: 1.08x faster                                                   |
| sympy_expand             | 314 ms                                                      | 297 ms: 1.06x faster                                                    |
| regex_effbot             | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                   |
| json                     | 3.14 ms                                                     | 3.00 ms: 1.04x faster                                                   |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.9 ms: 1.03x faster                                                   |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                    |
| logging_format           | 6.76 us                                                     | 6.67 us: 1.01x faster                                                   |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                                   |
| telco                    | 3.94 ms                                                     | 4.26 ms: 1.08x slower                                                   |
| async_generators         | 222 ms                                                      | 252 ms: 1.14x slower                                                    |
| python_startup_no_site   | 15.5 ms                                                     | 19.2 ms: 1.24x slower                                                   |
| python_startup           | 20.6 ms                                                     | 26.1 ms: 1.26x slower                                                   |
| coverage                 | 39.0 ms                                                     | 52.2 ms: 1.34x slower                                                   |
| gc_traversal             | 1.41 ms                                                     | 2.14 ms: 1.52x slower                                                   |
| create_gc_cycles         | 800 us                                                      | 1.31 ms: 1.63x slower                                                   |
| Geometric mean           | (ref)                                                       | 1.32x faster                                                            |

Benchmark hidden because not significant (1): logging_simple
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250708-3.15.0a0-997a858-JIT/bm-20250708-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-997a858.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.317x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown