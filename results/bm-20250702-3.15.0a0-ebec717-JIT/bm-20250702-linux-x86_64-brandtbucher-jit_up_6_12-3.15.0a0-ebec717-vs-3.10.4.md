# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_6_12
- machine: linux-x86_64
- commit hash: ebec717
- commit date: 2025-07-02
- overall geometric mean: 1.424x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 263 ms: 1.32x faster                                               |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                             |
| html5lib       | 88.9 ms                                                | 61.9 ms: 1.43x faster                                              |
| Geometric mean | (ref)                                                  | 1.33x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 602 ms: 2.94x faster                                               |
| async_tree_none         | 728 ms                                                 | 257 ms: 2.84x faster                                               |
| async_tree_memoization  | 870 ms                                                 | 322 ms: 2.70x faster                                               |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 502 ms: 2.03x faster                                               |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.3 ms: 1.79x faster                                              |
| nbody          | 154 ms                                                 | 94.1 ms: 1.63x faster                                              |
| pidigits       | 191 ms                                                 | 201 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                  | 1.41x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                               |
| regex_v8       | 27.8 ms                                                | 22.5 ms: 1.23x faster                                              |
| regex_effbot   | 3.63 ms                                                | 3.20 ms: 1.13x faster                                              |
| regex_dna      | 227 ms                                                 | 206 ms: 1.10x faster                                               |
| Geometric mean | (ref)                                                  | 1.23x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 190 us: 1.74x faster                                               |
| tomli_loads          | 3.14 sec                                               | 1.84 sec: 1.71x faster                                             |
| pickle_pure_python   | 484 us                                                 | 327 us: 1.48x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 55.1 ms: 1.44x faster                                              |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.28x faster                                              |
| xml_etree_generate   | 99.4 ms                                                | 79.7 ms: 1.25x faster                                              |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 98.9 ms: 1.17x faster                                              |
| json_loads           | 31.2 us                                                | 28.1 us: 1.11x faster                                              |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                              |
| python_startup_no_site | 5.93 ms                                                | 6.96 ms: 1.17x slower                                              |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.6 ms: 1.54x faster                                              |
| genshi_text     | 31.8 ms                                                | 21.2 ms: 1.50x faster                                              |
| django_template | 48.2 ms                                                | 32.8 ms: 1.47x faster                                              |
| genshi_xml      | 66.0 ms                                                | 50.4 ms: 1.31x faster                                              |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.20x faster                                               |
| async_tree_io            | 1.77 sec                                               | 602 ms: 2.94x faster                                               |
| async_tree_none          | 728 ms                                                 | 257 ms: 2.84x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 322 ms: 2.70x faster                                               |
| generators               | 80.1 ms                                                | 30.3 ms: 2.65x faster                                              |
| richards_super           | 94.7 ms                                                | 36.2 ms: 2.62x faster                                              |
| deltablue                | 7.91 ms                                                | 3.10 ms: 2.56x faster                                              |
| richards                 | 79.3 ms                                                | 32.0 ms: 2.48x faster                                              |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                             |
| go                       | 240 ms                                                 | 115 ms: 2.08x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 502 ms: 2.03x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 29.6 us: 1.97x faster                                              |
| pylint                   | 551 ms                                                 | 287 ms: 1.92x faster                                               |
| chaos                    | 115 ms                                                 | 61.0 ms: 1.89x faster                                              |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.87x faster                                               |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                               |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                               |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                               |
| spectral_norm            | 170 ms                                                 | 93.1 ms: 1.83x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 65.8 ms: 1.80x faster                                              |
| float                    | 117 ms                                                 | 65.3 ms: 1.79x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 72.4 ms: 1.77x faster                                              |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.76x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 190 us: 1.74x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.84 sec: 1.71x faster                                             |
| pyflate                  | 716 ms                                                 | 421 ms: 1.70x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.13 ms: 1.70x faster                                              |
| djangocms                | 38.4 us                                                | 23.2 us: 1.65x faster                                              |
| nbody                    | 154 ms                                                 | 94.1 ms: 1.63x faster                                              |
| mako                     | 16.3 ms                                                | 10.6 ms: 1.54x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                              |
| genshi_text              | 31.8 ms                                                | 21.2 ms: 1.50x faster                                              |
| pprint_pformat           | 2.10 sec                                               | 1.41 sec: 1.49x faster                                             |
| pickle_pure_python       | 484 us                                                 | 327 us: 1.48x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 689 ms: 1.48x faster                                               |
| scimark_fft              | 466 ms                                                 | 316 ms: 1.47x faster                                               |
| scimark_lu               | 176 ms                                                 | 120 ms: 1.47x faster                                               |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                               |
| django_template          | 48.2 ms                                                | 32.8 ms: 1.47x faster                                              |
| logging_simple           | 8.30 us                                                | 5.68 us: 1.46x faster                                              |
| logging_format           | 9.09 us                                                | 6.33 us: 1.44x faster                                              |
| xml_etree_process        | 79.1 ms                                                | 55.1 ms: 1.44x faster                                              |
| html5lib                 | 88.9 ms                                                | 61.9 ms: 1.43x faster                                              |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.42x faster                                             |
| dulwich_log              | 84.3 ms                                                | 59.4 ms: 1.42x faster                                              |
| coroutines               | 35.1 ms                                                | 25.0 ms: 1.40x faster                                              |
| thrift                   | 1.07 ms                                                | 775 us: 1.38x faster                                               |
| 2to3                     | 348 ms                                                 | 263 ms: 1.32x faster                                               |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                              |
| genshi_xml               | 66.0 ms                                                | 50.4 ms: 1.31x faster                                              |
| sympy_sum                | 196 ms                                                 | 154 ms: 1.28x faster                                               |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.28x faster                                              |
| nqueens                  | 106 ms                                                 | 83.5 ms: 1.27x faster                                              |
| sympy_str                | 346 ms                                                 | 274 ms: 1.26x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.17 ms: 1.25x faster                                              |
| xml_etree_generate       | 99.4 ms                                                | 79.7 ms: 1.25x faster                                              |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                             |
| regex_v8                 | 27.8 ms                                                | 22.5 ms: 1.23x faster                                              |
| sympy_expand             | 566 ms                                                 | 467 ms: 1.21x faster                                               |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                              |
| pathlib                  | 20.5 ms                                                | 17.1 ms: 1.20x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 98.9 ms: 1.17x faster                                              |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.20 ms: 1.13x faster                                              |
| json_loads               | 31.2 us                                                | 28.1 us: 1.11x faster                                              |
| regex_dna                | 227 ms                                                 | 206 ms: 1.10x faster                                               |
| json                     | 5.69 ms                                                | 5.26 ms: 1.08x faster                                              |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                              |
| async_generators         | 444 ms                                                 | 431 ms: 1.03x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                               |
| pidigits                 | 191 ms                                                 | 201 ms: 1.05x slower                                               |
| coverage                 | 79.4 ms                                                | 88.2 ms: 1.11x slower                                              |
| python_startup_no_site   | 5.93 ms                                                | 6.96 ms: 1.17x slower                                              |
| gc_traversal             | 3.62 ms                                                | 5.13 ms: 1.42x slower                                              |
| create_gc_cycles         | 1.62 ms                                                | 2.63 ms: 1.63x slower                                              |
| telco                    | 7.27 ms                                                | 160 ms: 22.09x slower                                              |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                       |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250702-3.15.0a0-ebec717-JIT/bm-20250702-linux-x86_64-brandtbucher-jit_up_6_12-3.15.0a0-ebec717.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.424x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.38x