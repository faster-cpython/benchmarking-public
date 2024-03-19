# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_mprotect_cost
- machine: linux-x86_64
- commit hash: c8d6017
- commit date: 2024-03-18
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 282 ms: 1.24x faster                                                         |
| chameleon      | 9.68 ms                                                | 6.84 ms: 1.42x faster                                                        |
| docutils       | 3.30 sec                                               | 2.78 sec: 1.18x faster                                                       |
| html5lib       | 88.9 ms                                                | 66.4 ms: 1.34x faster                                                        |
| tornado_http   | 136 ms                                                 | 99.0 ms: 1.38x faster                                                        |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 447 ms: 1.63x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 577 ms: 1.51x faster                                                         |
| async_tree_io           | 1.77 sec                                               | 1.22 sec: 1.45x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 723 ms: 1.40x faster                                                         |
| Geometric mean          | (ref)                                                  | 1.50x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 94.2 ms: 1.63x faster                                                        |
| float          | 117 ms                                                 | 80.5 ms: 1.45x faster                                                        |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 143 ms: 1.31x faster                                                         |
| regex_v8       | 27.8 ms                                                | 25.8 ms: 1.08x faster                                                        |
| regex_dna      | 227 ms                                                 | 231 ms: 1.02x slower                                                         |
| regex_effbot   | 3.63 ms                                                | 3.85 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.61x faster                                                         |
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 239 us: 1.38x faster                                                         |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 87.6 ms: 1.14x faster                                                        |
| json_loads           | 31.2 us                                                | 27.9 us: 1.12x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 108 ms: 1.07x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 161 ms: 1.05x faster                                                         |
| unpickle_list        | 5.20 us                                                | 5.02 us: 1.04x faster                                                        |
| pickle_list          | 5.08 us                                                | 4.92 us: 1.03x faster                                                        |
| unpickle             | 14.4 us                                                | 14.6 us: 1.02x slower                                                        |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                                        |
| pickle_dict          | 29.6 us                                                | 34.1 us: 1.15x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.8 ms: 1.24x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 10.3 ms: 1.74x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.19x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                        |
| django_template | 48.2 ms                                                | 34.9 ms: 1.38x faster                                                        |
| genshi_text     | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 55.3 ms: 1.19x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 111 us: 4.92x faster                                                         |
| generators               | 80.1 ms                                                | 29.8 ms: 2.69x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.43 ms: 2.30x faster                                                        |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                         |
| asyncio_tcp              | 922 ms                                                 | 504 ms: 1.83x faster                                                         |
| chaos                    | 115 ms                                                 | 64.4 ms: 1.79x faster                                                        |
| richards_super           | 94.7 ms                                                | 53.0 ms: 1.79x faster                                                        |
| raytrace                 | 507 ms                                                 | 295 ms: 1.72x faster                                                         |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.72x faster                                                         |
| pylint                   | 551 ms                                                 | 325 ms: 1.70x faster                                                         |
| richards                 | 79.3 ms                                                | 46.7 ms: 1.70x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 75.4 ms: 1.69x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 71.0 ms: 1.67x faster                                                        |
| comprehensions           | 28.8 us                                                | 17.3 us: 1.66x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.65x faster                                                        |
| async_tree_none          | 728 ms                                                 | 447 ms: 1.63x faster                                                         |
| nbody                    | 154 ms                                                 | 94.2 ms: 1.63x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.61x faster                                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.66 ms: 1.55x faster                                                        |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                        |
| go                       | 240 ms                                                 | 158 ms: 1.52x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 577 ms: 1.51x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 38.9 us: 1.50x faster                                                        |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.50x faster                                                         |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                        |
| hexiom                   | 10.4 ms                                                | 7.05 ms: 1.47x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 1.22 sec: 1.45x faster                                                       |
| float                    | 117 ms                                                 | 80.5 ms: 1.45x faster                                                        |
| pyflate                  | 716 ms                                                 | 495 ms: 1.45x faster                                                         |
| chameleon                | 9.68 ms                                                | 6.84 ms: 1.42x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.88 us: 1.41x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 723 ms: 1.40x faster                                                         |
| logging_format           | 9.09 us                                                | 6.48 us: 1.40x faster                                                        |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 239 us: 1.38x faster                                                         |
| django_template          | 48.2 ms                                                | 34.9 ms: 1.38x faster                                                        |
| tornado_http             | 136 ms                                                 | 99.0 ms: 1.38x faster                                                        |
| scimark_fft              | 466 ms                                                 | 340 ms: 1.37x faster                                                         |
| deepcopy                 | 479 us                                                 | 349 us: 1.37x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 3.05 us: 1.37x faster                                                        |
| scimark_lu               | 176 ms                                                 | 129 ms: 1.36x faster                                                         |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                        |
| fannkuch                 | 532 ms                                                 | 397 ms: 1.34x faster                                                         |
| html5lib                 | 88.9 ms                                                | 66.4 ms: 1.34x faster                                                        |
| thrift                   | 1.07 ms                                                | 802 us: 1.34x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.58 sec: 1.33x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.32x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 772 ms: 1.32x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.92 ms: 1.32x faster                                                        |
| regex_compile            | 188 ms                                                 | 143 ms: 1.31x faster                                                         |
| genshi_text              | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.26 sec: 1.25x faster                                                       |
| python_startup           | 14.6 ms                                                | 11.8 ms: 1.24x faster                                                        |
| 2to3                     | 348 ms                                                 | 282 ms: 1.24x faster                                                         |
| sqlglot_optimize         | 69.2 ms                                                | 56.3 ms: 1.23x faster                                                        |
| sympy_sum                | 196 ms                                                 | 161 ms: 1.22x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 21.2 ms: 1.22x faster                                                        |
| sympy_str                | 346 ms                                                 | 285 ms: 1.21x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 70.5 ms: 1.20x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 55.3 ms: 1.19x faster                                                        |
| djangocms                | 38.4 us                                                | 32.2 us: 1.19x faster                                                        |
| aiohttp                  | 1.44 ms                                                | 1.21 ms: 1.19x faster                                                        |
| nqueens                  | 106 ms                                                 | 89.3 ms: 1.19x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.78 sec: 1.18x faster                                                       |
| dask                     | 441 ms                                                 | 373 ms: 1.18x faster                                                         |
| gunicorn                 | 1.53 ms                                                | 1.30 ms: 1.18x faster                                                        |
| sympy_expand             | 566 ms                                                 | 486 ms: 1.16x faster                                                         |
| bench_thread_pool        | 986 us                                                 | 859 us: 1.15x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 87.6 ms: 1.14x faster                                                        |
| json_loads               | 31.2 us                                                | 27.9 us: 1.12x faster                                                        |
| json                     | 5.69 ms                                                | 5.15 ms: 1.11x faster                                                        |
| pathlib                  | 20.5 ms                                                | 18.7 ms: 1.10x faster                                                        |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 25.8 ms: 1.08x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 108 ms: 1.07x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                                        |
| create_gc_cycles         | 1.62 ms                                                | 1.55 ms: 1.05x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 161 ms: 1.05x faster                                                         |
| unpickle_list            | 5.20 us                                                | 5.02 us: 1.04x faster                                                        |
| pickle_list              | 5.08 us                                                | 4.92 us: 1.03x faster                                                        |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.84 sec: 1.00x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 563 ms: 1.01x slower                                                         |
| unpickle                 | 14.4 us                                                | 14.6 us: 1.02x slower                                                        |
| regex_dna                | 227 ms                                                 | 231 ms: 1.02x slower                                                         |
| async_generators         | 444 ms                                                 | 464 ms: 1.05x slower                                                         |
| regex_effbot             | 3.63 ms                                                | 3.85 ms: 1.06x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 3.92 ms: 1.08x slower                                                        |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                                        |
| telco                    | 7.27 ms                                                | 8.33 ms: 1.15x slower                                                        |
| pickle_dict              | 29.6 us                                                | 34.1 us: 1.15x slower                                                        |
| coverage                 | 79.4 ms                                                | 96.9 ms: 1.22x slower                                                        |
| unpack_sequence          | 60.0 ns                                                | 89.2 ns: 1.49x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 10.3 ms: 1.74x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                                 |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240318-3.13.0a5+-c8d6017-JIT/bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x


# Memory

- memory change: 1.33x