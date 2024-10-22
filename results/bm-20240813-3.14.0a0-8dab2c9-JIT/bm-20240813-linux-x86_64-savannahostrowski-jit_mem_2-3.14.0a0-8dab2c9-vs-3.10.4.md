# Results vs. 3.10.4

- fork: savannahostrowski
- ref: jit_mem_2
- machine: linux-x86_64
- commit hash: 8dab2c9
- commit date: 2024-08-13
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 284 ms: 1.23x faster                                                  |
| docutils       | 3.30 sec                                               | 2.98 sec: 1.11x faster                                                |
| html5lib       | 88.9 ms                                                | 67.4 ms: 1.32x faster                                                 |
| tornado_http   | 136 ms                                                 | 94.1 ms: 1.45x faster                                                 |
| Geometric mean | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 331 ms: 2.20x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 431 ms: 2.02x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 914 ms: 1.94x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 568 ms: 1.79x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.98x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.0 ms: 1.92x faster                                                 |
| float          | 117 ms                                                 | 73.9 ms: 1.58x faster                                                 |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.46x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 142 ms: 1.33x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                 |
| regex_dna      | 227 ms                                                 | 215 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.90 sec: 1.66x faster                                                |
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                                  |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 58.8 ms: 1.35x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 84.9 ms: 1.17x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                  |
| json_loads           | 31.2 us                                                | 28.4 us: 1.10x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 153 ms: 1.10x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.87 ms: 1.65x faster                                                 |
| django_template | 48.2 ms                                                | 37.0 ms: 1.30x faster                                                 |
| genshi_text     | 31.8 ms                                                | 25.2 ms: 1.26x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 56.6 ms: 1.17x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.16x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.13 ms: 2.52x faster                                                 |
| generators               | 80.1 ms                                                | 35.4 ms: 2.26x faster                                                 |
| async_tree_none          | 728 ms                                                 | 331 ms: 2.20x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 27.3 us: 2.14x faster                                                 |
| richards_super           | 94.7 ms                                                | 45.6 ms: 2.08x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 431 ms: 2.02x faster                                                  |
| chaos                    | 115 ms                                                 | 58.1 ms: 1.99x faster                                                 |
| richards                 | 79.3 ms                                                | 40.5 ms: 1.96x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 914 ms: 1.94x faster                                                  |
| nbody                    | 154 ms                                                 | 80.0 ms: 1.92x faster                                                 |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.90x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 67.3 ms: 1.90x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 62.6 ms: 1.89x faster                                                 |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                                  |
| logging_silent           | 190 ns                                                 | 103 ns: 1.85x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 503 ms: 1.83x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 568 ms: 1.79x faster                                                  |
| deepcopy                 | 479 us                                                 | 269 us: 1.78x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                 |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.67x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.90 sec: 1.66x faster                                                |
| mako                     | 16.3 ms                                                | 9.87 ms: 1.65x faster                                                 |
| pyflate                  | 716 ms                                                 | 434 ms: 1.65x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                                 |
| go                       | 240 ms                                                 | 148 ms: 1.62x faster                                                  |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.61x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                                  |
| float                    | 117 ms                                                 | 73.9 ms: 1.58x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.54x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.23 ms: 1.53x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.80 ms: 1.53x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.53x faster                                                 |
| scimark_fft              | 466 ms                                                 | 306 ms: 1.52x faster                                                  |
| pylint                   | 551 ms                                                 | 366 ms: 1.51x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.54 us: 1.50x faster                                                 |
| logging_format           | 9.09 us                                                | 6.10 us: 1.49x faster                                                 |
| tornado_http             | 136 ms                                                 | 94.1 ms: 1.45x faster                                                 |
| fannkuch                 | 532 ms                                                 | 369 ms: 1.44x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                |
| python_startup           | 14.6 ms                                                | 10.4 ms: 1.40x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 745 ms: 1.37x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                                |
| thrift                   | 1.07 ms                                                | 795 us: 1.35x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 58.8 ms: 1.35x faster                                                 |
| regex_compile            | 188 ms                                                 | 142 ms: 1.33x faster                                                  |
| html5lib                 | 88.9 ms                                                | 67.4 ms: 1.32x faster                                                 |
| django_template          | 48.2 ms                                                | 37.0 ms: 1.30x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                  |
| genshi_text              | 31.8 ms                                                | 25.2 ms: 1.26x faster                                                 |
| 2to3                     | 348 ms                                                 | 284 ms: 1.23x faster                                                  |
| nqueens                  | 106 ms                                                 | 87.8 ms: 1.21x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 821 us: 1.20x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 58.3 ms: 1.19x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 84.9 ms: 1.17x faster                                                 |
| sympy_str                | 346 ms                                                 | 296 ms: 1.17x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 56.6 ms: 1.17x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                 |
| sympy_sum                | 196 ms                                                 | 170 ms: 1.16x faster                                                  |
| meteor_contest           | 120 ms                                                 | 104 ms: 1.15x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                                 |
| sympy_expand             | 566 ms                                                 | 505 ms: 1.12x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                                |
| docutils                 | 3.30 sec                                               | 2.98 sec: 1.11x faster                                                |
| json_loads               | 31.2 us                                                | 28.4 us: 1.10x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 153 ms: 1.10x faster                                                  |
| regex_dna                | 227 ms                                                 | 215 ms: 1.05x faster                                                  |
| gc_traversal             | 3.62 ms                                                | 3.48 ms: 1.04x faster                                                 |
| json                     | 5.69 ms                                                | 5.50 ms: 1.04x faster                                                 |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                  |
| async_generators         | 444 ms                                                 | 447 ms: 1.01x slower                                                  |
| coverage                 | 79.4 ms                                                | 84.8 ms: 1.07x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.73 ms: 1.07x slower                                                 |
| telco                    | 7.27 ms                                                | 7.82 ms: 1.08x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                          |

Benchmark hidden because not significant (2): regex_effbot, bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240813-3.14.0a0-8dab2c9-JIT/bm-20240813-linux-x86_64-savannahostrowski-jit_mem_2-3.14.0a0-8dab2c9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.18x