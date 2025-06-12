# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_hot
- machine: linux-x86_64
- commit hash: 858624a
- commit date: 2025-06-12
- overall geometric mean: 1.337x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                              |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.25x faster                                            |
| html5lib       | 88.9 ms                                                | 62.3 ms: 1.43x faster                                             |
| Geometric mean | (ref)                                                  | 1.33x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 597 ms: 2.96x faster                                              |
| async_tree_none         | 728 ms                                                 | 260 ms: 2.80x faster                                              |
| async_tree_memoization  | 870 ms                                                 | 312 ms: 2.78x faster                                              |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 498 ms: 2.04x faster                                              |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.2 ms: 1.80x faster                                             |
| nbody          | 154 ms                                                 | 93.5 ms: 1.64x faster                                             |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.44x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.48x faster                                              |
| regex_v8       | 27.8 ms                                                | 23.7 ms: 1.17x faster                                             |
| regex_effbot   | 3.63 ms                                                | 3.45 ms: 1.05x faster                                             |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                              |
| Geometric mean | (ref)                                                  | 1.17x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 194 us: 1.70x faster                                              |
| tomli_loads          | 3.14 sec                                               | 1.87 sec: 1.68x faster                                            |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                              |
| xml_etree_process    | 79.1 ms                                                | 54.7 ms: 1.45x faster                                             |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.26x faster                                             |
| xml_etree_generate   | 99.4 ms                                                | 79.0 ms: 1.26x faster                                             |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                              |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                             |
| json_loads           | 31.2 us                                                | 28.1 us: 1.11x faster                                             |
| Geometric mean       | (ref)                                                  | 1.36x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                             |
| python_startup_no_site | 5.93 ms                                                | 6.93 ms: 1.17x slower                                             |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.6 ms: 1.54x faster                                             |
| django_template | 48.2 ms                                                | 32.4 ms: 1.49x faster                                             |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                             |
| genshi_xml      | 66.0 ms                                                | 49.9 ms: 1.32x faster                                             |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 168 us: 3.24x faster                                              |
| async_tree_io            | 1.77 sec                                               | 597 ms: 2.96x faster                                              |
| async_tree_none          | 728 ms                                                 | 260 ms: 2.80x faster                                              |
| async_tree_memoization   | 870 ms                                                 | 312 ms: 2.78x faster                                              |
| generators               | 80.1 ms                                                | 30.4 ms: 2.64x faster                                             |
| deltablue                | 7.91 ms                                                | 3.06 ms: 2.59x faster                                             |
| richards_super           | 94.7 ms                                                | 38.3 ms: 2.47x faster                                             |
| richards                 | 79.3 ms                                                | 32.9 ms: 2.41x faster                                             |
| mdp                      | 2.85 sec                                               | 1.24 sec: 2.31x faster                                            |
| go                       | 240 ms                                                 | 117 ms: 2.05x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 498 ms: 2.04x faster                                              |
| deepcopy_memo            | 58.5 us                                                | 29.6 us: 1.98x faster                                             |
| pylint                   | 551 ms                                                 | 283 ms: 1.95x faster                                              |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                              |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                              |
| chaos                    | 115 ms                                                 | 62.6 ms: 1.85x faster                                             |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.82x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 65.3 ms: 1.81x faster                                             |
| float                    | 117 ms                                                 | 65.2 ms: 1.80x faster                                             |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                             |
| pyflate                  | 716 ms                                                 | 416 ms: 1.72x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 74.9 ms: 1.71x faster                                             |
| unpickle_pure_python     | 331 us                                                 | 194 us: 1.70x faster                                              |
| tomli_loads              | 3.14 sec                                               | 1.87 sec: 1.68x faster                                            |
| hexiom                   | 10.4 ms                                                | 6.27 ms: 1.66x faster                                             |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                              |
| nbody                    | 154 ms                                                 | 93.5 ms: 1.64x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                             |
| mako                     | 16.3 ms                                                | 10.6 ms: 1.54x faster                                             |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                              |
| django_template          | 48.2 ms                                                | 32.4 ms: 1.49x faster                                             |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                             |
| regex_compile            | 188 ms                                                 | 128 ms: 1.48x faster                                              |
| scimark_lu               | 176 ms                                                 | 121 ms: 1.46x faster                                              |
| xml_etree_process        | 79.1 ms                                                | 54.7 ms: 1.45x faster                                             |
| html5lib                 | 88.9 ms                                                | 62.3 ms: 1.43x faster                                             |
| scimark_fft              | 466 ms                                                 | 330 ms: 1.41x faster                                              |
| coroutines               | 35.1 ms                                                | 25.1 ms: 1.40x faster                                             |
| dulwich_log              | 84.3 ms                                                | 61.5 ms: 1.37x faster                                             |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                            |
| sympy_integrate          | 25.8 ms                                                | 19.3 ms: 1.34x faster                                             |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                              |
| logging_format           | 9.09 us                                                | 6.79 us: 1.34x faster                                             |
| logging_simple           | 8.30 us                                                | 6.24 us: 1.33x faster                                             |
| genshi_xml               | 66.0 ms                                                | 49.9 ms: 1.32x faster                                             |
| fannkuch                 | 532 ms                                                 | 404 ms: 1.32x faster                                              |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.95 ms: 1.31x faster                                             |
| pprint_pformat           | 2.10 sec                                               | 1.61 sec: 1.30x faster                                            |
| nqueens                  | 106 ms                                                 | 82.9 ms: 1.28x faster                                             |
| pprint_safe_repr         | 1.02 sec                                               | 800 ms: 1.27x faster                                              |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                              |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.26x faster                                             |
| xml_etree_generate       | 99.4 ms                                                | 79.0 ms: 1.26x faster                                             |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.25x faster                                            |
| sympy_expand             | 566 ms                                                 | 469 ms: 1.21x faster                                              |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.21x faster                                             |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                              |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                             |
| regex_v8                 | 27.8 ms                                                | 23.7 ms: 1.17x faster                                             |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                              |
| json_loads               | 31.2 us                                                | 28.1 us: 1.11x faster                                             |
| json                     | 5.69 ms                                                | 5.21 ms: 1.09x faster                                             |
| sqlite_synth             | 3.02 us                                                | 2.82 us: 1.07x faster                                             |
| regex_effbot             | 3.63 ms                                                | 3.45 ms: 1.05x faster                                             |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                              |
| async_generators         | 444 ms                                                 | 431 ms: 1.03x faster                                              |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                              |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                              |
| telco                    | 7.27 ms                                                | 7.76 ms: 1.07x slower                                             |
| python_startup_no_site   | 5.93 ms                                                | 6.93 ms: 1.17x slower                                             |
| gc_traversal             | 3.62 ms                                                | 5.14 ms: 1.42x slower                                             |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                             |
| logging_silent           | 190 ns                                                 | 475 ns: 2.50x slower                                              |
| coverage                 | 79.4 ms                                                | 425 ms: 5.35x slower                                              |
| thrift                   | 1.07 ms                                                | 148 ms: 138.36x slower                                            |
| Geometric mean           | (ref)                                                  | 1.32x faster                                                      |
Ignored benchmarks (24) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250612-3.15.0a0-858624a-JIT/bm-20250612-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-858624a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.337x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.33x