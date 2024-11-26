# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.410x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 271 ms: 1.28x faster                                                |
| docutils       | 3.30 sec                                               | 2.88 sec: 1.14x faster                                              |
| html5lib       | 88.9 ms                                                | 67.1 ms: 1.32x faster                                               |
| tornado_http   | 136 ms                                                 | 94.0 ms: 1.45x faster                                               |
| Geometric mean | (ref)                                                  | 1.30x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 338 ms: 2.15x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 417 ms: 2.09x faster                                                |
| async_tree_io           | 1.77 sec                                               | 861 ms: 2.05x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 573 ms: 1.77x faster                                                |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.4 ms: 1.86x faster                                               |
| float          | 117 ms                                                 | 75.6 ms: 1.55x faster                                               |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.43x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.40x faster                                                |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                               |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                |
| Geometric mean | (ref)                                                  | 1.14x faster                                                        |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.64x faster                                              |
| pickle_pure_python   | 484 us                                                 | 313 us: 1.55x faster                                                |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 54.8 ms: 1.44x faster                                               |
| json_dumps           | 14.2 ms                                                | 10.8 ms: 1.31x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 78.3 ms: 1.27x faster                                               |
| json_loads           | 31.2 us                                                | 26.6 us: 1.17x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 100 ms: 1.15x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.8 ms: 1.23x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                               |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.0 ms: 1.63x faster                                               |
| django_template | 48.2 ms                                                | 35.4 ms: 1.36x faster                                               |
| genshi_text     | 31.8 ms                                                | 26.3 ms: 1.21x faster                                               |
| genshi_xml      | 66.0 ms                                                | 58.4 ms: 1.13x faster                                               |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                                |
| deltablue                | 7.91 ms                                                | 3.24 ms: 2.44x faster                                               |
| generators               | 80.1 ms                                                | 35.1 ms: 2.28x faster                                               |
| richards_super           | 94.7 ms                                                | 43.8 ms: 2.16x faster                                               |
| async_tree_none          | 728 ms                                                 | 338 ms: 2.15x faster                                                |
| richards                 | 79.3 ms                                                | 37.1 ms: 2.13x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 417 ms: 2.09x faster                                                |
| async_tree_io            | 1.77 sec                                               | 861 ms: 2.05x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.2 us: 2.00x faster                                               |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 68.4 ms: 1.87x faster                                               |
| nbody                    | 154 ms                                                 | 82.4 ms: 1.86x faster                                               |
| raytrace                 | 507 ms                                                 | 272 ms: 1.86x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 63.5 ms: 1.86x faster                                               |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                                |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                |
| go                       | 240 ms                                                 | 130 ms: 1.84x faster                                                |
| deepcopy                 | 479 us                                                 | 266 us: 1.80x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 573 ms: 1.77x faster                                                |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                               |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.64x faster                                              |
| mako                     | 16.3 ms                                                | 10.0 ms: 1.63x faster                                               |
| pyflate                  | 716 ms                                                 | 447 ms: 1.60x faster                                                |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.55x faster                                                |
| float                    | 117 ms                                                 | 75.6 ms: 1.55x faster                                               |
| pickle_pure_python       | 484 us                                                 | 313 us: 1.55x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 1.67 ms: 1.55x faster                                               |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                               |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.91 ms: 1.50x faster                                               |
| pylint                   | 551 ms                                                 | 367 ms: 1.50x faster                                                |
| logging_format           | 9.09 us                                                | 6.08 us: 1.49x faster                                               |
| logging_simple           | 8.30 us                                                | 5.57 us: 1.49x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 689 ms: 1.48x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.43 sec: 1.47x faster                                              |
| spectral_norm            | 170 ms                                                 | 116 ms: 1.47x faster                                                |
| tornado_http             | 136 ms                                                 | 94.0 ms: 1.45x faster                                               |
| scimark_fft              | 466 ms                                                 | 322 ms: 1.45x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 54.8 ms: 1.44x faster                                               |
| fannkuch                 | 532 ms                                                 | 375 ms: 1.42x faster                                                |
| regex_compile            | 188 ms                                                 | 135 ms: 1.40x faster                                                |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                              |
| django_template          | 48.2 ms                                                | 35.4 ms: 1.36x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.77 ms: 1.36x faster                                               |
| thrift                   | 1.07 ms                                                | 800 us: 1.34x faster                                                |
| html5lib                 | 88.9 ms                                                | 67.1 ms: 1.32x faster                                               |
| json_dumps               | 14.2 ms                                                | 10.8 ms: 1.31x faster                                               |
| 2to3                     | 348 ms                                                 | 271 ms: 1.28x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 78.3 ms: 1.27x faster                                               |
| dulwich_log              | 84.3 ms                                                | 66.5 ms: 1.27x faster                                               |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                               |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                |
| python_startup           | 14.6 ms                                                | 11.8 ms: 1.23x faster                                               |
| genshi_text              | 31.8 ms                                                | 26.3 ms: 1.21x faster                                               |
| sqlglot_optimize         | 69.2 ms                                                | 58.3 ms: 1.19x faster                                               |
| nqueens                  | 106 ms                                                 | 89.4 ms: 1.18x faster                                               |
| json_loads               | 31.2 us                                                | 26.6 us: 1.17x faster                                               |
| sympy_str                | 346 ms                                                 | 296 ms: 1.17x faster                                                |
| json                     | 5.69 ms                                                | 4.93 ms: 1.15x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 100 ms: 1.15x faster                                                |
| sympy_expand             | 566 ms                                                 | 494 ms: 1.14x faster                                                |
| docutils                 | 3.30 sec                                               | 2.88 sec: 1.14x faster                                              |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                |
| sympy_sum                | 196 ms                                                 | 174 ms: 1.13x faster                                                |
| genshi_xml               | 66.0 ms                                                | 58.4 ms: 1.13x faster                                               |
| bench_thread_pool        | 986 us                                                 | 879 us: 1.12x faster                                                |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                              |
| sympy_integrate          | 25.8 ms                                                | 23.1 ms: 1.12x faster                                               |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                |
| async_generators         | 444 ms                                                 | 449 ms: 1.01x slower                                                |
| telco                    | 7.27 ms                                                | 7.71 ms: 1.06x slower                                               |
| coverage                 | 79.4 ms                                                | 84.3 ms: 1.06x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.74 ms: 1.31x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.67 ms: 1.65x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 83.4 ms: 3.47x slower                                               |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                        |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241021-3.14.0a1+-7b3da21-JIT/bm-20241021-linux-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.410x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.33x