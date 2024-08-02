# Results vs. 3.10.4

- fork: brandtbucher
- ref: underflow
- machine: linux-x86_64
- commit hash: 5156311
- commit date: 2024-07-08
- overall geometric mean: 1.40x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 282 ms: 1.23x faster                                             |
| docutils       | 3.30 sec                                               | 3.02 sec: 1.09x faster                                           |
| html5lib       | 88.9 ms                                                | 69.9 ms: 1.27x faster                                            |
| tornado_http   | 136 ms                                                 | 97.6 ms: 1.40x faster                                            |
| Geometric mean | (ref)                                                  | 1.24x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.23x faster                                             |
| async_tree_memoization  | 870 ms                                                 | 414 ms: 2.10x faster                                             |
| async_tree_io           | 1.77 sec                                               | 887 ms: 1.99x faster                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 568 ms: 1.79x faster                                             |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 78.9 ms: 1.95x faster                                            |
| float          | 117 ms                                                 | 70.6 ms: 1.66x faster                                            |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.49x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.36x faster                                             |
| regex_v8       | 27.8 ms                                                | 24.1 ms: 1.15x faster                                            |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.12x faster                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 199 us: 1.66x faster                                             |
| pickle_pure_python   | 484 us                                                 | 297 us: 1.63x faster                                             |
| tomli_loads          | 3.14 sec                                               | 2.06 sec: 1.53x faster                                           |
| xml_etree_process    | 79.1 ms                                                | 57.8 ms: 1.37x faster                                            |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.34x faster                                            |
| xml_etree_generate   | 99.4 ms                                                | 82.5 ms: 1.20x faster                                            |
| xml_etree_iterparse  | 115 ms                                                 | 99.1 ms: 1.17x faster                                            |
| json_loads           | 31.2 us                                                | 27.5 us: 1.14x faster                                            |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                             |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                            |
| python_startup_no_site | 5.93 ms                                                | 7.12 ms: 1.20x slower                                            |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.72 ms: 1.68x faster                                            |
| genshi_text     | 31.8 ms                                                | 23.5 ms: 1.35x faster                                            |
| django_template | 48.2 ms                                                | 36.7 ms: 1.31x faster                                            |
| genshi_xml      | 66.0 ms                                                | 59.5 ms: 1.11x faster                                            |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 173 us: 3.14x faster                                             |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.23x faster                                             |
| async_tree_memoization   | 870 ms                                                 | 414 ms: 2.10x faster                                             |
| deepcopy_memo            | 58.5 us                                                | 28.4 us: 2.06x faster                                            |
| scimark_monte_carlo      | 118 ms                                                 | 58.1 ms: 2.04x faster                                            |
| chaos                    | 115 ms                                                 | 57.6 ms: 2.00x faster                                            |
| async_tree_io            | 1.77 sec                                               | 887 ms: 1.99x faster                                             |
| richards_super           | 94.7 ms                                                | 48.1 ms: 1.97x faster                                            |
| nbody                    | 154 ms                                                 | 78.9 ms: 1.95x faster                                            |
| crypto_pyaes             | 128 ms                                                 | 66.7 ms: 1.92x faster                                            |
| deltablue                | 7.91 ms                                                | 4.14 ms: 1.91x faster                                            |
| raytrace                 | 507 ms                                                 | 272 ms: 1.86x faster                                             |
| generators               | 80.1 ms                                                | 43.2 ms: 1.85x faster                                            |
| richards                 | 79.3 ms                                                | 43.0 ms: 1.84x faster                                            |
| asyncio_tcp              | 922 ms                                                 | 503 ms: 1.83x faster                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 568 ms: 1.79x faster                                             |
| deepcopy                 | 479 us                                                 | 271 us: 1.77x faster                                             |
| comprehensions           | 28.8 us                                                | 16.3 us: 1.76x faster                                            |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                             |
| spectral_norm            | 170 ms                                                 | 100 ms: 1.69x faster                                             |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                            |
| mako                     | 16.3 ms                                                | 9.72 ms: 1.68x faster                                            |
| unpickle_pure_python     | 331 us                                                 | 199 us: 1.66x faster                                             |
| go                       | 240 ms                                                 | 145 ms: 1.66x faster                                             |
| float                    | 117 ms                                                 | 70.6 ms: 1.66x faster                                            |
| logging_silent           | 190 ns                                                 | 115 ns: 1.65x faster                                             |
| pyflate                  | 716 ms                                                 | 439 ms: 1.63x faster                                             |
| pickle_pure_python       | 484 us                                                 | 297 us: 1.63x faster                                             |
| hexiom                   | 10.4 ms                                                | 6.55 ms: 1.59x faster                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.67 ms: 1.54x faster                                            |
| tomli_loads              | 3.14 sec                                               | 2.06 sec: 1.53x faster                                           |
| fannkuch                 | 532 ms                                                 | 352 ms: 1.51x faster                                             |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                            |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.80 us: 1.49x faster                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.43 ms: 1.46x faster                                            |
| logging_simple           | 8.30 us                                                | 5.69 us: 1.46x faster                                            |
| logging_format           | 9.09 us                                                | 6.30 us: 1.44x faster                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                           |
| scimark_lu               | 176 ms                                                 | 124 ms: 1.42x faster                                             |
| pylint                   | 551 ms                                                 | 392 ms: 1.41x faster                                             |
| tornado_http             | 136 ms                                                 | 97.6 ms: 1.40x faster                                            |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                            |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.37x faster                                           |
| xml_etree_process        | 79.1 ms                                                | 57.8 ms: 1.37x faster                                            |
| pprint_safe_repr         | 1.02 sec                                               | 745 ms: 1.37x faster                                             |
| regex_compile            | 188 ms                                                 | 138 ms: 1.36x faster                                             |
| genshi_text              | 31.8 ms                                                | 23.5 ms: 1.35x faster                                            |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.34x faster                                            |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                           |
| thrift                   | 1.07 ms                                                | 806 us: 1.33x faster                                             |
| django_template          | 48.2 ms                                                | 36.7 ms: 1.31x faster                                            |
| nqueens                  | 106 ms                                                 | 83.0 ms: 1.28x faster                                            |
| html5lib                 | 88.9 ms                                                | 69.9 ms: 1.27x faster                                            |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                            |
| sqlglot_normalize        | 143 ms                                                 | 116 ms: 1.24x faster                                             |
| 2to3                     | 348 ms                                                 | 282 ms: 1.23x faster                                             |
| sqlglot_optimize         | 69.2 ms                                                | 56.1 ms: 1.23x faster                                            |
| xml_etree_generate       | 99.4 ms                                                | 82.5 ms: 1.20x faster                                            |
| bench_thread_pool        | 986 us                                                 | 827 us: 1.19x faster                                             |
| dask                     | 441 ms                                                 | 370 ms: 1.19x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 99.1 ms: 1.17x faster                                            |
| dulwich_log              | 84.3 ms                                                | 72.6 ms: 1.16x faster                                            |
| regex_v8                 | 27.8 ms                                                | 24.1 ms: 1.15x faster                                            |
| json_loads               | 31.2 us                                                | 27.5 us: 1.14x faster                                            |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                             |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                             |
| sympy_str                | 346 ms                                                 | 307 ms: 1.12x faster                                             |
| json                     | 5.69 ms                                                | 5.09 ms: 1.12x faster                                            |
| sympy_integrate          | 25.8 ms                                                | 23.1 ms: 1.12x faster                                            |
| genshi_xml               | 66.0 ms                                                | 59.5 ms: 1.11x faster                                            |
| sympy_sum                | 196 ms                                                 | 179 ms: 1.10x faster                                             |
| docutils                 | 3.30 sec                                               | 3.02 sec: 1.09x faster                                           |
| sympy_expand             | 566 ms                                                 | 518 ms: 1.09x faster                                             |
| mdp                      | 2.85 sec                                               | 2.75 sec: 1.04x faster                                           |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                             |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                             |
| async_generators         | 444 ms                                                 | 458 ms: 1.03x slower                                             |
| gc_traversal             | 3.62 ms                                                | 3.75 ms: 1.03x slower                                            |
| telco                    | 7.27 ms                                                | 7.87 ms: 1.08x slower                                            |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                            |
| coverage                 | 79.4 ms                                                | 94.1 ms: 1.18x slower                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.12 ms: 1.20x slower                                            |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                     |

Benchmark hidden because not significant (3): regex_effbot, bench_mp_pool, asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240708-3.14.0a0-5156311-JIT/bm-20240708-linux-x86_64-brandtbucher-underflow-3.14.0a0-5156311.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.20x