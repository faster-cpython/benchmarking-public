# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_11_9
- machine: linux-x86_64
- commit hash: 50321ce
- commit date: 2025-06-30
- overall geometric mean: 1.488x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.34x faster                                               |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                             |
| html5lib       | 88.9 ms                                                | 62.3 ms: 1.43x faster                                              |
| Geometric mean | (ref)                                                  | 1.34x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 600 ms: 2.95x faster                                               |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                               |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.78x faster                                               |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 492 ms: 2.06x faster                                               |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 117 ms                                                 | 66.2 ms: 1.77x faster                                              |
| nbody          | 154 ms                                                 | 95.8 ms: 1.60x faster                                              |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.42x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                               |
| regex_v8       | 27.8 ms                                                | 22.6 ms: 1.23x faster                                              |
| regex_effbot   | 3.63 ms                                                | 3.14 ms: 1.16x faster                                              |
| regex_dna      | 227 ms                                                 | 198 ms: 1.14x faster                                               |
| Geometric mean | (ref)                                                  | 1.24x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.82 sec: 1.72x faster                                             |
| unpickle_pure_python | 331 us                                                 | 192 us: 1.72x faster                                               |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 55.4 ms: 1.43x faster                                              |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.27x faster                                              |
| xml_etree_generate   | 99.4 ms                                                | 79.8 ms: 1.25x faster                                              |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                              |
| json_loads           | 31.2 us                                                | 28.4 us: 1.10x faster                                              |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                              |
| python_startup_no_site | 5.93 ms                                                | 6.94 ms: 1.17x slower                                              |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.5 ms: 1.56x faster                                              |
| django_template | 48.2 ms                                                | 32.4 ms: 1.49x faster                                              |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                              |
| genshi_xml      | 66.0 ms                                                | 49.7 ms: 1.33x faster                                              |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.25x faster                                               |
| async_tree_io            | 1.77 sec                                               | 600 ms: 2.95x faster                                               |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.78x faster                                               |
| generators               | 80.1 ms                                                | 30.0 ms: 2.67x faster                                              |
| deltablue                | 7.91 ms                                                | 3.03 ms: 2.61x faster                                              |
| richards_super           | 94.7 ms                                                | 39.7 ms: 2.38x faster                                              |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                             |
| richards                 | 79.3 ms                                                | 34.7 ms: 2.29x faster                                              |
| go                       | 240 ms                                                 | 116 ms: 2.08x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 492 ms: 2.06x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 29.6 us: 1.97x faster                                              |
| pylint                   | 551 ms                                                 | 283 ms: 1.95x faster                                               |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                               |
| chaos                    | 115 ms                                                 | 61.8 ms: 1.87x faster                                              |
| deepcopy                 | 479 us                                                 | 260 us: 1.85x faster                                               |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                               |
| spectral_norm            | 170 ms                                                 | 92.6 ms: 1.83x faster                                              |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 65.3 ms: 1.81x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 70.8 ms: 1.81x faster                                              |
| float                    | 117 ms                                                 | 66.2 ms: 1.77x faster                                              |
| comprehensions           | 28.8 us                                                | 16.3 us: 1.76x faster                                              |
| tomli_loads              | 3.14 sec                                               | 1.82 sec: 1.72x faster                                             |
| unpickle_pure_python     | 331 us                                                 | 192 us: 1.72x faster                                               |
| pyflate                  | 716 ms                                                 | 417 ms: 1.72x faster                                               |
| djangocms                | 38.4 us                                                | 22.6 us: 1.70x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.21 ms: 1.68x faster                                              |
| nbody                    | 154 ms                                                 | 95.8 ms: 1.60x faster                                              |
| mako                     | 16.3 ms                                                | 10.5 ms: 1.56x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                              |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                               |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                               |
| scimark_fft              | 466 ms                                                 | 308 ms: 1.51x faster                                               |
| django_template          | 48.2 ms                                                | 32.4 ms: 1.49x faster                                              |
| logging_simple           | 8.30 us                                                | 5.60 us: 1.48x faster                                              |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                              |
| pprint_pformat           | 2.10 sec                                               | 1.43 sec: 1.47x faster                                             |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                               |
| logging_format           | 9.09 us                                                | 6.20 us: 1.47x faster                                              |
| xml_etree_process        | 79.1 ms                                                | 55.4 ms: 1.43x faster                                              |
| html5lib                 | 88.9 ms                                                | 62.3 ms: 1.43x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 715 ms: 1.42x faster                                               |
| dulwich_log              | 84.3 ms                                                | 59.5 ms: 1.42x faster                                              |
| thrift                   | 1.07 ms                                                | 761 us: 1.41x faster                                               |
| coroutines               | 35.1 ms                                                | 25.0 ms: 1.40x faster                                              |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.38x faster                                             |
| 2to3                     | 348 ms                                                 | 259 ms: 1.34x faster                                               |
| fannkuch                 | 532 ms                                                 | 397 ms: 1.34x faster                                               |
| genshi_xml               | 66.0 ms                                                | 49.7 ms: 1.33x faster                                              |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.92 ms: 1.32x faster                                              |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.30x faster                                               |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                               |
| nqueens                  | 106 ms                                                 | 83.2 ms: 1.27x faster                                              |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.27x faster                                              |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                             |
| xml_etree_generate       | 99.4 ms                                                | 79.8 ms: 1.25x faster                                              |
| regex_v8                 | 27.8 ms                                                | 22.6 ms: 1.23x faster                                              |
| sympy_expand             | 566 ms                                                 | 465 ms: 1.22x faster                                               |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                               |
| pathlib                  | 20.5 ms                                                | 17.2 ms: 1.19x faster                                              |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                              |
| regex_effbot             | 3.63 ms                                                | 3.14 ms: 1.16x faster                                              |
| regex_dna                | 227 ms                                                 | 198 ms: 1.14x faster                                               |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                               |
| json_loads               | 31.2 us                                                | 28.4 us: 1.10x faster                                              |
| json                     | 5.69 ms                                                | 5.26 ms: 1.08x faster                                              |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                              |
| async_generators         | 444 ms                                                 | 431 ms: 1.03x faster                                               |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                               |
| telco                    | 7.27 ms                                                | 7.72 ms: 1.06x slower                                              |
| coverage                 | 79.4 ms                                                | 87.2 ms: 1.10x slower                                              |
| python_startup_no_site   | 5.93 ms                                                | 6.94 ms: 1.17x slower                                              |
| gc_traversal             | 3.62 ms                                                | 4.97 ms: 1.37x slower                                              |
| create_gc_cycles         | 1.62 ms                                                | 2.58 ms: 1.59x slower                                              |
| Geometric mean           | (ref)                                                  | 1.49x faster                                                       |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250630-3.15.0a0-50321ce-JIT/bm-20250630-linux-x86_64-brandtbucher-jit_up_11_9-3.15.0a0-50321ce.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.488x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.34x

# Memory
- memory change: 1.33x