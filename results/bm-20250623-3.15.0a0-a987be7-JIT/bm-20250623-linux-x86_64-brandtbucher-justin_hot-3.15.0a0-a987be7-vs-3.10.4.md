# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_hot
- machine: linux-x86_64
- commit hash: a987be7
- commit date: 2025-06-23
- overall geometric mean: 1.476x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.34x faster                                              |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                            |
| html5lib       | 88.9 ms                                                | 61.9 ms: 1.43x faster                                             |
| Geometric mean | (ref)                                                  | 1.34x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 598 ms: 2.96x faster                                              |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                              |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.78x faster                                              |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 495 ms: 2.05x faster                                              |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.0 ms: 1.80x faster                                             |
| nbody          | 154 ms                                                 | 96.0 ms: 1.60x faster                                             |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.43x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                              |
| regex_v8       | 27.8 ms                                                | 22.5 ms: 1.23x faster                                             |
| regex_dna      | 227 ms                                                 | 199 ms: 1.14x faster                                              |
| regex_effbot   | 3.63 ms                                                | 3.25 ms: 1.12x faster                                             |
| Geometric mean | (ref)                                                  | 1.24x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 195 us: 1.70x faster                                              |
| tomli_loads          | 3.14 sec                                               | 1.86 sec: 1.69x faster                                            |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.51x faster                                              |
| xml_etree_process    | 79.1 ms                                                | 55.4 ms: 1.43x faster                                             |
| json_dumps           | 14.2 ms                                                | 10.9 ms: 1.30x faster                                             |
| xml_etree_generate   | 99.4 ms                                                | 80.0 ms: 1.24x faster                                             |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                              |
| xml_etree_iterparse  | 115 ms                                                 | 98.3 ms: 1.17x faster                                             |
| json_loads           | 31.2 us                                                | 28.2 us: 1.11x faster                                             |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                             |
| python_startup_no_site | 5.93 ms                                                | 6.93 ms: 1.17x slower                                             |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.4 ms: 1.56x faster                                             |
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                             |
| django_template | 48.2 ms                                                | 32.4 ms: 1.49x faster                                             |
| genshi_xml      | 66.0 ms                                                | 50.4 ms: 1.31x faster                                             |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.22x faster                                              |
| async_tree_io            | 1.77 sec                                               | 598 ms: 2.96x faster                                              |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                              |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.78x faster                                              |
| generators               | 80.1 ms                                                | 30.4 ms: 2.63x faster                                             |
| deltablue                | 7.91 ms                                                | 3.06 ms: 2.58x faster                                             |
| richards_super           | 94.7 ms                                                | 38.6 ms: 2.45x faster                                             |
| richards                 | 79.3 ms                                                | 32.9 ms: 2.41x faster                                             |
| mdp                      | 2.85 sec                                               | 1.25 sec: 2.29x faster                                            |
| go                       | 240 ms                                                 | 117 ms: 2.05x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 495 ms: 2.05x faster                                              |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.97x faster                                             |
| pylint                   | 551 ms                                                 | 282 ms: 1.95x faster                                              |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                              |
| chaos                    | 115 ms                                                 | 62.3 ms: 1.85x faster                                             |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                              |
| float                    | 117 ms                                                 | 65.0 ms: 1.80x faster                                             |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.79x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 66.5 ms: 1.78x faster                                             |
| comprehensions           | 28.8 us                                                | 16.3 us: 1.76x faster                                             |
| pyflate                  | 716 ms                                                 | 406 ms: 1.76x faster                                              |
| djangocms                | 38.4 us                                                | 22.0 us: 1.74x faster                                             |
| crypto_pyaes             | 128 ms                                                 | 74.4 ms: 1.72x faster                                             |
| unpickle_pure_python     | 331 us                                                 | 195 us: 1.70x faster                                              |
| tomli_loads              | 3.14 sec                                               | 1.86 sec: 1.69x faster                                            |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.66x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.30 ms: 1.65x faster                                             |
| nbody                    | 154 ms                                                 | 96.0 ms: 1.60x faster                                             |
| mako                     | 16.3 ms                                                | 10.4 ms: 1.56x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                             |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.51x faster                                              |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                             |
| django_template          | 48.2 ms                                                | 32.4 ms: 1.49x faster                                             |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                              |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                              |
| html5lib                 | 88.9 ms                                                | 61.9 ms: 1.43x faster                                             |
| xml_etree_process        | 79.1 ms                                                | 55.4 ms: 1.43x faster                                             |
| scimark_fft              | 466 ms                                                 | 328 ms: 1.42x faster                                              |
| dulwich_log              | 84.3 ms                                                | 59.6 ms: 1.41x faster                                             |
| coroutines               | 35.1 ms                                                | 24.9 ms: 1.41x faster                                             |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                            |
| thrift                   | 1.07 ms                                                | 781 us: 1.37x faster                                              |
| logging_simple           | 8.30 us                                                | 6.11 us: 1.36x faster                                             |
| logging_format           | 9.09 us                                                | 6.74 us: 1.35x faster                                             |
| 2to3                     | 348 ms                                                 | 259 ms: 1.34x faster                                              |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                             |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                              |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                              |
| genshi_xml               | 66.0 ms                                                | 50.4 ms: 1.31x faster                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.94 ms: 1.31x faster                                             |
| json_dumps               | 14.2 ms                                                | 10.9 ms: 1.30x faster                                             |
| pprint_pformat           | 2.10 sec                                               | 1.64 sec: 1.28x faster                                            |
| nqueens                  | 106 ms                                                 | 82.6 ms: 1.28x faster                                             |
| sympy_str                | 346 ms                                                 | 271 ms: 1.28x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 804 ms: 1.27x faster                                              |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                            |
| xml_etree_generate       | 99.4 ms                                                | 80.0 ms: 1.24x faster                                             |
| regex_v8                 | 27.8 ms                                                | 22.5 ms: 1.23x faster                                             |
| sympy_expand             | 566 ms                                                 | 466 ms: 1.21x faster                                              |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.21x faster                                             |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                             |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                              |
| xml_etree_iterparse      | 115 ms                                                 | 98.3 ms: 1.17x faster                                             |
| regex_dna                | 227 ms                                                 | 199 ms: 1.14x faster                                              |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                              |
| regex_effbot             | 3.63 ms                                                | 3.25 ms: 1.12x faster                                             |
| json_loads               | 31.2 us                                                | 28.2 us: 1.11x faster                                             |
| json                     | 5.69 ms                                                | 5.23 ms: 1.09x faster                                             |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                             |
| async_generators         | 444 ms                                                 | 431 ms: 1.03x faster                                              |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                              |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                              |
| telco                    | 7.27 ms                                                | 7.59 ms: 1.04x slower                                             |
| coverage                 | 79.4 ms                                                | 87.0 ms: 1.10x slower                                             |
| python_startup_no_site   | 5.93 ms                                                | 6.93 ms: 1.17x slower                                             |
| gc_traversal             | 3.62 ms                                                | 4.97 ms: 1.37x slower                                             |
| create_gc_cycles         | 1.62 ms                                                | 2.60 ms: 1.60x slower                                             |
| logging_silent           | 190 ns                                                 | 472 ns: 2.49x slower                                              |
| Geometric mean           | (ref)                                                  | 1.45x faster                                                      |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250623-3.15.0a0-a987be7-JIT/bm-20250623-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-a987be7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.476x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.33x