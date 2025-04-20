# Results vs. 3.10.4

- fork: python
- ref: 71da68d5887b6c058907
- machine: windows-amd64
- commit hash: 71da68d
- commit date: 2025-04-19
- overall geometric mean: 1.507x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 204 ms: 1.21x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.54 sec: 1.25x faster                                                      |
| html5lib       | 51.0 ms                                                     | 34.3 ms: 1.49x faster                                                       |
| Geometric mean | (ref)                                                       | 1.31x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 344 ms: 3.23x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 184 ms: 2.85x faster                                                        |
| async_tree_none         | 435 ms                                                      | 155 ms: 2.80x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 310 ms: 2.06x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.70x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 36.0 ms: 1.71x faster                                                       |
| nbody          | 71.3 ms                                                     | 55.2 ms: 1.29x faster                                                       |
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                       | 1.31x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 67.1 ms: 1.58x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.0 ms: 1.18x faster                                                       |
| regex_dna      | 136 ms                                                      | 119 ms: 1.14x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 103 us: 1.78x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 162 us: 1.66x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 5.55 ms: 1.65x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.02 sec: 1.63x faster                                                      |
| pickle_dict          | 17.2 us                                                     | 11.8 us: 1.46x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 32.8 ms: 1.35x faster                                                       |
| pickle_list          | 2.75 us                                                     | 2.05 us: 1.34x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.05 us: 1.33x faster                                                       |
| unpickle             | 9.09 us                                                     | 7.46 us: 1.22x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 47.7 ms: 1.16x faster                                                       |
| pickle               | 6.85 us                                                     | 6.06 us: 1.13x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 90.1 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.0 ms: 1.07x faster                                                       |
| json_loads           | 14.0 us                                                     | 13.8 us: 1.02x faster                                                       |
| Geometric mean       | (ref)                                                       | 1.33x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.7 ms: 1.30x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 21.0 ms: 1.35x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 11.3 ms: 1.76x faster                                                       |
| mako            | 9.03 ms                                                     | 5.81 ms: 1.55x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 27.3 ms: 1.50x faster                                                       |
| django_template | 28.9 ms                                                     | 19.6 ms: 1.47x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.57x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 87.3 us: 3.85x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 344 ms: 3.23x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 184 ms: 2.85x faster                                                        |
| async_tree_none          | 435 ms                                                      | 155 ms: 2.80x faster                                                        |
| deltablue                | 4.19 ms                                                     | 1.54 ms: 2.72x faster                                                       |
| mdp                      | 1.78 sec                                                    | 668 ms: 2.67x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 31.1 ms: 2.44x faster                                                       |
| go                       | 139 ms                                                      | 58.0 ms: 2.39x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 41.4 ns: 2.28x faster                                                       |
| scimark_sor              | 106 ms                                                      | 48.4 ms: 2.19x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 13.1 us: 2.19x faster                                                       |
| generators               | 32.4 ms                                                     | 15.0 ms: 2.16x faster                                                       |
| richards_super           | 52.2 ms                                                     | 24.3 ms: 2.15x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 27.0 ms: 2.12x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 310 ms: 2.06x faster                                                        |
| chaos                    | 61.7 ms                                                     | 30.2 ms: 2.04x faster                                                       |
| comprehensions           | 16.5 us                                                     | 8.17 us: 2.02x faster                                                       |
| richards                 | 42.4 ms                                                     | 21.3 ms: 2.00x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 2.88 ms: 1.99x faster                                                       |
| raytrace                 | 273 ms                                                      | 138 ms: 1.98x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 44.8 ms: 1.92x faster                                                       |
| pylint                   | 350 ms                                                      | 186 ms: 1.89x faster                                                        |
| deepcopy                 | 255 us                                                      | 136 us: 1.88x faster                                                        |
| pyflate                  | 409 ms                                                      | 229 ms: 1.79x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 103 us: 1.78x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 11.3 ms: 1.76x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 424 ms: 1.73x faster                                                        |
| float                    | 61.7 ms                                                     | 36.0 ms: 1.71x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 46.3 ms: 1.67x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 162 us: 1.66x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 5.55 ms: 1.65x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.02 sec: 1.63x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 39.0 ms: 1.60x faster                                                       |
| regex_compile            | 106 ms                                                      | 67.1 ms: 1.58x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.34 sec: 1.58x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 783 ms: 1.56x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.81 ms: 1.55x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 388 ms: 1.52x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.46 us: 1.51x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 27.3 ms: 1.50x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 34.3 ms: 1.49x faster                                                       |
| django_template          | 28.9 ms                                                     | 19.6 ms: 1.47x faster                                                       |
| coroutines               | 16.0 ms                                                     | 10.9 ms: 1.47x faster                                                       |
| pickle_dict              | 17.2 us                                                     | 11.8 us: 1.46x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 45.8 ms: 1.46x faster                                                       |
| pycparser                | 930 ms                                                      | 653 ms: 1.42x faster                                                        |
| sympy_sum                | 107 ms                                                      | 77.0 ms: 1.39x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 28.6 ns: 1.39x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 11.1 ms: 1.38x faster                                                       |
| scimark_fft              | 187 ms                                                      | 138 ms: 1.36x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 32.8 ms: 1.35x faster                                                       |
| pickle_list              | 2.75 us                                                     | 2.05 us: 1.34x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 37.8 ms: 1.33x faster                                                       |
| sympy_str                | 194 ms                                                      | 146 ms: 1.33x faster                                                        |
| unpickle_list            | 2.71 us                                                     | 2.05 us: 1.33x faster                                                       |
| nbody                    | 71.3 ms                                                     | 55.2 ms: 1.29x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.48 us: 1.29x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.14 ms: 1.27x faster                                                       |
| sympy_expand             | 314 ms                                                      | 251 ms: 1.25x faster                                                        |
| fannkuch                 | 256 ms                                                      | 205 ms: 1.25x faster                                                        |
| docutils                 | 1.92 sec                                                    | 1.54 sec: 1.25x faster                                                      |
| async_generators         | 222 ms                                                      | 182 ms: 1.22x faster                                                        |
| unpickle                 | 9.09 us                                                     | 7.46 us: 1.22x faster                                                       |
| 2to3                     | 246 ms                                                      | 204 ms: 1.21x faster                                                        |
| regex_v8                 | 15.4 ms                                                     | 13.0 ms: 1.18x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 47.7 ms: 1.16x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 65.5 ms: 1.16x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 834 us: 1.15x faster                                                        |
| regex_dna                | 136 ms                                                      | 119 ms: 1.14x faster                                                        |
| logging_format           | 6.76 us                                                     | 5.95 us: 1.14x faster                                                       |
| pickle                   | 6.85 us                                                     | 6.06 us: 1.13x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.51 us: 1.13x faster                                                       |
| json                     | 3.14 ms                                                     | 2.90 ms: 1.08x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 90.1 ms: 1.08x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.0 ms: 1.07x faster                                                       |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                        |
| json_loads               | 14.0 us                                                     | 13.8 us: 1.02x faster                                                       |
| telco                    | 3.94 ms                                                     | 3.96 ms: 1.01x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.7 ms: 1.30x slower                                                       |
| coverage                 | 39.0 ms                                                     | 51.9 ms: 1.33x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 21.0 ms: 1.35x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.8 ms: 1.43x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.38 ms: 1.72x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.71 ms: 1.92x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.48x faster                                                                |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (16) of results/bm-20250419-3.14.0a7+-71da68d-CLANG/bm-20250419-pythonperf1-amd64-python-71da68d5887b6c058907-3.14.0a7+-71da68d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.507x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.41x
- 95% likely to have a speedup of 1.40x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: unknown