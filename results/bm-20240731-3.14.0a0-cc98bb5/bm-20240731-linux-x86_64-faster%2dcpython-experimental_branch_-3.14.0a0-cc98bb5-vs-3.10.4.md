# Results vs. 3.10.4

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.44x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.33x faster                                                            |
| docutils       | 3.30 sec                                               | 2.73 sec: 1.21x faster                                                          |
| html5lib       | 88.9 ms                                                | 65.0 ms: 1.37x faster                                                           |
| tornado_http   | 136 ms                                                 | 90.0 ms: 1.51x faster                                                           |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 323 ms: 2.25x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 401 ms: 2.17x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 901 ms: 1.96x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 559 ms: 1.82x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.04x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 84.5 ms: 1.82x faster                                                           |
| float          | 117 ms                                                 | 75.9 ms: 1.54x faster                                                           |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.42x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 131 ms: 1.44x faster                                                            |
| regex_v8       | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                           |
| regex_dna      | 227 ms                                                 | 226 ms: 1.00x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.78 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 301 us: 1.61x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.51x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 59.3 ms: 1.33x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 85.5 ms: 1.16x faster                                                           |
| json_loads           | 31.2 us                                                | 28.0 us: 1.12x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 153 ms: 1.10x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                           |
| genshi_text     | 31.8 ms                                                | 22.4 ms: 1.42x faster                                                           |
| django_template | 48.2 ms                                                | 34.3 ms: 1.40x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 49.5 ms: 1.33x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.30x faster                                                            |
| generators               | 80.1 ms                                                | 28.2 ms: 2.84x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.12 ms: 2.53x faster                                                           |
| async_tree_none          | 728 ms                                                 | 323 ms: 2.25x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 401 ms: 2.17x faster                                                            |
| chaos                    | 115 ms                                                 | 57.9 ms: 1.99x faster                                                           |
| raytrace                 | 507 ms                                                 | 257 ms: 1.97x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                                           |
| async_tree_io            | 1.77 sec                                               | 901 ms: 1.96x faster                                                            |
| logging_silent           | 190 ns                                                 | 100.0 ns: 1.90x faster                                                          |
| asyncio_tcp              | 922 ms                                                 | 491 ms: 1.88x faster                                                            |
| richards_super           | 94.7 ms                                                | 50.6 ms: 1.87x faster                                                           |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                            |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.82x faster                                                            |
| nbody                    | 154 ms                                                 | 84.5 ms: 1.82x faster                                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 559 ms: 1.82x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 66.7 ms: 1.77x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 72.3 ms: 1.77x faster                                                           |
| go                       | 240 ms                                                 | 136 ms: 1.77x faster                                                            |
| richards                 | 79.3 ms                                                | 45.1 ms: 1.76x faster                                                           |
| pylint                   | 551 ms                                                 | 316 ms: 1.74x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.25 ms: 1.73x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.28 ms: 1.66x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 301 us: 1.61x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                            |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                                           |
| float                    | 117 ms                                                 | 75.9 ms: 1.54x faster                                                           |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                           |
| logging_simple           | 8.30 us                                                | 5.42 us: 1.53x faster                                                           |
| pyflate                  | 716 ms                                                 | 469 ms: 1.53x faster                                                            |
| tornado_http             | 136 ms                                                 | 90.0 ms: 1.51x faster                                                           |
| logging_format           | 9.09 us                                                | 6.03 us: 1.51x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.51x faster                                                          |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.50x faster                                                            |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                           |
| regex_compile            | 188 ms                                                 | 131 ms: 1.44x faster                                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.43x faster                                                          |
| genshi_text              | 31.8 ms                                                | 22.4 ms: 1.42x faster                                                           |
| django_template          | 48.2 ms                                                | 34.3 ms: 1.40x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                                          |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.38x faster                                                          |
| thrift                   | 1.07 ms                                                | 784 us: 1.37x faster                                                            |
| html5lib                 | 88.9 ms                                                | 65.0 ms: 1.37x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 748 ms: 1.36x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.79 ms: 1.35x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 49.5 ms: 1.33x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 59.3 ms: 1.33x faster                                                           |
| nqueens                  | 106 ms                                                 | 79.4 ms: 1.33x faster                                                           |
| 2to3                     | 348 ms                                                 | 261 ms: 1.33x faster                                                            |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                                            |
| pathlib                  | 20.5 ms                                                | 15.6 ms: 1.31x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 53.3 ms: 1.30x faster                                                           |
| scimark_fft              | 466 ms                                                 | 359 ms: 1.30x faster                                                            |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.29x faster                                                            |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 788 us: 1.25x faster                                                            |
| dask                     | 441 ms                                                 | 353 ms: 1.25x faster                                                            |
| sympy_expand             | 566 ms                                                 | 460 ms: 1.23x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.73 sec: 1.21x faster                                                          |
| xml_etree_generate       | 99.4 ms                                                | 85.5 ms: 1.16x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                                          |
| json_loads               | 31.2 us                                                | 28.0 us: 1.12x faster                                                           |
| json                     | 5.69 ms                                                | 5.10 ms: 1.12x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                                            |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 153 ms: 1.10x faster                                                            |
| async_generators         | 444 ms                                                 | 429 ms: 1.03x faster                                                            |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| regex_dna                | 227 ms                                                 | 226 ms: 1.00x faster                                                            |
| gc_traversal             | 3.62 ms                                                | 3.65 ms: 1.01x slower                                                           |
| regex_effbot             | 3.63 ms                                                | 3.78 ms: 1.04x slower                                                           |
| coverage                 | 79.4 ms                                                | 84.6 ms: 1.07x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.73 ms: 1.07x slower                                                           |
| telco                    | 7.27 ms                                                | 8.10 ms: 1.11x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                                    |

Benchmark hidden because not significant (2): bench_mp_pool, asyncio_websockets
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240731-3.14.0a0-cc98bb5/bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.12x