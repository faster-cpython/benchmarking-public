# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 55cda27
- commit date: 2024-07-02
- overall geometric mean: 1.39x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 284 ms: 1.23x faster                                             |
| docutils       | 3.30 sec                                               | 3.03 sec: 1.09x faster                                           |
| html5lib       | 88.9 ms                                                | 68.4 ms: 1.30x faster                                            |
| tornado_http   | 136 ms                                                 | 97.4 ms: 1.40x faster                                            |
| Geometric mean | (ref)                                                  | 1.25x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.24x faster                                             |
| async_tree_memoization  | 870 ms                                                 | 411 ms: 2.12x faster                                             |
| async_tree_io           | 1.77 sec                                               | 863 ms: 2.05x faster                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 567 ms: 1.79x faster                                             |
| Geometric mean          | (ref)                                                  | 2.04x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.1 ms: 1.94x faster                                            |
| float          | 117 ms                                                 | 69.6 ms: 1.68x faster                                            |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.50x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 139 ms: 1.36x faster                                             |
| regex_v8       | 27.8 ms                                                | 26.0 ms: 1.07x faster                                            |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.10x faster                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 204 us: 1.62x faster                                             |
| pickle_pure_python   | 484 us                                                 | 300 us: 1.62x faster                                             |
| tomli_loads          | 3.14 sec                                               | 2.04 sec: 1.54x faster                                           |
| xml_etree_process    | 79.1 ms                                                | 57.9 ms: 1.37x faster                                            |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                            |
| xml_etree_generate   | 99.4 ms                                                | 82.0 ms: 1.21x faster                                            |
| xml_etree_iterparse  | 115 ms                                                 | 99.7 ms: 1.16x faster                                            |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.13x faster                                             |
| json_loads           | 31.2 us                                                | 27.8 us: 1.12x faster                                            |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                            |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                            |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.61 ms: 1.70x faster                                            |
| django_template | 48.2 ms                                                | 36.9 ms: 1.31x faster                                            |
| genshi_text     | 31.8 ms                                                | 24.4 ms: 1.31x faster                                            |
| genshi_xml      | 66.0 ms                                                | 62.7 ms: 1.05x faster                                            |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 172 us: 3.16x faster                                             |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.24x faster                                             |
| async_tree_memoization   | 870 ms                                                 | 411 ms: 2.12x faster                                             |
| scimark_monte_carlo      | 118 ms                                                 | 57.3 ms: 2.06x faster                                            |
| deepcopy_memo            | 58.5 us                                                | 28.4 us: 2.06x faster                                            |
| async_tree_io            | 1.77 sec                                               | 863 ms: 2.05x faster                                             |
| logging_silent           | 190 ns                                                 | 97.6 ns: 1.94x faster                                            |
| nbody                    | 154 ms                                                 | 79.1 ms: 1.94x faster                                            |
| deltablue                | 7.91 ms                                                | 4.10 ms: 1.93x faster                                            |
| crypto_pyaes             | 128 ms                                                 | 66.8 ms: 1.91x faster                                            |
| chaos                    | 115 ms                                                 | 60.5 ms: 1.91x faster                                            |
| richards_super           | 94.7 ms                                                | 50.1 ms: 1.89x faster                                            |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                             |
| asyncio_tcp              | 922 ms                                                 | 507 ms: 1.82x faster                                             |
| richards                 | 79.3 ms                                                | 44.2 ms: 1.79x faster                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 567 ms: 1.79x faster                                             |
| deepcopy                 | 479 us                                                 | 274 us: 1.75x faster                                             |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                            |
| mako                     | 16.3 ms                                                | 9.61 ms: 1.70x faster                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.69x faster                                            |
| float                    | 117 ms                                                 | 69.6 ms: 1.68x faster                                            |
| go                       | 240 ms                                                 | 144 ms: 1.66x faster                                             |
| scimark_sor              | 220 ms                                                 | 132 ms: 1.66x faster                                             |
| pyflate                  | 716 ms                                                 | 432 ms: 1.66x faster                                             |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.64x faster                                             |
| unpickle_pure_python     | 331 us                                                 | 204 us: 1.62x faster                                             |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.62x faster                                             |
| hexiom                   | 10.4 ms                                                | 6.58 ms: 1.58x faster                                            |
| generators               | 80.1 ms                                                | 51.2 ms: 1.56x faster                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                            |
| tomli_loads              | 3.14 sec                                               | 2.04 sec: 1.54x faster                                           |
| scimark_fft              | 466 ms                                                 | 305 ms: 1.53x faster                                             |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.77 us: 1.50x faster                                            |
| logging_simple           | 8.30 us                                                | 5.55 us: 1.50x faster                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.37 ms: 1.48x faster                                            |
| fannkuch                 | 532 ms                                                 | 360 ms: 1.48x faster                                             |
| logging_format           | 9.09 us                                                | 6.17 us: 1.47x faster                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                           |
| tornado_http             | 136 ms                                                 | 97.4 ms: 1.40x faster                                            |
| scimark_lu               | 176 ms                                                 | 126 ms: 1.40x faster                                             |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                            |
| pylint                   | 551 ms                                                 | 398 ms: 1.38x faster                                             |
| pprint_safe_repr         | 1.02 sec                                               | 744 ms: 1.37x faster                                             |
| xml_etree_process        | 79.1 ms                                                | 57.9 ms: 1.37x faster                                            |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                            |
| regex_compile            | 188 ms                                                 | 139 ms: 1.36x faster                                             |
| thrift                   | 1.07 ms                                                | 799 us: 1.34x faster                                             |
| pprint_pformat           | 2.10 sec                                               | 1.59 sec: 1.32x faster                                           |
| django_template          | 48.2 ms                                                | 36.9 ms: 1.31x faster                                            |
| genshi_text              | 31.8 ms                                                | 24.4 ms: 1.31x faster                                            |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.30x faster                                           |
| html5lib                 | 88.9 ms                                                | 68.4 ms: 1.30x faster                                            |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.28x faster                                            |
| 2to3                     | 348 ms                                                 | 284 ms: 1.23x faster                                             |
| nqueens                  | 106 ms                                                 | 86.7 ms: 1.22x faster                                            |
| xml_etree_generate       | 99.4 ms                                                | 82.0 ms: 1.21x faster                                            |
| sqlglot_optimize         | 69.2 ms                                                | 57.5 ms: 1.20x faster                                            |
| sqlglot_normalize        | 143 ms                                                 | 119 ms: 1.20x faster                                             |
| dask                     | 441 ms                                                 | 369 ms: 1.19x faster                                             |
| bench_thread_pool        | 986 us                                                 | 836 us: 1.18x faster                                             |
| dulwich_log              | 84.3 ms                                                | 72.3 ms: 1.17x faster                                            |
| xml_etree_iterparse      | 115 ms                                                 | 99.7 ms: 1.16x faster                                            |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.13x faster                                             |
| json_loads               | 31.2 us                                                | 27.8 us: 1.12x faster                                            |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                             |
| json                     | 5.69 ms                                                | 5.09 ms: 1.12x faster                                            |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                           |
| sympy_str                | 346 ms                                                 | 310 ms: 1.12x faster                                             |
| sympy_integrate          | 25.8 ms                                                | 23.2 ms: 1.11x faster                                            |
| sympy_sum                | 196 ms                                                 | 179 ms: 1.10x faster                                             |
| sympy_expand             | 566 ms                                                 | 517 ms: 1.09x faster                                             |
| docutils                 | 3.30 sec                                               | 3.03 sec: 1.09x faster                                           |
| regex_v8                 | 27.8 ms                                                | 26.0 ms: 1.07x faster                                            |
| genshi_xml               | 66.0 ms                                                | 62.7 ms: 1.05x faster                                            |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                             |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                             |
| async_generators         | 444 ms                                                 | 459 ms: 1.03x slower                                             |
| gc_traversal             | 3.62 ms                                                | 3.81 ms: 1.05x slower                                            |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                            |
| telco                    | 7.27 ms                                                | 8.07 ms: 1.11x slower                                            |
| coverage                 | 79.4 ms                                                | 93.3 ms: 1.17x slower                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                            |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                     |

Benchmark hidden because not significant (3): asyncio_websockets, bench_mp_pool, regex_effbot
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240702-3.14.0a0-55cda27-JIT/bm-20240702-linux-x86_64-brandtbucher-underflow-3.14.0a0-55cda27.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.19x