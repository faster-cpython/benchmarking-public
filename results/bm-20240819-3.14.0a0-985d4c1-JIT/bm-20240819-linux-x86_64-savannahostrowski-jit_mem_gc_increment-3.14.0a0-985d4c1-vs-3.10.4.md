# Results vs. 3.10.4

- fork: savannahostrowski
- ref: jit_mem_gc_increment
- machine: linux-x86_64
- commit hash: 985d4c1
- commit date: 2024-08-19
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 283 ms: 1.23x faster                                                             |
| docutils       | 3.30 sec                                               | 2.98 sec: 1.11x faster                                                           |
| html5lib       | 88.9 ms                                                | 66.8 ms: 1.33x faster                                                            |
| tornado_http   | 136 ms                                                 | 93.1 ms: 1.46x faster                                                            |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.23x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 419 ms: 2.07x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 903 ms: 1.96x faster                                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 567 ms: 1.79x faster                                                             |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.8 ms: 1.88x faster                                                            |
| float          | 117 ms                                                 | 72.0 ms: 1.63x faster                                                            |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                  | 1.46x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 142 ms: 1.33x faster                                                             |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                            |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                                             |
| regex_effbot   | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                           |
| pickle_pure_python   | 484 us                                                 | 300 us: 1.61x faster                                                             |
| unpickle_pure_python | 331 us                                                 | 212 us: 1.56x faster                                                             |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 59.3 ms: 1.33x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 98.9 ms: 1.17x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 85.9 ms: 1.16x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                                             |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                            |
| python_startup_no_site | 5.93 ms                                                | 7.14 ms: 1.20x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.84 ms: 1.66x faster                                                            |
| django_template | 48.2 ms                                                | 35.9 ms: 1.34x faster                                                            |
| genshi_text     | 31.8 ms                                                | 25.8 ms: 1.23x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 61.1 ms: 1.08x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.17x faster                                                             |
| deltablue                | 7.91 ms                                                | 3.14 ms: 2.52x faster                                                            |
| generators               | 80.1 ms                                                | 33.4 ms: 2.40x faster                                                            |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.23x faster                                                             |
| deepcopy_memo            | 58.5 us                                                | 26.5 us: 2.21x faster                                                            |
| richards_super           | 94.7 ms                                                | 45.0 ms: 2.11x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 419 ms: 2.07x faster                                                             |
| richards                 | 79.3 ms                                                | 39.6 ms: 2.00x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 903 ms: 1.96x faster                                                             |
| chaos                    | 115 ms                                                 | 58.9 ms: 1.96x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 66.5 ms: 1.92x faster                                                            |
| raytrace                 | 507 ms                                                 | 265 ms: 1.91x faster                                                             |
| logging_silent           | 190 ns                                                 | 99.2 ns: 1.91x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 62.8 ms: 1.88x faster                                                            |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                             |
| nbody                    | 154 ms                                                 | 81.8 ms: 1.88x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 494 ms: 1.87x faster                                                             |
| deepcopy                 | 479 us                                                 | 265 us: 1.81x faster                                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 567 ms: 1.79x faster                                                             |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                            |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.67x faster                                                             |
| go                       | 240 ms                                                 | 144 ms: 1.66x faster                                                             |
| mako                     | 16.3 ms                                                | 9.84 ms: 1.66x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.65x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.64x faster                                                           |
| scimark_lu               | 176 ms                                                 | 107 ms: 1.64x faster                                                             |
| float                    | 117 ms                                                 | 72.0 ms: 1.63x faster                                                            |
| pyflate                  | 716 ms                                                 | 443 ms: 1.62x faster                                                             |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.61x faster                                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 212 us: 1.56x faster                                                             |
| sqlglot_transpile        | 2.57 ms                                                | 1.66 ms: 1.55x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.81 ms: 1.53x faster                                                            |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                                            |
| pylint                   | 551 ms                                                 | 367 ms: 1.50x faster                                                             |
| scimark_fft              | 466 ms                                                 | 311 ms: 1.50x faster                                                             |
| logging_format           | 9.09 us                                                | 6.09 us: 1.49x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.57 us: 1.49x faster                                                            |
| tornado_http             | 136 ms                                                 | 93.1 ms: 1.46x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.52 ms: 1.43x faster                                                            |
| fannkuch                 | 532 ms                                                 | 375 ms: 1.42x faster                                                             |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.82 sec: 1.42x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 726 ms: 1.40x faster                                                             |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                           |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                            |
| thrift                   | 1.07 ms                                                | 790 us: 1.36x faster                                                             |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                            |
| django_template          | 48.2 ms                                                | 35.9 ms: 1.34x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 59.3 ms: 1.33x faster                                                            |
| html5lib                 | 88.9 ms                                                | 66.8 ms: 1.33x faster                                                            |
| regex_compile            | 188 ms                                                 | 142 ms: 1.33x faster                                                             |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.28x faster                                                             |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                            |
| genshi_text              | 31.8 ms                                                | 25.8 ms: 1.23x faster                                                            |
| 2to3                     | 348 ms                                                 | 283 ms: 1.23x faster                                                             |
| nqueens                  | 106 ms                                                 | 86.1 ms: 1.23x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 819 us: 1.20x faster                                                             |
| sqlglot_optimize         | 69.2 ms                                                | 58.3 ms: 1.19x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 98.9 ms: 1.17x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 85.9 ms: 1.16x faster                                                            |
| sympy_str                | 346 ms                                                 | 302 ms: 1.15x faster                                                             |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                                             |
| sympy_sum                | 196 ms                                                 | 174 ms: 1.13x faster                                                             |
| sympy_integrate          | 25.8 ms                                                | 23.0 ms: 1.12x faster                                                            |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                             |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.98 sec: 1.11x faster                                                           |
| sympy_expand             | 566 ms                                                 | 511 ms: 1.11x faster                                                             |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 61.1 ms: 1.08x faster                                                            |
| json                     | 5.69 ms                                                | 5.35 ms: 1.06x faster                                                            |
| mdp                      | 2.85 sec                                               | 2.73 sec: 1.04x faster                                                           |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                                             |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                             |
| gc_traversal             | 3.62 ms                                                | 3.58 ms: 1.01x faster                                                            |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                             |
| async_generators         | 444 ms                                                 | 458 ms: 1.03x slower                                                             |
| regex_effbot             | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                            |
| create_gc_cycles         | 1.62 ms                                                | 1.71 ms: 1.05x slower                                                            |
| telco                    | 7.27 ms                                                | 7.80 ms: 1.07x slower                                                            |
| coverage                 | 79.4 ms                                                | 85.5 ms: 1.08x slower                                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.14 ms: 1.20x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                     |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240819-3.14.0a0-985d4c1-JIT/bm-20240819-linux-x86_64-savannahostrowski-jit_mem_gc_increment-3.14.0a0-985d4c1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.19x