# Results vs. 3.10.4

- fork: python
- ref: a3990df6121880e8c678
- machine: windows-amd64
- commit hash: a3990df
- commit date: 2025-03-08
- overall geometric mean: 1.192x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 230 ms: 1.07x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.76 sec: 1.09x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.5 ms: 1.29x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 404 ms: 2.74x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 209 ms: 2.51x faster                                                        |
| async_tree_none         | 435 ms                                                      | 180 ms: 2.42x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 361 ms: 1.77x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 47.4 ms: 1.30x faster                                                       |
| nbody          | 71.3 ms                                                     | 64.4 ms: 1.11x faster                                                       |
| pidigits       | 149 ms                                                      | 156 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 86.7 ms: 1.22x faster                                                       |
| regex_dna      | 136 ms                                                      | 130 ms: 1.05x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 17.0 ms: 1.10x slower                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.88 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 148 us: 1.24x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 219 us: 1.23x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                      |
| json_dumps           | 9.16 ms                                                     | 7.80 ms: 1.17x faster                                                       |
| pickle_dict          | 17.2 us                                                     | 15.4 us: 1.11x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.53 us: 1.07x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 46.4 ms: 1.04x slower                                                       |
| unpickle             | 9.09 us                                                     | 9.50 us: 1.05x slower                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 103 ms: 1.06x slower                                                        |
| pickle_list          | 2.75 us                                                     | 2.95 us: 1.07x slower                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 70.6 ms: 1.09x slower                                                       |
| pickle               | 6.85 us                                                     | 7.68 us: 1.12x slower                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 66.7 ms: 1.20x slower                                                       |
| json_loads           | 14.0 us                                                     | 19.9 us: 1.42x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 27.3 ms: 1.32x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 21.3 ms: 1.37x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.35x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 14.8 ms: 1.34x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 32.3 ms: 1.27x faster                                                       |
| django_template | 28.9 ms                                                     | 24.7 ms: 1.17x faster                                                       |
| mako            | 9.03 ms                                                     | 8.33 ms: 1.08x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.21x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.04x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 404 ms: 2.74x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 209 ms: 2.51x faster                                                        |
| async_tree_none          | 435 ms                                                      | 180 ms: 2.42x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 31.9 ms: 2.37x faster                                                       |
| deltablue                | 4.19 ms                                                     | 1.94 ms: 2.15x faster                                                       |
| generators               | 32.4 ms                                                     | 16.9 ms: 1.91x faster                                                       |
| go                       | 139 ms                                                      | 76.7 ms: 1.81x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 361 ms: 1.77x faster                                                        |
| pylint                   | 350 ms                                                      | 207 ms: 1.70x faster                                                        |
| raytrace                 | 273 ms                                                      | 177 ms: 1.55x faster                                                        |
| unpack_sequence          | 39.6 ns                                                     | 25.6 ns: 1.55x faster                                                       |
| richards_super           | 52.2 ms                                                     | 34.4 ms: 1.52x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 63.3 ns: 1.49x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.8 ms: 1.48x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.46 sec: 1.44x faster                                                      |
| sqlglot_parse            | 1.22 ms                                                     | 844 us: 1.44x faster                                                        |
| deepcopy_memo            | 28.8 us                                                     | 20.1 us: 1.43x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.7 us: 1.41x faster                                                       |
| deepcopy                 | 255 us                                                      | 182 us: 1.41x faster                                                        |
| richards                 | 42.4 ms                                                     | 30.4 ms: 1.40x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 41.0 ms: 1.40x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.06 ms: 1.39x faster                                                       |
| scimark_sor              | 106 ms                                                      | 76.4 ms: 1.39x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 527 ms: 1.39x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 4.20 ms: 1.37x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 14.8 ms: 1.34x faster                                                       |
| pyflate                  | 409 ms                                                      | 306 ms: 1.34x faster                                                        |
| float                    | 61.7 ms                                                     | 47.4 ms: 1.30x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.5 ms: 1.29x faster                                                       |
| pycparser                | 930 ms                                                      | 725 ms: 1.28x faster                                                        |
| genshi_xml               | 41.0 ms                                                     | 32.3 ms: 1.27x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 67.8 ms: 1.27x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 148 us: 1.24x faster                                                        |
| pickle_pure_python       | 270 us                                                      | 219 us: 1.23x faster                                                        |
| regex_compile            | 106 ms                                                      | 86.7 ms: 1.22x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 42.4 ms: 1.19x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 65.4 ms: 1.18x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 53.0 ms: 1.18x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 7.80 ms: 1.17x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.63 us: 1.17x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.7 ms: 1.17x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.8 ms: 1.16x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.92 us: 1.15x faster                                                       |
| sympy_sum                | 107 ms                                                      | 93.6 ms: 1.14x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.07 sec: 1.14x faster                                                      |
| thrift                   | 617 us                                                      | 551 us: 1.12x faster                                                        |
| pprint_safe_repr         | 592 ms                                                      | 531 ms: 1.12x faster                                                        |
| pickle_dict              | 17.2 us                                                     | 15.4 us: 1.11x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.8 ms: 1.11x faster                                                       |
| nbody                    | 71.3 ms                                                     | 64.4 ms: 1.11x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 36.0 ms: 1.11x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.76 sec: 1.09x faster                                                      |
| mako                     | 9.03 ms                                                     | 8.33 ms: 1.08x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.64 sec: 1.08x faster                                                      |
| unpickle_list            | 2.71 us                                                     | 2.53 us: 1.07x faster                                                       |
| sympy_str                | 194 ms                                                      | 182 ms: 1.07x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 895 us: 1.07x faster                                                        |
| 2to3                     | 246 ms                                                      | 230 ms: 1.07x faster                                                        |
| sqlglot_normalize        | 205 ms                                                      | 193 ms: 1.06x faster                                                        |
| regex_dna                | 136 ms                                                      | 130 ms: 1.05x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.61 ms: 1.05x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 64.5 ms: 1.03x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 74.8 ms: 1.02x faster                                                       |
| sympy_expand             | 314 ms                                                      | 311 ms: 1.01x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.88 us: 1.02x slower                                                       |
| scimark_fft              | 187 ms                                                      | 192 ms: 1.03x slower                                                        |
| async_generators         | 222 ms                                                      | 228 ms: 1.03x slower                                                        |
| logging_simple           | 6.22 us                                                     | 6.42 us: 1.03x slower                                                       |
| pidigits                 | 149 ms                                                      | 156 ms: 1.04x slower                                                        |
| xml_etree_process        | 44.5 ms                                                     | 46.4 ms: 1.04x slower                                                       |
| unpickle                 | 9.09 us                                                     | 9.50 us: 1.05x slower                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 103 ms: 1.06x slower                                                        |
| pickle_list              | 2.75 us                                                     | 2.95 us: 1.07x slower                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 70.6 ms: 1.09x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 17.0 ms: 1.10x slower                                                       |
| fannkuch                 | 256 ms                                                      | 281 ms: 1.10x slower                                                        |
| pickle                   | 6.85 us                                                     | 7.68 us: 1.12x slower                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.88 ms: 1.13x slower                                                       |
| json                     | 3.14 ms                                                     | 3.73 ms: 1.19x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 66.7 ms: 1.20x slower                                                       |
| python_startup           | 20.6 ms                                                     | 27.3 ms: 1.32x slower                                                       |
| telco                    | 3.94 ms                                                     | 5.33 ms: 1.35x slower                                                       |
| coverage                 | 39.0 ms                                                     | 53.2 ms: 1.36x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 21.3 ms: 1.37x slower                                                       |
| json_loads               | 14.0 us                                                     | 19.9 us: 1.42x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 92.6 ms: 1.49x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.37 ms: 1.71x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.61 ms: 1.85x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                                |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250308-3.14.0a5+-a3990df-CLANG/bm-20250308-pythonperf1-amd64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.192x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown