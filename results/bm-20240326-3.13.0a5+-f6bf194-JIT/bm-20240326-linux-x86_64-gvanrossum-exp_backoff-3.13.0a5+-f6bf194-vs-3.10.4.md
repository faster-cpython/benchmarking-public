# Results vs. 3.10.4

- fork: gvanrossum
- ref: exp_backoff
- machine: linux-x86_64
- commit hash: f6bf194
- commit date: 2024-03-26
- overall geometric mean: 1.32x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 279 ms: 1.25x faster                                              |
| chameleon      | 9.68 ms                                                | 7.17 ms: 1.35x faster                                             |
| docutils       | 3.30 sec                                               | 2.84 sec: 1.16x faster                                            |
| html5lib       | 88.9 ms                                                | 66.2 ms: 1.34x faster                                             |
| tornado_http   | 136 ms                                                 | 96.5 ms: 1.41x faster                                             |
| Geometric mean | (ref)                                                  | 1.30x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 920 ms: 1.92x faster                                              |
| async_tree_memoization  | 870 ms                                                 | 459 ms: 1.90x faster                                              |
| async_tree_none         | 728 ms                                                 | 386 ms: 1.88x faster                                              |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 599 ms: 1.70x faster                                              |
| Geometric mean          | (ref)                                                  | 1.85x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 92.2 ms: 1.67x faster                                             |
| float          | 117 ms                                                 | 77.5 ms: 1.51x faster                                             |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                              |
| Geometric mean | (ref)                                                  | 1.36x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 139 ms: 1.36x faster                                              |
| regex_v8       | 27.8 ms                                                | 25.7 ms: 1.08x faster                                             |
| regex_dna      | 227 ms                                                 | 227 ms: 1.00x slower                                              |
| regex_effbot   | 3.63 ms                                                | 3.77 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                  | 1.09x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                              |
| tomli_loads          | 3.14 sec                                               | 2.06 sec: 1.53x faster                                            |
| unpickle_pure_python | 331 us                                                 | 232 us: 1.43x faster                                              |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.34x faster                                             |
| xml_etree_process    | 79.1 ms                                                | 60.1 ms: 1.32x faster                                             |
| xml_etree_generate   | 99.4 ms                                                | 86.9 ms: 1.14x faster                                             |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                             |
| xml_etree_iterparse  | 115 ms                                                 | 107 ms: 1.08x faster                                              |
| xml_etree_parse      | 168 ms                                                 | 161 ms: 1.04x faster                                              |
| pickle_list          | 5.08 us                                                | 4.95 us: 1.03x faster                                             |
| unpickle_list        | 5.20 us                                                | 5.43 us: 1.04x slower                                             |
| pickle               | 10.7 us                                                | 12.0 us: 1.13x slower                                             |
| pickle_dict          | 29.6 us                                                | 33.5 us: 1.13x slower                                             |
| unpickle             | 14.4 us                                                | 17.0 us: 1.18x slower                                             |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.0 ms: 1.33x faster                                             |
| python_startup_no_site | 5.93 ms                                                | 9.48 ms: 1.60x slower                                             |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.9 ms: 1.50x faster                                             |
| django_template | 48.2 ms                                                | 35.8 ms: 1.35x faster                                             |
| genshi_text     | 31.8 ms                                                | 25.2 ms: 1.26x faster                                             |
| genshi_xml      | 66.0 ms                                                | 54.1 ms: 1.22x faster                                             |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 114 us: 4.77x faster                                              |
| generators               | 80.1 ms                                                | 30.3 ms: 2.64x faster                                             |
| deltablue                | 7.91 ms                                                | 3.32 ms: 2.38x faster                                             |
| async_tree_io            | 1.77 sec                                               | 920 ms: 1.92x faster                                              |
| async_tree_memoization   | 870 ms                                                 | 459 ms: 1.90x faster                                              |
| async_tree_none          | 728 ms                                                 | 386 ms: 1.88x faster                                              |
| richards_super           | 94.7 ms                                                | 50.7 ms: 1.87x faster                                             |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                              |
| chaos                    | 115 ms                                                 | 63.3 ms: 1.82x faster                                             |
| asyncio_tcp              | 922 ms                                                 | 506 ms: 1.82x faster                                              |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                              |
| richards                 | 79.3 ms                                                | 44.1 ms: 1.80x faster                                             |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.76x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 599 ms: 1.70x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 75.5 ms: 1.69x faster                                             |
| nbody                    | 154 ms                                                 | 92.2 ms: 1.67x faster                                             |
| pylint                   | 551 ms                                                 | 332 ms: 1.66x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 71.3 ms: 1.66x faster                                             |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                             |
| go                       | 240 ms                                                 | 148 ms: 1.62x faster                                              |
| comprehensions           | 28.8 us                                                | 18.0 us: 1.60x faster                                             |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                              |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                             |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                              |
| tomli_loads              | 3.14 sec                                               | 2.06 sec: 1.53x faster                                            |
| hexiom                   | 10.4 ms                                                | 6.87 ms: 1.51x faster                                             |
| float                    | 117 ms                                                 | 77.5 ms: 1.51x faster                                             |
| mako                     | 16.3 ms                                                | 10.9 ms: 1.50x faster                                             |
| deepcopy_memo            | 58.5 us                                                | 39.0 us: 1.50x faster                                             |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.49x faster                                             |
| pyflate                  | 716 ms                                                 | 486 ms: 1.47x faster                                              |
| spectral_norm            | 170 ms                                                 | 116 ms: 1.46x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 232 us: 1.43x faster                                              |
| tornado_http             | 136 ms                                                 | 96.5 ms: 1.41x faster                                             |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                            |
| logging_simple           | 8.30 us                                                | 6.02 us: 1.38x faster                                             |
| logging_format           | 9.09 us                                                | 6.66 us: 1.36x faster                                             |
| regex_compile            | 188 ms                                                 | 139 ms: 1.36x faster                                              |
| scimark_fft              | 466 ms                                                 | 344 ms: 1.35x faster                                              |
| chameleon                | 9.68 ms                                                | 7.17 ms: 1.35x faster                                             |
| django_template          | 48.2 ms                                                | 35.8 ms: 1.35x faster                                             |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                            |
| html5lib                 | 88.9 ms                                                | 66.2 ms: 1.34x faster                                             |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.34x faster                                             |
| pprint_safe_repr         | 1.02 sec                                               | 762 ms: 1.34x faster                                              |
| deepcopy                 | 479 us                                                 | 359 us: 1.33x faster                                              |
| python_startup           | 14.6 ms                                                | 11.0 ms: 1.33x faster                                             |
| fannkuch                 | 532 ms                                                 | 401 ms: 1.33x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 3.15 us: 1.32x faster                                             |
| xml_etree_process        | 79.1 ms                                                | 60.1 ms: 1.32x faster                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.93 ms: 1.31x faster                                             |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                              |
| pycparser                | 1.58 sec                                               | 1.24 sec: 1.27x faster                                            |
| genshi_text              | 31.8 ms                                                | 25.2 ms: 1.26x faster                                             |
| 2to3                     | 348 ms                                                 | 279 ms: 1.25x faster                                              |
| thrift                   | 1.07 ms                                                | 858 us: 1.25x faster                                              |
| dulwich_log              | 84.3 ms                                                | 68.6 ms: 1.23x faster                                             |
| genshi_xml               | 66.0 ms                                                | 54.1 ms: 1.22x faster                                             |
| sqlglot_optimize         | 69.2 ms                                                | 56.7 ms: 1.22x faster                                             |
| sympy_integrate          | 25.8 ms                                                | 21.3 ms: 1.21x faster                                             |
| sympy_sum                | 196 ms                                                 | 163 ms: 1.21x faster                                              |
| nqueens                  | 106 ms                                                 | 87.9 ms: 1.20x faster                                             |
| sympy_str                | 346 ms                                                 | 289 ms: 1.20x faster                                              |
| djangocms                | 38.4 us                                                | 32.2 us: 1.19x faster                                             |
| aiohttp                  | 1.44 ms                                                | 1.21 ms: 1.19x faster                                             |
| gunicorn                 | 1.53 ms                                                | 1.30 ms: 1.17x faster                                             |
| dask                     | 441 ms                                                 | 376 ms: 1.17x faster                                              |
| mypy2                    | 894 ms                                                 | 766 ms: 1.17x faster                                              |
| unpack_sequence          | 60.0 ns                                                | 51.5 ns: 1.16x faster                                             |
| docutils                 | 3.30 sec                                               | 2.84 sec: 1.16x faster                                            |
| bench_thread_pool        | 986 us                                                 | 852 us: 1.16x faster                                              |
| sympy_expand             | 566 ms                                                 | 491 ms: 1.15x faster                                              |
| xml_etree_generate       | 99.4 ms                                                | 86.9 ms: 1.14x faster                                             |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                             |
| pathlib                  | 20.5 ms                                                | 18.9 ms: 1.08x faster                                             |
| regex_v8                 | 27.8 ms                                                | 25.7 ms: 1.08x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 107 ms: 1.08x faster                                              |
| meteor_contest           | 120 ms                                                 | 111 ms: 1.07x faster                                              |
| mdp                      | 2.85 sec                                               | 2.66 sec: 1.07x faster                                            |
| json                     | 5.69 ms                                                | 5.42 ms: 1.05x faster                                             |
| sqlite_synth             | 3.02 us                                                | 2.89 us: 1.05x faster                                             |
| xml_etree_parse          | 168 ms                                                 | 161 ms: 1.04x faster                                              |
| pickle_list              | 5.08 us                                                | 4.95 us: 1.03x faster                                             |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                              |
| regex_dna                | 227 ms                                                 | 227 ms: 1.00x slower                                              |
| asyncio_websockets       | 559 ms                                                 | 570 ms: 1.02x slower                                              |
| regex_effbot             | 3.63 ms                                                | 3.77 ms: 1.04x slower                                             |
| create_gc_cycles         | 1.62 ms                                                | 1.69 ms: 1.04x slower                                             |
| unpickle_list            | 5.20 us                                                | 5.43 us: 1.04x slower                                             |
| async_generators         | 444 ms                                                 | 468 ms: 1.05x slower                                              |
| gc_traversal             | 3.62 ms                                                | 3.86 ms: 1.06x slower                                             |
| pickle                   | 10.7 us                                                | 12.0 us: 1.13x slower                                             |
| pickle_dict              | 29.6 us                                                | 33.5 us: 1.13x slower                                             |
| telco                    | 7.27 ms                                                | 8.58 ms: 1.18x slower                                             |
| unpickle                 | 14.4 us                                                | 17.0 us: 1.18x slower                                             |
| coverage                 | 79.4 ms                                                | 100 ms: 1.26x slower                                              |
| python_startup_no_site   | 5.93 ms                                                | 9.48 ms: 1.60x slower                                             |
| Geometric mean           | (ref)                                                  | 1.32x faster                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240326-3.13.0a5+-f6bf194-JIT/bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x


# Memory

- memory change: 1.16x