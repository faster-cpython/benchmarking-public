# Results vs. 3.10.4

- fork: gvanrossum
- ref: exp_backoff
- machine: linux-x86_64
- commit hash: 716c0c6
- commit date: 2024-03-21
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 304 ms: 1.14x faster                                              |
| chameleon      | 9.68 ms                                                | 6.98 ms: 1.39x faster                                             |
| docutils       | 3.30 sec                                               | 4.82 sec: 1.46x slower                                            |
| html5lib       | 88.9 ms                                                | 75.8 ms: 1.17x faster                                             |
| tornado_http   | 136 ms                                                 | 101 ms: 1.36x faster                                              |
| Geometric mean | (ref)                                                  | 1.12x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 1.02 sec                                               | 4.17 sec: 4.11x slower                                            |
| async_tree_none         | 728 ms                                                 | 3.39 sec: 4.65x slower                                            |
| async_tree_memoization  | 870 ms                                                 | 4.37 sec: 5.02x slower                                            |
| async_tree_io           | 1.77 sec                                               | 13.1 sec: 7.41x slower                                            |
| Geometric mean          | (ref)                                                  | 5.16x slower                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 94.2 ms: 1.63x faster                                             |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                              |
| float          | 117 ms                                                 | 143 ms: 1.22x slower                                              |
| Geometric mean | (ref)                                                  | 1.10x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 142 ms: 1.33x faster                                              |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                             |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                              |
| regex_effbot   | 3.63 ms                                                | 3.81 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                  | 1.11x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 303 us: 1.60x faster                                              |
| tomli_loads          | 3.14 sec                                               | 2.10 sec: 1.49x faster                                            |
| unpickle_pure_python | 331 us                                                 | 241 us: 1.37x faster                                              |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                             |
| xml_etree_process    | 79.1 ms                                                | 68.8 ms: 1.15x faster                                             |
| json_loads           | 31.2 us                                                | 27.7 us: 1.13x faster                                             |
| pickle_list          | 5.08 us                                                | 4.80 us: 1.06x faster                                             |
| unpickle_list        | 5.20 us                                                | 5.27 us: 1.01x slower                                             |
| unpickle             | 14.4 us                                                | 15.5 us: 1.08x slower                                             |
| pickle               | 10.7 us                                                | 11.6 us: 1.08x slower                                             |
| pickle_dict          | 29.6 us                                                | 34.5 us: 1.16x slower                                             |
| xml_etree_parse      | 168 ms                                                 | 216 ms: 1.28x slower                                              |
| xml_etree_iterparse  | 115 ms                                                 | 163 ms: 1.41x slower                                              |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                      |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.8 ms: 1.23x faster                                             |
| python_startup_no_site | 5.93 ms                                                | 10.1 ms: 1.71x slower                                             |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.1 ms: 1.46x faster                                             |
| django_template | 48.2 ms                                                | 36.0 ms: 1.34x faster                                             |
| genshi_text     | 31.8 ms                                                | 24.2 ms: 1.32x faster                                             |
| genshi_xml      | 66.0 ms                                                | 59.8 ms: 1.10x faster                                             |
| Geometric mean  | (ref)                                                  | 1.30x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 111 us: 4.90x faster                                              |
| generators               | 80.1 ms                                                | 30.2 ms: 2.65x faster                                             |
| deltablue                | 7.91 ms                                                | 3.90 ms: 2.03x faster                                             |
| richards_super           | 94.7 ms                                                | 50.0 ms: 1.90x faster                                             |
| logging_silent           | 190 ns                                                 | 102 ns: 1.87x faster                                              |
| asyncio_tcp              | 922 ms                                                 | 509 ms: 1.81x faster                                              |
| chaos                    | 115 ms                                                 | 64.5 ms: 1.79x faster                                             |
| richards                 | 79.3 ms                                                | 44.3 ms: 1.79x faster                                             |
| raytrace                 | 507 ms                                                 | 284 ms: 1.79x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 69.5 ms: 1.70x faster                                             |
| scimark_sor              | 220 ms                                                 | 131 ms: 1.68x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 76.3 ms: 1.68x faster                                             |
| comprehensions           | 28.8 us                                                | 17.6 us: 1.64x faster                                             |
| nbody                    | 154 ms                                                 | 94.2 ms: 1.63x faster                                             |
| pickle_pure_python       | 484 us                                                 | 303 us: 1.60x faster                                              |
| go                       | 240 ms                                                 | 155 ms: 1.55x faster                                              |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                             |
| sqlglot_parse            | 2.17 ms                                                | 1.44 ms: 1.50x faster                                             |
| deepcopy_memo            | 58.5 us                                                | 39.0 us: 1.50x faster                                             |
| tomli_loads              | 3.14 sec                                               | 2.10 sec: 1.49x faster                                            |
| hexiom                   | 10.4 ms                                                | 6.96 ms: 1.49x faster                                             |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.47x faster                                              |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.46x faster                                             |
| pyflate                  | 716 ms                                                 | 493 ms: 1.45x faster                                              |
| sqlglot_transpile        | 2.57 ms                                                | 1.80 ms: 1.43x faster                                             |
| logging_simple           | 8.30 us                                                | 5.85 us: 1.42x faster                                             |
| logging_format           | 9.09 us                                                | 6.47 us: 1.41x faster                                             |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                            |
| chameleon                | 9.68 ms                                                | 6.98 ms: 1.39x faster                                             |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.38x faster                                            |
| unpickle_pure_python     | 331 us                                                 | 241 us: 1.37x faster                                              |
| scimark_fft              | 466 ms                                                 | 341 ms: 1.37x faster                                              |
| scimark_lu               | 176 ms                                                 | 129 ms: 1.36x faster                                              |
| tornado_http             | 136 ms                                                 | 101 ms: 1.36x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 751 ms: 1.35x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.79 ms: 1.35x faster                                             |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                             |
| django_template          | 48.2 ms                                                | 36.0 ms: 1.34x faster                                             |
| deepcopy                 | 479 us                                                 | 358 us: 1.34x faster                                              |
| regex_compile            | 188 ms                                                 | 142 ms: 1.33x faster                                              |
| thrift                   | 1.07 ms                                                | 813 us: 1.32x faster                                              |
| genshi_text              | 31.8 ms                                                | 24.2 ms: 1.32x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 3.18 us: 1.31x faster                                             |
| fannkuch                 | 532 ms                                                 | 407 ms: 1.31x faster                                              |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.26x faster                                              |
| python_startup           | 14.6 ms                                                | 11.8 ms: 1.23x faster                                             |
| dulwich_log              | 84.3 ms                                                | 69.0 ms: 1.22x faster                                             |
| sympy_integrate          | 25.8 ms                                                | 21.4 ms: 1.21x faster                                             |
| sympy_str                | 346 ms                                                 | 288 ms: 1.20x faster                                              |
| nqueens                  | 106 ms                                                 | 88.4 ms: 1.20x faster                                             |
| sympy_sum                | 196 ms                                                 | 165 ms: 1.19x faster                                              |
| sqlglot_optimize         | 69.2 ms                                                | 58.8 ms: 1.18x faster                                             |
| html5lib                 | 88.9 ms                                                | 75.8 ms: 1.17x faster                                             |
| bench_thread_pool        | 986 us                                                 | 847 us: 1.16x faster                                              |
| sympy_expand             | 566 ms                                                 | 491 ms: 1.15x faster                                              |
| xml_etree_process        | 79.1 ms                                                | 68.8 ms: 1.15x faster                                             |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                             |
| 2to3                     | 348 ms                                                 | 304 ms: 1.14x faster                                              |
| aiohttp                  | 1.44 ms                                                | 1.27 ms: 1.14x faster                                             |
| djangocms                | 38.4 us                                                | 34.1 us: 1.13x faster                                             |
| json_loads               | 31.2 us                                                | 27.7 us: 1.13x faster                                             |
| gunicorn                 | 1.53 ms                                                | 1.36 ms: 1.13x faster                                             |
| genshi_xml               | 66.0 ms                                                | 59.8 ms: 1.10x faster                                             |
| create_gc_cycles         | 1.62 ms                                                | 1.49 ms: 1.09x faster                                             |
| meteor_contest           | 120 ms                                                 | 111 ms: 1.08x faster                                              |
| pycparser                | 1.58 sec                                               | 1.47 sec: 1.07x faster                                            |
| pathlib                  | 20.5 ms                                                | 19.1 ms: 1.07x faster                                             |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                             |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                             |
| pickle_list              | 5.08 us                                                | 4.80 us: 1.06x faster                                             |
| mypy2                    | 894 ms                                                 | 851 ms: 1.05x faster                                              |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                              |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                              |
| unpickle_list            | 5.20 us                                                | 5.27 us: 1.01x slower                                             |
| asyncio_websockets       | 559 ms                                                 | 570 ms: 1.02x slower                                              |
| gc_traversal             | 3.62 ms                                                | 3.74 ms: 1.03x slower                                             |
| regex_effbot             | 3.63 ms                                                | 3.81 ms: 1.05x slower                                             |
| unpickle                 | 14.4 us                                                | 15.5 us: 1.08x slower                                             |
| pickle                   | 10.7 us                                                | 11.6 us: 1.08x slower                                             |
| telco                    | 7.27 ms                                                | 8.43 ms: 1.16x slower                                             |
| pickle_dict              | 29.6 us                                                | 34.5 us: 1.16x slower                                             |
| float                    | 117 ms                                                 | 143 ms: 1.22x slower                                              |
| coverage                 | 79.4 ms                                                | 96.9 ms: 1.22x slower                                             |
| async_generators         | 444 ms                                                 | 556 ms: 1.25x slower                                              |
| xml_etree_parse          | 168 ms                                                 | 216 ms: 1.28x slower                                              |
| xml_etree_iterparse      | 115 ms                                                 | 163 ms: 1.41x slower                                              |
| docutils                 | 3.30 sec                                               | 4.82 sec: 1.46x slower                                            |
| unpack_sequence          | 60.0 ns                                                | 91.8 ns: 1.53x slower                                             |
| python_startup_no_site   | 5.93 ms                                                | 10.1 ms: 1.71x slower                                             |
| dask                     | 441 ms                                                 | 759 ms: 1.72x slower                                              |
| pylint                   | 551 ms                                                 | 1.01 sec: 1.83x slower                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 4.17 sec: 4.11x slower                                            |
| async_tree_none          | 728 ms                                                 | 3.39 sec: 4.65x slower                                            |
| async_tree_memoization   | 870 ms                                                 | 4.37 sec: 5.02x slower                                            |
| async_tree_io            | 1.77 sec                                               | 13.1 sec: 7.41x slower                                            |
| Geometric mean           | (ref)                                                  | 1.13x faster                                                      |

Benchmark hidden because not significant (3): xml_etree_generate, bench_mp_pool, mdp
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240321-3.13.0a5+-716c0c6-JIT/bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.08x


# Memory

- memory change: 1.20x