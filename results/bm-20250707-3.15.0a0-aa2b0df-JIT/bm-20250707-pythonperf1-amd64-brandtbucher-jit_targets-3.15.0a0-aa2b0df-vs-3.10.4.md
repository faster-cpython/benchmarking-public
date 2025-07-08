# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_targets
- machine: windows-amd64
- commit hash: aa2b0df
- commit date: 2025-07-07
- overall geometric mean: 1.315x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 218 ms: 1.13x faster                                                    |
| docutils       | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                  |
| html5lib       | 51.0 ms                                                     | 37.9 ms: 1.35x faster                                                   |
| Geometric mean | (ref)                                                       | 1.21x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 397 ms: 2.79x faster                                                    |
| async_tree_none         | 435 ms                                                      | 169 ms: 2.57x faster                                                    |
| async_tree_memoization  | 526 ms                                                      | 206 ms: 2.56x faster                                                    |
| async_tree_cpu_io_mixed | 638 ms                                                      | 334 ms: 1.91x faster                                                    |
| Geometric mean          | (ref)                                                       | 2.43x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 44.9 ms: 1.37x faster                                                   |
| nbody          | 71.3 ms                                                     | 59.8 ms: 1.19x faster                                                   |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                       | 1.19x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.8 ms: 1.35x faster                                                   |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                    |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                   |
| regex_effbot   | 1.66 ms                                                     | 1.62 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                       | 1.14x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 105 us: 1.75x faster                                                    |
| tomli_loads          | 1.67 sec                                                    | 1.12 sec: 1.49x faster                                                  |
| json_dumps           | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                                   |
| pickle_pure_python   | 270 us                                                      | 207 us: 1.30x faster                                                    |
| xml_etree_process    | 44.5 ms                                                     | 34.8 ms: 1.28x faster                                                   |
| xml_etree_generate   | 55.5 ms                                                     | 49.2 ms: 1.13x faster                                                   |
| xml_etree_parse      | 96.8 ms                                                     | 88.5 ms: 1.09x faster                                                   |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.6 ms: 1.02x faster                                                   |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                       | 1.26x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                   |
| python_startup         | 20.6 ms                                                     | 25.9 ms: 1.26x slower                                                   |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.38 ms: 1.68x faster                                                   |
| genshi_text     | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                   |
| genshi_xml      | 41.0 ms                                                     | 35.2 ms: 1.17x faster                                                   |
| django_template | 28.9 ms                                                     | 25.0 ms: 1.16x faster                                                   |
| Geometric mean  | (ref)                                                       | 1.30x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.25x faster                                                    |
| async_tree_io            | 1.11 sec                                                    | 397 ms: 2.79x faster                                                    |
| async_tree_none          | 435 ms                                                      | 169 ms: 2.57x faster                                                    |
| async_tree_memoization   | 526 ms                                                      | 206 ms: 2.56x faster                                                    |
| pathlib                  | 75.7 ms                                                     | 31.6 ms: 2.39x faster                                                   |
| mdp                      | 1.78 sec                                                    | 797 ms: 2.23x faster                                                    |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 334 ms: 1.91x faster                                                    |
| deltablue                | 4.19 ms                                                     | 2.21 ms: 1.89x faster                                                   |
| go                       | 139 ms                                                      | 77.4 ms: 1.80x faster                                                   |
| pylint                   | 350 ms                                                      | 199 ms: 1.76x faster                                                    |
| unpickle_pure_python     | 183 us                                                      | 105 us: 1.75x faster                                                    |
| logging_silent           | 94.6 ns                                                     | 54.2 ns: 1.75x faster                                                   |
| richards_super           | 52.2 ms                                                     | 30.6 ms: 1.71x faster                                                   |
| mako                     | 9.03 ms                                                     | 5.38 ms: 1.68x faster                                                   |
| generators               | 32.4 ms                                                     | 19.5 ms: 1.66x faster                                                   |
| deepcopy_memo            | 28.8 us                                                     | 17.8 us: 1.62x faster                                                   |
| pyflate                  | 409 ms                                                      | 253 ms: 1.62x faster                                                    |
| comprehensions           | 16.5 us                                                     | 10.3 us: 1.61x faster                                                   |
| richards                 | 42.4 ms                                                     | 26.9 ms: 1.57x faster                                                   |
| chaos                    | 61.7 ms                                                     | 40.6 ms: 1.52x faster                                                   |
| deepcopy                 | 255 us                                                      | 169 us: 1.51x faster                                                    |
| tomli_loads              | 1.67 sec                                                    | 1.12 sec: 1.49x faster                                                  |
| raytrace                 | 273 ms                                                      | 183 ms: 1.49x faster                                                    |
| json_dumps               | 9.16 ms                                                     | 6.27 ms: 1.46x faster                                                   |
| scimark_lu               | 85.8 ms                                                     | 58.8 ms: 1.46x faster                                                   |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.9 ms: 1.40x faster                                                   |
| hexiom                   | 5.74 ms                                                     | 4.12 ms: 1.39x faster                                                   |
| pprint_pformat           | 1.22 sec                                                    | 881 ms: 1.38x faster                                                    |
| float                    | 61.7 ms                                                     | 44.9 ms: 1.37x faster                                                   |
| pprint_safe_repr         | 592 ms                                                      | 434 ms: 1.36x faster                                                    |
| scimark_sor              | 106 ms                                                      | 77.9 ms: 1.36x faster                                                   |
| crypto_pyaes             | 62.5 ms                                                     | 45.9 ms: 1.36x faster                                                   |
| html5lib                 | 51.0 ms                                                     | 37.9 ms: 1.35x faster                                                   |
| regex_compile            | 106 ms                                                      | 78.8 ms: 1.35x faster                                                   |
| pycparser                | 930 ms                                                      | 695 ms: 1.34x faster                                                    |
| pickle_pure_python       | 270 us                                                      | 207 us: 1.30x faster                                                    |
| xml_etree_process        | 44.5 ms                                                     | 34.8 ms: 1.28x faster                                                   |
| genshi_text              | 19.8 ms                                                     | 15.7 ms: 1.26x faster                                                   |
| thrift                   | 617 us                                                      | 496 us: 1.24x faster                                                    |
| scimark_fft              | 187 ms                                                      | 152 ms: 1.24x faster                                                    |
| sympy_sum                | 107 ms                                                      | 86.9 ms: 1.23x faster                                                   |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.23x faster                                                   |
| dulwich_log              | 50.5 ms                                                     | 41.1 ms: 1.23x faster                                                   |
| deepcopy_reduce          | 2.20 us                                                     | 1.81 us: 1.22x faster                                                   |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.25 ms: 1.21x faster                                                   |
| sympy_integrate          | 15.3 ms                                                     | 12.7 ms: 1.20x faster                                                   |
| spectral_norm            | 77.3 ms                                                     | 64.5 ms: 1.20x faster                                                   |
| nbody                    | 71.3 ms                                                     | 59.8 ms: 1.19x faster                                                   |
| genshi_xml               | 41.0 ms                                                     | 35.2 ms: 1.17x faster                                                   |
| docutils                 | 1.92 sec                                                    | 1.65 sec: 1.16x faster                                                  |
| django_template          | 28.9 ms                                                     | 25.0 ms: 1.16x faster                                                   |
| sympy_str                | 194 ms                                                      | 170 ms: 1.15x faster                                                    |
| xml_etree_generate       | 55.5 ms                                                     | 49.2 ms: 1.13x faster                                                   |
| nqueens                  | 66.6 ms                                                     | 59.0 ms: 1.13x faster                                                   |
| 2to3                     | 246 ms                                                      | 218 ms: 1.13x faster                                                    |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                    |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                                   |
| fannkuch                 | 256 ms                                                      | 232 ms: 1.10x faster                                                    |
| xml_etree_parse          | 96.8 ms                                                     | 88.5 ms: 1.09x faster                                                   |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                   |
| sympy_expand             | 314 ms                                                      | 291 ms: 1.08x faster                                                    |
| meteor_contest           | 75.9 ms                                                     | 70.8 ms: 1.07x faster                                                   |
| json                     | 3.14 ms                                                     | 2.93 ms: 1.07x faster                                                   |
| logging_format           | 6.76 us                                                     | 6.58 us: 1.03x faster                                                   |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                    |
| regex_effbot             | 1.66 ms                                                     | 1.62 ms: 1.02x faster                                                   |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.6 ms: 1.02x faster                                                   |
| logging_simple           | 6.22 us                                                     | 6.16 us: 1.01x faster                                                   |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.03x slower                                                   |
| telco                    | 3.94 ms                                                     | 4.37 ms: 1.11x slower                                                   |
| async_generators         | 222 ms                                                      | 248 ms: 1.12x slower                                                    |
| python_startup_no_site   | 15.5 ms                                                     | 19.3 ms: 1.24x slower                                                   |
| python_startup           | 20.6 ms                                                     | 25.9 ms: 1.26x slower                                                   |
| coverage                 | 39.0 ms                                                     | 49.3 ms: 1.26x slower                                                   |
| gc_traversal             | 1.41 ms                                                     | 2.13 ms: 1.51x slower                                                   |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.65x slower                                                   |
| Geometric mean           | (ref)                                                       | 1.32x faster                                                            |
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250707-3.15.0a0-aa2b0df-JIT/bm-20250707-pythonperf1-amd64-brandtbucher-jit_targets-3.15.0a0-aa2b0df.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.315x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown