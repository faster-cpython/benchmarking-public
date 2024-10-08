# Results vs. 3.10.4

- fork: savannahostrowski
- ref: jit_mem_100
- machine: linux-x86_64
- commit hash: 11fa189
- commit date: 2024-08-13
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 293 ms: 1.19x faster                                                    |
| docutils       | 3.30 sec                                               | 2.87 sec: 1.15x faster                                                  |
| html5lib       | 88.9 ms                                                | 65.3 ms: 1.36x faster                                                   |
| tornado_http   | 136 ms                                                 | 94.2 ms: 1.45x faster                                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 335 ms: 2.18x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 435 ms: 2.00x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 918 ms: 1.93x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 572 ms: 1.78x faster                                                    |
| Geometric mean          | (ref)                                                  | 1.96x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.7 ms: 1.88x faster                                                   |
| float          | 117 ms                                                 | 74.0 ms: 1.58x faster                                                   |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                  | 1.45x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 142 ms: 1.33x faster                                                    |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                   |
| regex_dna      | 227 ms                                                 | 211 ms: 1.08x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.49 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.14x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.89 sec: 1.66x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 304 us: 1.59x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                                    |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 59.0 ms: 1.34x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 85.4 ms: 1.16x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 103 ms: 1.13x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 153 ms: 1.10x faster                                                    |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.19x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.90 ms: 1.65x faster                                                   |
| django_template | 48.2 ms                                                | 35.4 ms: 1.36x faster                                                   |
| genshi_text     | 31.8 ms                                                | 25.3 ms: 1.26x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 56.3 ms: 1.17x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.21x faster                                                    |
| deltablue                | 7.91 ms                                                | 3.17 ms: 2.50x faster                                                   |
| generators               | 80.1 ms                                                | 34.8 ms: 2.30x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 26.6 us: 2.20x faster                                                   |
| async_tree_none          | 728 ms                                                 | 335 ms: 2.18x faster                                                    |
| richards_super           | 94.7 ms                                                | 45.9 ms: 2.07x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 435 ms: 2.00x faster                                                    |
| chaos                    | 115 ms                                                 | 58.2 ms: 1.98x faster                                                   |
| richards                 | 79.3 ms                                                | 40.5 ms: 1.96x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 918 ms: 1.93x faster                                                    |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.91x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 66.8 ms: 1.91x faster                                                   |
| logging_silent           | 190 ns                                                 | 99.7 ns: 1.90x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 62.6 ms: 1.89x faster                                                   |
| raytrace                 | 507 ms                                                 | 269 ms: 1.88x faster                                                    |
| nbody                    | 154 ms                                                 | 81.7 ms: 1.88x faster                                                   |
| asyncio_tcp              | 922 ms                                                 | 501 ms: 1.84x faster                                                    |
| deepcopy                 | 479 us                                                 | 265 us: 1.81x faster                                                    |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 572 ms: 1.78x faster                                                    |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                   |
| spectral_norm            | 170 ms                                                 | 99.9 ms: 1.70x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 1.89 sec: 1.66x faster                                                  |
| mako                     | 16.3 ms                                                | 9.90 ms: 1.65x faster                                                   |
| go                       | 240 ms                                                 | 148 ms: 1.62x faster                                                    |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.61x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.35 ms: 1.61x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.59x faster                                                    |
| pyflate                  | 716 ms                                                 | 451 ms: 1.59x faster                                                    |
| float                    | 117 ms                                                 | 74.0 ms: 1.58x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                                    |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.80 ms: 1.53x faster                                                   |
| pylint                   | 551 ms                                                 | 367 ms: 1.50x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.72 ms: 1.50x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                                   |
| logging_format           | 9.09 us                                                | 6.15 us: 1.48x faster                                                   |
| scimark_fft              | 466 ms                                                 | 318 ms: 1.47x faster                                                    |
| fannkuch                 | 532 ms                                                 | 367 ms: 1.45x faster                                                    |
| tornado_http             | 136 ms                                                 | 94.2 ms: 1.45x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.54 ms: 1.43x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 738 ms: 1.38x faster                                                    |
| thrift                   | 1.07 ms                                                | 787 us: 1.36x faster                                                    |
| html5lib                 | 88.9 ms                                                | 65.3 ms: 1.36x faster                                                   |
| django_template          | 48.2 ms                                                | 35.4 ms: 1.36x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.35x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 59.0 ms: 1.34x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.58 sec: 1.33x faster                                                  |
| regex_compile            | 188 ms                                                 | 142 ms: 1.33x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                   |
| genshi_text              | 31.8 ms                                                | 25.3 ms: 1.26x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                    |
| nqueens                  | 106 ms                                                 | 85.7 ms: 1.23x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 821 us: 1.20x faster                                                    |
| 2to3                     | 348 ms                                                 | 293 ms: 1.19x faster                                                    |
| genshi_xml               | 66.0 ms                                                | 56.3 ms: 1.17x faster                                                   |
| sympy_str                | 346 ms                                                 | 296 ms: 1.17x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 85.4 ms: 1.16x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 59.6 ms: 1.16x faster                                                   |
| sympy_sum                | 196 ms                                                 | 169 ms: 1.16x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.87 sec: 1.15x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 22.7 ms: 1.14x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 103 ms: 1.13x faster                                                    |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                                    |
| sympy_expand             | 566 ms                                                 | 505 ms: 1.12x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.10x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 153 ms: 1.10x faster                                                    |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                   |
| json                     | 5.69 ms                                                | 5.25 ms: 1.08x faster                                                   |
| regex_dna                | 227 ms                                                 | 211 ms: 1.08x faster                                                    |
| regex_effbot             | 3.63 ms                                                | 3.49 ms: 1.04x faster                                                   |
| gc_traversal             | 3.62 ms                                                | 3.51 ms: 1.03x faster                                                   |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                    |
| async_generators         | 444 ms                                                 | 455 ms: 1.03x slower                                                    |
| telco                    | 7.27 ms                                                | 7.75 ms: 1.07x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                                   |
| coverage                 | 79.4 ms                                                | 85.6 ms: 1.08x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.19x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                            |

Benchmark hidden because not significant (2): bench_mp_pool, asyncio_websockets
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240813-3.14.0a0-11fa189-JIT/bm-20240813-linux-x86_64-savannahostrowski-jit_mem_100-3.14.0a0-11fa189.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.17x