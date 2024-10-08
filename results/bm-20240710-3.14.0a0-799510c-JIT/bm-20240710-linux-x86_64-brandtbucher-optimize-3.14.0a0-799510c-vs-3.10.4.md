# Results vs. 3.10.4

- fork: brandtbucher
- ref: optimize
- machine: linux-x86_64
- commit hash: 799510c
- commit date: 2024-07-10
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 271 ms: 1.29x faster                                            |
| docutils       | 3.30 sec                                               | 6.74 sec: 2.05x slower                                          |
| html5lib       | 88.9 ms                                                | 77.0 ms: 1.15x faster                                           |
| tornado_http   | 136 ms                                                 | 97.9 ms: 1.39x faster                                           |
| Geometric mean | (ref)                                                  | 1.00x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 329 ms: 2.21x faster                                            |
| async_tree_memoization  | 870 ms                                                 | 412 ms: 2.11x faster                                            |
| async_tree_io           | 1.77 sec                                               | 896 ms: 1.97x faster                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 573 ms: 1.77x faster                                            |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 77.4 ms: 1.98x faster                                           |
| float          | 117 ms                                                 | 70.9 ms: 1.65x faster                                           |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                            |
| Geometric mean | (ref)                                                  | 1.50x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                            |
| regex_v8       | 27.8 ms                                                | 25.6 ms: 1.08x faster                                           |
| regex_dna      | 227 ms                                                 | 223 ms: 1.01x faster                                            |
| regex_effbot   | 3.63 ms                                                | 3.88 ms: 1.07x slower                                           |
| Geometric mean | (ref)                                                  | 1.10x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                          |
| pickle_pure_python   | 484 us                                                 | 303 us: 1.60x faster                                            |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                            |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                           |
| xml_etree_process    | 79.1 ms                                                | 58.1 ms: 1.36x faster                                           |
| xml_etree_generate   | 99.4 ms                                                | 84.8 ms: 1.17x faster                                           |
| json_loads           | 31.2 us                                                | 27.4 us: 1.14x faster                                           |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                            |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.13x faster                                            |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                           |
| python_startup_no_site | 5.93 ms                                                | 7.12 ms: 1.20x slower                                           |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.87 ms: 1.65x faster                                           |
| django_template | 48.2 ms                                                | 40.3 ms: 1.20x faster                                           |
| genshi_text     | 31.8 ms                                                | 27.0 ms: 1.18x faster                                           |
| genshi_xml      | 66.0 ms                                                | 62.2 ms: 1.06x faster                                           |
| Geometric mean  | (ref)                                                  | 1.25x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                            |
| deltablue                | 7.91 ms                                                | 3.43 ms: 2.31x faster                                           |
| async_tree_none          | 728 ms                                                 | 329 ms: 2.21x faster                                            |
| deepcopy_memo            | 58.5 us                                                | 27.2 us: 2.15x faster                                           |
| richards_super           | 94.7 ms                                                | 44.6 ms: 2.12x faster                                           |
| async_tree_memoization   | 870 ms                                                 | 412 ms: 2.11x faster                                            |
| chaos                    | 115 ms                                                 | 56.0 ms: 2.06x faster                                           |
| richards                 | 79.3 ms                                                | 38.5 ms: 2.06x faster                                           |
| nbody                    | 154 ms                                                 | 77.4 ms: 1.98x faster                                           |
| async_tree_io            | 1.77 sec                                               | 896 ms: 1.97x faster                                            |
| crypto_pyaes             | 128 ms                                                 | 66.6 ms: 1.92x faster                                           |
| logging_silent           | 190 ns                                                 | 102 ns: 1.85x faster                                            |
| scimark_monte_carlo      | 118 ms                                                 | 64.1 ms: 1.84x faster                                           |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                            |
| asyncio_tcp              | 922 ms                                                 | 516 ms: 1.79x faster                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 573 ms: 1.77x faster                                            |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                            |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.74x faster                                           |
| spectral_norm            | 170 ms                                                 | 98.0 ms: 1.73x faster                                           |
| go                       | 240 ms                                                 | 140 ms: 1.71x faster                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                           |
| generators               | 80.1 ms                                                | 47.6 ms: 1.68x faster                                           |
| mako                     | 16.3 ms                                                | 9.87 ms: 1.65x faster                                           |
| float                    | 117 ms                                                 | 70.9 ms: 1.65x faster                                           |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                          |
| pickle_pure_python       | 484 us                                                 | 303 us: 1.60x faster                                            |
| hexiom                   | 10.4 ms                                                | 6.52 ms: 1.59x faster                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.64 us: 1.58x faster                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                           |
| pyflate                  | 716 ms                                                 | 463 ms: 1.55x faster                                            |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                            |
| logging_simple           | 8.30 us                                                | 5.54 us: 1.50x faster                                           |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                           |
| scimark_fft              | 466 ms                                                 | 316 ms: 1.47x faster                                            |
| scimark_lu               | 176 ms                                                 | 121 ms: 1.46x faster                                            |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                            |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                          |
| pprint_safe_repr         | 1.02 sec                                               | 716 ms: 1.42x faster                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                          |
| fannkuch                 | 532 ms                                                 | 377 ms: 1.41x faster                                            |
| tornado_http             | 136 ms                                                 | 97.9 ms: 1.39x faster                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.67 ms: 1.39x faster                                           |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                           |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                           |
| xml_etree_process        | 79.1 ms                                                | 58.1 ms: 1.36x faster                                           |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.35x faster                                          |
| thrift                   | 1.07 ms                                                | 806 us: 1.33x faster                                            |
| pylint                   | 551 ms                                                 | 425 ms: 1.30x faster                                            |
| dulwich_log              | 84.3 ms                                                | 65.4 ms: 1.29x faster                                           |
| 2to3                     | 348 ms                                                 | 271 ms: 1.29x faster                                            |
| coroutines               | 35.1 ms                                                | 27.5 ms: 1.27x faster                                           |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                           |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                            |
| django_template          | 48.2 ms                                                | 40.3 ms: 1.20x faster                                           |
| genshi_text              | 31.8 ms                                                | 27.0 ms: 1.18x faster                                           |
| xml_etree_generate       | 99.4 ms                                                | 84.8 ms: 1.17x faster                                           |
| sympy_sum                | 196 ms                                                 | 168 ms: 1.17x faster                                            |
| bench_thread_pool        | 986 us                                                 | 853 us: 1.16x faster                                            |
| html5lib                 | 88.9 ms                                                | 77.0 ms: 1.15x faster                                           |
| sqlglot_optimize         | 69.2 ms                                                | 60.0 ms: 1.15x faster                                           |
| dask                     | 441 ms                                                 | 383 ms: 1.15x faster                                            |
| sympy_expand             | 566 ms                                                 | 493 ms: 1.15x faster                                            |
| sympy_str                | 346 ms                                                 | 302 ms: 1.15x faster                                            |
| json_loads               | 31.2 us                                                | 27.4 us: 1.14x faster                                           |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                            |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.13x faster                                            |
| nqueens                  | 106 ms                                                 | 94.1 ms: 1.12x faster                                           |
| json                     | 5.69 ms                                                | 5.08 ms: 1.12x faster                                           |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                            |
| regex_v8                 | 27.8 ms                                                | 25.6 ms: 1.08x faster                                           |
| genshi_xml               | 66.0 ms                                                | 62.2 ms: 1.06x faster                                           |
| mdp                      | 2.85 sec                                               | 2.70 sec: 1.05x faster                                          |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                            |
| sympy_integrate          | 25.8 ms                                                | 25.3 ms: 1.02x faster                                           |
| regex_dna                | 227 ms                                                 | 223 ms: 1.01x faster                                            |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                            |
| gc_traversal             | 3.62 ms                                                | 3.80 ms: 1.05x slower                                           |
| regex_effbot             | 3.63 ms                                                | 3.88 ms: 1.07x slower                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                           |
| telco                    | 7.27 ms                                                | 7.90 ms: 1.09x slower                                           |
| async_generators         | 444 ms                                                 | 514 ms: 1.16x slower                                            |
| coverage                 | 79.4 ms                                                | 93.3 ms: 1.17x slower                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.12 ms: 1.20x slower                                           |
| docutils                 | 3.30 sec                                               | 6.74 sec: 2.05x slower                                          |
| raytrace                 | 507 ms                                                 | 4.85 sec: 9.57x slower                                          |
| Geometric mean           | (ref)                                                  | 1.33x faster                                                    |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240710-3.14.0a0-799510c-JIT/bm-20240710-linux-x86_64-brandtbucher-optimize-3.14.0a0-799510c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.19x