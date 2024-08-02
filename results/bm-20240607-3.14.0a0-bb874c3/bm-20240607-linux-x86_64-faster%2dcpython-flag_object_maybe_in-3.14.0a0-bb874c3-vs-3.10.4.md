# Results vs. 3.10.4

- fork: faster-cpython
- ref: flag_object_maybe_in
- machine: linux-x86_64
- commit hash: bb874c3
- commit date: 2024-06-07
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 272 ms: 1.28x faster                                                            |
| docutils       | 3.30 sec                                               | 2.78 sec: 1.19x faster                                                          |
| html5lib       | 88.9 ms                                                | 66.9 ms: 1.33x faster                                                           |
| tornado_http   | 136 ms                                                 | 94.8 ms: 1.44x faster                                                           |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 378 ms: 1.93x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 957 ms: 1.85x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 478 ms: 1.82x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 632 ms: 1.61x faster                                                            |
| Geometric mean          | (ref)                                                  | 1.80x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 97.0 ms: 1.58x faster                                                           |
| float          | 117 ms                                                 | 79.7 ms: 1.47x faster                                                           |
| pidigits       | 191 ms                                                 | 190 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.33x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.39x faster                                                            |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                           |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.74 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 312 us: 1.56x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 223 us: 1.48x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.21 sec: 1.42x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 61.1 ms: 1.29x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 87.3 ms: 1.14x faster                                                           |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 108 ms: 1.07x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 159 ms: 1.05x faster                                                            |
| pickle_list          | 5.08 us                                                | 5.15 us: 1.01x slower                                                           |
| unpickle_list        | 5.20 us                                                | 5.38 us: 1.04x slower                                                           |
| unpickle             | 14.4 us                                                | 15.2 us: 1.06x slower                                                           |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                                           |
| pickle_dict          | 29.6 us                                                | 33.7 us: 1.14x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.7 ms: 1.36x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                           |
| django_template | 48.2 ms                                                | 35.3 ms: 1.36x faster                                                           |
| genshi_text     | 31.8 ms                                                | 23.8 ms: 1.34x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 52.1 ms: 1.27x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.30x faster                                                            |
| generators               | 80.1 ms                                                | 29.6 ms: 2.70x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.34 ms: 2.37x faster                                                           |
| async_tree_none          | 728 ms                                                 | 378 ms: 1.93x faster                                                            |
| chaos                    | 115 ms                                                 | 61.4 ms: 1.88x faster                                                           |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                                            |
| logging_silent           | 190 ns                                                 | 102 ns: 1.85x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 957 ms: 1.85x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 500 ms: 1.84x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 478 ms: 1.82x faster                                                            |
| pylint                   | 551 ms                                                 | 316 ms: 1.75x faster                                                            |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.72x faster                                                            |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                           |
| richards_super           | 94.7 ms                                                | 56.0 ms: 1.69x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 70.3 ms: 1.68x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 77.2 ms: 1.66x faster                                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.65x faster                                                           |
| go                       | 240 ms                                                 | 146 ms: 1.64x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.35 ms: 1.64x faster                                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 632 ms: 1.61x faster                                                            |
| richards                 | 79.3 ms                                                | 49.4 ms: 1.60x faster                                                           |
| nbody                    | 154 ms                                                 | 97.0 ms: 1.58x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 312 us: 1.56x faster                                                            |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.50x faster                                                           |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 223 us: 1.48x faster                                                            |
| float                    | 117 ms                                                 | 79.7 ms: 1.47x faster                                                           |
| deepcopy_memo            | 58.5 us                                                | 40.2 us: 1.45x faster                                                           |
| spectral_norm            | 170 ms                                                 | 118 ms: 1.44x faster                                                            |
| tornado_http             | 136 ms                                                 | 94.8 ms: 1.44x faster                                                           |
| tomli_loads              | 3.14 sec                                               | 2.21 sec: 1.42x faster                                                          |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                           |
| logging_simple           | 8.30 us                                                | 5.87 us: 1.41x faster                                                           |
| logging_format           | 9.09 us                                                | 6.48 us: 1.40x faster                                                           |
| pyflate                  | 716 ms                                                 | 514 ms: 1.39x faster                                                            |
| regex_compile            | 188 ms                                                 | 135 ms: 1.39x faster                                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.84 sec: 1.39x faster                                                          |
| django_template          | 48.2 ms                                                | 35.3 ms: 1.36x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                          |
| python_startup           | 14.6 ms                                                | 10.7 ms: 1.36x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                                          |
| genshi_text              | 31.8 ms                                                | 23.8 ms: 1.34x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                           |
| html5lib                 | 88.9 ms                                                | 66.9 ms: 1.33x faster                                                           |
| thrift                   | 1.07 ms                                                | 810 us: 1.32x faster                                                            |
| pprint_safe_repr         | 1.02 sec                                               | 770 ms: 1.32x faster                                                            |
| nqueens                  | 106 ms                                                 | 81.2 ms: 1.30x faster                                                           |
| deepcopy                 | 479 us                                                 | 369 us: 1.30x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 61.1 ms: 1.29x faster                                                           |
| fannkuch                 | 532 ms                                                 | 411 ms: 1.29x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.01 ms: 1.29x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.29x faster                                                            |
| dulwich_log              | 84.3 ms                                                | 65.6 ms: 1.28x faster                                                           |
| 2to3                     | 348 ms                                                 | 272 ms: 1.28x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 3.29 us: 1.27x faster                                                           |
| genshi_xml               | 66.0 ms                                                | 52.1 ms: 1.27x faster                                                           |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.27x faster                                                           |
| sympy_sum                | 196 ms                                                 | 157 ms: 1.25x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 20.7 ms: 1.25x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 55.6 ms: 1.24x faster                                                           |
| scimark_fft              | 466 ms                                                 | 376 ms: 1.24x faster                                                            |
| sympy_str                | 346 ms                                                 | 281 ms: 1.23x faster                                                            |
| sympy_expand             | 566 ms                                                 | 475 ms: 1.19x faster                                                            |
| dask                     | 441 ms                                                 | 371 ms: 1.19x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.78 sec: 1.19x faster                                                          |
| bench_thread_pool        | 986 us                                                 | 840 us: 1.17x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 87.3 ms: 1.14x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.59 sec: 1.10x faster                                                          |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                           |
| meteor_contest           | 120 ms                                                 | 111 ms: 1.08x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 108 ms: 1.07x faster                                                            |
| json                     | 5.69 ms                                                | 5.38 ms: 1.06x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 159 ms: 1.05x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.93 us: 1.03x faster                                                           |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                                            |
| bench_mp_pool            | 24.0 ms                                                | 23.9 ms: 1.00x faster                                                           |
| pidigits                 | 191 ms                                                 | 190 ms: 1.00x faster                                                            |
| async_generators         | 444 ms                                                 | 449 ms: 1.01x slower                                                            |
| pickle_list              | 5.08 us                                                | 5.15 us: 1.01x slower                                                           |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.01x slower                                                            |
| regex_effbot             | 3.63 ms                                                | 3.74 ms: 1.03x slower                                                           |
| unpickle_list            | 5.20 us                                                | 5.38 us: 1.04x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 3.79 ms: 1.05x slower                                                           |
| unpickle                 | 14.4 us                                                | 15.2 us: 1.06x slower                                                           |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.77 ms: 1.09x slower                                                           |
| pickle_dict              | 29.6 us                                                | 33.7 us: 1.14x slower                                                           |
| telco                    | 7.27 ms                                                | 8.41 ms: 1.16x slower                                                           |
| coverage                 | 79.4 ms                                                | 92.4 ms: 1.16x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.12 ms: 1.20x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.33x faster                                                                    |
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240607-3.14.0a0-bb874c3/bm-20240607-linux-x86_64-faster%2dcpython-flag_object_maybe_in-3.14.0a0-bb874c3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.11x