# Results vs. 3.10.4

- fork: serhiy-storchaka
- ref: pickle_save_global3
- machine: linux-x86_64
- commit hash: 5efa5a5
- commit date: 2024-07-30
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 263 ms: 1.33x faster                                                             |
| docutils       | 3.30 sec                                               | 2.73 sec: 1.21x faster                                                           |
| html5lib       | 88.9 ms                                                | 65.8 ms: 1.35x faster                                                            |
| tornado_http   | 136 ms                                                 | 90.2 ms: 1.51x faster                                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 324 ms: 2.25x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 425 ms: 2.05x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 903 ms: 1.96x faster                                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 567 ms: 1.79x faster                                                             |
| Geometric mean          | (ref)                                                  | 2.00x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.5 ms: 1.77x faster                                                            |
| float          | 117 ms                                                 | 78.6 ms: 1.49x faster                                                            |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                  | 1.39x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.44x faster                                                             |
| regex_v8       | 27.8 ms                                                | 26.4 ms: 1.05x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.83 ms: 1.06x slower                                                            |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                     |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                                             |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                             |
| tomli_loads          | 3.14 sec                                               | 2.04 sec: 1.54x faster                                                           |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 84.9 ms: 1.17x faster                                                            |
| json_loads           | 31.2 us                                                | 27.8 us: 1.12x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                             |
| xml_etree_parse      | 168 ms                                                 | 158 ms: 1.06x faster                                                             |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                            |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                            |
| genshi_text     | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                            |
| django_template | 48.2 ms                                                | 35.0 ms: 1.37x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 50.2 ms: 1.32x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.37x faster                                                             |
| generators               | 80.1 ms                                                | 28.5 ms: 2.81x faster                                                            |
| deltablue                | 7.91 ms                                                | 3.23 ms: 2.45x faster                                                            |
| async_tree_none          | 728 ms                                                 | 324 ms: 2.25x faster                                                             |
| async_tree_memoization   | 870 ms                                                 | 425 ms: 2.05x faster                                                             |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                                            |
| raytrace                 | 507 ms                                                 | 258 ms: 1.97x faster                                                             |
| async_tree_io            | 1.77 sec                                               | 903 ms: 1.96x faster                                                             |
| asyncio_tcp              | 922 ms                                                 | 487 ms: 1.89x faster                                                             |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                                             |
| deepcopy                 | 479 us                                                 | 261 us: 1.83x faster                                                             |
| richards_super           | 94.7 ms                                                | 51.8 ms: 1.83x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 567 ms: 1.79x faster                                                             |
| nbody                    | 154 ms                                                 | 86.5 ms: 1.77x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 67.2 ms: 1.76x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 72.9 ms: 1.75x faster                                                            |
| pylint                   | 551 ms                                                 | 316 ms: 1.74x faster                                                             |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.73x faster                                                             |
| richards                 | 79.3 ms                                                | 45.8 ms: 1.73x faster                                                            |
| go                       | 240 ms                                                 | 140 ms: 1.72x faster                                                             |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.26 ms: 1.66x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                                             |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.57x faster                                                             |
| spectral_norm            | 170 ms                                                 | 109 ms: 1.56x faster                                                             |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                             |
| tomli_loads              | 3.14 sec                                               | 2.04 sec: 1.54x faster                                                           |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.44 us: 1.53x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                                            |
| logging_format           | 9.09 us                                                | 6.01 us: 1.51x faster                                                            |
| tornado_http             | 136 ms                                                 | 90.2 ms: 1.51x faster                                                            |
| pyflate                  | 716 ms                                                 | 477 ms: 1.50x faster                                                             |
| float                    | 117 ms                                                 | 78.6 ms: 1.49x faster                                                            |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                            |
| regex_compile            | 188 ms                                                 | 130 ms: 1.44x faster                                                             |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.51 ms: 1.43x faster                                                            |
| genshi_text              | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                            |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                            |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.39x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                            |
| django_template          | 48.2 ms                                                | 35.0 ms: 1.37x faster                                                            |
| pprint_safe_repr         | 1.02 sec                                               | 744 ms: 1.37x faster                                                             |
| thrift                   | 1.07 ms                                                | 784 us: 1.37x faster                                                             |
| html5lib                 | 88.9 ms                                                | 65.8 ms: 1.35x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                             |
| nqueens                  | 106 ms                                                 | 79.6 ms: 1.33x faster                                                            |
| 2to3                     | 348 ms                                                 | 263 ms: 1.33x faster                                                             |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                                             |
| genshi_xml               | 66.0 ms                                                | 50.2 ms: 1.32x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                                            |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                             |
| sqlglot_optimize         | 69.2 ms                                                | 53.1 ms: 1.30x faster                                                            |
| scimark_fft              | 466 ms                                                 | 359 ms: 1.30x faster                                                             |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                                             |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 786 us: 1.26x faster                                                             |
| sympy_expand             | 566 ms                                                 | 458 ms: 1.23x faster                                                             |
| docutils                 | 3.30 sec                                               | 2.73 sec: 1.21x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 84.9 ms: 1.17x faster                                                            |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                                           |
| json                     | 5.69 ms                                                | 5.04 ms: 1.13x faster                                                            |
| json_loads               | 31.2 us                                                | 27.8 us: 1.12x faster                                                            |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                             |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                             |
| xml_etree_parse          | 168 ms                                                 | 158 ms: 1.06x faster                                                             |
| regex_v8                 | 27.8 ms                                                | 26.4 ms: 1.05x faster                                                            |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                             |
| gc_traversal             | 3.62 ms                                                | 3.56 ms: 1.02x faster                                                            |
| regex_effbot             | 3.63 ms                                                | 3.83 ms: 1.06x slower                                                            |
| coverage                 | 79.4 ms                                                | 84.1 ms: 1.06x slower                                                            |
| create_gc_cycles         | 1.62 ms                                                | 1.72 ms: 1.06x slower                                                            |
| telco                    | 7.27 ms                                                | 8.11 ms: 1.12x slower                                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                     |

Benchmark hidden because not significant (4): async_generators, bench_mp_pool, asyncio_websockets, regex_dna
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240730-3.14.0a0-5efa5a5/bm-20240730-linux-x86_64-serhiy%2dstorchaka-pickle_save_global3-3.14.0a0-5efa5a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.12x