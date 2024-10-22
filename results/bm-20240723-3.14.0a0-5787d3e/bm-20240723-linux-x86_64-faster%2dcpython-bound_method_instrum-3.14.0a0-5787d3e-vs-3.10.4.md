# Results vs. 3.10.4

- fork: faster-cpython
- ref: bound_method_instrum
- machine: linux-x86_64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.44x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.34x faster                                                            |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                          |
| html5lib       | 88.9 ms                                                | 64.4 ms: 1.38x faster                                                           |
| tornado_http   | 136 ms                                                 | 89.5 ms: 1.52x faster                                                           |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.23x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 409 ms: 2.13x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 848 ms: 2.08x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 566 ms: 1.79x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 85.2 ms: 1.80x faster                                                           |
| float          | 117 ms                                                 | 76.4 ms: 1.53x faster                                                           |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.41x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                            |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                           |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 295 us: 1.64x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 210 us: 1.58x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.04 sec: 1.54x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 58.3 ms: 1.36x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 84.6 ms: 1.18x faster                                                           |
| json_loads           | 31.2 us                                                | 27.5 us: 1.14x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.7 ms: 1.52x faster                                                           |
| genshi_text     | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                           |
| django_template | 48.2 ms                                                | 33.7 ms: 1.43x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 48.6 ms: 1.36x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.39x faster                                                            |
| generators               | 80.1 ms                                                | 27.9 ms: 2.88x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.11 ms: 2.54x faster                                                           |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.23x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 409 ms: 2.13x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 848 ms: 2.08x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 28.6 us: 2.04x faster                                                           |
| logging_silent           | 190 ns                                                 | 95.7 ns: 1.98x faster                                                           |
| raytrace                 | 507 ms                                                 | 256 ms: 1.98x faster                                                            |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                                           |
| asyncio_tcp              | 922 ms                                                 | 491 ms: 1.88x faster                                                            |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                                            |
| richards_super           | 94.7 ms                                                | 51.2 ms: 1.85x faster                                                           |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.82x faster                                                            |
| nbody                    | 154 ms                                                 | 85.2 ms: 1.80x faster                                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 566 ms: 1.79x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 72.2 ms: 1.77x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                                           |
| pylint                   | 551 ms                                                 | 316 ms: 1.75x faster                                                            |
| hexiom                   | 10.4 ms                                                | 5.98 ms: 1.74x faster                                                           |
| richards                 | 79.3 ms                                                | 45.8 ms: 1.73x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 68.3 ms: 1.73x faster                                                           |
| go                       | 240 ms                                                 | 140 ms: 1.72x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 295 us: 1.64x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.64 us: 1.58x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 210 us: 1.58x faster                                                            |
| coroutines               | 35.1 ms                                                | 22.3 ms: 1.57x faster                                                           |
| pyflate                  | 716 ms                                                 | 458 ms: 1.56x faster                                                            |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.55x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 2.04 sec: 1.54x faster                                                          |
| float                    | 117 ms                                                 | 76.4 ms: 1.53x faster                                                           |
| spectral_norm            | 170 ms                                                 | 111 ms: 1.53x faster                                                            |
| logging_format           | 9.09 us                                                | 5.96 us: 1.53x faster                                                           |
| tornado_http             | 136 ms                                                 | 89.5 ms: 1.52x faster                                                           |
| logging_simple           | 8.30 us                                                | 5.46 us: 1.52x faster                                                           |
| mako                     | 16.3 ms                                                | 10.7 ms: 1.52x faster                                                           |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.78 sec: 1.44x faster                                                          |
| genshi_text              | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                           |
| django_template          | 48.2 ms                                                | 33.7 ms: 1.43x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 721 ms: 1.41x faster                                                            |
| thrift                   | 1.07 ms                                                | 768 us: 1.39x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.66 ms: 1.39x faster                                                           |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| html5lib                 | 88.9 ms                                                | 64.4 ms: 1.38x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 48.6 ms: 1.36x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 58.3 ms: 1.36x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.35x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                          |
| 2to3                     | 348 ms                                                 | 261 ms: 1.34x faster                                                            |
| nqueens                  | 106 ms                                                 | 79.4 ms: 1.33x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 63.5 ms: 1.33x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.31x faster                                                           |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                            |
| pathlib                  | 20.5 ms                                                | 15.6 ms: 1.31x faster                                                           |
| fannkuch                 | 532 ms                                                 | 407 ms: 1.31x faster                                                            |
| sqlglot_optimize         | 69.2 ms                                                | 53.0 ms: 1.30x faster                                                           |
| scimark_fft              | 466 ms                                                 | 359 ms: 1.30x faster                                                            |
| sympy_str                | 346 ms                                                 | 269 ms: 1.28x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 784 us: 1.26x faster                                                            |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                                            |
| dask                     | 441 ms                                                 | 356 ms: 1.24x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                          |
| xml_etree_generate       | 99.4 ms                                                | 84.6 ms: 1.18x faster                                                           |
| json_loads               | 31.2 us                                                | 27.5 us: 1.14x faster                                                           |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                            |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                                          |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                                            |
| async_generators         | 444 ms                                                 | 429 ms: 1.03x faster                                                            |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                                            |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| gc_traversal             | 3.62 ms                                                | 3.78 ms: 1.04x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                                           |
| telco                    | 7.27 ms                                                | 7.95 ms: 1.09x slower                                                           |
| coverage                 | 79.4 ms                                                | 90.5 ms: 1.14x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                                    |

Benchmark hidden because not significant (3): asyncio_websockets, bench_mp_pool, regex_effbot
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240723-3.14.0a0-5787d3e/bm-20240723-linux-x86_64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.12x