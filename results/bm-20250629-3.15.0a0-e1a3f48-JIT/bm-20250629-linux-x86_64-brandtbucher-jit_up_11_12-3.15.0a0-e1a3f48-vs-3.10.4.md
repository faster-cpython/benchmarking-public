# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_11_12
- machine: linux-x86_64
- commit hash: e1a3f48
- commit date: 2025-06-29
- overall geometric mean: 1.485x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                              |
| html5lib       | 88.9 ms                                                | 62.2 ms: 1.43x faster                                               |
| Geometric mean | (ref)                                                  | 1.34x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 607 ms: 2.92x faster                                                |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 314 ms: 2.77x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 500 ms: 2.03x faster                                                |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 66.0 ms: 1.78x faster                                               |
| nbody          | 154 ms                                                 | 96.1 ms: 1.60x faster                                               |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.42x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                                |
| regex_v8       | 27.8 ms                                                | 22.3 ms: 1.25x faster                                               |
| regex_dna      | 227 ms                                                 | 200 ms: 1.13x faster                                                |
| regex_effbot   | 3.63 ms                                                | 3.23 ms: 1.12x faster                                               |
| Geometric mean | (ref)                                                  | 1.24x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 190 us: 1.74x faster                                                |
| tomli_loads          | 3.14 sec                                               | 1.81 sec: 1.74x faster                                              |
| pickle_pure_python   | 484 us                                                 | 324 us: 1.49x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 56.6 ms: 1.40x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.0 ms: 1.29x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 81.2 ms: 1.22x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                               |
| json_loads           | 31.2 us                                                | 28.4 us: 1.10x faster                                               |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 6.94 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.6 ms: 1.53x faster                                               |
| django_template | 48.2 ms                                                | 32.8 ms: 1.47x faster                                               |
| genshi_text     | 31.8 ms                                                | 21.8 ms: 1.46x faster                                               |
| genshi_xml      | 66.0 ms                                                | 50.7 ms: 1.30x faster                                               |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                |
| async_tree_io            | 1.77 sec                                               | 607 ms: 2.92x faster                                                |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 314 ms: 2.77x faster                                                |
| deltablue                | 7.91 ms                                                | 3.02 ms: 2.62x faster                                               |
| generators               | 80.1 ms                                                | 31.3 ms: 2.56x faster                                               |
| richards_super           | 94.7 ms                                                | 39.8 ms: 2.38x faster                                               |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.33x faster                                              |
| richards                 | 79.3 ms                                                | 34.7 ms: 2.28x faster                                               |
| go                       | 240 ms                                                 | 115 ms: 2.09x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 500 ms: 2.03x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                               |
| pylint                   | 551 ms                                                 | 284 ms: 1.94x faster                                                |
| chaos                    | 115 ms                                                 | 61.0 ms: 1.89x faster                                               |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                                |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.87x faster                                                |
| spectral_norm            | 170 ms                                                 | 91.7 ms: 1.85x faster                                               |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 65.3 ms: 1.81x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 71.7 ms: 1.78x faster                                               |
| float                    | 117 ms                                                 | 66.0 ms: 1.78x faster                                               |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                               |
| unpickle_pure_python     | 331 us                                                 | 190 us: 1.74x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.81 sec: 1.74x faster                                              |
| djangocms                | 38.4 us                                                | 22.5 us: 1.71x faster                                               |
| pyflate                  | 716 ms                                                 | 420 ms: 1.70x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.21 ms: 1.68x faster                                               |
| nbody                    | 154 ms                                                 | 96.1 ms: 1.60x faster                                               |
| mako                     | 16.3 ms                                                | 10.6 ms: 1.53x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                               |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                                |
| pickle_pure_python       | 484 us                                                 | 324 us: 1.49x faster                                                |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                                |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                               |
| django_template          | 48.2 ms                                                | 32.8 ms: 1.47x faster                                               |
| genshi_text              | 31.8 ms                                                | 21.8 ms: 1.46x faster                                               |
| logging_format           | 9.09 us                                                | 6.26 us: 1.45x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 708 ms: 1.44x faster                                                |
| html5lib                 | 88.9 ms                                                | 62.2 ms: 1.43x faster                                               |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.41x faster                                              |
| dulwich_log              | 84.3 ms                                                | 59.9 ms: 1.41x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 56.6 ms: 1.40x faster                                               |
| coroutines               | 35.1 ms                                                | 25.1 ms: 1.39x faster                                               |
| thrift                   | 1.07 ms                                                | 779 us: 1.37x faster                                                |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                |
| fannkuch                 | 532 ms                                                 | 396 ms: 1.34x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.88 ms: 1.33x faster                                               |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                |
| genshi_xml               | 66.0 ms                                                | 50.7 ms: 1.30x faster                                               |
| json_dumps               | 14.2 ms                                                | 11.0 ms: 1.29x faster                                               |
| nqueens                  | 106 ms                                                 | 82.1 ms: 1.29x faster                                               |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                                |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                              |
| regex_v8                 | 27.8 ms                                                | 22.3 ms: 1.25x faster                                               |
| xml_etree_generate       | 99.4 ms                                                | 81.2 ms: 1.22x faster                                               |
| sympy_expand             | 566 ms                                                 | 466 ms: 1.21x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                               |
| regex_dna                | 227 ms                                                 | 200 ms: 1.13x faster                                                |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.23 ms: 1.12x faster                                               |
| json_loads               | 31.2 us                                                | 28.4 us: 1.10x faster                                               |
| json                     | 5.69 ms                                                | 5.23 ms: 1.09x faster                                               |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                               |
| async_generators         | 444 ms                                                 | 432 ms: 1.03x faster                                                |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                |
| telco                    | 7.27 ms                                                | 7.82 ms: 1.08x slower                                               |
| coverage                 | 79.4 ms                                                | 88.2 ms: 1.11x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 6.94 ms: 1.17x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.78 ms: 1.32x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                               |
| Geometric mean           | (ref)                                                  | 1.49x faster                                                        |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250629-3.15.0a0-e1a3f48-JIT/bm-20250629-linux-x86_64-brandtbucher-jit_up_11_12-3.15.0a0-e1a3f48.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.485x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.34x

# Memory
- memory change: 1.33x