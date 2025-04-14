# Results vs. 3.10.4

- fork: python
- ref: 718d234e4086a65d78c8
- machine: windows-amd64
- commit hash: 718d234
- commit date: 2025-04-12
- overall geometric mean: 1.513x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.37x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 202 ms: 1.22x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.54 sec: 1.25x faster                                                      |
| html5lib       | 51.0 ms                                                     | 34.1 ms: 1.50x faster                                                       |
| Geometric mean | (ref)                                                       | 1.32x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 339 ms: 3.27x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 184 ms: 2.86x faster                                                        |
| async_tree_none         | 435 ms                                                      | 155 ms: 2.82x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 308 ms: 2.07x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.72x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 36.1 ms: 1.71x faster                                                       |
| nbody          | 71.3 ms                                                     | 51.5 ms: 1.38x faster                                                       |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.34x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 66.8 ms: 1.59x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 13.5 ms: 1.15x faster                                                       |
| regex_dna      | 136 ms                                                      | 121 ms: 1.12x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 104 us: 1.76x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.01 sec: 1.65x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 165 us: 1.64x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 5.78 ms: 1.58x faster                                                       |
| pickle_dict          | 17.2 us                                                     | 12.1 us: 1.42x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 32.7 ms: 1.36x faster                                                       |
| unpickle_list        | 2.71 us                                                     | 2.04 us: 1.33x faster                                                       |
| pickle_list          | 2.75 us                                                     | 2.10 us: 1.31x faster                                                       |
| unpickle             | 9.09 us                                                     | 7.26 us: 1.25x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 47.6 ms: 1.17x faster                                                       |
| pickle               | 6.85 us                                                     | 6.18 us: 1.11x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 90.0 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.6 ms: 1.05x faster                                                       |
| json_loads           | 14.0 us                                                     | 13.6 us: 1.03x faster                                                       |
| Geometric mean       | (ref)                                                       | 1.32x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.8 ms: 1.30x slower                                                       |
| python_startup_no_site | 15.5 ms                                                     | 20.8 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 11.2 ms: 1.77x faster                                                       |
| mako            | 9.03 ms                                                     | 5.75 ms: 1.57x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 26.9 ms: 1.53x faster                                                       |
| django_template | 28.9 ms                                                     | 19.5 ms: 1.48x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.58x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 86.6 us: 3.88x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 339 ms: 3.27x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 184 ms: 2.86x faster                                                        |
| async_tree_none          | 435 ms                                                      | 155 ms: 2.82x faster                                                        |
| deltablue                | 4.19 ms                                                     | 1.55 ms: 2.71x faster                                                       |
| mdp                      | 1.78 sec                                                    | 667 ms: 2.67x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 30.7 ms: 2.46x faster                                                       |
| go                       | 139 ms                                                      | 58.5 ms: 2.38x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 42.4 ns: 2.23x faster                                                       |
| scimark_sor              | 106 ms                                                      | 47.7 ms: 2.23x faster                                                       |
| richards_super           | 52.2 ms                                                     | 24.1 ms: 2.17x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 13.3 us: 2.16x faster                                                       |
| generators               | 32.4 ms                                                     | 15.1 ms: 2.14x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 27.3 ms: 2.10x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 308 ms: 2.07x faster                                                        |
| chaos                    | 61.7 ms                                                     | 30.2 ms: 2.05x faster                                                       |
| richards                 | 42.4 ms                                                     | 20.8 ms: 2.04x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 2.85 ms: 2.01x faster                                                       |
| comprehensions           | 16.5 us                                                     | 8.30 us: 1.99x faster                                                       |
| raytrace                 | 273 ms                                                      | 139 ms: 1.96x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 45.0 ms: 1.90x faster                                                       |
| pylint                   | 350 ms                                                      | 186 ms: 1.89x faster                                                        |
| deepcopy                 | 255 us                                                      | 136 us: 1.88x faster                                                        |
| pyflate                  | 409 ms                                                      | 231 ms: 1.77x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 11.2 ms: 1.77x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 104 us: 1.76x faster                                                        |
| float                    | 61.7 ms                                                     | 36.1 ms: 1.71x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 435 ms: 1.68x faster                                                        |
| spectral_norm            | 77.3 ms                                                     | 46.5 ms: 1.66x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.01 sec: 1.65x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 165 us: 1.64x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 38.9 ms: 1.61x faster                                                       |
| regex_compile            | 106 ms                                                      | 66.8 ms: 1.59x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.78 ms: 1.58x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 770 ms: 1.58x faster                                                        |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.34 sec: 1.58x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 375 ms: 1.58x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.75 ms: 1.57x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 26.9 ms: 1.53x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.46 us: 1.51x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 34.1 ms: 1.50x faster                                                       |
| django_template          | 28.9 ms                                                     | 19.5 ms: 1.48x faster                                                       |
| coroutines               | 16.0 ms                                                     | 10.9 ms: 1.47x faster                                                       |
| pycparser                | 930 ms                                                      | 648 ms: 1.44x faster                                                        |
| pickle_dict              | 17.2 us                                                     | 12.1 us: 1.42x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 46.9 ms: 1.42x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 11.0 ms: 1.38x faster                                                       |
| nbody                    | 71.3 ms                                                     | 51.5 ms: 1.38x faster                                                       |
| sympy_sum                | 107 ms                                                      | 77.7 ms: 1.38x faster                                                       |
| scimark_fft              | 187 ms                                                      | 137 ms: 1.37x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 32.7 ms: 1.36x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 29.2 ns: 1.36x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 37.3 ms: 1.35x faster                                                       |
| fannkuch                 | 256 ms                                                      | 190 ms: 1.35x faster                                                        |
| unpickle_list            | 2.71 us                                                     | 2.04 us: 1.33x faster                                                       |
| sympy_str                | 194 ms                                                      | 147 ms: 1.32x faster                                                        |
| pickle_list              | 2.75 us                                                     | 2.10 us: 1.31x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.49 us: 1.29x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.14 ms: 1.27x faster                                                       |
| sympy_expand             | 314 ms                                                      | 250 ms: 1.26x faster                                                        |
| unpickle                 | 9.09 us                                                     | 7.26 us: 1.25x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.54 sec: 1.25x faster                                                      |
| 2to3                     | 246 ms                                                      | 202 ms: 1.22x faster                                                        |
| async_generators         | 222 ms                                                      | 184 ms: 1.21x faster                                                        |
| xml_etree_generate       | 55.5 ms                                                     | 47.6 ms: 1.17x faster                                                       |
| logging_simple           | 6.22 us                                                     | 5.41 us: 1.15x faster                                                       |
| logging_format           | 6.76 us                                                     | 5.89 us: 1.15x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 13.5 ms: 1.15x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 842 us: 1.14x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 67.0 ms: 1.13x faster                                                       |
| regex_dna                | 136 ms                                                      | 121 ms: 1.12x faster                                                        |
| json                     | 3.14 ms                                                     | 2.81 ms: 1.12x faster                                                       |
| pickle                   | 6.85 us                                                     | 6.18 us: 1.11x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 90.0 ms: 1.08x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.6 ms: 1.05x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.03x faster                                                       |
| json_loads               | 14.0 us                                                     | 13.6 us: 1.03x faster                                                       |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                        |
| telco                    | 3.94 ms                                                     | 4.05 ms: 1.03x slower                                                       |
| coverage                 | 39.0 ms                                                     | 42.5 ms: 1.09x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.8 ms: 1.30x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 20.8 ms: 1.34x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 89.0 ms: 1.43x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.38 ms: 1.73x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.86 ms: 2.03x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.49x faster                                                                |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (16) of results/bm-20250412-3.14.0a7+-718d234-CLANG/bm-20250412-pythonperf1-amd64-python-718d234e4086a65d78c8-3.14.0a7+-718d234.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.513x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.41x
- 95% likely to have a speedup of 1.40x
- 99% likely to have a speedup of 1.37x

# Memory
- memory change: unknown