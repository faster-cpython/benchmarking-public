# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_12_8
- machine: linux-x86_64
- commit hash: 23be3e4
- commit date: 2025-06-30
- overall geometric mean: 1.480x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.34x faster                                               |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                             |
| html5lib       | 88.9 ms                                                | 62.3 ms: 1.43x faster                                              |
| Geometric mean | (ref)                                                  | 1.33x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 606 ms: 2.92x faster                                               |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                               |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.76x faster                                               |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 501 ms: 2.03x faster                                               |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 117 ms                                                 | 66.2 ms: 1.77x faster                                              |
| nbody          | 154 ms                                                 | 101 ms: 1.52x faster                                               |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.40x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                               |
| regex_v8       | 27.8 ms                                                | 23.0 ms: 1.21x faster                                              |
| regex_dna      | 227 ms                                                 | 208 ms: 1.09x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.45 ms: 1.05x faster                                              |
| Geometric mean | (ref)                                                  | 1.20x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 190 us: 1.74x faster                                               |
| tomli_loads          | 3.14 sec                                               | 1.83 sec: 1.72x faster                                             |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.51x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 55.7 ms: 1.42x faster                                              |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.27x faster                                              |
| xml_etree_generate   | 99.4 ms                                                | 80.0 ms: 1.24x faster                                              |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                              |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                              |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.19x faster                                              |
| python_startup_no_site | 5.93 ms                                                | 6.96 ms: 1.17x slower                                              |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.4 ms: 1.56x faster                                              |
| django_template | 48.2 ms                                                | 32.6 ms: 1.48x faster                                              |
| genshi_text     | 31.8 ms                                                | 22.0 ms: 1.45x faster                                              |
| genshi_xml      | 66.0 ms                                                | 50.8 ms: 1.30x faster                                              |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.24x faster                                               |
| async_tree_io            | 1.77 sec                                               | 606 ms: 2.92x faster                                               |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.76x faster                                               |
| deltablue                | 7.91 ms                                                | 3.03 ms: 2.61x faster                                              |
| generators               | 80.1 ms                                                | 31.4 ms: 2.55x faster                                              |
| richards_super           | 94.7 ms                                                | 38.0 ms: 2.50x faster                                              |
| richards                 | 79.3 ms                                                | 33.7 ms: 2.35x faster                                              |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.31x faster                                             |
| go                       | 240 ms                                                 | 115 ms: 2.09x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 501 ms: 2.03x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                              |
| pylint                   | 551 ms                                                 | 284 ms: 1.94x faster                                               |
| chaos                    | 115 ms                                                 | 61.2 ms: 1.89x faster                                              |
| raytrace                 | 507 ms                                                 | 269 ms: 1.88x faster                                               |
| spectral_norm            | 170 ms                                                 | 91.0 ms: 1.87x faster                                              |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                               |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 65.2 ms: 1.81x faster                                              |
| logging_silent           | 190 ns                                                 | 105 ns: 1.80x faster                                               |
| float                    | 117 ms                                                 | 66.2 ms: 1.77x faster                                              |
| comprehensions           | 28.8 us                                                | 16.3 us: 1.76x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 190 us: 1.74x faster                                               |
| pyflate                  | 716 ms                                                 | 413 ms: 1.74x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.83 sec: 1.72x faster                                             |
| djangocms                | 38.4 us                                                | 22.6 us: 1.70x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 75.6 ms: 1.69x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.24 ms: 1.67x faster                                              |
| mako                     | 16.3 ms                                                | 10.4 ms: 1.56x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                              |
| nbody                    | 154 ms                                                 | 101 ms: 1.52x faster                                               |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.51x faster                                               |
| scimark_fft              | 466 ms                                                 | 311 ms: 1.50x faster                                               |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                               |
| django_template          | 48.2 ms                                                | 32.6 ms: 1.48x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 697 ms: 1.46x faster                                               |
| scimark_lu               | 176 ms                                                 | 121 ms: 1.46x faster                                               |
| logging_simple           | 8.30 us                                                | 5.70 us: 1.46x faster                                              |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                             |
| genshi_text              | 31.8 ms                                                | 22.0 ms: 1.45x faster                                              |
| logging_format           | 9.09 us                                                | 6.32 us: 1.44x faster                                              |
| html5lib                 | 88.9 ms                                                | 62.3 ms: 1.43x faster                                              |
| xml_etree_process        | 79.1 ms                                                | 55.7 ms: 1.42x faster                                              |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.41x faster                                             |
| dulwich_log              | 84.3 ms                                                | 59.7 ms: 1.41x faster                                              |
| coroutines               | 35.1 ms                                                | 24.9 ms: 1.41x faster                                              |
| thrift                   | 1.07 ms                                                | 784 us: 1.37x faster                                               |
| fannkuch                 | 532 ms                                                 | 396 ms: 1.34x faster                                               |
| 2to3                     | 348 ms                                                 | 261 ms: 1.34x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.90 ms: 1.32x faster                                              |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                               |
| genshi_xml               | 66.0 ms                                                | 50.8 ms: 1.30x faster                                              |
| nqueens                  | 106 ms                                                 | 83.0 ms: 1.27x faster                                              |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.27x faster                                              |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                               |
| xml_etree_generate       | 99.4 ms                                                | 80.0 ms: 1.24x faster                                              |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                             |
| sympy_expand             | 566 ms                                                 | 468 ms: 1.21x faster                                               |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                              |
| regex_v8                 | 27.8 ms                                                | 23.0 ms: 1.21x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                               |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.19x faster                                              |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                              |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                               |
| regex_dna                | 227 ms                                                 | 208 ms: 1.09x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                              |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                              |
| json                     | 5.69 ms                                                | 5.30 ms: 1.07x faster                                              |
| regex_effbot             | 3.63 ms                                                | 3.45 ms: 1.05x faster                                              |
| async_generators         | 444 ms                                                 | 437 ms: 1.02x faster                                               |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                               |
| telco                    | 7.27 ms                                                | 7.68 ms: 1.06x slower                                              |
| coverage                 | 79.4 ms                                                | 87.8 ms: 1.11x slower                                              |
| python_startup_no_site   | 5.93 ms                                                | 6.96 ms: 1.17x slower                                              |
| gc_traversal             | 3.62 ms                                                | 4.95 ms: 1.37x slower                                              |
| create_gc_cycles         | 1.62 ms                                                | 2.60 ms: 1.60x slower                                              |
| Geometric mean           | (ref)                                                  | 1.48x faster                                                       |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250630-3.15.0a0-23be3e4-JIT/bm-20250630-linux-x86_64-brandtbucher-jit_up_12_8-3.15.0a0-23be3e4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.480x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.33x