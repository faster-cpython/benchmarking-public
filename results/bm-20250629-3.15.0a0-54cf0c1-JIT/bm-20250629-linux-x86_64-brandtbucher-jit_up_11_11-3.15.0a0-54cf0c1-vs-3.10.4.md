# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_11_11
- machine: linux-x86_64
- commit hash: 54cf0c1
- commit date: 2025-06-29
- overall geometric mean: 1.478x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                              |
| html5lib       | 88.9 ms                                                | 62.2 ms: 1.43x faster                                               |
| Geometric mean | (ref)                                                  | 1.34x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 602 ms: 2.94x faster                                                |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 498 ms: 2.04x faster                                                |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.9 ms: 1.78x faster                                               |
| nbody          | 154 ms                                                 | 95.2 ms: 1.61x faster                                               |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.43x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                                |
| regex_v8       | 27.8 ms                                                | 23.0 ms: 1.20x faster                                               |
| regex_dna      | 227 ms                                                 | 207 ms: 1.09x faster                                                |
| regex_effbot   | 3.63 ms                                                | 3.44 ms: 1.06x faster                                               |
| Geometric mean | (ref)                                                  | 1.20x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 192 us: 1.72x faster                                                |
| tomli_loads          | 3.14 sec                                               | 1.83 sec: 1.71x faster                                              |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.51x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 56.4 ms: 1.40x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.28x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 81.1 ms: 1.23x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 98.9 ms: 1.17x faster                                               |
| json_loads           | 31.2 us                                                | 28.0 us: 1.11x faster                                               |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 6.94 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.8 ms: 1.52x faster                                               |
| django_template | 48.2 ms                                                | 32.7 ms: 1.47x faster                                               |
| genshi_text     | 31.8 ms                                                | 21.9 ms: 1.45x faster                                               |
| genshi_xml      | 66.0 ms                                                | 50.2 ms: 1.32x faster                                               |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.25x faster                                                |
| async_tree_io            | 1.77 sec                                               | 602 ms: 2.94x faster                                                |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                                |
| generators               | 80.1 ms                                                | 30.3 ms: 2.64x faster                                               |
| deltablue                | 7.91 ms                                                | 3.05 ms: 2.59x faster                                               |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                              |
| go                       | 240 ms                                                 | 114 ms: 2.10x faster                                                |
| richards_super           | 94.7 ms                                                | 45.1 ms: 2.10x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 498 ms: 2.04x faster                                                |
| richards                 | 79.3 ms                                                | 39.2 ms: 2.02x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                               |
| pylint                   | 551 ms                                                 | 283 ms: 1.95x faster                                                |
| logging_silent           | 190 ns                                                 | 99.2 ns: 1.91x faster                                               |
| chaos                    | 115 ms                                                 | 61.1 ms: 1.89x faster                                               |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                                |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.87x faster                                                |
| spectral_norm            | 170 ms                                                 | 91.2 ms: 1.86x faster                                               |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 64.8 ms: 1.82x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 70.7 ms: 1.81x faster                                               |
| float                    | 117 ms                                                 | 65.9 ms: 1.78x faster                                               |
| comprehensions           | 28.8 us                                                | 16.3 us: 1.76x faster                                               |
| unpickle_pure_python     | 331 us                                                 | 192 us: 1.72x faster                                                |
| pyflate                  | 716 ms                                                 | 416 ms: 1.72x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.83 sec: 1.71x faster                                              |
| djangocms                | 38.4 us                                                | 22.4 us: 1.71x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.11 ms: 1.70x faster                                               |
| nbody                    | 154 ms                                                 | 95.2 ms: 1.61x faster                                               |
| mako                     | 16.3 ms                                                | 10.8 ms: 1.52x faster                                               |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.51x faster                                                |
| scimark_fft              | 466 ms                                                 | 309 ms: 1.51x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.78 us: 1.50x faster                                               |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                                |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                |
| django_template          | 48.2 ms                                                | 32.7 ms: 1.47x faster                                               |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                               |
| genshi_text              | 31.8 ms                                                | 21.9 ms: 1.45x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                              |
| logging_format           | 9.09 us                                                | 6.30 us: 1.44x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 709 ms: 1.44x faster                                                |
| html5lib                 | 88.9 ms                                                | 62.2 ms: 1.43x faster                                               |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.41x faster                                              |
| dulwich_log              | 84.3 ms                                                | 59.9 ms: 1.41x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 56.4 ms: 1.40x faster                                               |
| thrift                   | 1.07 ms                                                | 783 us: 1.37x faster                                                |
| coroutines               | 35.1 ms                                                | 25.8 ms: 1.36x faster                                               |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.80 ms: 1.35x faster                                               |
| fannkuch                 | 532 ms                                                 | 395 ms: 1.34x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                               |
| genshi_xml               | 66.0 ms                                                | 50.2 ms: 1.32x faster                                               |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                |
| nqueens                  | 106 ms                                                 | 82.5 ms: 1.28x faster                                               |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.28x faster                                               |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                                |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                              |
| xml_etree_generate       | 99.4 ms                                                | 81.1 ms: 1.23x faster                                               |
| sympy_expand             | 566 ms                                                 | 468 ms: 1.21x faster                                                |
| regex_v8                 | 27.8 ms                                                | 23.0 ms: 1.20x faster                                               |
| pathlib                  | 20.5 ms                                                | 17.1 ms: 1.20x faster                                               |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 98.9 ms: 1.17x faster                                               |
| json_loads               | 31.2 us                                                | 28.0 us: 1.11x faster                                               |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                |
| regex_dna                | 227 ms                                                 | 207 ms: 1.09x faster                                                |
| json                     | 5.69 ms                                                | 5.22 ms: 1.09x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.44 ms: 1.06x faster                                               |
| async_generators         | 444 ms                                                 | 433 ms: 1.02x faster                                                |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                |
| telco                    | 7.27 ms                                                | 7.87 ms: 1.08x slower                                               |
| coverage                 | 79.4 ms                                                | 87.7 ms: 1.10x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 6.94 ms: 1.17x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.91 ms: 1.36x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.60 ms: 1.60x slower                                               |
| Geometric mean           | (ref)                                                  | 1.48x faster                                                        |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250629-3.15.0a0-54cf0c1-JIT/bm-20250629-linux-x86_64-brandtbucher-jit_up_11_11-3.15.0a0-54cf0c1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.478x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.34x

# Memory
- memory change: 1.33x