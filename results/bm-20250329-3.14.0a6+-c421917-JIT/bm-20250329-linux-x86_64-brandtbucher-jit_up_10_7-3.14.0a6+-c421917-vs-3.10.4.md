# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_up_10_7
- machine: linux-x86_64
- commit hash: c421917
- commit date: 2025-03-29
- overall geometric mean: 1.433x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 267 ms: 1.30x faster                                                |
| docutils       | 3.30 sec                                               | 2.71 sec: 1.22x faster                                              |
| html5lib       | 88.9 ms                                                | 63.5 ms: 1.40x faster                                               |
| Geometric mean | (ref)                                                  | 1.30x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 616 ms: 2.87x faster                                                |
| async_tree_none         | 728 ms                                                 | 260 ms: 2.81x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.79x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 486 ms: 2.09x faster                                                |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.5 ms: 1.79x faster                                               |
| nbody          | 154 ms                                                 | 90.2 ms: 1.70x faster                                               |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.46x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                |
| regex_v8       | 27.8 ms                                                | 23.6 ms: 1.18x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.45 ms: 1.05x faster                                               |
| regex_dna      | 227 ms                                                 | 221 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.17x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.89 sec: 1.66x faster                                              |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.55x faster                                                |
| pickle_pure_python   | 484 us                                                 | 325 us: 1.49x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 56.3 ms: 1.40x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 80.3 ms: 1.24x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 98.1 ms: 1.18x faster                                               |
| json_loads           | 31.2 us                                                | 30.2 us: 1.03x faster                                               |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 8.19 ms: 1.38x slower                                               |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.1 ms: 1.50x faster                                               |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                               |
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                               |
| genshi_xml      | 66.0 ms                                                | 49.7 ms: 1.33x faster                                               |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.23x faster                                                |
| async_tree_io            | 1.77 sec                                               | 616 ms: 2.87x faster                                                |
| async_tree_none          | 728 ms                                                 | 260 ms: 2.81x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.79x faster                                                |
| generators               | 80.1 ms                                                | 29.4 ms: 2.72x faster                                               |
| deltablue                | 7.91 ms                                                | 3.04 ms: 2.61x faster                                               |
| richards_super           | 94.7 ms                                                | 40.1 ms: 2.36x faster                                               |
| richards                 | 79.3 ms                                                | 35.8 ms: 2.21x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 486 ms: 2.09x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 28.9 us: 2.02x faster                                               |
| pylint                   | 551 ms                                                 | 285 ms: 1.94x faster                                                |
| logging_silent           | 190 ns                                                 | 98.5 ns: 1.93x faster                                               |
| chaos                    | 115 ms                                                 | 60.5 ms: 1.91x faster                                               |
| raytrace                 | 507 ms                                                 | 269 ms: 1.89x faster                                                |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                |
| go                       | 240 ms                                                 | 132 ms: 1.82x faster                                                |
| deepcopy                 | 479 us                                                 | 266 us: 1.80x faster                                                |
| spectral_norm            | 170 ms                                                 | 94.9 ms: 1.79x faster                                               |
| float                    | 117 ms                                                 | 65.5 ms: 1.79x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 69.0 ms: 1.71x faster                                               |
| nbody                    | 154 ms                                                 | 90.2 ms: 1.70x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 76.4 ms: 1.67x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.89 sec: 1.66x faster                                              |
| pyflate                  | 716 ms                                                 | 436 ms: 1.64x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.55x faster                                                |
| comprehensions           | 28.8 us                                                | 19.0 us: 1.51x faster                                               |
| django_template          | 48.2 ms                                                | 32.1 ms: 1.50x faster                                               |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 2.80 us: 1.49x faster                                               |
| pickle_pure_python       | 484 us                                                 | 325 us: 1.49x faster                                                |
| logging_simple           | 8.30 us                                                | 5.57 us: 1.49x faster                                               |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                               |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                               |
| hexiom                   | 10.4 ms                                                | 7.04 ms: 1.48x faster                                               |
| logging_format           | 9.09 us                                                | 6.17 us: 1.47x faster                                               |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 56.3 ms: 1.40x faster                                               |
| html5lib                 | 88.9 ms                                                | 63.5 ms: 1.40x faster                                               |
| dulwich_log              | 84.3 ms                                                | 60.4 ms: 1.40x faster                                               |
| thrift                   | 1.07 ms                                                | 778 us: 1.38x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.78 ms: 1.35x faster                                               |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                              |
| pprint_pformat           | 2.10 sec                                               | 1.58 sec: 1.33x faster                                              |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.6 ms: 1.33x faster                                               |
| genshi_xml               | 66.0 ms                                                | 49.7 ms: 1.33x faster                                               |
| 2to3                     | 348 ms                                                 | 267 ms: 1.30x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 783 ms: 1.30x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 20.4 ms: 1.27x faster                                               |
| fannkuch                 | 532 ms                                                 | 422 ms: 1.26x faster                                                |
| sympy_sum                | 196 ms                                                 | 156 ms: 1.26x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 137 ms: 1.25x faster                                                |
| sympy_str                | 346 ms                                                 | 279 ms: 1.24x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 80.3 ms: 1.24x faster                                               |
| nqueens                  | 106 ms                                                 | 86.1 ms: 1.23x faster                                               |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.22x faster                                               |
| docutils                 | 3.30 sec                                               | 2.71 sec: 1.22x faster                                              |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 98.1 ms: 1.18x faster                                               |
| regex_v8                 | 27.8 ms                                                | 23.6 ms: 1.18x faster                                               |
| sympy_expand             | 566 ms                                                 | 481 ms: 1.18x faster                                                |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                               |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                              |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                               |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                |
| bench_thread_pool        | 986 us                                                 | 892 us: 1.11x faster                                                |
| async_generators         | 444 ms                                                 | 414 ms: 1.07x faster                                                |
| json                     | 5.69 ms                                                | 5.34 ms: 1.07x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.45 ms: 1.05x faster                                               |
| json_loads               | 31.2 us                                                | 30.2 us: 1.03x faster                                               |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                |
| regex_dna                | 227 ms                                                 | 221 ms: 1.02x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                |
| telco                    | 7.27 ms                                                | 7.82 ms: 1.08x slower                                               |
| coverage                 | 79.4 ms                                                | 85.8 ms: 1.08x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.98 ms: 1.37x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 8.19 ms: 1.38x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.54x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 82.9 ms: 3.45x slower                                               |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                        |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250329-3.14.0a6+-c421917-JIT/bm-20250329-linux-x86_64-brandtbucher-jit_up_10_7-3.14.0a6+-c421917.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.433x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.30x