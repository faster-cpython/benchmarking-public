# Results vs. 3.10.4

- fork: faster-cpython
- ref: lower_before
- machine: linux-x86_64
- commit hash: 68df0a5
- commit date: 2024-06-17
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 270 ms: 1.29x faster                                                    |
| docutils       | 3.30 sec                                               | 2.79 sec: 1.18x faster                                                  |
| html5lib       | 88.9 ms                                                | 68.9 ms: 1.29x faster                                                   |
| tornado_http   | 136 ms                                                 | 93.6 ms: 1.46x faster                                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 370 ms: 1.97x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 951 ms: 1.86x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 489 ms: 1.78x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 622 ms: 1.63x faster                                                    |
| Geometric mean          | (ref)                                                  | 1.81x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.3 ms: 1.74x faster                                                   |
| float          | 117 ms                                                 | 78.1 ms: 1.50x faster                                                   |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.38x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.41x faster                                                    |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                   |
| regex_dna      | 227 ms                                                 | 232 ms: 1.02x slower                                                    |
| regex_effbot   | 3.63 ms                                                | 3.79 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                    |
| tomli_loads          | 3.14 sec                                               | 2.18 sec: 1.44x faster                                                  |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 86.3 ms: 1.15x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                                    |
| json_loads           | 31.2 us                                                | 29.0 us: 1.08x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 160 ms: 1.05x faster                                                    |
| unpickle             | 14.4 us                                                | 14.8 us: 1.03x slower                                                   |
| unpickle_list        | 5.20 us                                                | 5.50 us: 1.06x slower                                                   |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                                   |
| pickle_dict          | 29.6 us                                                | 34.7 us: 1.17x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                            |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.7 ms: 1.37x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.2 ms: 1.45x faster                                                   |
| django_template | 48.2 ms                                                | 34.4 ms: 1.40x faster                                                   |
| genshi_text     | 31.8 ms                                                | 23.7 ms: 1.34x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 51.5 ms: 1.28x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                                    |
| generators               | 80.1 ms                                                | 29.4 ms: 2.72x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.24 ms: 2.44x faster                                                   |
| async_tree_none          | 728 ms                                                 | 370 ms: 1.97x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 29.9 us: 1.95x faster                                                   |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                                    |
| chaos                    | 115 ms                                                 | 60.4 ms: 1.91x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 951 ms: 1.86x faster                                                    |
| asyncio_tcp              | 922 ms                                                 | 505 ms: 1.83x faster                                                    |
| logging_silent           | 190 ns                                                 | 105 ns: 1.80x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 489 ms: 1.78x faster                                                    |
| deepcopy                 | 479 us                                                 | 270 us: 1.78x faster                                                    |
| pylint                   | 551 ms                                                 | 316 ms: 1.75x faster                                                    |
| nbody                    | 154 ms                                                 | 88.3 ms: 1.74x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 74.0 ms: 1.73x faster                                                   |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 69.1 ms: 1.71x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.09 ms: 1.71x faster                                                   |
| richards_super           | 94.7 ms                                                | 56.1 ms: 1.69x faster                                                   |
| go                       | 240 ms                                                 | 145 ms: 1.66x faster                                                    |
| scimark_sor              | 220 ms                                                 | 133 ms: 1.65x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 622 ms: 1.63x faster                                                    |
| richards                 | 79.3 ms                                                | 49.8 ms: 1.59x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                                    |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                    |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.51x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 2.78 us: 1.50x faster                                                   |
| float                    | 117 ms                                                 | 78.1 ms: 1.50x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                                   |
| tornado_http             | 136 ms                                                 | 93.6 ms: 1.46x faster                                                   |
| pyflate                  | 716 ms                                                 | 492 ms: 1.45x faster                                                    |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.45x faster                                                   |
| coroutines               | 35.1 ms                                                | 24.3 ms: 1.44x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 2.18 sec: 1.44x faster                                                  |
| logging_format           | 9.09 us                                                | 6.35 us: 1.43x faster                                                   |
| regex_compile            | 188 ms                                                 | 134 ms: 1.41x faster                                                    |
| django_template          | 48.2 ms                                                | 34.4 ms: 1.40x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.7 ms: 1.37x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.36x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                  |
| nqueens                  | 106 ms                                                 | 78.2 ms: 1.35x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 755 ms: 1.35x faster                                                    |
| genshi_text              | 31.8 ms                                                | 23.7 ms: 1.34x faster                                                   |
| fannkuch                 | 532 ms                                                 | 401 ms: 1.33x faster                                                    |
| thrift                   | 1.07 ms                                                | 810 us: 1.32x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.29x faster                                                    |
| html5lib                 | 88.9 ms                                                | 68.9 ms: 1.29x faster                                                   |
| 2to3                     | 348 ms                                                 | 270 ms: 1.29x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 65.6 ms: 1.29x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 51.5 ms: 1.28x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 20.2 ms: 1.28x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.07 ms: 1.27x faster                                                   |
| sympy_sum                | 196 ms                                                 | 154 ms: 1.27x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 55.0 ms: 1.26x faster                                                   |
| sympy_str                | 346 ms                                                 | 280 ms: 1.24x faster                                                    |
| scimark_fft              | 466 ms                                                 | 377 ms: 1.24x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 807 us: 1.22x faster                                                    |
| dask                     | 441 ms                                                 | 367 ms: 1.20x faster                                                    |
| sympy_expand             | 566 ms                                                 | 473 ms: 1.20x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.79 sec: 1.18x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 86.3 ms: 1.15x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                   |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.63 sec: 1.08x faster                                                  |
| json_loads               | 31.2 us                                                | 29.0 us: 1.08x faster                                                   |
| json                     | 5.69 ms                                                | 5.35 ms: 1.06x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 160 ms: 1.05x faster                                                    |
| sqlite_synth             | 3.02 us                                                | 2.96 us: 1.02x faster                                                   |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                                    |
| bench_mp_pool            | 24.0 ms                                                | 23.9 ms: 1.00x faster                                                   |
| async_generators         | 444 ms                                                 | 442 ms: 1.00x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.01x slower                                                    |
| regex_dna                | 227 ms                                                 | 232 ms: 1.02x slower                                                    |
| unpickle                 | 14.4 us                                                | 14.8 us: 1.03x slower                                                   |
| regex_effbot             | 3.63 ms                                                | 3.79 ms: 1.04x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 3.80 ms: 1.05x slower                                                   |
| unpickle_list            | 5.20 us                                                | 5.50 us: 1.06x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.08x slower                                                   |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                                   |
| telco                    | 7.27 ms                                                | 8.33 ms: 1.15x slower                                                   |
| pickle_dict              | 29.6 us                                                | 34.7 us: 1.17x slower                                                   |
| coverage                 | 79.4 ms                                                | 94.5 ms: 1.19x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                            |

Benchmark hidden because not significant (1): pickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240617-3.14.0a0-68df0a5/bm-20240617-linux-x86_64-faster%2dcpython-lower_before-3.14.0a0-68df0a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.12x