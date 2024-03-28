# Results vs. 3.10.4

- fork: gvanrossum
- ref: exp_backoff
- machine: linux-x86_64
- commit hash: 225ea17
- commit date: 2024-03-27
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 279 ms: 1.25x faster                                              |
| chameleon      | 9.68 ms                                                | 7.21 ms: 1.34x faster                                             |
| docutils       | 3.30 sec                                               | 2.89 sec: 1.14x faster                                            |
| html5lib       | 88.9 ms                                                | 66.2 ms: 1.34x faster                                             |
| tornado_http   | 136 ms                                                 | 96.6 ms: 1.41x faster                                             |
| Geometric mean | (ref)                                                  | 1.29x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_memoization  | 870 ms                                                 | 459 ms: 1.89x faster                                              |
| async_tree_io           | 1.77 sec                                               | 942 ms: 1.88x faster                                              |
| async_tree_none         | 728 ms                                                 | 390 ms: 1.87x faster                                              |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 601 ms: 1.69x faster                                              |
| Geometric mean          | (ref)                                                  | 1.83x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 91.9 ms: 1.67x faster                                             |
| float          | 117 ms                                                 | 77.8 ms: 1.50x faster                                             |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                  | 1.36x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 146 ms: 1.29x faster                                              |
| regex_v8       | 27.8 ms                                                | 26.1 ms: 1.06x faster                                             |
| regex_dna      | 227 ms                                                 | 229 ms: 1.01x slower                                              |
| regex_effbot   | 3.63 ms                                                | 3.81 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                  | 1.07x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 308 us: 1.57x faster                                              |
| tomli_loads          | 3.14 sec                                               | 2.07 sec: 1.52x faster                                            |
| unpickle_pure_python | 331 us                                                 | 246 us: 1.35x faster                                              |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.34x faster                                             |
| xml_etree_process    | 79.1 ms                                                | 60.5 ms: 1.31x faster                                             |
| xml_etree_generate   | 99.4 ms                                                | 88.6 ms: 1.12x faster                                             |
| json_loads           | 31.2 us                                                | 29.1 us: 1.07x faster                                             |
| xml_etree_iterparse  | 115 ms                                                 | 108 ms: 1.07x faster                                              |
| xml_etree_parse      | 168 ms                                                 | 162 ms: 1.04x faster                                              |
| pickle_list          | 5.08 us                                                | 5.30 us: 1.04x slower                                             |
| unpickle             | 14.4 us                                                | 16.4 us: 1.14x slower                                             |
| pickle               | 10.7 us                                                | 12.3 us: 1.16x slower                                             |
| pickle_dict          | 29.6 us                                                | 37.2 us: 1.26x slower                                             |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                      |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.1 ms: 1.32x faster                                             |
| python_startup_no_site | 5.93 ms                                                | 9.55 ms: 1.61x slower                                             |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.8 ms: 1.52x faster                                             |
| django_template | 48.2 ms                                                | 35.9 ms: 1.34x faster                                             |
| genshi_text     | 31.8 ms                                                | 24.5 ms: 1.30x faster                                             |
| genshi_xml      | 66.0 ms                                                | 53.5 ms: 1.23x faster                                             |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 115 us: 4.74x faster                                              |
| generators               | 80.1 ms                                                | 30.2 ms: 2.66x faster                                             |
| deltablue                | 7.91 ms                                                | 3.94 ms: 2.01x faster                                             |
| async_tree_memoization   | 870 ms                                                 | 459 ms: 1.89x faster                                              |
| async_tree_io            | 1.77 sec                                               | 942 ms: 1.88x faster                                              |
| async_tree_none          | 728 ms                                                 | 390 ms: 1.87x faster                                              |
| chaos                    | 115 ms                                                 | 63.3 ms: 1.82x faster                                             |
| asyncio_tcp              | 922 ms                                                 | 508 ms: 1.81x faster                                              |
| logging_silent           | 190 ns                                                 | 105 ns: 1.80x faster                                              |
| richards_super           | 94.7 ms                                                | 52.8 ms: 1.79x faster                                             |
| raytrace                 | 507 ms                                                 | 293 ms: 1.73x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 74.9 ms: 1.71x faster                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 601 ms: 1.69x faster                                              |
| richards                 | 79.3 ms                                                | 47.0 ms: 1.69x faster                                             |
| nbody                    | 154 ms                                                 | 91.9 ms: 1.67x faster                                             |
| scimark_monte_carlo      | 118 ms                                                 | 71.6 ms: 1.65x faster                                             |
| scimark_sor              | 220 ms                                                 | 134 ms: 1.64x faster                                              |
| pylint                   | 551 ms                                                 | 337 ms: 1.63x faster                                              |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.62x faster                                             |
| comprehensions           | 28.8 us                                                | 18.2 us: 1.58x faster                                             |
| pickle_pure_python       | 484 us                                                 | 308 us: 1.57x faster                                              |
| go                       | 240 ms                                                 | 154 ms: 1.56x faster                                              |
| sqlglot_transpile        | 2.57 ms                                                | 1.66 ms: 1.55x faster                                             |
| tomli_loads              | 3.14 sec                                               | 2.07 sec: 1.52x faster                                            |
| mako                     | 16.3 ms                                                | 10.8 ms: 1.52x faster                                             |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                             |
| float                    | 117 ms                                                 | 77.8 ms: 1.50x faster                                             |
| deepcopy_memo            | 58.5 us                                                | 39.3 us: 1.49x faster                                             |
| pyflate                  | 716 ms                                                 | 485 ms: 1.48x faster                                              |
| hexiom                   | 10.4 ms                                                | 7.12 ms: 1.46x faster                                             |
| spectral_norm            | 170 ms                                                 | 117 ms: 1.46x faster                                              |
| tornado_http             | 136 ms                                                 | 96.6 ms: 1.41x faster                                             |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                            |
| logging_simple           | 8.30 us                                                | 5.98 us: 1.39x faster                                             |
| fannkuch                 | 532 ms                                                 | 389 ms: 1.37x faster                                              |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.36x faster                                            |
| pprint_safe_repr         | 1.02 sec                                               | 748 ms: 1.36x faster                                              |
| logging_format           | 9.09 us                                                | 6.68 us: 1.36x faster                                             |
| unpickle_pure_python     | 331 us                                                 | 246 us: 1.35x faster                                              |
| deepcopy                 | 479 us                                                 | 356 us: 1.34x faster                                              |
| chameleon                | 9.68 ms                                                | 7.21 ms: 1.34x faster                                             |
| html5lib                 | 88.9 ms                                                | 66.2 ms: 1.34x faster                                             |
| django_template          | 48.2 ms                                                | 35.9 ms: 1.34x faster                                             |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.34x faster                                             |
| scimark_fft              | 466 ms                                                 | 348 ms: 1.34x faster                                              |
| python_startup           | 14.6 ms                                                | 11.1 ms: 1.32x faster                                             |
| scimark_lu               | 176 ms                                                 | 134 ms: 1.32x faster                                              |
| xml_etree_process        | 79.1 ms                                                | 60.5 ms: 1.31x faster                                             |
| thrift                   | 1.07 ms                                                | 823 us: 1.30x faster                                              |
| genshi_text              | 31.8 ms                                                | 24.5 ms: 1.30x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 3.21 us: 1.30x faster                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.00 ms: 1.29x faster                                             |
| regex_compile            | 188 ms                                                 | 146 ms: 1.29x faster                                              |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                              |
| pycparser                | 1.58 sec                                               | 1.25 sec: 1.26x faster                                            |
| 2to3                     | 348 ms                                                 | 279 ms: 1.25x faster                                              |
| genshi_xml               | 66.0 ms                                                | 53.5 ms: 1.23x faster                                             |
| nqueens                  | 106 ms                                                 | 88.7 ms: 1.19x faster                                             |
| sqlglot_optimize         | 69.2 ms                                                | 58.0 ms: 1.19x faster                                             |
| dulwich_log              | 84.3 ms                                                | 70.8 ms: 1.19x faster                                             |
| djangocms                | 38.4 us                                                | 32.4 us: 1.19x faster                                             |
| aiohttp                  | 1.44 ms                                                | 1.21 ms: 1.18x faster                                             |
| sympy_sum                | 196 ms                                                 | 167 ms: 1.18x faster                                              |
| sympy_str                | 346 ms                                                 | 293 ms: 1.18x faster                                              |
| sympy_integrate          | 25.8 ms                                                | 21.9 ms: 1.18x faster                                             |
| dask                     | 441 ms                                                 | 375 ms: 1.17x faster                                              |
| gunicorn                 | 1.53 ms                                                | 1.31 ms: 1.17x faster                                             |
| bench_thread_pool        | 986 us                                                 | 856 us: 1.15x faster                                              |
| mypy2                    | 894 ms                                                 | 785 ms: 1.14x faster                                              |
| docutils                 | 3.30 sec                                               | 2.89 sec: 1.14x faster                                            |
| sympy_expand             | 566 ms                                                 | 497 ms: 1.14x faster                                              |
| xml_etree_generate       | 99.4 ms                                                | 88.6 ms: 1.12x faster                                             |
| meteor_contest           | 120 ms                                                 | 111 ms: 1.08x faster                                              |
| mdp                      | 2.85 sec                                               | 2.65 sec: 1.08x faster                                            |
| pathlib                  | 20.5 ms                                                | 19.0 ms: 1.08x faster                                             |
| json_loads               | 31.2 us                                                | 29.1 us: 1.07x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 108 ms: 1.07x faster                                              |
| regex_v8                 | 27.8 ms                                                | 26.1 ms: 1.06x faster                                             |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.05x faster                                             |
| xml_etree_parse          | 168 ms                                                 | 162 ms: 1.04x faster                                              |
| json                     | 5.69 ms                                                | 5.50 ms: 1.04x faster                                             |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                              |
| regex_dna                | 227 ms                                                 | 229 ms: 1.01x slower                                              |
| asyncio_websockets       | 559 ms                                                 | 570 ms: 1.02x slower                                              |
| pickle_list              | 5.08 us                                                | 5.30 us: 1.04x slower                                             |
| create_gc_cycles         | 1.62 ms                                                | 1.70 ms: 1.05x slower                                             |
| regex_effbot             | 3.63 ms                                                | 3.81 ms: 1.05x slower                                             |
| async_generators         | 444 ms                                                 | 467 ms: 1.05x slower                                              |
| gc_traversal             | 3.62 ms                                                | 3.95 ms: 1.09x slower                                             |
| unpickle                 | 14.4 us                                                | 16.4 us: 1.14x slower                                             |
| pickle                   | 10.7 us                                                | 12.3 us: 1.16x slower                                             |
| telco                    | 7.27 ms                                                | 8.82 ms: 1.21x slower                                             |
| coverage                 | 79.4 ms                                                | 97.9 ms: 1.23x slower                                             |
| pickle_dict              | 29.6 us                                                | 37.2 us: 1.26x slower                                             |
| unpack_sequence          | 60.0 ns                                                | 86.4 ns: 1.44x slower                                             |
| python_startup_no_site   | 5.93 ms                                                | 9.55 ms: 1.61x slower                                             |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                      |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240327-3.13.0a5+-225ea17-JIT/bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x


# Memory

- memory change: 1.18x