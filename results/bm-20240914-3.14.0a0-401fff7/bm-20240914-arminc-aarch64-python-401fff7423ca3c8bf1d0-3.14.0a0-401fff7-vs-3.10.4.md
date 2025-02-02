# Results vs. 3.10.4

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-aarch64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.334x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 295 ms: 1.29x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                  |
| html5lib       | 86.5 ms                                                               | 65.5 ms: 1.32x faster                                                   |
| tornado_http   | 178 ms                                                                | 128 ms: 1.40x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 424 ms: 2.24x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 558 ms: 2.03x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.14 sec: 2.00x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 737 ms: 1.73x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.99x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 110 ms: 1.50x faster                                                    |
| float          | 135 ms                                                                | 92.7 ms: 1.45x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 126 ms: 1.40x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| regex_dna      | 257 ms                                                                | 249 ms: 1.03x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.92 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 362 us: 1.46x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 252 us: 1.45x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 79.5 ms: 1.25x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.41 us: 1.09x faster                                                   |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| pickle_list          | 5.24 us                                                               | 5.19 us: 1.01x faster                                                   |
| json_loads           | 30.9 us                                                               | 31.8 us: 1.03x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 37.6 us: 1.07x slower                                                   |
| pickle               | 12.5 us                                                               | 13.5 us: 1.09x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.4 us: 1.11x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 12.9 ms: 1.15x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.20x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.5 ms: 1.40x faster                                                   |
| django_template | 53.3 ms                                                               | 41.7 ms: 1.28x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 193 us: 3.43x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.92 ms: 2.28x faster                                                   |
| async_tree_none          | 950 ms                                                                | 424 ms: 2.24x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.01 ms: 2.07x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 558 ms: 2.03x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.14 sec: 2.00x faster                                                  |
| generators               | 68.1 ms                                                               | 34.7 ms: 1.96x faster                                                   |
| go                       | 264 ms                                                                | 139 ms: 1.90x faster                                                    |
| raytrace                 | 573 ms                                                                | 303 ms: 1.89x faster                                                    |
| richards_super           | 107 ms                                                                | 59.4 ms: 1.81x faster                                                   |
| chaos                    | 121 ms                                                                | 69.0 ms: 1.75x faster                                                   |
| richards                 | 91.7 ms                                                               | 52.7 ms: 1.74x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 737 ms: 1.73x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.40 ms: 1.72x faster                                                   |
| scimark_lu               | 227 ms                                                                | 135 ms: 1.68x faster                                                    |
| logging_silent           | 222 ns                                                                | 133 ns: 1.67x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 81.3 ms: 1.65x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 576 ms: 1.64x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.7 us: 1.64x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 1.74 ms: 1.63x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.6 us: 1.61x faster                                                   |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.56x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 82.5 ms: 1.55x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.10 ms: 1.54x faster                                                   |
| deepcopy                 | 511 us                                                                | 334 us: 1.53x faster                                                    |
| nbody                    | 166 ms                                                                | 110 ms: 1.50x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.22 sec: 1.48x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 362 us: 1.46x faster                                                    |
| float                    | 135 ms                                                                | 92.7 ms: 1.45x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 252 us: 1.45x faster                                                    |
| pyflate                  | 795 ms                                                                | 562 ms: 1.41x faster                                                    |
| regex_compile            | 177 ms                                                                | 126 ms: 1.40x faster                                                    |
| tornado_http             | 178 ms                                                                | 128 ms: 1.40x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.5 ms: 1.40x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.01 us: 1.40x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.22 sec: 1.39x faster                                                  |
| logging_format           | 10.6 us                                                               | 7.63 us: 1.39x faster                                                   |
| thrift                   | 1.26 ms                                                               | 931 us: 1.35x faster                                                    |
| pylint                   | 485 ms                                                                | 359 ms: 1.35x faster                                                    |
| spectral_norm            | 186 ms                                                                | 140 ms: 1.33x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 65.5 ms: 1.32x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.52 us: 1.31x faster                                                   |
| sympy_sum                | 184 ms                                                                | 142 ms: 1.30x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.7 ms: 1.30x faster                                                   |
| 2to3                     | 381 ms                                                                | 295 ms: 1.29x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.23 ms: 1.29x faster                                                   |
| django_template          | 53.3 ms                                                               | 41.7 ms: 1.28x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.8 ms: 1.27x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| pathlib                  | 26.3 ms                                                               | 20.7 ms: 1.27x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 58.3 ms: 1.26x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 79.5 ms: 1.25x faster                                                   |
| sympy_str                | 329 ms                                                                | 264 ms: 1.24x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 926 ms: 1.24x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.91 sec: 1.24x faster                                                  |
| sqlglot_normalize        | 156 ms                                                                | 127 ms: 1.23x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 62.3 ms: 1.21x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.42 ms: 1.19x faster                                                   |
| fannkuch                 | 546 ms                                                                | 460 ms: 1.19x faster                                                    |
| sympy_expand             | 543 ms                                                                | 460 ms: 1.18x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                  |
| nqueens                  | 117 ms                                                                | 101 ms: 1.17x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                                   |
| meteor_contest           | 126 ms                                                                | 111 ms: 1.13x faster                                                    |
| scimark_fft              | 500 ms                                                                | 442 ms: 1.13x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.33 sec: 1.11x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.41 us: 1.09x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.81 us: 1.08x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| json                     | 5.88 ms                                                               | 5.57 ms: 1.06x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| regex_dna                | 257 ms                                                                | 249 ms: 1.03x faster                                                    |
| pickle_list              | 5.24 us                                                               | 5.19 us: 1.01x faster                                                   |
| json_loads               | 30.9 us                                                               | 31.8 us: 1.03x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.33 ms: 1.03x slower                                                   |
| async_generators         | 452 ms                                                                | 483 ms: 1.07x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 37.6 us: 1.07x slower                                                   |
| pickle                   | 12.5 us                                                               | 13.5 us: 1.09x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.4 us: 1.11x slower                                                   |
| python_startup           | 11.2 ms                                                               | 12.9 ms: 1.15x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.92 ms: 1.16x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.86 ms: 1.16x slower                                                   |
| coverage                 | 83.6 ms                                                               | 97.5 ms: 1.17x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.18 ms: 1.25x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.32x faster                                                            |

Benchmark hidden because not significant (2): pidigits, asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240914-3.14.0a0-401fff7/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.334x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.14x