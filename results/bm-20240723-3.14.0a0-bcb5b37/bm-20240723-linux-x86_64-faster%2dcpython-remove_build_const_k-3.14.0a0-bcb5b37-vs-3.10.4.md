# Results vs. 3.10.4

- fork: faster-cpython
- ref: remove_build_const_k
- machine: linux-x86_64
- commit hash: bcb5b37
- commit date: 2024-07-23
- overall geometric mean: 1.45x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                                            |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                          |
| html5lib       | 88.9 ms                                                | 63.5 ms: 1.40x faster                                                           |
| tornado_http   | 136 ms                                                 | 89.7 ms: 1.52x faster                                                           |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 323 ms: 2.25x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 406 ms: 2.14x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 835 ms: 2.12x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 566 ms: 1.80x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.07x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.5 ms: 1.77x faster                                                           |
| float          | 117 ms                                                 | 77.3 ms: 1.52x faster                                                           |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.40x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                            |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.10x faster                                                           |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.69 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 296 us: 1.64x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 209 us: 1.58x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.02 sec: 1.55x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 58.1 ms: 1.36x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 84.5 ms: 1.18x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                                            |
| json_loads           | 31.2 us                                                | 28.1 us: 1.11x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 153 ms: 1.10x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.19x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.8 ms: 1.52x faster                                                           |
| django_template | 48.2 ms                                                | 33.6 ms: 1.43x faster                                                           |
| genshi_text     | 31.8 ms                                                | 22.5 ms: 1.42x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 49.1 ms: 1.35x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                                            |
| generators               | 80.1 ms                                                | 27.7 ms: 2.90x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.16 ms: 2.50x faster                                                           |
| async_tree_none          | 728 ms                                                 | 323 ms: 2.25x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 406 ms: 2.14x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 835 ms: 2.12x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 29.0 us: 2.01x faster                                                           |
| raytrace                 | 507 ms                                                 | 253 ms: 2.01x faster                                                            |
| chaos                    | 115 ms                                                 | 57.6 ms: 2.00x faster                                                           |
| logging_silent           | 190 ns                                                 | 98.1 ns: 1.93x faster                                                           |
| asyncio_tcp              | 922 ms                                                 | 490 ms: 1.88x faster                                                            |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                                            |
| richards_super           | 94.7 ms                                                | 51.7 ms: 1.83x faster                                                           |
| pylint                   | 551 ms                                                 | 301 ms: 1.83x faster                                                            |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 70.5 ms: 1.81x faster                                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 566 ms: 1.80x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 66.6 ms: 1.77x faster                                                           |
| nbody                    | 154 ms                                                 | 86.5 ms: 1.77x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.75x faster                                                           |
| richards                 | 79.3 ms                                                | 45.6 ms: 1.74x faster                                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.25 ms: 1.73x faster                                                           |
| go                       | 240 ms                                                 | 139 ms: 1.73x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.06 ms: 1.72x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.56 ms: 1.64x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 296 us: 1.64x faster                                                            |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                                            |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.60x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 209 us: 1.58x faster                                                            |
| coroutines               | 35.1 ms                                                | 22.2 ms: 1.58x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.02 sec: 1.55x faster                                                          |
| logging_simple           | 8.30 us                                                | 5.40 us: 1.54x faster                                                           |
| tornado_http             | 136 ms                                                 | 89.7 ms: 1.52x faster                                                           |
| mako                     | 16.3 ms                                                | 10.8 ms: 1.52x faster                                                           |
| float                    | 117 ms                                                 | 77.3 ms: 1.52x faster                                                           |
| logging_format           | 9.09 us                                                | 6.03 us: 1.51x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.35 ms: 1.49x faster                                                           |
| pyflate                  | 716 ms                                                 | 482 ms: 1.49x faster                                                            |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.78 sec: 1.44x faster                                                          |
| django_template          | 48.2 ms                                                | 33.6 ms: 1.43x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                          |
| genshi_text              | 31.8 ms                                                | 22.5 ms: 1.42x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 722 ms: 1.41x faster                                                            |
| html5lib                 | 88.9 ms                                                | 63.5 ms: 1.40x faster                                                           |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                           |
| thrift                   | 1.07 ms                                                | 777 us: 1.38x faster                                                            |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 105 ms: 1.36x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 58.1 ms: 1.36x faster                                                           |
| fannkuch                 | 532 ms                                                 | 395 ms: 1.35x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 49.1 ms: 1.35x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                                          |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                                            |
| dulwich_log              | 84.3 ms                                                | 63.4 ms: 1.33x faster                                                           |
| nqueens                  | 106 ms                                                 | 80.5 ms: 1.31x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                                           |
| scimark_fft              | 466 ms                                                 | 356 ms: 1.31x faster                                                            |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                            |
| sqlglot_optimize         | 69.2 ms                                                | 52.8 ms: 1.31x faster                                                           |
| pathlib                  | 20.5 ms                                                | 15.6 ms: 1.31x faster                                                           |
| sympy_str                | 346 ms                                                 | 271 ms: 1.28x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 785 us: 1.26x faster                                                            |
| dask                     | 441 ms                                                 | 352 ms: 1.25x faster                                                            |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                          |
| xml_etree_generate       | 99.4 ms                                                | 84.5 ms: 1.18x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.13x faster                                                          |
| json                     | 5.69 ms                                                | 5.06 ms: 1.12x faster                                                           |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                                            |
| json_loads               | 31.2 us                                                | 28.1 us: 1.11x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 153 ms: 1.10x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.10x faster                                                           |
| async_generators         | 444 ms                                                 | 427 ms: 1.04x faster                                                            |
| gc_traversal             | 3.62 ms                                                | 3.54 ms: 1.02x faster                                                           |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                            |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                                            |
| regex_effbot             | 3.63 ms                                                | 3.69 ms: 1.02x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.73 ms: 1.07x slower                                                           |
| telco                    | 7.27 ms                                                | 8.15 ms: 1.12x slower                                                           |
| coverage                 | 79.4 ms                                                | 90.9 ms: 1.14x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.19x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.45x faster                                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240723-3.14.0a0-bcb5b37/bm-20240723-linux-x86_64-faster%2dcpython-remove_build_const_k-3.14.0a0-bcb5b37.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.12x