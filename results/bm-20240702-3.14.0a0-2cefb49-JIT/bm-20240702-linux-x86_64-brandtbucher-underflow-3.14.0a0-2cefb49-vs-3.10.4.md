# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 2cefb49
- commit date: 2024-07-02
- overall geometric mean: 1.40x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 277 ms: 1.26x faster                                             |
| docutils       | 3.30 sec                                               | 3.03 sec: 1.09x faster                                           |
| html5lib       | 88.9 ms                                                | 69.2 ms: 1.28x faster                                            |
| tornado_http   | 136 ms                                                 | 97.0 ms: 1.41x faster                                            |
| Geometric mean | (ref)                                                  | 1.25x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 324 ms: 2.25x faster                                             |
| async_tree_memoization  | 870 ms                                                 | 410 ms: 2.12x faster                                             |
| async_tree_io           | 1.77 sec                                               | 853 ms: 2.07x faster                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 567 ms: 1.79x faster                                             |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.2 ms: 1.91x faster                                            |
| float          | 117 ms                                                 | 70.6 ms: 1.66x faster                                            |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.48x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 140 ms: 1.35x faster                                             |
| regex_v8       | 27.8 ms                                                | 26.7 ms: 1.04x faster                                            |
| regex_dna      | 227 ms                                                 | 238 ms: 1.05x slower                                             |
| regex_effbot   | 3.63 ms                                                | 4.03 ms: 1.11x slower                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 296 us: 1.64x faster                                             |
| unpickle_pure_python | 331 us                                                 | 202 us: 1.64x faster                                             |
| tomli_loads          | 3.14 sec                                               | 2.07 sec: 1.52x faster                                           |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                            |
| xml_etree_process    | 79.1 ms                                                | 59.1 ms: 1.34x faster                                            |
| xml_etree_generate   | 99.4 ms                                                | 82.1 ms: 1.21x faster                                            |
| xml_etree_iterparse  | 115 ms                                                 | 99.0 ms: 1.17x faster                                            |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                             |
| json_loads           | 31.2 us                                                | 27.7 us: 1.12x faster                                            |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                            |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                            |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.85 ms: 1.66x faster                                            |
| django_template | 48.2 ms                                                | 35.7 ms: 1.35x faster                                            |
| genshi_text     | 31.8 ms                                                | 24.2 ms: 1.31x faster                                            |
| genshi_xml      | 66.0 ms                                                | 61.8 ms: 1.07x faster                                            |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.17x faster                                             |
| generators               | 80.1 ms                                                | 30.8 ms: 2.60x faster                                            |
| async_tree_none          | 728 ms                                                 | 324 ms: 2.25x faster                                             |
| async_tree_memoization   | 870 ms                                                 | 410 ms: 2.12x faster                                             |
| async_tree_io            | 1.77 sec                                               | 853 ms: 2.07x faster                                             |
| deepcopy_memo            | 58.5 us                                                | 28.3 us: 2.06x faster                                            |
| scimark_monte_carlo      | 118 ms                                                 | 58.2 ms: 2.03x faster                                            |
| richards_super           | 94.7 ms                                                | 47.9 ms: 1.98x faster                                            |
| chaos                    | 115 ms                                                 | 59.1 ms: 1.95x faster                                            |
| logging_silent           | 190 ns                                                 | 97.2 ns: 1.95x faster                                            |
| nbody                    | 154 ms                                                 | 80.2 ms: 1.91x faster                                            |
| raytrace                 | 507 ms                                                 | 266 ms: 1.90x faster                                             |
| deltablue                | 7.91 ms                                                | 4.19 ms: 1.89x faster                                            |
| crypto_pyaes             | 128 ms                                                 | 67.9 ms: 1.88x faster                                            |
| richards                 | 79.3 ms                                                | 43.0 ms: 1.84x faster                                            |
| asyncio_tcp              | 922 ms                                                 | 505 ms: 1.83x faster                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 567 ms: 1.79x faster                                             |
| deepcopy                 | 479 us                                                 | 269 us: 1.78x faster                                             |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                            |
| go                       | 240 ms                                                 | 143 ms: 1.68x faster                                             |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                            |
| scimark_sor              | 220 ms                                                 | 132 ms: 1.66x faster                                             |
| float                    | 117 ms                                                 | 70.6 ms: 1.66x faster                                            |
| mako                     | 16.3 ms                                                | 9.85 ms: 1.66x faster                                            |
| pickle_pure_python       | 484 us                                                 | 296 us: 1.64x faster                                             |
| unpickle_pure_python     | 331 us                                                 | 202 us: 1.64x faster                                             |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                             |
| pyflate                  | 716 ms                                                 | 444 ms: 1.61x faster                                             |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                            |
| hexiom                   | 10.4 ms                                                | 6.67 ms: 1.56x faster                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.54x faster                                            |
| tomli_loads              | 3.14 sec                                               | 2.07 sec: 1.52x faster                                           |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                            |
| pylint                   | 551 ms                                                 | 367 ms: 1.50x faster                                             |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                            |
| fannkuch                 | 532 ms                                                 | 360 ms: 1.48x faster                                             |
| scimark_fft              | 466 ms                                                 | 316 ms: 1.47x faster                                             |
| logging_format           | 9.09 us                                                | 6.17 us: 1.47x faster                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.45 ms: 1.45x faster                                            |
| pprint_safe_repr         | 1.02 sec                                               | 712 ms: 1.43x faster                                             |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                           |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                           |
| tornado_http             | 136 ms                                                 | 97.0 ms: 1.41x faster                                            |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                            |
| scimark_lu               | 176 ms                                                 | 127 ms: 1.38x faster                                             |
| django_template          | 48.2 ms                                                | 35.7 ms: 1.35x faster                                            |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                            |
| regex_compile            | 188 ms                                                 | 140 ms: 1.35x faster                                             |
| xml_etree_process        | 79.1 ms                                                | 59.1 ms: 1.34x faster                                            |
| thrift                   | 1.07 ms                                                | 802 us: 1.34x faster                                             |
| genshi_text              | 31.8 ms                                                | 24.2 ms: 1.31x faster                                            |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.30x faster                                           |
| html5lib                 | 88.9 ms                                                | 69.2 ms: 1.28x faster                                            |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.27x faster                                            |
| 2to3                     | 348 ms                                                 | 277 ms: 1.26x faster                                             |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                             |
| sqlglot_optimize         | 69.2 ms                                                | 55.8 ms: 1.24x faster                                            |
| nqueens                  | 106 ms                                                 | 86.7 ms: 1.22x faster                                            |
| xml_etree_generate       | 99.4 ms                                                | 82.1 ms: 1.21x faster                                            |
| dask                     | 441 ms                                                 | 368 ms: 1.20x faster                                             |
| dulwich_log              | 84.3 ms                                                | 71.3 ms: 1.18x faster                                            |
| bench_thread_pool        | 986 us                                                 | 837 us: 1.18x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 99.0 ms: 1.17x faster                                            |
| sympy_sum                | 196 ms                                                 | 169 ms: 1.16x faster                                             |
| sympy_integrate          | 25.8 ms                                                | 22.5 ms: 1.15x faster                                            |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                             |
| sympy_str                | 346 ms                                                 | 305 ms: 1.13x faster                                             |
| json_loads               | 31.2 us                                                | 27.7 us: 1.12x faster                                            |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                             |
| json                     | 5.69 ms                                                | 5.14 ms: 1.11x faster                                            |
| mdp                      | 2.85 sec                                               | 2.60 sec: 1.10x faster                                           |
| sympy_expand             | 566 ms                                                 | 518 ms: 1.09x faster                                             |
| docutils                 | 3.30 sec                                               | 3.03 sec: 1.09x faster                                           |
| genshi_xml               | 66.0 ms                                                | 61.8 ms: 1.07x faster                                            |
| regex_v8                 | 27.8 ms                                                | 26.7 ms: 1.04x faster                                            |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                             |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                             |
| async_generators         | 444 ms                                                 | 458 ms: 1.03x slower                                             |
| gc_traversal             | 3.62 ms                                                | 3.77 ms: 1.04x slower                                            |
| regex_dna                | 227 ms                                                 | 238 ms: 1.05x slower                                             |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                            |
| telco                    | 7.27 ms                                                | 7.97 ms: 1.10x slower                                            |
| regex_effbot             | 3.63 ms                                                | 4.03 ms: 1.11x slower                                            |
| coverage                 | 79.4 ms                                                | 93.4 ms: 1.18x slower                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                            |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                     |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240702-3.14.0a0-2cefb49-JIT/bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-2cefb49.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.19x