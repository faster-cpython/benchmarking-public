# Results vs. 3.10.4

- fork: encukou
- ref: immortal_interned
- machine: linux-x86_64
- commit hash: 686d2b6
- commit date: 2024-06-18
- overall geometric mean: 1.36x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 273 ms: 1.28x faster                                                |
| docutils       | 3.30 sec                                               | 2.79 sec: 1.18x faster                                              |
| html5lib       | 88.9 ms                                                | 68.3 ms: 1.30x faster                                               |
| tornado_http   | 136 ms                                                 | 94.2 ms: 1.45x faster                                               |
| Geometric mean | (ref)                                                  | 1.30x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 375 ms: 1.94x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 463 ms: 1.88x faster                                                |
| async_tree_io           | 1.77 sec                                               | 946 ms: 1.87x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 625 ms: 1.62x faster                                                |
| Geometric mean          | (ref)                                                  | 1.83x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.5 ms: 1.77x faster                                               |
| float          | 117 ms                                                 | 77.7 ms: 1.51x faster                                               |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.39x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 133 ms: 1.42x faster                                                |
| regex_v8       | 27.8 ms                                                | 25.9 ms: 1.07x faster                                               |
| regex_dna      | 227 ms                                                 | 235 ms: 1.04x slower                                                |
| regex_effbot   | 3.63 ms                                                | 3.83 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                  | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 308 us: 1.57x faster                                                |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                                |
| tomli_loads          | 3.14 sec                                               | 2.12 sec: 1.48x faster                                              |
| json_dumps           | 14.2 ms                                                | 10.9 ms: 1.30x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 60.9 ms: 1.30x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 87.2 ms: 1.14x faster                                               |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 157 ms: 1.07x faster                                                |
| pickle_list          | 5.08 us                                                | 5.00 us: 1.02x faster                                               |
| unpickle             | 14.4 us                                                | 15.3 us: 1.06x slower                                               |
| pickle               | 10.7 us                                                | 11.9 us: 1.12x slower                                               |
| pickle_dict          | 29.6 us                                                | 35.6 us: 1.20x slower                                               |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                        |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.8 ms: 1.35x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 7.18 ms: 1.21x slower                                               |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                               |
| django_template | 48.2 ms                                                | 34.6 ms: 1.39x faster                                               |
| genshi_text     | 31.8 ms                                                | 23.3 ms: 1.37x faster                                               |
| genshi_xml      | 66.0 ms                                                | 50.4 ms: 1.31x faster                                               |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                                |
| generators               | 80.1 ms                                                | 29.5 ms: 2.72x faster                                               |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                               |
| async_tree_none          | 728 ms                                                 | 375 ms: 1.94x faster                                                |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                                |
| chaos                    | 115 ms                                                 | 61.3 ms: 1.88x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 463 ms: 1.88x faster                                                |
| async_tree_io            | 1.77 sec                                               | 946 ms: 1.87x faster                                                |
| asyncio_tcp              | 922 ms                                                 | 497 ms: 1.86x faster                                                |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                |
| deepcopy                 | 479 us                                                 | 267 us: 1.79x faster                                                |
| nbody                    | 154 ms                                                 | 86.5 ms: 1.77x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 67.7 ms: 1.75x faster                                               |
| pylint                   | 551 ms                                                 | 317 ms: 1.74x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 74.8 ms: 1.71x faster                                               |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                               |
| richards_super           | 94.7 ms                                                | 55.5 ms: 1.71x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.18 ms: 1.68x faster                                               |
| go                       | 240 ms                                                 | 145 ms: 1.65x faster                                                |
| scimark_sor              | 220 ms                                                 | 133 ms: 1.65x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 625 ms: 1.62x faster                                                |
| richards                 | 79.3 ms                                                | 48.9 ms: 1.62x faster                                               |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                               |
| pickle_pure_python       | 484 us                                                 | 308 us: 1.57x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                                |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                               |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                               |
| float                    | 117 ms                                                 | 77.7 ms: 1.51x faster                                               |
| pyflate                  | 716 ms                                                 | 478 ms: 1.50x faster                                                |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                                |
| tomli_loads              | 3.14 sec                                               | 2.12 sec: 1.48x faster                                              |
| tornado_http             | 136 ms                                                 | 94.2 ms: 1.45x faster                                               |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                               |
| logging_simple           | 8.30 us                                                | 5.82 us: 1.43x faster                                               |
| regex_compile            | 188 ms                                                 | 133 ms: 1.42x faster                                                |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.83 sec: 1.40x faster                                              |
| logging_format           | 9.09 us                                                | 6.49 us: 1.40x faster                                               |
| django_template          | 48.2 ms                                                | 34.6 ms: 1.39x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.37x faster                                              |
| fannkuch                 | 532 ms                                                 | 388 ms: 1.37x faster                                                |
| genshi_text              | 31.8 ms                                                | 23.3 ms: 1.37x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 745 ms: 1.37x faster                                                |
| python_startup           | 14.6 ms                                                | 10.8 ms: 1.35x faster                                               |
| thrift                   | 1.07 ms                                                | 804 us: 1.33x faster                                                |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                              |
| nqueens                  | 106 ms                                                 | 80.3 ms: 1.32x faster                                               |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                |
| genshi_xml               | 66.0 ms                                                | 50.4 ms: 1.31x faster                                               |
| json_dumps               | 14.2 ms                                                | 10.9 ms: 1.30x faster                                               |
| html5lib                 | 88.9 ms                                                | 68.3 ms: 1.30x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 60.9 ms: 1.30x faster                                               |
| dulwich_log              | 84.3 ms                                                | 65.2 ms: 1.29x faster                                               |
| 2to3                     | 348 ms                                                 | 273 ms: 1.28x faster                                                |
| sympy_sum                | 196 ms                                                 | 154 ms: 1.27x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 20.3 ms: 1.27x faster                                               |
| scimark_fft              | 466 ms                                                 | 367 ms: 1.27x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 54.6 ms: 1.27x faster                                               |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.27x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.15 ms: 1.26x faster                                               |
| sympy_str                | 346 ms                                                 | 279 ms: 1.24x faster                                                |
| dask                     | 441 ms                                                 | 366 ms: 1.20x faster                                                |
| sympy_expand             | 566 ms                                                 | 472 ms: 1.20x faster                                                |
| bench_thread_pool        | 986 us                                                 | 832 us: 1.19x faster                                                |
| docutils                 | 3.30 sec                                               | 2.79 sec: 1.18x faster                                              |
| xml_etree_generate       | 99.4 ms                                                | 87.2 ms: 1.14x faster                                               |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                                |
| json                     | 5.69 ms                                                | 5.21 ms: 1.09x faster                                               |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.09x faster                                                |
| regex_v8                 | 27.8 ms                                                | 25.9 ms: 1.07x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 157 ms: 1.07x faster                                                |
| mdp                      | 2.85 sec                                               | 2.72 sec: 1.05x faster                                              |
| sqlite_synth             | 3.02 us                                                | 2.95 us: 1.02x faster                                               |
| pickle_list              | 5.08 us                                                | 5.00 us: 1.02x faster                                               |
| async_generators         | 444 ms                                                 | 440 ms: 1.01x faster                                                |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                                |
| bench_mp_pool            | 24.0 ms                                                | 23.9 ms: 1.00x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.01x slower                                                |
| regex_dna                | 227 ms                                                 | 235 ms: 1.04x slower                                                |
| gc_traversal             | 3.62 ms                                                | 3.81 ms: 1.05x slower                                               |
| regex_effbot             | 3.63 ms                                                | 3.83 ms: 1.05x slower                                               |
| unpickle                 | 14.4 us                                                | 15.3 us: 1.06x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                               |
| pickle                   | 10.7 us                                                | 11.9 us: 1.12x slower                                               |
| telco                    | 7.27 ms                                                | 8.32 ms: 1.14x slower                                               |
| coverage                 | 79.4 ms                                                | 93.8 ms: 1.18x slower                                               |
| pickle_dict              | 29.6 us                                                | 35.6 us: 1.20x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 7.18 ms: 1.21x slower                                               |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                        |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240618-3.14.0a0-686d2b6/bm-20240618-linux-x86_64-encukou-immortal_interned-3.14.0a0-686d2b6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.11x