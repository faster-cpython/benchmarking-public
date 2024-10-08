# Results vs. 3.10.4

- fork: savannahostrowski
- ref: jit_inv_mem_1m
- machine: linux-x86_64
- commit hash: 563a4d7
- commit date: 2024-09-19
- overall geometric mean: 1.37x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 277 ms: 1.26x faster                                                       |
| docutils       | 3.30 sec                                               | 2.96 sec: 1.12x faster                                                     |
| html5lib       | 88.9 ms                                                | 65.1 ms: 1.37x faster                                                      |
| tornado_http   | 136 ms                                                 | 94.6 ms: 1.44x faster                                                      |
| Geometric mean | (ref)                                                  | 1.29x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 317 ms: 2.30x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 394 ms: 2.21x faster                                                       |
| async_tree_io           | 1.77 sec                                               | 858 ms: 2.06x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 565 ms: 1.80x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.08x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.3 ms: 1.89x faster                                                      |
| float          | 117 ms                                                 | 69.7 ms: 1.68x faster                                                      |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.48x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 144 ms: 1.31x faster                                                       |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.13x faster                                                      |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                                       |
| regex_effbot   | 3.63 ms                                                | 3.76 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                     |
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 54.5 ms: 1.45x faster                                                      |
| json_dumps           | 14.2 ms                                                | 9.88 ms: 1.44x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 78.0 ms: 1.28x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 98.8 ms: 1.17x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 144 ms: 1.17x faster                                                       |
| json_loads           | 31.2 us                                                | 26.9 us: 1.16x faster                                                      |
| unpickle_list        | 5.20 us                                                | 5.31 us: 1.02x slower                                                      |
| unpickle             | 14.4 us                                                | 14.9 us: 1.03x slower                                                      |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                                      |
| pickle_dict          | 29.6 us                                                | 34.9 us: 1.18x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.79 ms: 1.67x faster                                                      |
| django_template | 48.2 ms                                                | 36.1 ms: 1.33x faster                                                      |
| genshi_text     | 31.8 ms                                                | 25.8 ms: 1.23x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 61.2 ms: 1.08x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.24 ms: 2.44x faster                                                      |
| async_tree_none          | 728 ms                                                 | 317 ms: 2.30x faster                                                       |
| generators               | 80.1 ms                                                | 36.2 ms: 2.21x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 394 ms: 2.21x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 27.5 us: 2.13x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 858 ms: 2.06x faster                                                       |
| richards_super           | 94.7 ms                                                | 47.7 ms: 1.99x faster                                                      |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 66.3 ms: 1.93x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 487 ms: 1.89x faster                                                       |
| richards                 | 79.3 ms                                                | 41.9 ms: 1.89x faster                                                      |
| nbody                    | 154 ms                                                 | 81.3 ms: 1.89x faster                                                      |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.87x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 63.4 ms: 1.87x faster                                                      |
| raytrace                 | 507 ms                                                 | 279 ms: 1.82x faster                                                       |
| go                       | 240 ms                                                 | 133 ms: 1.81x faster                                                       |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 565 ms: 1.80x faster                                                       |
| deepcopy                 | 479 us                                                 | 269 us: 1.78x faster                                                       |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                                      |
| float                    | 117 ms                                                 | 69.7 ms: 1.68x faster                                                      |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                       |
| mako                     | 16.3 ms                                                | 9.79 ms: 1.67x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.35 ms: 1.61x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                                       |
| scimark_lu               | 176 ms                                                 | 111 ms: 1.58x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                                      |
| pyflate                  | 716 ms                                                 | 470 ms: 1.52x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.70 ms: 1.51x faster                                                      |
| scimark_fft              | 466 ms                                                 | 309 ms: 1.51x faster                                                       |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.39 ms: 1.47x faster                                                      |
| logging_format           | 9.09 us                                                | 6.18 us: 1.47x faster                                                      |
| hexiom                   | 10.4 ms                                                | 7.07 ms: 1.47x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.67 us: 1.47x faster                                                      |
| pylint                   | 551 ms                                                 | 377 ms: 1.46x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 54.5 ms: 1.45x faster                                                      |
| tornado_http             | 136 ms                                                 | 94.6 ms: 1.44x faster                                                      |
| json_dumps               | 14.2 ms                                                | 9.88 ms: 1.44x faster                                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                     |
| fannkuch                 | 532 ms                                                 | 374 ms: 1.42x faster                                                       |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                      |
| html5lib                 | 88.9 ms                                                | 65.1 ms: 1.37x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 745 ms: 1.37x faster                                                       |
| thrift                   | 1.07 ms                                                | 788 us: 1.36x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                                     |
| django_template          | 48.2 ms                                                | 36.1 ms: 1.33x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                                     |
| regex_compile            | 188 ms                                                 | 144 ms: 1.31x faster                                                       |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 78.0 ms: 1.28x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                                       |
| 2to3                     | 348 ms                                                 | 277 ms: 1.26x faster                                                       |
| genshi_text              | 31.8 ms                                                | 25.8 ms: 1.23x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 68.5 ms: 1.23x faster                                                      |
| nqueens                  | 106 ms                                                 | 88.8 ms: 1.19x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 58.4 ms: 1.18x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 840 us: 1.17x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 98.8 ms: 1.17x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 144 ms: 1.17x faster                                                       |
| json_loads               | 31.2 us                                                | 26.9 us: 1.16x faster                                                      |
| sympy_str                | 346 ms                                                 | 305 ms: 1.13x faster                                                       |
| json                     | 5.69 ms                                                | 5.03 ms: 1.13x faster                                                      |
| sympy_sum                | 196 ms                                                 | 174 ms: 1.13x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.13x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 23.1 ms: 1.12x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.96 sec: 1.12x faster                                                     |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                                      |
| sympy_expand             | 566 ms                                                 | 513 ms: 1.10x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 61.2 ms: 1.08x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.71 sec: 1.05x faster                                                     |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                                       |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                       |
| unpickle_list            | 5.20 us                                                | 5.31 us: 1.02x slower                                                      |
| async_generators         | 444 ms                                                 | 453 ms: 1.02x slower                                                       |
| gc_traversal             | 3.62 ms                                                | 3.74 ms: 1.03x slower                                                      |
| unpickle                 | 14.4 us                                                | 14.9 us: 1.03x slower                                                      |
| regex_effbot             | 3.63 ms                                                | 3.76 ms: 1.03x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                                      |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                                      |
| telco                    | 7.27 ms                                                | 7.98 ms: 1.10x slower                                                      |
| coverage                 | 79.4 ms                                                | 88.0 ms: 1.11x slower                                                      |
| pickle_dict              | 29.6 us                                                | 34.9 us: 1.18x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                      |
| unpack_sequence          | 60.0 ns                                                | 113 ns: 1.89x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                               |

Benchmark hidden because not significant (2): bench_mp_pool, pickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240919-3.14.0a0-563a4d7-JIT/bm-20240919-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-563a4d7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.19x