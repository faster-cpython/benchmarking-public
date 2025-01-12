# Results vs. 3.10.4

- fork: python
- ref: 22a442181d5f1ac496da
- machine: windows-amd64
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.221x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                      |
| html5lib       | 51.0 ms                                                     | 39.3 ms: 1.30x faster                                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 411 ms: 2.70x faster                                                        |
| async_tree_none         | 435 ms                                                      | 188 ms: 2.31x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 228 ms: 2.31x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 348 ms: 1.83x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.27x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 49.6 ms: 1.24x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| nbody          | 71.3 ms                                                     | 72.7 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 85.1 ms: 1.25x faster                                                       |
| regex_dna      | 136 ms                                                      | 112 ms: 1.21x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.42 ms: 1.17x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.5 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.63 ms: 1.38x faster                                                       |
| unpickle_pure_python | 183 us                                                      | 143 us: 1.28x faster                                                        |
| pickle_pure_python   | 270 us                                                      | 219 us: 1.23x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 39.8 ms: 1.12x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 89.5 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.4 ms: 1.06x faster                                                       |
| unpickle             | 9.09 us                                                     | 8.72 us: 1.04x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 56.5 ms: 1.02x slower                                                       |
| json_loads           | 14.0 us                                                     | 14.7 us: 1.05x slower                                                       |
| unpickle_list        | 2.71 us                                                     | 2.94 us: 1.08x slower                                                       |
| pickle               | 6.85 us                                                     | 8.13 us: 1.19x slower                                                       |
| pickle_dict          | 17.2 us                                                     | 20.6 us: 1.20x slower                                                       |
| pickle_list          | 2.75 us                                                     | 3.50 us: 1.27x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.2 ms: 1.11x slower                                                       |
| python_startup         | 20.6 ms                                                     | 23.6 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.65 ms: 1.36x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.1 ms: 1.23x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 35.1 ms: 1.17x faster                                                       |
| django_template | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.22x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.94x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 411 ms: 2.70x faster                                                        |
| async_tree_none          | 435 ms                                                      | 188 ms: 2.31x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 228 ms: 2.31x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.22 ms: 1.89x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 348 ms: 1.83x faster                                                        |
| pylint                   | 350 ms                                                      | 201 ms: 1.74x faster                                                        |
| go                       | 139 ms                                                      | 84.1 ms: 1.65x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 61.1 ns: 1.55x faster                                                       |
| generators               | 32.4 ms                                                     | 21.4 ms: 1.51x faster                                                       |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.40 sec: 1.50x faster                                                      |
| richards_super           | 52.2 ms                                                     | 34.9 ms: 1.50x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 58.6 ms: 1.46x faster                                                       |
| chaos                    | 61.7 ms                                                     | 42.3 ms: 1.46x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 19.8 us: 1.45x faster                                                       |
| raytrace                 | 273 ms                                                      | 192 ms: 1.43x faster                                                        |
| deepcopy                 | 255 us                                                      | 180 us: 1.42x faster                                                        |
| sqlglot_parse            | 1.22 ms                                                     | 862 us: 1.41x faster                                                        |
| comprehensions           | 16.5 us                                                     | 11.8 us: 1.40x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.63 ms: 1.38x faster                                                       |
| richards                 | 42.4 ms                                                     | 30.9 ms: 1.37x faster                                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 1.08 ms: 1.36x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 538 ms: 1.36x faster                                                        |
| mako                     | 9.03 ms                                                     | 6.65 ms: 1.36x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.25 ms: 1.35x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 47.1 ms: 1.33x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 39.3 ms: 1.30x faster                                                       |
| pyflate                  | 409 ms                                                      | 317 ms: 1.29x faster                                                        |
| pycparser                | 930 ms                                                      | 723 ms: 1.29x faster                                                        |
| unpickle_pure_python     | 183 us                                                      | 143 us: 1.28x faster                                                        |
| scimark_sor              | 106 ms                                                      | 83.1 ms: 1.28x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 45.1 ms: 1.27x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 61.5 ms: 1.26x faster                                                       |
| regex_compile            | 106 ms                                                      | 85.1 ms: 1.25x faster                                                       |
| float                    | 61.7 ms                                                     | 49.6 ms: 1.24x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 219 us: 1.23x faster                                                        |
| genshi_text              | 19.8 ms                                                     | 16.1 ms: 1.23x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                                      |
| regex_dna                | 136 ms                                                      | 112 ms: 1.21x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.20x faster                                                       |
| sympy_sum                | 107 ms                                                      | 89.4 ms: 1.20x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 42.3 ms: 1.19x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.49 sec: 1.19x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.4 ms: 1.19x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.85 us: 1.19x faster                                                       |
| thrift                   | 617 us                                                      | 520 us: 1.19x faster                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.42 ms: 1.17x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 35.1 ms: 1.17x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 827 us: 1.16x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 13.2 ms: 1.15x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.1 ms: 1.15x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.67 sec: 1.15x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.07 sec: 1.14x faster                                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 35.6 ms: 1.12x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.8 ms: 1.12x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 531 ms: 1.11x faster                                                        |
| sympy_str                | 194 ms                                                      | 176 ms: 1.11x faster                                                        |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 89.5 ms: 1.08x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 61.8 ms: 1.08x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.56 ms: 1.07x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.5 ms: 1.06x faster                                                       |
| sqlglot_normalize        | 205 ms                                                      | 193 ms: 1.06x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.4 ms: 1.06x faster                                                       |
| unpack_sequence          | 39.6 ns                                                     | 37.6 ns: 1.05x faster                                                       |
| unpickle                 | 9.09 us                                                     | 8.72 us: 1.04x faster                                                       |
| sympy_expand             | 314 ms                                                      | 302 ms: 1.04x faster                                                        |
| scimark_fft              | 187 ms                                                      | 185 ms: 1.01x faster                                                        |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.67 us: 1.01x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.27 us: 1.01x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 56.5 ms: 1.02x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 77.4 ms: 1.02x slower                                                       |
| nbody                    | 71.3 ms                                                     | 72.7 ms: 1.02x slower                                                       |
| fannkuch                 | 256 ms                                                      | 262 ms: 1.02x slower                                                        |
| json                     | 3.14 ms                                                     | 3.23 ms: 1.03x slower                                                       |
| json_loads               | 14.0 us                                                     | 14.7 us: 1.05x slower                                                       |
| async_generators         | 222 ms                                                      | 232 ms: 1.05x slower                                                        |
| pathlib                  | 75.7 ms                                                     | 79.6 ms: 1.05x slower                                                       |
| unpickle_list            | 2.71 us                                                     | 2.94 us: 1.08x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 17.2 ms: 1.11x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.6 ms: 1.15x slower                                                       |
| pickle                   | 6.85 us                                                     | 8.13 us: 1.19x slower                                                       |
| pickle_dict              | 17.2 us                                                     | 20.6 us: 1.20x slower                                                       |
| coverage                 | 39.0 ms                                                     | 46.9 ms: 1.20x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.81 ms: 1.22x slower                                                       |
| pickle_list              | 2.75 us                                                     | 3.50 us: 1.27x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 83.2 ms: 1.34x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.00 ms: 1.42x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.53x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.20x faster                                                                |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (12) of results/bm-20250111-3.14.0a3+-22a4421/bm-20250111-pythonperf1-amd64-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.221x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: unknown