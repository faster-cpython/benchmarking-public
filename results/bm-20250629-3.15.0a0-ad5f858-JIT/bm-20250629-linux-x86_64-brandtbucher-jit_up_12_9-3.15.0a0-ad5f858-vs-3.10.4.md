# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_12_9
- machine: linux-x86_64
- commit hash: ad5f858
- commit date: 2025-06-29
- overall geometric mean: 1.482x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                               |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                             |
| html5lib       | 88.9 ms                                                | 62.1 ms: 1.43x faster                                              |
| Geometric mean | (ref)                                                  | 1.34x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 600 ms: 2.95x faster                                               |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                               |
| async_tree_memoization  | 870 ms                                                 | 317 ms: 2.75x faster                                               |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 494 ms: 2.06x faster                                               |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 117 ms                                                 | 66.3 ms: 1.77x faster                                              |
| nbody          | 154 ms                                                 | 96.3 ms: 1.59x faster                                              |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.42x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                               |
| regex_v8       | 27.8 ms                                                | 23.9 ms: 1.16x faster                                              |
| regex_effbot   | 3.63 ms                                                | 3.42 ms: 1.06x faster                                              |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.18x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 190 us: 1.74x faster                                               |
| tomli_loads          | 3.14 sec                                               | 1.85 sec: 1.70x faster                                             |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.52x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 55.4 ms: 1.43x faster                                              |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.28x faster                                              |
| xml_etree_generate   | 99.4 ms                                                | 80.0 ms: 1.24x faster                                              |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 98.8 ms: 1.17x faster                                              |
| json_loads           | 31.2 us                                                | 28.1 us: 1.11x faster                                              |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.1 ms: 1.20x faster                                              |
| python_startup_no_site | 5.93 ms                                                | 6.90 ms: 1.16x slower                                              |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.5 ms: 1.55x faster                                              |
| django_template | 48.2 ms                                                | 32.5 ms: 1.48x faster                                              |
| genshi_text     | 31.8 ms                                                | 21.9 ms: 1.45x faster                                              |
| genshi_xml      | 66.0 ms                                                | 50.3 ms: 1.31x faster                                              |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.23x faster                                               |
| async_tree_io            | 1.77 sec                                               | 600 ms: 2.95x faster                                               |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 317 ms: 2.75x faster                                               |
| richards_super           | 94.7 ms                                                | 36.3 ms: 2.61x faster                                              |
| deltablue                | 7.91 ms                                                | 3.03 ms: 2.61x faster                                              |
| generators               | 80.1 ms                                                | 31.7 ms: 2.53x faster                                              |
| richards                 | 79.3 ms                                                | 31.9 ms: 2.48x faster                                              |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.31x faster                                             |
| go                       | 240 ms                                                 | 114 ms: 2.10x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 494 ms: 2.06x faster                                               |
| pylint                   | 551 ms                                                 | 282 ms: 1.96x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 29.9 us: 1.95x faster                                              |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.87x faster                                               |
| chaos                    | 115 ms                                                 | 61.9 ms: 1.87x faster                                              |
| raytrace                 | 507 ms                                                 | 272 ms: 1.87x faster                                               |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                               |
| spectral_norm            | 170 ms                                                 | 93.1 ms: 1.82x faster                                              |
| logging_silent           | 190 ns                                                 | 105 ns: 1.80x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 65.7 ms: 1.80x faster                                              |
| float                    | 117 ms                                                 | 66.3 ms: 1.77x faster                                              |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 190 us: 1.74x faster                                               |
| djangocms                | 38.4 us                                                | 22.5 us: 1.71x faster                                              |
| pyflate                  | 716 ms                                                 | 421 ms: 1.70x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.85 sec: 1.70x faster                                             |
| crypto_pyaes             | 128 ms                                                 | 75.5 ms: 1.69x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.21 ms: 1.67x faster                                              |
| nbody                    | 154 ms                                                 | 96.3 ms: 1.59x faster                                              |
| mako                     | 16.3 ms                                                | 10.5 ms: 1.55x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                              |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.52x faster                                               |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                               |
| django_template          | 48.2 ms                                                | 32.5 ms: 1.48x faster                                              |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                               |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                              |
| pprint_pformat           | 2.10 sec                                               | 1.44 sec: 1.47x faster                                             |
| scimark_fft              | 466 ms                                                 | 319 ms: 1.46x faster                                               |
| genshi_text              | 31.8 ms                                                | 21.9 ms: 1.45x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 708 ms: 1.44x faster                                               |
| html5lib                 | 88.9 ms                                                | 62.1 ms: 1.43x faster                                              |
| logging_format           | 9.09 us                                                | 6.35 us: 1.43x faster                                              |
| xml_etree_process        | 79.1 ms                                                | 55.4 ms: 1.43x faster                                              |
| dulwich_log              | 84.3 ms                                                | 59.4 ms: 1.42x faster                                              |
| coroutines               | 35.1 ms                                                | 25.0 ms: 1.40x faster                                              |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                             |
| thrift                   | 1.07 ms                                                | 783 us: 1.37x faster                                               |
| fannkuch                 | 532 ms                                                 | 396 ms: 1.34x faster                                               |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                              |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                               |
| genshi_xml               | 66.0 ms                                                | 50.3 ms: 1.31x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.99 ms: 1.30x faster                                              |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.28x faster                                              |
| nqueens                  | 106 ms                                                 | 82.9 ms: 1.28x faster                                              |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                               |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                             |
| xml_etree_generate       | 99.4 ms                                                | 80.0 ms: 1.24x faster                                              |
| sympy_expand             | 566 ms                                                 | 469 ms: 1.21x faster                                               |
| python_startup           | 14.6 ms                                                | 12.1 ms: 1.20x faster                                              |
| pathlib                  | 20.5 ms                                                | 17.1 ms: 1.20x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 98.8 ms: 1.17x faster                                              |
| regex_v8                 | 27.8 ms                                                | 23.9 ms: 1.16x faster                                              |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                               |
| json_loads               | 31.2 us                                                | 28.1 us: 1.11x faster                                              |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                              |
| json                     | 5.69 ms                                                | 5.24 ms: 1.09x faster                                              |
| regex_effbot             | 3.63 ms                                                | 3.42 ms: 1.06x faster                                              |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                               |
| async_generators         | 444 ms                                                 | 426 ms: 1.04x faster                                               |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                               |
| telco                    | 7.27 ms                                                | 7.78 ms: 1.07x slower                                              |
| coverage                 | 79.4 ms                                                | 87.9 ms: 1.11x slower                                              |
| python_startup_no_site   | 5.93 ms                                                | 6.90 ms: 1.16x slower                                              |
| gc_traversal             | 3.62 ms                                                | 4.88 ms: 1.35x slower                                              |
| create_gc_cycles         | 1.62 ms                                                | 2.58 ms: 1.59x slower                                              |
| Geometric mean           | (ref)                                                  | 1.49x faster                                                       |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250629-3.15.0a0-ad5f858-JIT/bm-20250629-linux-x86_64-brandtbucher-jit_up_12_9-3.15.0a0-ad5f858.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.482x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.33x