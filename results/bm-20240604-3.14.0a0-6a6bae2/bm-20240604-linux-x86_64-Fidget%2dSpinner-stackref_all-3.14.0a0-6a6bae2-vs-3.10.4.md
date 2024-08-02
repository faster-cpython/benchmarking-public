# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: 6a6bae2
- commit date: 2024-06-04
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 270 ms: 1.29x faster                                                    |
| docutils       | 3.30 sec                                               | 2.78 sec: 1.19x faster                                                  |
| html5lib       | 88.9 ms                                                | 67.1 ms: 1.33x faster                                                   |
| tornado_http   | 136 ms                                                 | 94.0 ms: 1.45x faster                                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 373 ms: 1.95x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 946 ms: 1.87x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 470 ms: 1.85x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 621 ms: 1.64x faster                                                    |
| Geometric mean          | (ref)                                                  | 1.82x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.1 ms: 1.74x faster                                                   |
| float          | 117 ms                                                 | 77.8 ms: 1.51x faster                                                   |
| pidigits       | 191 ms                                                 | 190 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                  | 1.38x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.39x faster                                                    |
| regex_v8       | 27.8 ms                                                | 26.2 ms: 1.06x faster                                                   |
| regex_dna      | 227 ms                                                 | 229 ms: 1.01x slower                                                    |
| regex_effbot   | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 306 us: 1.58x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 221 us: 1.49x faster                                                    |
| tomli_loads          | 3.14 sec                                               | 2.15 sec: 1.46x faster                                                  |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 85.8 ms: 1.16x faster                                                   |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 108 ms: 1.07x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 158 ms: 1.06x faster                                                    |
| unpickle_list        | 5.20 us                                                | 5.42 us: 1.04x slower                                                   |
| unpickle             | 14.4 us                                                | 15.2 us: 1.05x slower                                                   |
| pickle               | 10.7 us                                                | 11.9 us: 1.12x slower                                                   |
| pickle_dict          | 29.6 us                                                | 35.6 us: 1.20x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                            |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.7 ms: 1.37x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.13 ms: 1.20x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                   |
| django_template | 48.2 ms                                                | 34.9 ms: 1.38x faster                                                   |
| genshi_text     | 31.8 ms                                                | 23.3 ms: 1.37x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 52.0 ms: 1.27x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.29x faster                                                    |
| generators               | 80.1 ms                                                | 29.5 ms: 2.72x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.25 ms: 2.43x faster                                                   |
| async_tree_none          | 728 ms                                                 | 373 ms: 1.95x faster                                                    |
| chaos                    | 115 ms                                                 | 59.7 ms: 1.93x faster                                                   |
| raytrace                 | 507 ms                                                 | 263 ms: 1.93x faster                                                    |
| logging_silent           | 190 ns                                                 | 99.6 ns: 1.90x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 946 ms: 1.87x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 470 ms: 1.85x faster                                                    |
| asyncio_tcp              | 922 ms                                                 | 501 ms: 1.84x faster                                                    |
| richards_super           | 94.7 ms                                                | 54.0 ms: 1.75x faster                                                   |
| pylint                   | 551 ms                                                 | 315 ms: 1.75x faster                                                    |
| nbody                    | 154 ms                                                 | 88.1 ms: 1.74x faster                                                   |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 73.7 ms: 1.74x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 68.5 ms: 1.73x faster                                                   |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                                   |
| go                       | 240 ms                                                 | 142 ms: 1.70x faster                                                    |
| richards                 | 79.3 ms                                                | 47.7 ms: 1.66x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.29 ms: 1.65x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 621 ms: 1.64x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.59x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 306 us: 1.58x faster                                                    |
| spectral_norm            | 170 ms                                                 | 112 ms: 1.51x faster                                                    |
| pyflate                  | 716 ms                                                 | 474 ms: 1.51x faster                                                    |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                    |
| float                    | 117 ms                                                 | 77.8 ms: 1.51x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 221 us: 1.49x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 39.3 us: 1.49x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 2.15 sec: 1.46x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.69 us: 1.46x faster                                                   |
| tornado_http             | 136 ms                                                 | 94.0 ms: 1.45x faster                                                   |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                   |
| logging_format           | 9.09 us                                                | 6.36 us: 1.43x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.84 sec: 1.40x faster                                                  |
| regex_compile            | 188 ms                                                 | 135 ms: 1.39x faster                                                    |
| django_template          | 48.2 ms                                                | 34.9 ms: 1.38x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.37x faster                                                  |
| genshi_text              | 31.8 ms                                                | 23.3 ms: 1.37x faster                                                   |
| python_startup           | 14.6 ms                                                | 10.7 ms: 1.37x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 753 ms: 1.35x faster                                                    |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                   |
| thrift                   | 1.07 ms                                                | 805 us: 1.33x faster                                                    |
| html5lib                 | 88.9 ms                                                | 67.1 ms: 1.33x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                   |
| nqueens                  | 106 ms                                                 | 80.2 ms: 1.32x faster                                                   |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.94 ms: 1.31x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                    |
| deepcopy                 | 479 us                                                 | 367 us: 1.31x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.31x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 65.0 ms: 1.30x faster                                                   |
| 2to3                     | 348 ms                                                 | 270 ms: 1.29x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 20.3 ms: 1.27x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 52.0 ms: 1.27x faster                                                   |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.27x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 54.8 ms: 1.26x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 3.32 us: 1.26x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                   |
| sympy_str                | 346 ms                                                 | 279 ms: 1.24x faster                                                    |
| scimark_fft              | 466 ms                                                 | 379 ms: 1.23x faster                                                    |
| sympy_expand             | 566 ms                                                 | 470 ms: 1.20x faster                                                    |
| dask                     | 441 ms                                                 | 368 ms: 1.20x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.78 sec: 1.19x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 833 us: 1.18x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 85.8 ms: 1.16x faster                                                   |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                    |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 108 ms: 1.07x faster                                                    |
| json                     | 5.69 ms                                                | 5.35 ms: 1.06x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 158 ms: 1.06x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 26.2 ms: 1.06x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.73 sec: 1.04x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.97 us: 1.02x faster                                                   |
| pidigits                 | 191 ms                                                 | 190 ms: 1.00x faster                                                    |
| async_generators         | 444 ms                                                 | 447 ms: 1.01x slower                                                    |
| regex_dna                | 227 ms                                                 | 229 ms: 1.01x slower                                                    |
| asyncio_websockets       | 559 ms                                                 | 568 ms: 1.02x slower                                                    |
| regex_effbot             | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                   |
| unpickle_list            | 5.20 us                                                | 5.42 us: 1.04x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 3.81 ms: 1.05x slower                                                   |
| unpickle                 | 14.4 us                                                | 15.2 us: 1.05x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                   |
| pickle                   | 10.7 us                                                | 11.9 us: 1.12x slower                                                   |
| telco                    | 7.27 ms                                                | 8.36 ms: 1.15x slower                                                   |
| coverage                 | 79.4 ms                                                | 92.5 ms: 1.16x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.13 ms: 1.20x slower                                                   |
| pickle_dict              | 29.6 us                                                | 35.6 us: 1.20x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                            |

Benchmark hidden because not significant (2): bench_mp_pool, pickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240604-3.14.0a0-6a6bae2/bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.11x