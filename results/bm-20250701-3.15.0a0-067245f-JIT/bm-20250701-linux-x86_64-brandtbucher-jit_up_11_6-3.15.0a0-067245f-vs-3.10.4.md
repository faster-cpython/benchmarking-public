# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_11_6
- machine: linux-x86_64
- commit hash: 067245f
- commit date: 2025-07-01
- overall geometric mean: 1.486x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.34x faster                                               |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                             |
| html5lib       | 88.9 ms                                                | 61.9 ms: 1.43x faster                                              |
| Geometric mean | (ref)                                                  | 1.34x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 602 ms: 2.94x faster                                               |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.77x faster                                               |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.76x faster                                               |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 494 ms: 2.06x faster                                               |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.6 ms: 1.79x faster                                              |
| nbody          | 154 ms                                                 | 93.6 ms: 1.64x faster                                              |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.44x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                               |
| regex_v8       | 27.8 ms                                                | 23.8 ms: 1.17x faster                                              |
| regex_effbot   | 3.63 ms                                                | 3.43 ms: 1.06x faster                                              |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.18x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 190 us: 1.74x faster                                               |
| tomli_loads          | 3.14 sec                                               | 1.82 sec: 1.73x faster                                             |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.50x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 55.8 ms: 1.42x faster                                              |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.29x faster                                              |
| xml_etree_generate   | 99.4 ms                                                | 80.2 ms: 1.24x faster                                              |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.19x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 99.3 ms: 1.16x faster                                              |
| json_loads           | 31.2 us                                                | 28.0 us: 1.12x faster                                              |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.19x faster                                              |
| python_startup_no_site | 5.93 ms                                                | 6.95 ms: 1.17x slower                                              |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.4 ms: 1.56x faster                                              |
| django_template | 48.2 ms                                                | 32.4 ms: 1.49x faster                                              |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                              |
| genshi_xml      | 66.0 ms                                                | 50.1 ms: 1.32x faster                                              |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                               |
| async_tree_io            | 1.77 sec                                               | 602 ms: 2.94x faster                                               |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.77x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.76x faster                                               |
| generators               | 80.1 ms                                                | 30.2 ms: 2.65x faster                                              |
| deltablue                | 7.91 ms                                                | 3.04 ms: 2.60x faster                                              |
| richards_super           | 94.7 ms                                                | 38.9 ms: 2.43x faster                                              |
| richards                 | 79.3 ms                                                | 33.7 ms: 2.35x faster                                              |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.31x faster                                             |
| go                       | 240 ms                                                 | 114 ms: 2.11x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 494 ms: 2.06x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                              |
| pylint                   | 551 ms                                                 | 284 ms: 1.94x faster                                               |
| spectral_norm            | 170 ms                                                 | 90.0 ms: 1.89x faster                                              |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                               |
| chaos                    | 115 ms                                                 | 61.5 ms: 1.88x faster                                              |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.87x faster                                               |
| deepcopy                 | 479 us                                                 | 257 us: 1.86x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 65.0 ms: 1.82x faster                                              |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                               |
| float                    | 117 ms                                                 | 65.6 ms: 1.79x faster                                              |
| comprehensions           | 28.8 us                                                | 16.3 us: 1.77x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 72.8 ms: 1.75x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 190 us: 1.74x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.82 sec: 1.73x faster                                             |
| pyflate                  | 716 ms                                                 | 415 ms: 1.72x faster                                               |
| djangocms                | 38.4 us                                                | 22.6 us: 1.70x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.25 ms: 1.66x faster                                              |
| nbody                    | 154 ms                                                 | 93.6 ms: 1.64x faster                                              |
| mako                     | 16.3 ms                                                | 10.4 ms: 1.56x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                              |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.50x faster                                               |
| logging_simple           | 8.30 us                                                | 5.53 us: 1.50x faster                                              |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                               |
| django_template          | 48.2 ms                                                | 32.4 ms: 1.49x faster                                              |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                               |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 691 ms: 1.47x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.43 sec: 1.47x faster                                             |
| scimark_lu               | 176 ms                                                 | 120 ms: 1.47x faster                                               |
| logging_format           | 9.09 us                                                | 6.21 us: 1.46x faster                                              |
| html5lib                 | 88.9 ms                                                | 61.9 ms: 1.43x faster                                              |
| xml_etree_process        | 79.1 ms                                                | 55.8 ms: 1.42x faster                                              |
| dulwich_log              | 84.3 ms                                                | 60.0 ms: 1.40x faster                                              |
| coroutines               | 35.1 ms                                                | 25.4 ms: 1.38x faster                                              |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                             |
| thrift                   | 1.07 ms                                                | 779 us: 1.38x faster                                               |
| 2to3                     | 348 ms                                                 | 261 ms: 1.34x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.87 ms: 1.33x faster                                              |
| fannkuch                 | 532 ms                                                 | 401 ms: 1.33x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                              |
| genshi_xml               | 66.0 ms                                                | 50.1 ms: 1.32x faster                                              |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.31x faster                                               |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.29x faster                                              |
| nqueens                  | 106 ms                                                 | 82.4 ms: 1.28x faster                                              |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                               |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                             |
| xml_etree_generate       | 99.4 ms                                                | 80.2 ms: 1.24x faster                                              |
| sympy_expand             | 566 ms                                                 | 467 ms: 1.21x faster                                               |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.19x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.19x faster                                               |
| pathlib                  | 20.5 ms                                                | 17.2 ms: 1.19x faster                                              |
| regex_v8                 | 27.8 ms                                                | 23.8 ms: 1.17x faster                                              |
| xml_etree_iterparse      | 115 ms                                                 | 99.3 ms: 1.16x faster                                              |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                               |
| json_loads               | 31.2 us                                                | 28.0 us: 1.12x faster                                              |
| json                     | 5.69 ms                                                | 5.17 ms: 1.10x faster                                              |
| sqlite_synth             | 3.02 us                                                | 2.82 us: 1.07x faster                                              |
| regex_effbot             | 3.63 ms                                                | 3.43 ms: 1.06x faster                                              |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                               |
| async_generators         | 444 ms                                                 | 424 ms: 1.05x faster                                               |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                               |
| telco                    | 7.27 ms                                                | 7.75 ms: 1.07x slower                                              |
| coverage                 | 79.4 ms                                                | 87.4 ms: 1.10x slower                                              |
| python_startup_no_site   | 5.93 ms                                                | 6.95 ms: 1.17x slower                                              |
| gc_traversal             | 3.62 ms                                                | 4.87 ms: 1.35x slower                                              |
| create_gc_cycles         | 1.62 ms                                                | 2.57 ms: 1.59x slower                                              |
| Geometric mean           | (ref)                                                  | 1.49x faster                                                       |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250701-3.15.0a0-067245f-JIT/bm-20250701-linux-x86_64-brandtbucher-jit_up_11_6-3.15.0a0-067245f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.486x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.33x