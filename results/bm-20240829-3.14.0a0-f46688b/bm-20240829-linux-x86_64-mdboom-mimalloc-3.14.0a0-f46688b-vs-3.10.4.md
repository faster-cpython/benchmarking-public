# Results vs. 3.10.4

- fork: mdboom
- ref: mimalloc
- machine: linux-x86_64
- commit hash: f46688b
- commit date: 2024-08-29
- overall geometric mean: 1.459x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 251 ms: 1.39x faster                                      |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.24x faster                                    |
| html5lib       | 88.9 ms                                                | 61.9 ms: 1.44x faster                                     |
| tornado_http   | 136 ms                                                 | 86.9 ms: 1.57x faster                                     |
| Geometric mean | (ref)                                                  | 1.40x faster                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 328 ms: 2.22x faster                                      |
| async_tree_memoization  | 870 ms                                                 | 415 ms: 2.10x faster                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 569 ms: 1.79x faster                                      |
| async_tree_io           | 1.77 sec                                               | 1.00 sec: 1.77x faster                                    |
| Geometric mean          | (ref)                                                  | 1.96x faster                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| nbody          | 154 ms                                                 | 89.7 ms: 1.71x faster                                     |
| float          | 117 ms                                                 | 75.7 ms: 1.55x faster                                     |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                      |
| Geometric mean | (ref)                                                  | 1.40x faster                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                      |
| regex_v8       | 27.8 ms                                                | 23.3 ms: 1.19x faster                                     |
| regex_dna      | 227 ms                                                 | 208 ms: 1.09x faster                                      |
| regex_effbot   | 3.63 ms                                                | 3.34 ms: 1.09x faster                                     |
| Geometric mean | (ref)                                                  | 1.20x faster                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 296 us: 1.64x faster                                      |
| tomli_loads          | 3.14 sec                                               | 2.01 sec: 1.56x faster                                    |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.55x faster                                      |
| json_dumps           | 14.2 ms                                                | 10.1 ms: 1.40x faster                                     |
| xml_etree_process    | 79.1 ms                                                | 58.9 ms: 1.34x faster                                     |
| xml_etree_generate   | 99.4 ms                                                | 84.7 ms: 1.17x faster                                     |
| json_loads           | 31.2 us                                                | 27.5 us: 1.14x faster                                     |
| xml_etree_iterparse  | 115 ms                                                 | 103 ms: 1.12x faster                                      |
| xml_etree_parse      | 168 ms                                                 | 153 ms: 1.10x faster                                      |
| Geometric mean       | (ref)                                                  | 1.32x faster                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.4 ms: 1.40x faster                                     |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                     |
| Geometric mean         | (ref)                                                  | 1.08x faster                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.4 ms: 1.57x faster                                     |
| django_template | 48.2 ms                                                | 33.2 ms: 1.45x faster                                     |
| genshi_text     | 31.8 ms                                                | 22.8 ms: 1.40x faster                                     |
| genshi_xml      | 66.0 ms                                                | 49.1 ms: 1.35x faster                                     |
| Geometric mean  | (ref)                                                  | 1.44x faster                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 157 us: 3.47x faster                                      |
| generators               | 80.1 ms                                                | 28.2 ms: 2.84x faster                                     |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                     |
| async_tree_none          | 728 ms                                                 | 328 ms: 2.22x faster                                      |
| async_tree_memoization   | 870 ms                                                 | 415 ms: 2.10x faster                                      |
| go                       | 240 ms                                                 | 116 ms: 2.07x faster                                      |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 1.99x faster                                     |
| chaos                    | 115 ms                                                 | 58.5 ms: 1.97x faster                                     |
| logging_silent           | 190 ns                                                 | 98.5 ns: 1.93x faster                                     |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                      |
| deepcopy                 | 479 us                                                 | 253 us: 1.89x faster                                      |
| asyncio_tcp              | 922 ms                                                 | 496 ms: 1.86x faster                                      |
| crypto_pyaes             | 128 ms                                                 | 69.9 ms: 1.83x faster                                     |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                      |
| scimark_monte_carlo      | 118 ms                                                 | 66.1 ms: 1.79x faster                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 569 ms: 1.79x faster                                      |
| richards_super           | 94.7 ms                                                | 53.5 ms: 1.77x faster                                     |
| async_tree_io            | 1.77 sec                                               | 1.00 sec: 1.77x faster                                    |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                     |
| pylint                   | 551 ms                                                 | 319 ms: 1.73x faster                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.26 ms: 1.72x faster                                     |
| nbody                    | 154 ms                                                 | 89.7 ms: 1.71x faster                                     |
| richards                 | 79.3 ms                                                | 47.0 ms: 1.69x faster                                     |
| hexiom                   | 10.4 ms                                                | 6.19 ms: 1.68x faster                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                     |
| pickle_pure_python       | 484 us                                                 | 296 us: 1.64x faster                                      |
| pyflate                  | 716 ms                                                 | 442 ms: 1.62x faster                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.61 us: 1.60x faster                                     |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.59x faster                                      |
| mako                     | 16.3 ms                                                | 10.4 ms: 1.57x faster                                     |
| spectral_norm            | 170 ms                                                 | 108 ms: 1.57x faster                                      |
| tornado_http             | 136 ms                                                 | 86.9 ms: 1.57x faster                                     |
| tomli_loads              | 3.14 sec                                               | 2.01 sec: 1.56x faster                                    |
| float                    | 117 ms                                                 | 75.7 ms: 1.55x faster                                     |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.55x faster                                      |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.52x faster                                     |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                      |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                     |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                     |
| pprint_safe_repr         | 1.02 sec                                               | 697 ms: 1.46x faster                                      |
| pycparser                | 1.58 sec                                               | 1.08 sec: 1.46x faster                                    |
| pprint_pformat           | 2.10 sec                                               | 1.44 sec: 1.46x faster                                    |
| django_template          | 48.2 ms                                                | 33.2 ms: 1.45x faster                                     |
| html5lib                 | 88.9 ms                                                | 61.9 ms: 1.44x faster                                     |
| thrift                   | 1.07 ms                                                | 747 us: 1.43x faster                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.83 sec: 1.41x faster                                    |
| json_dumps               | 14.2 ms                                                | 10.1 ms: 1.40x faster                                     |
| genshi_text              | 31.8 ms                                                | 22.8 ms: 1.40x faster                                     |
| python_startup           | 14.6 ms                                                | 10.4 ms: 1.40x faster                                     |
| 2to3                     | 348 ms                                                 | 251 ms: 1.39x faster                                      |
| sqlglot_normalize        | 143 ms                                                 | 104 ms: 1.38x faster                                      |
| nqueens                  | 106 ms                                                 | 77.9 ms: 1.36x faster                                     |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.35x faster                                      |
| genshi_xml               | 66.0 ms                                                | 49.1 ms: 1.35x faster                                     |
| xml_etree_process        | 79.1 ms                                                | 58.9 ms: 1.34x faster                                     |
| pathlib                  | 20.5 ms                                                | 15.2 ms: 1.34x faster                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.84 ms: 1.34x faster                                     |
| scimark_fft              | 466 ms                                                 | 350 ms: 1.33x faster                                      |
| sqlglot_optimize         | 69.2 ms                                                | 52.1 ms: 1.33x faster                                     |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.33x faster                                     |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                      |
| sympy_str                | 346 ms                                                 | 263 ms: 1.31x faster                                      |
| sympy_expand             | 566 ms                                                 | 447 ms: 1.26x faster                                      |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.24x faster                                    |
| regex_v8                 | 27.8 ms                                                | 23.3 ms: 1.19x faster                                     |
| xml_etree_generate       | 99.4 ms                                                | 84.7 ms: 1.17x faster                                     |
| json                     | 5.69 ms                                                | 4.97 ms: 1.14x faster                                     |
| json_loads               | 31.2 us                                                | 27.5 us: 1.14x faster                                     |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                    |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                      |
| xml_etree_iterparse      | 115 ms                                                 | 103 ms: 1.12x faster                                      |
| xml_etree_parse          | 168 ms                                                 | 153 ms: 1.10x faster                                      |
| regex_dna                | 227 ms                                                 | 208 ms: 1.09x faster                                      |
| regex_effbot             | 3.63 ms                                                | 3.34 ms: 1.09x faster                                     |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                      |
| asyncio_websockets       | 559 ms                                                 | 542 ms: 1.03x faster                                      |
| async_generators         | 444 ms                                                 | 437 ms: 1.01x faster                                      |
| gc_traversal             | 3.62 ms                                                | 3.62 ms: 1.00x faster                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                     |
| coverage                 | 79.4 ms                                                | 89.3 ms: 1.12x slower                                     |
| telco                    | 7.27 ms                                                | 8.47 ms: 1.17x slower                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                     |
| bench_thread_pool        | 986 us                                                 | 1.24 ms: 1.26x slower                                     |
| Geometric mean           | (ref)                                                  | 1.45x faster                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240829-3.14.0a0-f46688b/bm-20240829-linux-x86_64-mdboom-mimalloc-3.14.0a0-f46688b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.459x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.38x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.34x

# Memory
- memory change: 1.22x