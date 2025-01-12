# Results vs. 3.10.4

- fork: python
- ref: 22a442181d5f1ac496da
- machine: windows-amd64
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.261x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 225 ms: 1.09x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.74 sec: 1.10x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.3 ms: 1.30x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 405 ms: 2.73x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 224 ms: 2.35x faster                                                        |
| async_tree_none         | 435 ms                                                      | 187 ms: 2.33x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 351 ms: 1.81x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.28x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 39.3 ms: 1.57x faster                                                       |
| nbody          | 71.3 ms                                                     | 53.9 ms: 1.32x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.28x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.5 ms: 1.33x faster                                                       |
| regex_dna      | 136 ms                                                      | 116 ms: 1.17x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 108 us: 1.70x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 6.28 ms: 1.46x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.19 sec: 1.41x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 208 us: 1.29x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 88.5 ms: 1.09x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 51.2 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.4 ms: 1.08x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.85 us: 1.03x faster                                                       |
| json_loads           | 14.0 us                                                     | 14.3 us: 1.02x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 18.3 us: 1.06x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.01 us: 1.09x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 3.02 us: 1.11x slower                                                       |
| pickle               | 6.85 us                                                     | 7.97 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.3 ms: 1.11x slower                                                       |
| python_startup         | 20.6 ms                                                     | 23.6 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.08 ms: 1.78x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 18.3 ms: 1.08x faster                                                       |
| django_template | 28.9 ms                                                     | 27.5 ms: 1.05x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 46.0 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.16x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.95x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 405 ms: 2.73x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 224 ms: 2.35x faster                                                        |
| async_tree_none          | 435 ms                                                      | 187 ms: 2.33x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.28 ms: 1.84x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 351 ms: 1.81x faster                                                        |
| mako                     | 9.03 ms                                                     | 5.08 ms: 1.78x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 16.3 us: 1.76x faster                                                       |
| scimark_sor              | 106 ms                                                      | 61.3 ms: 1.73x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 108 us: 1.70x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 57.0 ns: 1.66x faster                                                       |
| pylint                   | 350 ms                                                      | 211 ms: 1.66x faster                                                        |
| scimark_lu               | 85.8 ms                                                     | 53.0 ms: 1.62x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 36.4 ms: 1.57x faster                                                       |
| float                    | 61.7 ms                                                     | 39.3 ms: 1.57x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 49.8 ms: 1.55x faster                                                       |
| go                       | 139 ms                                                      | 89.8 ms: 1.55x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.37 sec: 1.55x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 41.2 ms: 1.52x faster                                                       |
| chaos                    | 61.7 ms                                                     | 41.0 ms: 1.51x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 820 us: 1.48x faster                                                        |
| pyflate                  | 409 ms                                                      | 276 ms: 1.48x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 6.28 ms: 1.46x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.6 us: 1.42x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.19 sec: 1.41x faster                                                      |
| sqlglot_transpile        | 1.48 ms                                                     | 1.06 ms: 1.39x faster                                                       |
| richards_super           | 52.2 ms                                                     | 37.9 ms: 1.38x faster                                                       |
| generators               | 32.4 ms                                                     | 23.7 ms: 1.37x faster                                                       |
| raytrace                 | 273 ms                                                      | 200 ms: 1.36x faster                                                        |
| asyncio_tcp              | 732 ms                                                      | 537 ms: 1.36x faster                                                        |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.04 ms: 1.34x faster                                                       |
| regex_compile            | 106 ms                                                      | 79.5 ms: 1.33x faster                                                       |
| nbody                    | 71.3 ms                                                     | 53.9 ms: 1.32x faster                                                       |
| scimark_fft              | 187 ms                                                      | 143 ms: 1.31x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 39.3 ms: 1.30x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 208 us: 1.29x faster                                                        |
| pprint_pformat           | 1.22 sec                                                    | 948 ms: 1.29x faster                                                        |
| pycparser                | 930 ms                                                      | 734 ms: 1.27x faster                                                        |
| richards                 | 42.4 ms                                                     | 33.6 ms: 1.26x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 40.6 ms: 1.24x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 476 ms: 1.24x faster                                                        |
| xml_etree_process        | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.57 us: 1.22x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.83 us: 1.20x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.49 sec: 1.20x faster                                                      |
| sympy_sum                | 107 ms                                                      | 90.5 ms: 1.18x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.18x faster                                                       |
| regex_dna                | 136 ms                                                      | 116 ms: 1.17x faster                                                        |
| thrift                   | 617 us                                                      | 529 us: 1.17x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 5.00 ms: 1.15x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 844 us: 1.13x faster                                                        |
| sympy_str                | 194 ms                                                      | 174 ms: 1.12x faster                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.74 sec: 1.10x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 88.5 ms: 1.09x faster                                                       |
| 2to3                     | 246 ms                                                      | 225 ms: 1.09x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 18.3 ms: 1.08x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 51.2 ms: 1.08x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.4 ms: 1.08x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 37.1 ms: 1.07x faster                                                       |
| sympy_expand             | 314 ms                                                      | 297 ms: 1.06x faster                                                        |
| json                     | 3.14 ms                                                     | 2.98 ms: 1.05x faster                                                       |
| django_template          | 28.9 ms                                                     | 27.5 ms: 1.05x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 63.5 ms: 1.05x faster                                                       |
| fannkuch                 | 256 ms                                                      | 247 ms: 1.04x faster                                                        |
| unpickle                 | 9.09 us                                                     | 8.85 us: 1.03x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                                       |
| meteor_contest           | 75.9 ms                                                     | 74.2 ms: 1.02x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.62 us: 1.02x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 202 ms: 1.02x faster                                                        |
| pidigits                 | 149 ms                                                      | 147 ms: 1.02x faster                                                        |
| json_loads               | 14.0 us                                                     | 14.3 us: 1.02x slower                                                       |
| unpack_sequence          | 39.6 ns                                                     | 41.5 ns: 1.05x slower                                                       |
| pathlib                  | 75.7 ms                                                     | 79.9 ms: 1.06x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 18.3 us: 1.06x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.01 us: 1.09x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.35 ms: 1.10x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 3.02 us: 1.11x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.3 ms: 1.11x slower                                                       |
| genshi_xml               | 41.0 ms                                                     | 46.0 ms: 1.12x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.6 ms: 1.15x slower                                                       |
| pickle                   | 6.85 us                                                     | 7.97 us: 1.16x slower                                                       |
| async_generators         | 222 ms                                                      | 261 ms: 1.18x slower                                                        |
| coverage                 | 39.0 ms                                                     | 47.7 ms: 1.22x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 83.5 ms: 1.35x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.00 ms: 1.42x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.53x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                                |

Benchmark hidden because not significant (1): logging_simple
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.261x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown