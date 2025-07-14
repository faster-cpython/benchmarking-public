# Results vs. 3.10.4

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: linux-x86_64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.319x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.25x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.86 sec: 1.19x faster                                                      |
| html5lib       | 94.6 ms                                                      | 65.5 ms: 1.44x faster                                                       |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 630 ms: 2.54x faster                                                        |
| async_tree_none         | 692 ms                                                       | 273 ms: 2.53x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 332 ms: 2.47x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 505 ms: 1.85x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 70.8 ms: 1.57x faster                                                       |
| nbody          | 134 ms                                                       | 93.0 ms: 1.44x faster                                                       |
| pidigits       | 271 ms                                                       | 256 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 133 ms: 1.43x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 23.3 ms: 1.17x faster                                                       |
| regex_dna      | 261 ms                                                       | 229 ms: 1.14x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 206 us: 1.51x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.02 sec: 1.44x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 333 us: 1.37x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.3 ms: 1.29x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 59.3 ms: 1.28x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.6 us: 1.18x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 139 ms: 1.15x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 97.4 ms: 1.13x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 81.9 ms: 1.13x faster                                                       |
| unpickle_list        | 4.65 us                                                      | 5.02 us: 1.08x slower                                                       |
| unpickle             | 13.5 us                                                      | 14.8 us: 1.09x slower                                                       |
| pickle_list          | 4.12 us                                                      | 5.03 us: 1.22x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 36.6 us: 1.24x slower                                                       |
| pickle               | 9.89 us                                                      | 12.7 us: 1.28x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.10x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.83 ms: 1.21x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.3 ms: 1.42x faster                                                       |
| mako            | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.2 ms: 1.35x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 52.8 ms: 1.20x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.33x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 167 us: 3.20x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 630 ms: 2.54x faster                                                        |
| async_tree_none          | 692 ms                                                       | 273 ms: 2.53x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 332 ms: 2.47x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.27 sec: 2.36x faster                                                      |
| deltablue                | 7.50 ms                                                      | 3.20 ms: 2.34x faster                                                       |
| go                       | 262 ms                                                       | 119 ms: 2.21x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 364 ms: 2.14x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| generators               | 57.3 ms                                                      | 29.5 ms: 1.94x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 505 ms: 1.85x faster                                                        |
| chaos                    | 109 ms                                                       | 59.0 ms: 1.84x faster                                                       |
| logging_silent           | 167 ns                                                       | 94.1 ns: 1.78x faster                                                       |
| pylint                   | 566 ms                                                       | 319 ms: 1.78x faster                                                        |
| richards_super           | 90.6 ms                                                      | 51.8 ms: 1.75x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 61.8 ms: 1.74x faster                                                       |
| scimark_lu               | 167 ms                                                       | 96.6 ms: 1.73x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 28.8 us: 1.73x faster                                                       |
| raytrace                 | 489 ms                                                       | 284 ms: 1.72x faster                                                        |
| pyflate                  | 733 ms                                                       | 427 ms: 1.72x faster                                                        |
| scimark_sor              | 180 ms                                                       | 105 ms: 1.72x faster                                                        |
| deepcopy                 | 468 us                                                       | 276 us: 1.70x faster                                                        |
| richards                 | 75.1 ms                                                      | 45.6 ms: 1.65x faster                                                       |
| comprehensions           | 26.7 us                                                      | 16.4 us: 1.63x faster                                                       |
| spectral_norm            | 139 ms                                                       | 86.8 ms: 1.60x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 5.91 ms: 1.59x faster                                                       |
| float                    | 111 ms                                                       | 70.8 ms: 1.57x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 76.1 ms: 1.57x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 206 us: 1.51x faster                                                        |
| logging_simple           | 8.88 us                                                      | 5.94 us: 1.49x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.57 us: 1.47x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 65.5 ms: 1.44x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.02 sec: 1.44x faster                                                      |
| nbody                    | 134 ms                                                       | 93.0 ms: 1.44x faster                                                       |
| regex_compile            | 190 ms                                                       | 133 ms: 1.43x faster                                                        |
| django_template          | 50.2 ms                                                      | 35.3 ms: 1.42x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 58.5 ms: 1.39x faster                                                       |
| thrift                   | 1.18 ms                                                      | 856 us: 1.37x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.37x faster                                                      |
| pickle_pure_python       | 455 us                                                       | 333 us: 1.37x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.58 sec: 1.36x faster                                                      |
| mako                     | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.3 ms: 1.36x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 23.2 ms: 1.35x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 775 ms: 1.35x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.97 us: 1.35x faster                                                       |
| fannkuch                 | 483 ms                                                       | 360 ms: 1.34x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 45.0 ns: 1.33x faster                                                       |
| sympy_sum                | 193 ms                                                       | 149 ms: 1.29x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.3 ms: 1.29x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 21.9 ms: 1.29x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 59.3 ms: 1.28x faster                                                       |
| sympy_str                | 360 ms                                                       | 284 ms: 1.27x faster                                                        |
| nqueens                  | 115 ms                                                       | 91.1 ms: 1.26x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 17.1 ms: 1.25x faster                                                       |
| 2to3                     | 350 ms                                                       | 281 ms: 1.25x faster                                                        |
| sympy_expand             | 600 ms                                                       | 486 ms: 1.24x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 52.8 ms: 1.20x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.86 sec: 1.19x faster                                                      |
| json_loads               | 30.3 us                                                      | 25.6 us: 1.18x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 974 us: 1.17x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 23.3 ms: 1.17x faster                                                       |
| scimark_fft              | 361 ms                                                       | 311 ms: 1.16x faster                                                        |
| meteor_contest           | 138 ms                                                       | 120 ms: 1.16x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 139 ms: 1.15x faster                                                        |
| regex_dna                | 261 ms                                                       | 229 ms: 1.14x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 97.4 ms: 1.13x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 81.9 ms: 1.13x faster                                                       |
| json                     | 5.86 ms                                                      | 5.38 ms: 1.09x faster                                                       |
| pidigits                 | 271 ms                                                       | 256 ms: 1.06x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.84 us: 1.05x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.86 ms: 1.04x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 382 ms: 1.02x faster                                                        |
| unpickle_list            | 4.65 us                                                      | 5.02 us: 1.08x slower                                                       |
| unpickle                 | 13.5 us                                                      | 14.8 us: 1.09x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.83 ms: 1.21x slower                                                       |
| pickle_list              | 4.12 us                                                      | 5.03 us: 1.22x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 36.6 us: 1.24x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.7 us: 1.28x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| coverage                 | 63.3 ms                                                      | 84.4 ms: 1.33x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.93 ms: 1.66x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.47 ms: 1.90x slower                                                       |
| telco                    | 7.23 ms                                                      | 161 ms: 22.23x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 1.55 sec: 242.77x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.22x faster                                                                |

Benchmark hidden because not significant (1): async_generators
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250712-3.15.0a0-47b01da/bm-20250712-pythonperf2-x86_64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.319x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.38x