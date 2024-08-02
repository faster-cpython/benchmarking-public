# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow_no_yield
- machine: linux-x86_64
- commit hash: ae6f199
- commit date: 2024-07-08
- overall geometric mean: 1.41x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 275 ms: 1.27x faster                                                      |
| docutils       | 3.30 sec                                               | 3.00 sec: 1.10x faster                                                    |
| html5lib       | 88.9 ms                                                | 67.4 ms: 1.32x faster                                                     |
| tornado_http   | 136 ms                                                 | 96.8 ms: 1.41x faster                                                     |
| Geometric mean | (ref)                                                  | 1.27x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 324 ms: 2.25x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 834 ms: 2.12x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 411 ms: 2.12x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 568 ms: 1.79x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.06x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.0 ms: 1.90x faster                                                     |
| float          | 117 ms                                                 | 69.5 ms: 1.68x faster                                                     |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.48x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 140 ms: 1.35x faster                                                      |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.13x faster                                                     |
| regex_effbot   | 3.63 ms                                                | 3.70 ms: 1.02x slower                                                     |
| regex_dna      | 227 ms                                                 | 232 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 295 us: 1.64x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 206 us: 1.60x faster                                                      |
| tomli_loads          | 3.14 sec                                               | 2.03 sec: 1.54x faster                                                    |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 57.9 ms: 1.37x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 82.2 ms: 1.21x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 99.7 ms: 1.16x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                      |
| json_loads           | 31.2 us                                                | 27.8 us: 1.12x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.81 ms: 1.66x faster                                                     |
| django_template | 48.2 ms                                                | 36.9 ms: 1.31x faster                                                     |
| genshi_text     | 31.8 ms                                                | 25.2 ms: 1.26x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 58.7 ms: 1.12x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.17x faster                                                      |
| generators               | 80.1 ms                                                | 30.0 ms: 2.67x faster                                                     |
| async_tree_none          | 728 ms                                                 | 324 ms: 2.25x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 834 ms: 2.12x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 411 ms: 2.12x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 57.4 ms: 2.06x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 28.8 us: 2.03x faster                                                     |
| richards_super           | 94.7 ms                                                | 47.6 ms: 1.99x faster                                                     |
| chaos                    | 115 ms                                                 | 58.8 ms: 1.96x faster                                                     |
| logging_silent           | 190 ns                                                 | 98.1 ns: 1.93x faster                                                     |
| nbody                    | 154 ms                                                 | 81.0 ms: 1.90x faster                                                     |
| deltablue                | 7.91 ms                                                | 4.20 ms: 1.89x faster                                                     |
| raytrace                 | 507 ms                                                 | 269 ms: 1.88x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 67.8 ms: 1.88x faster                                                     |
| richards                 | 79.3 ms                                                | 43.1 ms: 1.84x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 504 ms: 1.83x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 568 ms: 1.79x faster                                                      |
| deepcopy                 | 479 us                                                 | 270 us: 1.77x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                     |
| float                    | 117 ms                                                 | 69.5 ms: 1.68x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                     |
| scimark_sor              | 220 ms                                                 | 131 ms: 1.67x faster                                                      |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.67x faster                                                      |
| mako                     | 16.3 ms                                                | 9.81 ms: 1.66x faster                                                     |
| go                       | 240 ms                                                 | 145 ms: 1.66x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 295 us: 1.64x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 206 us: 1.60x faster                                                      |
| pyflate                  | 716 ms                                                 | 448 ms: 1.60x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.68 ms: 1.56x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 2.03 sec: 1.54x faster                                                    |
| pylint                   | 551 ms                                                 | 358 ms: 1.54x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.33 ms: 1.49x faster                                                     |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.61 us: 1.48x faster                                                     |
| logging_format           | 9.09 us                                                | 6.15 us: 1.48x faster                                                     |
| scimark_fft              | 466 ms                                                 | 316 ms: 1.47x faster                                                      |
| fannkuch                 | 532 ms                                                 | 362 ms: 1.47x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 707 ms: 1.44x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.44x faster                                                    |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                    |
| scimark_lu               | 176 ms                                                 | 124 ms: 1.42x faster                                                      |
| tornado_http             | 136 ms                                                 | 96.8 ms: 1.41x faster                                                     |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.38x faster                                                    |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 57.9 ms: 1.37x faster                                                     |
| regex_compile            | 188 ms                                                 | 140 ms: 1.35x faster                                                      |
| thrift                   | 1.07 ms                                                | 807 us: 1.33x faster                                                      |
| html5lib                 | 88.9 ms                                                | 67.4 ms: 1.32x faster                                                     |
| django_template          | 48.2 ms                                                | 36.9 ms: 1.31x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                     |
| 2to3                     | 348 ms                                                 | 275 ms: 1.27x faster                                                      |
| genshi_text              | 31.8 ms                                                | 25.2 ms: 1.26x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 55.6 ms: 1.24x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 68.2 ms: 1.24x faster                                                     |
| nqueens                  | 106 ms                                                 | 86.5 ms: 1.22x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 82.2 ms: 1.21x faster                                                     |
| dask                     | 441 ms                                                 | 368 ms: 1.20x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 845 us: 1.17x faster                                                      |
| sympy_sum                | 196 ms                                                 | 169 ms: 1.16x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 99.7 ms: 1.16x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 22.5 ms: 1.15x faster                                                     |
| sympy_str                | 346 ms                                                 | 302 ms: 1.14x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.13x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 58.7 ms: 1.12x faster                                                     |
| json_loads               | 31.2 us                                                | 27.8 us: 1.12x faster                                                     |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                      |
| sympy_expand             | 566 ms                                                 | 512 ms: 1.11x faster                                                      |
| docutils                 | 3.30 sec                                               | 3.00 sec: 1.10x faster                                                    |
| json                     | 5.69 ms                                                | 5.19 ms: 1.10x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.74 sec: 1.04x faster                                                    |
| gc_traversal             | 3.62 ms                                                | 3.55 ms: 1.02x faster                                                     |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| async_generators         | 444 ms                                                 | 452 ms: 1.02x slower                                                      |
| regex_effbot             | 3.63 ms                                                | 3.70 ms: 1.02x slower                                                     |
| regex_dna                | 227 ms                                                 | 232 ms: 1.02x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                                     |
| telco                    | 7.27 ms                                                | 7.89 ms: 1.09x slower                                                     |
| coverage                 | 79.4 ms                                                | 92.6 ms: 1.17x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                              |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240708-3.14.0a0-ae6f199-JIT/bm-20240708-linux-x86_64-brandtbucher-underflow_no_yield-3.14.0a0-ae6f199.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.19x