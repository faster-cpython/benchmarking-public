# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_guard_float_int_
- machine: linux-x86_64
- commit hash: 602f0e9
- commit date: 2025-03-27
- overall geometric mean: 1.468x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.34x faster                                                         |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                       |
| html5lib       | 88.9 ms                                                | 61.6 ms: 1.44x faster                                                        |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 612 ms: 2.89x faster                                                         |
| async_tree_none         | 728 ms                                                 | 260 ms: 2.80x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.78x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 487 ms: 2.09x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 63.4 ms: 1.85x faster                                                        |
| nbody          | 154 ms                                                 | 86.3 ms: 1.78x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.50x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                                         |
| regex_v8       | 27.8 ms                                                | 23.0 ms: 1.21x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.23 ms: 1.12x faster                                                        |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.20x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.87 sec: 1.68x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 325 us: 1.49x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 56.0 ms: 1.41x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 79.0 ms: 1.26x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                                        |
| json_loads           | 31.2 us                                                | 29.7 us: 1.05x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 8.19 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                        |
| django_template | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                        |
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 49.4 ms: 1.34x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.27x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 612 ms: 2.89x faster                                                         |
| generators               | 80.1 ms                                                | 28.1 ms: 2.85x faster                                                        |
| async_tree_none          | 728 ms                                                 | 260 ms: 2.80x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.78x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.07 ms: 2.58x faster                                                        |
| richards_super           | 94.7 ms                                                | 40.8 ms: 2.32x faster                                                        |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                                       |
| richards                 | 79.3 ms                                                | 35.5 ms: 2.23x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 487 ms: 2.09x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 29.2 us: 2.01x faster                                                        |
| chaos                    | 115 ms                                                 | 58.4 ms: 1.98x faster                                                        |
| pylint                   | 551 ms                                                 | 279 ms: 1.97x faster                                                         |
| logging_silent           | 190 ns                                                 | 96.2 ns: 1.97x faster                                                        |
| raytrace                 | 507 ms                                                 | 266 ms: 1.90x faster                                                         |
| go                       | 240 ms                                                 | 126 ms: 1.90x faster                                                         |
| float                    | 117 ms                                                 | 63.4 ms: 1.85x faster                                                        |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                         |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                         |
| spectral_norm            | 170 ms                                                 | 94.6 ms: 1.80x faster                                                        |
| nbody                    | 154 ms                                                 | 86.3 ms: 1.78x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 67.5 ms: 1.75x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 75.9 ms: 1.68x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.87 sec: 1.68x faster                                                       |
| pyflate                  | 716 ms                                                 | 441 ms: 1.62x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                        |
| hexiom                   | 10.4 ms                                                | 6.69 ms: 1.55x faster                                                        |
| comprehensions           | 28.8 us                                                | 18.7 us: 1.54x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                         |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                        |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                         |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.50x faster                                                        |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                                         |
| django_template          | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.55 us: 1.49x faster                                                        |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 325 us: 1.49x faster                                                         |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                        |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.48 ms: 1.44x faster                                                        |
| html5lib                 | 88.9 ms                                                | 61.6 ms: 1.44x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 56.0 ms: 1.41x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 60.2 ms: 1.40x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                                       |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.1 ms: 1.37x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 49.4 ms: 1.34x faster                                                        |
| 2to3                     | 348 ms                                                 | 261 ms: 1.34x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.60 sec: 1.31x faster                                                       |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 783 ms: 1.30x faster                                                         |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                         |
| fannkuch                 | 532 ms                                                 | 419 ms: 1.27x faster                                                         |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                                         |
| nqueens                  | 106 ms                                                 | 83.7 ms: 1.26x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 79.0 ms: 1.26x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                       |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                        |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 23.0 ms: 1.21x faster                                                        |
| sympy_expand             | 566 ms                                                 | 472 ms: 1.20x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.23 ms: 1.12x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 880 us: 1.12x faster                                                         |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                         |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                        |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                                        |
| async_generators         | 444 ms                                                 | 414 ms: 1.07x faster                                                         |
| json                     | 5.69 ms                                                | 5.34 ms: 1.07x faster                                                        |
| json_loads               | 31.2 us                                                | 29.7 us: 1.05x faster                                                        |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                                         |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                         |
| coverage                 | 79.4 ms                                                | 83.7 ms: 1.05x slower                                                        |
| telco                    | 7.27 ms                                                | 8.02 ms: 1.10x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.76 ms: 1.31x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 8.19 ms: 1.38x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.53x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 83.0 ms: 3.45x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                                 |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250327-3.14.0a6+-602f0e9-JIT/bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.468x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.30x