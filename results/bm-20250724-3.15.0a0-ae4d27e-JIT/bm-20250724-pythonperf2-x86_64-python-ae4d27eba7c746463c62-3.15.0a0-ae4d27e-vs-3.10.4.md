# Results vs. 3.10.4

- fork: python
- ref: ae4d27eba7c746463c62
- machine: linux-x86_64
- commit hash: ae4d27e
- commit date: 2025-07-24
- overall geometric mean: 1.335x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 286 ms: 1.23x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                      |
| html5lib       | 94.6 ms                                                      | 67.1 ms: 1.41x faster                                                       |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 618 ms: 2.59x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 327 ms: 2.50x faster                                                        |
| async_tree_none         | 692 ms                                                       | 280 ms: 2.47x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 501 ms: 1.87x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.34x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 63.6 ms: 1.75x faster                                                       |
| nbody          | 134 ms                                                       | 99.4 ms: 1.35x faster                                                       |
| pidigits       | 271 ms                                                       | 256 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.36x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 133 ms: 1.43x faster                                                        |
| regex_dna      | 261 ms                                                       | 227 ms: 1.15x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 24.4 ms: 1.11x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.59 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 193 us: 1.62x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 1.91 sec: 1.53x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 331 us: 1.38x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 56.0 ms: 1.36x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 80.4 ms: 1.15x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 99.1 ms: 1.11x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.10x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.84 ms: 1.21x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.65 ms: 1.52x faster                                                       |
| django_template | 50.2 ms                                                      | 35.2 ms: 1.43x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.3 ms: 1.35x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 54.3 ms: 1.17x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.36x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 169 us: 3.18x faster                                                        |
| deltablue                | 7.50 ms                                                      | 2.84 ms: 2.64x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 618 ms: 2.59x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 327 ms: 2.50x faster                                                        |
| async_tree_none          | 692 ms                                                       | 280 ms: 2.47x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.29 sec: 2.33x faster                                                      |
| richards_super           | 90.6 ms                                                      | 40.7 ms: 2.23x faster                                                       |
| richards                 | 75.1 ms                                                      | 35.1 ms: 2.14x faster                                                       |
| go                       | 262 ms                                                       | 129 ms: 2.03x faster                                                        |
| generators               | 57.3 ms                                                      | 30.1 ms: 1.91x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 501 ms: 1.87x faster                                                        |
| pyflate                  | 733 ms                                                       | 401 ms: 1.83x faster                                                        |
| chaos                    | 109 ms                                                       | 59.6 ms: 1.82x faster                                                       |
| logging_silent           | 167 ns                                                       | 92.4 ns: 1.81x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 27.9 us: 1.78x faster                                                       |
| scimark_lu               | 167 ms                                                       | 94.4 ms: 1.77x faster                                                       |
| scimark_sor              | 180 ms                                                       | 102 ms: 1.76x faster                                                        |
| float                    | 111 ms                                                       | 63.6 ms: 1.75x faster                                                       |
| pylint                   | 566 ms                                                       | 324 ms: 1.75x faster                                                        |
| spectral_norm            | 139 ms                                                       | 80.4 ms: 1.73x faster                                                       |
| raytrace                 | 489 ms                                                       | 284 ms: 1.72x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 63.2 ms: 1.70x faster                                                       |
| deepcopy                 | 468 us                                                       | 279 us: 1.68x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 193 us: 1.62x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 77.3 ms: 1.54x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.54x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 1.91 sec: 1.53x faster                                                      |
| mako                     | 14.7 ms                                                      | 9.65 ms: 1.52x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.20 ms: 1.52x faster                                                       |
| logging_simple           | 8.88 us                                                      | 5.96 us: 1.49x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.61 us: 1.46x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.49 sec: 1.44x faster                                                      |
| django_template          | 50.2 ms                                                      | 35.2 ms: 1.43x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 736 ms: 1.43x faster                                                        |
| regex_compile            | 190 ms                                                       | 133 ms: 1.43x faster                                                        |
| thrift                   | 1.18 ms                                                      | 829 us: 1.42x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 67.1 ms: 1.41x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 58.5 ms: 1.39x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 331 us: 1.38x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 56.0 ms: 1.36x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                      |
| coroutines               | 30.3 ms                                                      | 22.4 ms: 1.35x faster                                                       |
| nbody                    | 134 ms                                                       | 99.4 ms: 1.35x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 23.3 ms: 1.35x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.99 us: 1.34x faster                                                       |
| fannkuch                 | 483 ms                                                       | 366 ms: 1.32x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                       |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.4 ms: 1.26x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 17.0 ms: 1.26x faster                                                       |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                        |
| nqueens                  | 115 ms                                                       | 93.3 ms: 1.23x faster                                                       |
| 2to3                     | 350 ms                                                       | 286 ms: 1.23x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.21x faster                                                       |
| sympy_expand             | 600 ms                                                       | 499 ms: 1.20x faster                                                        |
| scimark_fft              | 361 ms                                                       | 301 ms: 1.20x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 54.3 ms: 1.17x faster                                                       |
| regex_dna                | 261 ms                                                       | 227 ms: 1.15x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 80.4 ms: 1.15x faster                                                       |
| meteor_contest           | 138 ms                                                       | 121 ms: 1.14x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 99.1 ms: 1.11x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 24.4 ms: 1.11x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.10x faster                                                        |
| json                     | 5.86 ms                                                      | 5.49 ms: 1.07x faster                                                       |
| pidigits                 | 271 ms                                                       | 256 ms: 1.06x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.83 us: 1.06x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.09 ms: 1.00x slower                                                       |
| async_generators         | 421 ms                                                       | 452 ms: 1.07x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.59 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.84 ms: 1.21x slower                                                       |
| coverage                 | 63.3 ms                                                      | 79.0 ms: 1.25x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.88 ms: 1.63x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.54 ms: 1.91x slower                                                       |
| telco                    | 7.23 ms                                                      | 159 ms: 21.94x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.34x faster                                                                |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250724-3.15.0a0-ae4d27e-JIT/bm-20250724-pythonperf2-x86_64-python-ae4d27eba7c746463c62-3.15.0a0-ae4d27e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.335x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.40x