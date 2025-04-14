# Results vs. 3.10.4

- fork: python
- ref: f33d21e24fdb05da7512
- machine: windows-amd64
- commit hash: f33d21e
- commit date: 2025-03-05
- overall geometric mean: 1.212x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 225 ms: 1.09x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.0 ms: 1.28x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 421 ms: 2.63x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 220 ms: 2.39x faster                                                        |
| async_tree_none         | 435 ms                                                      | 187 ms: 2.33x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 345 ms: 1.85x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.28x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 47.2 ms: 1.31x faster                                                       |
| pidigits       | 149 ms                                                      | 151 ms: 1.01x slower                                                        |
| nbody          | 71.3 ms                                                     | 73.4 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 136 ms                                                      | 113 ms: 1.20x faster                                                        |
| regex_compile  | 106 ms                                                      | 88.9 ms: 1.19x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.41 ms: 1.18x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.81 ms: 1.35x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 152 us: 1.20x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 229 us: 1.18x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.44 sec: 1.16x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 40.7 ms: 1.09x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 91.0 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.8 ms: 1.02x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.6 us: 1.04x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 58.0 ms: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.1 ms: 1.22x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 19.0 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.96 ms: 1.30x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.5 ms: 1.20x faster                                                       |
| django_template | 28.9 ms                                                     | 24.9 ms: 1.16x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 36.2 ms: 1.13x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 108 us: 3.12x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 421 ms: 2.63x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 220 ms: 2.39x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.0 ms: 2.36x faster                                                       |
| async_tree_none          | 435 ms                                                      | 187 ms: 2.33x faster                                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 345 ms: 1.85x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.29 ms: 1.83x faster                                                       |
| pylint                   | 350 ms                                                      | 200 ms: 1.75x faster                                                        |
| generators               | 32.4 ms                                                     | 19.7 ms: 1.65x faster                                                       |
| go                       | 139 ms                                                      | 88.6 ms: 1.57x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 61.9 ns: 1.53x faster                                                       |
| richards_super           | 52.2 ms                                                     | 35.3 ms: 1.48x faster                                                       |
| chaos                    | 61.7 ms                                                     | 43.0 ms: 1.43x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.6 us: 1.42x faster                                                       |
| raytrace                 | 273 ms                                                      | 195 ms: 1.40x faster                                                        |
| richards                 | 42.4 ms                                                     | 30.7 ms: 1.38x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 21.0 us: 1.37x faster                                                       |
| deepcopy                 | 255 us                                                      | 187 us: 1.36x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 891 us: 1.36x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.81 ms: 1.35x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.11 ms: 1.33x faster                                                       |
| float                    | 61.7 ms                                                     | 47.2 ms: 1.31x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.96 ms: 1.30x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.48 ms: 1.28x faster                                                       |
| pyflate                  | 409 ms                                                      | 320 ms: 1.28x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 40.0 ms: 1.28x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 67.7 ms: 1.27x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 61.5 ms: 1.26x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 49.9 ms: 1.25x faster                                                       |
| pycparser                | 930 ms                                                      | 746 ms: 1.25x faster                                                        |
| regex_dna                | 136 ms                                                      | 113 ms: 1.20x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.20x faster                                                       |
| thrift                   | 617 us                                                      | 513 us: 1.20x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 152 us: 1.20x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 16.5 ms: 1.20x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 47.8 ms: 1.20x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.49 sec: 1.20x faster                                                      |
| regex_compile            | 106 ms                                                      | 88.9 ms: 1.19x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.5 ms: 1.19x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.1 ms: 1.19x faster                                                       |
| scimark_sor              | 106 ms                                                      | 89.9 ms: 1.18x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.41 ms: 1.18x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 229 us: 1.18x faster                                                        |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.9 ms: 1.16x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.44 sec: 1.16x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.68 sec: 1.14x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.93 us: 1.14x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.2 ms: 1.13x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 850 us: 1.13x faster                                                        |
| sqlglot_optimize         | 39.8 ms                                                     | 35.7 ms: 1.11x faster                                                       |
| sympy_str                | 194 ms                                                      | 176 ms: 1.11x faster                                                        |
| 2to3                     | 246 ms                                                      | 225 ms: 1.09x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 40.7 ms: 1.09x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 91.0 ms: 1.06x faster                                                       |
| json                     | 3.14 ms                                                     | 2.95 ms: 1.06x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 194 ms: 1.06x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 1.16 sec: 1.05x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 63.2 ms: 1.05x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                                       |
| sympy_expand             | 314 ms                                                      | 300 ms: 1.05x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.64 ms: 1.03x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 577 ms: 1.03x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.8 ms: 1.02x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 76.5 ms: 1.01x slower                                                       |
| pidigits                 | 149 ms                                                      | 151 ms: 1.01x slower                                                        |
| async_generators         | 222 ms                                                      | 226 ms: 1.02x slower                                                        |
| scimark_fft              | 187 ms                                                      | 192 ms: 1.03x slower                                                        |
| nbody                    | 71.3 ms                                                     | 73.4 ms: 1.03x slower                                                       |
| logging_format           | 6.76 us                                                     | 6.98 us: 1.03x slower                                                       |
| logging_simple           | 6.22 us                                                     | 6.47 us: 1.04x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.6 us: 1.04x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 58.0 ms: 1.04x slower                                                       |
| fannkuch                 | 256 ms                                                      | 286 ms: 1.12x slower                                                        |
| telco                    | 3.94 ms                                                     | 4.78 ms: 1.21x slower                                                       |
| python_startup           | 20.6 ms                                                     | 25.1 ms: 1.22x slower                                                       |
| coverage                 | 39.0 ms                                                     | 47.7 ms: 1.22x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.0 ms: 1.23x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 86.6 ms: 1.40x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.03 ms: 1.44x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.23 ms: 1.54x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250305-3.14.0a5+-f33d21e/bm-20250305-pythonperf1-amd64-python-f33d21e24fdb05da7512-3.14.0a5+-f33d21e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.212x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown