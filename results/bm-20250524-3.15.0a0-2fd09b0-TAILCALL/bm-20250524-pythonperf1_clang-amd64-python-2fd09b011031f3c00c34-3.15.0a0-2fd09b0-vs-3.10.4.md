# Results vs. 3.10.4

- fork: python
- ref: 2fd09b011031f3c00c34
- machine: windows-amd64
- commit hash: 2fd09b0
- commit date: 2025-05-24
- overall geometric mean: 1.359x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 204 ms: 1.21x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.53 sec: 1.25x faster                                                     |
| html5lib       | 51.0 ms                                                     | 34.5 ms: 1.48x faster                                                      |
| Geometric mean | (ref)                                                       | 1.31x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 358 ms: 3.09x faster                                                       |
| async_tree_none         | 435 ms                                                      | 149 ms: 2.93x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 185 ms: 2.84x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 314 ms: 2.03x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.69x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 37.3 ms: 1.65x faster                                                      |
| nbody          | 71.3 ms                                                     | 50.7 ms: 1.41x faster                                                      |
| pidigits       | 149 ms                                                      | 145 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.34x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 67.6 ms: 1.57x faster                                                      |
| regex_dna      | 136 ms                                                      | 112 ms: 1.21x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 12.8 ms: 1.20x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.44 ms: 1.15x faster                                                      |
| Geometric mean | (ref)                                                       | 1.27x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 103 us: 1.77x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 5.20 ms: 1.76x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 167 us: 1.61x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.06 sec: 1.58x faster                                                     |
| pickle_dict          | 17.2 us                                                     | 11.3 us: 1.51x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 32.7 ms: 1.36x faster                                                      |
| pickle_list          | 2.75 us                                                     | 2.13 us: 1.29x faster                                                      |
| unpickle_list        | 2.71 us                                                     | 2.17 us: 1.25x faster                                                      |
| unpickle             | 9.09 us                                                     | 7.64 us: 1.19x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 47.7 ms: 1.16x faster                                                      |
| pickle               | 6.85 us                                                     | 6.16 us: 1.11x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 89.1 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.5 ms: 1.07x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.7 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.31x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.8 ms: 1.21x slower                                                      |
| python_startup         | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 11.5 ms: 1.72x faster                                                      |
| mako            | 9.03 ms                                                     | 5.90 ms: 1.53x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 27.5 ms: 1.49x faster                                                      |
| django_template | 28.9 ms                                                     | 20.1 ms: 1.44x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.54x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 90.8 us: 3.70x faster                                                      |
| async_tree_io            | 1.11 sec                                                    | 358 ms: 3.09x faster                                                       |
| async_tree_none          | 435 ms                                                      | 149 ms: 2.93x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 185 ms: 2.84x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 27.8 ms: 2.72x faster                                                      |
| deltablue                | 4.19 ms                                                     | 1.58 ms: 2.66x faster                                                      |
| mdp                      | 1.78 sec                                                    | 683 ms: 2.61x faster                                                       |
| go                       | 139 ms                                                      | 59.9 ms: 2.32x faster                                                      |
| scimark_sor              | 106 ms                                                      | 48.6 ms: 2.19x faster                                                      |
| richards_super           | 52.2 ms                                                     | 24.6 ms: 2.13x faster                                                      |
| generators               | 32.4 ms                                                     | 15.3 ms: 2.11x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 13.8 us: 2.08x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 28.0 ms: 2.05x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 314 ms: 2.03x faster                                                       |
| richards                 | 42.4 ms                                                     | 21.3 ms: 2.00x faster                                                      |
| chaos                    | 61.7 ms                                                     | 31.0 ms: 1.99x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 2.95 ms: 1.95x faster                                                      |
| comprehensions           | 16.5 us                                                     | 8.61 us: 1.92x faster                                                      |
| pylint                   | 350 ms                                                      | 185 ms: 1.89x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 45.7 ms: 1.88x faster                                                      |
| raytrace                 | 273 ms                                                      | 146 ms: 1.87x faster                                                       |
| asyncio_tcp              | 732 ms                                                      | 393 ms: 1.86x faster                                                       |
| deepcopy                 | 255 us                                                      | 139 us: 1.84x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 103 us: 1.77x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 5.20 ms: 1.76x faster                                                      |
| genshi_text              | 19.8 ms                                                     | 11.5 ms: 1.72x faster                                                      |
| pyflate                  | 409 ms                                                      | 238 ms: 1.72x faster                                                       |
| float                    | 61.7 ms                                                     | 37.3 ms: 1.65x faster                                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.31 sec: 1.61x faster                                                     |
| pickle_pure_python       | 270 us                                                      | 167 us: 1.61x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 48.8 ms: 1.58x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.06 sec: 1.58x faster                                                     |
| regex_compile            | 106 ms                                                      | 67.6 ms: 1.57x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 40.1 ms: 1.56x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.90 ms: 1.53x faster                                                      |
| pickle_dict              | 17.2 us                                                     | 11.3 us: 1.51x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.46 us: 1.51x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 27.5 ms: 1.49x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 34.5 ms: 1.48x faster                                                      |
| pycparser                | 930 ms                                                      | 643 ms: 1.45x faster                                                       |
| django_template          | 28.9 ms                                                     | 20.1 ms: 1.44x faster                                                      |
| coroutines               | 16.0 ms                                                     | 11.4 ms: 1.41x faster                                                      |
| nbody                    | 71.3 ms                                                     | 50.7 ms: 1.41x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 11.2 ms: 1.37x faster                                                      |
| sympy_sum                | 107 ms                                                      | 78.4 ms: 1.36x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 48.8 ms: 1.36x faster                                                      |
| unpack_sequence          | 39.6 ns                                                     | 29.1 ns: 1.36x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 32.7 ms: 1.36x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 37.3 ms: 1.35x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 908 ms: 1.34x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 444 ms: 1.33x faster                                                       |
| fannkuch                 | 256 ms                                                      | 196 ms: 1.31x faster                                                       |
| sympy_str                | 194 ms                                                      | 149 ms: 1.31x faster                                                       |
| scimark_fft              | 187 ms                                                      | 143 ms: 1.31x faster                                                       |
| pickle_list              | 2.75 us                                                     | 2.13 us: 1.29x faster                                                      |
| sqlite_synth             | 1.91 us                                                     | 1.48 us: 1.29x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.53 sec: 1.25x faster                                                     |
| unpickle_list            | 2.71 us                                                     | 2.17 us: 1.25x faster                                                      |
| sympy_expand             | 314 ms                                                      | 254 ms: 1.24x faster                                                       |
| regex_dna                | 136 ms                                                      | 112 ms: 1.21x faster                                                       |
| 2to3                     | 246 ms                                                      | 204 ms: 1.21x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 12.8 ms: 1.20x faster                                                      |
| unpickle                 | 9.09 us                                                     | 7.64 us: 1.19x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.29 ms: 1.19x faster                                                      |
| bench_thread_pool        | 958 us                                                      | 819 us: 1.17x faster                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 47.7 ms: 1.16x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 65.3 ms: 1.16x faster                                                      |
| regex_effbot             | 1.66 ms                                                     | 1.44 ms: 1.15x faster                                                      |
| async_generators         | 222 ms                                                      | 195 ms: 1.14x faster                                                       |
| logging_format           | 6.76 us                                                     | 6.01 us: 1.13x faster                                                      |
| pickle                   | 6.85 us                                                     | 6.16 us: 1.11x faster                                                      |
| logging_simple           | 6.22 us                                                     | 5.64 us: 1.10x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 89.1 ms: 1.09x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.5 ms: 1.07x faster                                                      |
| json                     | 3.14 ms                                                     | 2.94 ms: 1.07x faster                                                      |
| pidigits                 | 149 ms                                                      | 145 ms: 1.03x faster                                                       |
| telco                    | 3.94 ms                                                     | 4.08 ms: 1.03x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.7 us: 1.05x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 18.8 ms: 1.21x slower                                                      |
| python_startup           | 20.6 ms                                                     | 25.2 ms: 1.22x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 92.0 ms: 1.48x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.42 ms: 1.77x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.71 ms: 1.93x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 271 ns: 2.86x slower                                                       |
| coverage                 | 39.0 ms                                                     | 221 ms: 5.68x slower                                                       |
| thrift                   | 617 us                                                      | 85.9 ms: 139.15x slower                                                    |
| Geometric mean           | (ref)                                                       | 1.33x faster                                                               |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250524-3.15.0a0-2fd09b0-CLANG/bm-20250524-pythonperf1-amd64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.359x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: unknown