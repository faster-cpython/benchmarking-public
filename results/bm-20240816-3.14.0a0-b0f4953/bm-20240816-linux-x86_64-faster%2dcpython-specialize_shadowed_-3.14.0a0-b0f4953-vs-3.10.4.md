# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_shadowed_
- machine: linux-x86_64
- commit hash: b0f4953
- commit date: 2024-08-16
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                            |
| docutils       | 3.30 sec                                               | 2.71 sec: 1.22x faster                                                          |
| html5lib       | 88.9 ms                                                | 63.8 ms: 1.39x faster                                                           |
| tornado_http   | 136 ms                                                 | 90.3 ms: 1.51x faster                                                           |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 323 ms: 2.26x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 422 ms: 2.06x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 897 ms: 1.97x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 560 ms: 1.82x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.1 ms: 1.74x faster                                                           |
| float          | 117 ms                                                 | 78.9 ms: 1.48x faster                                                           |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.38x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.47x faster                                                            |
| regex_v8       | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                           |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.61x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.10 sec: 1.50x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 85.7 ms: 1.16x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                            |
| json_loads           | 31.2 us                                                | 28.5 us: 1.10x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                           |
| genshi_text     | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                           |
| django_template | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 49.3 ms: 1.34x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.42x faster                                                            |
| generators               | 80.1 ms                                                | 28.0 ms: 2.86x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.22 ms: 2.46x faster                                                           |
| async_tree_none          | 728 ms                                                 | 323 ms: 2.26x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 422 ms: 2.06x faster                                                            |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                                           |
| async_tree_io            | 1.77 sec                                               | 897 ms: 1.97x faster                                                            |
| raytrace                 | 507 ms                                                 | 260 ms: 1.95x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 30.1 us: 1.94x faster                                                           |
| asyncio_tcp              | 922 ms                                                 | 481 ms: 1.92x faster                                                            |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 560 ms: 1.82x faster                                                            |
| logging_silent           | 190 ns                                                 | 105 ns: 1.80x faster                                                            |
| richards_super           | 94.7 ms                                                | 52.8 ms: 1.80x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 71.5 ms: 1.79x faster                                                           |
| pylint                   | 551 ms                                                 | 316 ms: 1.74x faster                                                            |
| nbody                    | 154 ms                                                 | 88.1 ms: 1.74x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 68.3 ms: 1.73x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                           |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                                            |
| richards                 | 79.3 ms                                                | 46.5 ms: 1.70x faster                                                           |
| go                       | 240 ms                                                 | 142 ms: 1.69x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.24 ms: 1.67x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.61x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.55x faster                                                           |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                            |
| pyflate                  | 716 ms                                                 | 469 ms: 1.53x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                            |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                           |
| tornado_http             | 136 ms                                                 | 90.3 ms: 1.51x faster                                                           |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.51x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 2.10 sec: 1.50x faster                                                          |
| logging_simple           | 8.30 us                                                | 5.55 us: 1.50x faster                                                           |
| float                    | 117 ms                                                 | 78.9 ms: 1.48x faster                                                           |
| logging_format           | 9.09 us                                                | 6.18 us: 1.47x faster                                                           |
| regex_compile            | 188 ms                                                 | 129 ms: 1.47x faster                                                            |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                          |
| genshi_text              | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                          |
| django_template          | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 724 ms: 1.41x faster                                                            |
| thrift                   | 1.07 ms                                                | 766 us: 1.40x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                                          |
| html5lib                 | 88.9 ms                                                | 63.8 ms: 1.39x faster                                                           |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.72 ms: 1.37x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 49.3 ms: 1.34x faster                                                           |
| nqueens                  | 106 ms                                                 | 79.5 ms: 1.33x faster                                                           |
| fannkuch                 | 532 ms                                                 | 404 ms: 1.32x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.32x faster                                                            |
| pathlib                  | 20.5 ms                                                | 15.6 ms: 1.31x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.31x faster                                                           |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                            |
| sqlglot_optimize         | 69.2 ms                                                | 53.6 ms: 1.29x faster                                                           |
| scimark_fft              | 466 ms                                                 | 361 ms: 1.29x faster                                                            |
| sympy_str                | 346 ms                                                 | 271 ms: 1.28x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 784 us: 1.26x faster                                                            |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.71 sec: 1.22x faster                                                          |
| xml_etree_generate       | 99.4 ms                                                | 85.7 ms: 1.16x faster                                                           |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                            |
| json_loads               | 31.2 us                                                | 28.5 us: 1.10x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                                            |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.72 sec: 1.05x faster                                                          |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                            |
| async_generators         | 444 ms                                                 | 434 ms: 1.02x faster                                                            |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                                            |
| gc_traversal             | 3.62 ms                                                | 3.71 ms: 1.02x slower                                                           |
| coverage                 | 79.4 ms                                                | 84.4 ms: 1.06x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.73 ms: 1.07x slower                                                           |
| telco                    | 7.27 ms                                                | 8.33 ms: 1.15x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                    |

Benchmark hidden because not significant (3): asyncio_websockets, bench_mp_pool, regex_effbot
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240816-3.14.0a0-b0f4953/bm-20240816-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-b0f4953.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.12x