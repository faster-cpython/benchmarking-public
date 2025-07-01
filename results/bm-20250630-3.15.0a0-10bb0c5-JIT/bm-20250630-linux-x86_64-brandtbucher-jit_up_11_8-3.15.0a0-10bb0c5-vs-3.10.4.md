# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_11_8
- machine: linux-x86_64
- commit hash: 10bb0c5
- commit date: 2025-06-30
- overall geometric mean: 1.483x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.34x faster                                               |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                             |
| html5lib       | 88.9 ms                                                | 62.4 ms: 1.42x faster                                              |
| Geometric mean | (ref)                                                  | 1.33x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 601 ms: 2.94x faster                                               |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.78x faster                                               |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                               |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                               |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.4 ms: 1.79x faster                                              |
| nbody          | 154 ms                                                 | 93.1 ms: 1.65x faster                                              |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.44x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                               |
| regex_v8       | 27.8 ms                                                | 22.8 ms: 1.22x faster                                              |
| regex_dna      | 227 ms                                                 | 208 ms: 1.09x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.42 ms: 1.06x faster                                              |
| Geometric mean | (ref)                                                  | 1.20x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.80 sec: 1.74x faster                                             |
| unpickle_pure_python | 331 us                                                 | 192 us: 1.73x faster                                               |
| pickle_pure_python   | 484 us                                                 | 324 us: 1.50x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 56.3 ms: 1.40x faster                                              |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.28x faster                                              |
| xml_etree_generate   | 99.4 ms                                                | 80.9 ms: 1.23x faster                                              |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                              |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                              |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.19x faster                                              |
| python_startup_no_site | 5.93 ms                                                | 6.94 ms: 1.17x slower                                              |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.5 ms: 1.56x faster                                              |
| genshi_text     | 31.8 ms                                                | 21.2 ms: 1.50x faster                                              |
| django_template | 48.2 ms                                                | 33.1 ms: 1.46x faster                                              |
| genshi_xml      | 66.0 ms                                                | 49.7 ms: 1.33x faster                                              |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.25x faster                                               |
| async_tree_io            | 1.77 sec                                               | 601 ms: 2.94x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.78x faster                                               |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                               |
| deltablue                | 7.91 ms                                                | 3.06 ms: 2.59x faster                                              |
| generators               | 80.1 ms                                                | 31.6 ms: 2.53x faster                                              |
| richards_super           | 94.7 ms                                                | 40.7 ms: 2.33x faster                                              |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.30x faster                                             |
| richards                 | 79.3 ms                                                | 36.2 ms: 2.19x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                               |
| go                       | 240 ms                                                 | 117 ms: 2.05x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 29.6 us: 1.97x faster                                              |
| pylint                   | 551 ms                                                 | 283 ms: 1.95x faster                                               |
| spectral_norm            | 170 ms                                                 | 90.1 ms: 1.89x faster                                              |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                               |
| chaos                    | 115 ms                                                 | 61.6 ms: 1.87x faster                                              |
| deepcopy                 | 479 us                                                 | 260 us: 1.85x faster                                               |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 65.0 ms: 1.82x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 70.8 ms: 1.80x faster                                              |
| logging_silent           | 190 ns                                                 | 105 ns: 1.80x faster                                               |
| float                    | 117 ms                                                 | 65.4 ms: 1.79x faster                                              |
| comprehensions           | 28.8 us                                                | 16.3 us: 1.76x faster                                              |
| pyflate                  | 716 ms                                                 | 410 ms: 1.75x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.80 sec: 1.74x faster                                             |
| unpickle_pure_python     | 331 us                                                 | 192 us: 1.73x faster                                               |
| djangocms                | 38.4 us                                                | 22.4 us: 1.72x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.16 ms: 1.69x faster                                              |
| nbody                    | 154 ms                                                 | 93.1 ms: 1.65x faster                                              |
| mako                     | 16.3 ms                                                | 10.5 ms: 1.56x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.55x faster                                              |
| scimark_fft              | 466 ms                                                 | 307 ms: 1.52x faster                                               |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                               |
| genshi_text              | 31.8 ms                                                | 21.2 ms: 1.50x faster                                              |
| pickle_pure_python       | 484 us                                                 | 324 us: 1.50x faster                                               |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                               |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                              |
| logging_format           | 9.09 us                                                | 6.22 us: 1.46x faster                                              |
| django_template          | 48.2 ms                                                | 33.1 ms: 1.46x faster                                              |
| html5lib                 | 88.9 ms                                                | 62.4 ms: 1.42x faster                                              |
| dulwich_log              | 84.3 ms                                                | 59.3 ms: 1.42x faster                                              |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                             |
| xml_etree_process        | 79.1 ms                                                | 56.3 ms: 1.40x faster                                              |
| thrift                   | 1.07 ms                                                | 766 us: 1.40x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 729 ms: 1.40x faster                                               |
| coroutines               | 35.1 ms                                                | 25.3 ms: 1.39x faster                                              |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                             |
| fannkuch                 | 532 ms                                                 | 395 ms: 1.35x faster                                               |
| 2to3                     | 348 ms                                                 | 261 ms: 1.34x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.84 ms: 1.34x faster                                              |
| genshi_xml               | 66.0 ms                                                | 49.7 ms: 1.33x faster                                              |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                              |
| nqueens                  | 106 ms                                                 | 80.7 ms: 1.31x faster                                              |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.30x faster                                               |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.28x faster                                              |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                               |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                             |
| xml_etree_generate       | 99.4 ms                                                | 80.9 ms: 1.23x faster                                              |
| regex_v8                 | 27.8 ms                                                | 22.8 ms: 1.22x faster                                              |
| sympy_expand             | 566 ms                                                 | 466 ms: 1.21x faster                                               |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                              |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.19x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                              |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                              |
| regex_dna                | 227 ms                                                 | 208 ms: 1.09x faster                                               |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                              |
| json                     | 5.69 ms                                                | 5.36 ms: 1.06x faster                                              |
| regex_effbot             | 3.63 ms                                                | 3.42 ms: 1.06x faster                                              |
| async_generators         | 444 ms                                                 | 428 ms: 1.04x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                               |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                               |
| telco                    | 7.27 ms                                                | 7.70 ms: 1.06x slower                                              |
| coverage                 | 79.4 ms                                                | 87.9 ms: 1.11x slower                                              |
| python_startup_no_site   | 5.93 ms                                                | 6.94 ms: 1.17x slower                                              |
| gc_traversal             | 3.62 ms                                                | 4.98 ms: 1.37x slower                                              |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                              |
| Geometric mean           | (ref)                                                  | 1.49x faster                                                       |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250630-3.15.0a0-10bb0c5-JIT/bm-20250630-linux-x86_64-brandtbucher-jit_up_11_8-3.15.0a0-10bb0c5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.483x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.33x