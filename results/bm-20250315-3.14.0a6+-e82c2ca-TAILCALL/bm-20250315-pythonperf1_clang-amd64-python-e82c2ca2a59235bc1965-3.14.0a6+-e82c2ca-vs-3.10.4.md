# Results vs. 3.10.4

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: windows-amd64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.406x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 206 ms: 1.19x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.56 sec: 1.23x faster                                                      |
| html5lib       | 51.0 ms                                                     | 36.5 ms: 1.40x faster                                                       |
| Geometric mean | (ref)                                                       | 1.27x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 357 ms: 3.10x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 192 ms: 2.74x faster                                                        |
| async_tree_none         | 435 ms                                                      | 161 ms: 2.71x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 315 ms: 2.03x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.61x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 42.4 ms: 1.45x faster                                                       |
| nbody          | 71.3 ms                                                     | 57.7 ms: 1.24x faster                                                       |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.22x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 74.6 ms: 1.42x faster                                                       |
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 13.4 ms: 1.16x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.78 ms: 1.59x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 116 us: 1.58x faster                                                        |
| pickle_dict          | 17.2 us                                                     | 11.8 us: 1.46x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 186 us: 1.45x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.22 sec: 1.37x faster                                                      |
| pickle_list          | 2.75 us                                                     | 2.07 us: 1.33x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.11 us: 1.29x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 35.2 ms: 1.26x faster                                                       |
| unpickle             | 9.09 us                                                     | 7.50 us: 1.21x faster                                                       |
| pickle               | 6.85 us                                                     | 6.10 us: 1.12x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 50.1 ms: 1.11x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 89.6 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.9 ms: 1.05x faster                                                       |
| json_loads           | 14.0 us                                                     | 13.8 us: 1.02x faster                                                       |
| Geometric mean       | (ref)                                                       | 1.27x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.5 ms: 1.29x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 20.9 ms: 1.35x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 12.9 ms: 1.53x faster                                                       |
| mako            | 9.03 ms                                                     | 6.14 ms: 1.47x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 29.5 ms: 1.39x faster                                                       |
| django_template | 28.9 ms                                                     | 21.3 ms: 1.36x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.44x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 89.7 us: 3.74x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 357 ms: 3.10x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 192 ms: 2.74x faster                                                        |
| async_tree_none          | 435 ms                                                      | 161 ms: 2.71x faster                                                        |
| deltablue                | 4.19 ms                                                     | 1.71 ms: 2.45x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 31.4 ms: 2.41x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 45.7 ns: 2.07x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 315 ms: 2.03x faster                                                        |
| go                       | 139 ms                                                      | 68.7 ms: 2.02x faster                                                       |
| richards_super           | 52.2 ms                                                     | 26.0 ms: 2.01x faster                                                       |
| generators               | 32.4 ms                                                     | 17.3 ms: 1.88x faster                                                       |
| raytrace                 | 273 ms                                                      | 146 ms: 1.87x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 46.0 ms: 1.86x faster                                                       |
| pylint                   | 350 ms                                                      | 189 ms: 1.85x faster                                                        |
| richards                 | 42.4 ms                                                     | 23.1 ms: 1.84x faster                                                       |
| chaos                    | 61.7 ms                                                     | 34.0 ms: 1.82x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 3.26 ms: 1.76x faster                                                       |
| scimark_sor              | 106 ms                                                      | 61.0 ms: 1.74x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 33.1 ms: 1.73x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.7 us: 1.72x faster                                                       |
| deepcopy                 | 255 us                                                      | 149 us: 1.72x faster                                                        |
| comprehensions           | 16.5 us                                                     | 9.62 us: 1.71x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 45.2 ms: 1.71x faster                                                       |
| pyflate                  | 409 ms                                                      | 255 ms: 1.60x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 5.78 ms: 1.59x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 116 us: 1.58x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 12.9 ms: 1.53x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 42.0 ms: 1.49x faster                                                       |
| mako                     | 9.03 ms                                                     | 6.14 ms: 1.47x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.44 sec: 1.46x faster                                                      |
| pickle_dict              | 17.2 us                                                     | 11.8 us: 1.46x faster                                                       |
| float                    | 61.7 ms                                                     | 42.4 ms: 1.45x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 186 us: 1.45x faster                                                        |
| regex_compile            | 106 ms                                                      | 74.6 ms: 1.42x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.55 us: 1.42x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 520 ms: 1.41x faster                                                        |
| pycparser                | 930 ms                                                      | 663 ms: 1.40x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 36.5 ms: 1.40x faster                                                       |
| coroutines               | 16.0 ms                                                     | 11.4 ms: 1.40x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 29.5 ms: 1.39x faster                                                       |
| thrift                   | 617 us                                                      | 447 us: 1.38x faster                                                        |
| tomli_loads              | 1.67 sec                                                    | 1.22 sec: 1.37x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 898 ms: 1.36x faster                                                        |
| django_template          | 28.9 ms                                                     | 21.3 ms: 1.36x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 442 ms: 1.34x faster                                                        |
| mdp                      | 1.78 sec                                                    | 1.33 sec: 1.34x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.04 ms: 1.34x faster                                                       |
| pickle_list              | 2.75 us                                                     | 2.07 us: 1.33x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 51.2 ms: 1.30x faster                                                       |
| sympy_sum                | 107 ms                                                      | 82.4 ms: 1.30x faster                                                       |
| unpickle_list            | 2.71 us                                                     | 2.11 us: 1.29x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 39.5 ms: 1.28x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.0 ms: 1.28x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 35.2 ms: 1.26x faster                                                       |
| sympy_str                | 194 ms                                                      | 156 ms: 1.24x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.54 us: 1.24x faster                                                       |
| scimark_fft              | 187 ms                                                      | 152 ms: 1.24x faster                                                        |
| nbody                    | 71.3 ms                                                     | 57.7 ms: 1.24x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.56 sec: 1.23x faster                                                      |
| unpickle                 | 9.09 us                                                     | 7.50 us: 1.21x faster                                                       |
| 2to3                     | 246 ms                                                      | 206 ms: 1.19x faster                                                        |
| sympy_expand             | 314 ms                                                      | 264 ms: 1.19x faster                                                        |
| async_generators         | 222 ms                                                      | 189 ms: 1.17x faster                                                        |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                        |
| regex_v8                 | 15.4 ms                                                     | 13.4 ms: 1.16x faster                                                       |
| json                     | 3.14 ms                                                     | 2.75 ms: 1.14x faster                                                       |
| logging_format           | 6.76 us                                                     | 5.95 us: 1.14x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 845 us: 1.13x faster                                                        |
| logging_simple           | 6.22 us                                                     | 5.53 us: 1.13x faster                                                       |
| pickle                   | 6.85 us                                                     | 6.10 us: 1.12x faster                                                       |
| fannkuch                 | 256 ms                                                      | 230 ms: 1.11x faster                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 50.1 ms: 1.11x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 89.6 ms: 1.08x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 70.4 ms: 1.08x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.55 ms: 1.07x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 37.7 ns: 1.05x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.9 ms: 1.05x faster                                                       |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                        |
| json_loads               | 14.0 us                                                     | 13.8 us: 1.02x faster                                                       |
| coverage                 | 39.0 ms                                                     | 41.7 ms: 1.07x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.35 ms: 1.10x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.5 ms: 1.29x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.9 ms: 1.35x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 88.8 ms: 1.43x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.34 ms: 1.68x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.68 ms: 1.90x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.38x faster                                                                |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250315-3.14.0a6+-e82c2ca-CLANG/bm-20250315-pythonperf1-amd64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.406x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: unknown