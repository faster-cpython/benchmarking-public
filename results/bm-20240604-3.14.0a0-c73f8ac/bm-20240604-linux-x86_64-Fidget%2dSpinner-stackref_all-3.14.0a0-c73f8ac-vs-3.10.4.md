# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: c73f8ac
- commit date: 2024-06-04
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 272 ms: 1.28x faster                                                    |
| docutils       | 3.30 sec                                               | 2.80 sec: 1.18x faster                                                  |
| html5lib       | 88.9 ms                                                | 67.3 ms: 1.32x faster                                                   |
| tornado_http   | 136 ms                                                 | 94.6 ms: 1.44x faster                                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 374 ms: 1.95x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 950 ms: 1.86x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 473 ms: 1.84x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 632 ms: 1.61x faster                                                    |
| Geometric mean          | (ref)                                                  | 1.81x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 92.2 ms: 1.66x faster                                                   |
| float          | 117 ms                                                 | 79.0 ms: 1.48x faster                                                   |
| pidigits       | 191 ms                                                 | 190 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                  | 1.35x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 136 ms: 1.39x faster                                                    |
| regex_v8       | 27.8 ms                                                | 24.9 ms: 1.12x faster                                                   |
| regex_dna      | 227 ms                                                 | 221 ms: 1.02x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.70 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.12x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 312 us: 1.55x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 227 us: 1.45x faster                                                    |
| tomli_loads          | 3.14 sec                                               | 2.23 sec: 1.41x faster                                                  |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 61.1 ms: 1.30x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 87.5 ms: 1.14x faster                                                   |
| json_loads           | 31.2 us                                                | 29.2 us: 1.07x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 108 ms: 1.07x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 158 ms: 1.06x faster                                                    |
| unpickle             | 14.4 us                                                | 15.1 us: 1.05x slower                                                   |
| pickle_list          | 5.08 us                                                | 5.35 us: 1.05x slower                                                   |
| pickle               | 10.7 us                                                | 11.9 us: 1.12x slower                                                   |
| pickle_dict          | 29.6 us                                                | 36.2 us: 1.22x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                            |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.7 ms: 1.37x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 12.0 ms: 1.37x faster                                                   |
| genshi_text     | 31.8 ms                                                | 23.3 ms: 1.36x faster                                                   |
| django_template | 48.2 ms                                                | 36.1 ms: 1.33x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 53.9 ms: 1.22x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.19x faster                                                    |
| generators               | 80.1 ms                                                | 29.7 ms: 2.70x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.35 ms: 2.36x faster                                                   |
| async_tree_none          | 728 ms                                                 | 374 ms: 1.95x faster                                                    |
| raytrace                 | 507 ms                                                 | 269 ms: 1.88x faster                                                    |
| chaos                    | 115 ms                                                 | 62.0 ms: 1.86x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 950 ms: 1.86x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 473 ms: 1.84x faster                                                    |
| asyncio_tcp              | 922 ms                                                 | 505 ms: 1.83x faster                                                    |
| logging_silent           | 190 ns                                                 | 107 ns: 1.78x faster                                                    |
| richards_super           | 94.7 ms                                                | 54.4 ms: 1.74x faster                                                   |
| pylint                   | 551 ms                                                 | 317 ms: 1.74x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 69.9 ms: 1.69x faster                                                   |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                                   |
| scimark_sor              | 220 ms                                                 | 131 ms: 1.68x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 76.6 ms: 1.67x faster                                                   |
| nbody                    | 154 ms                                                 | 92.2 ms: 1.66x faster                                                   |
| go                       | 240 ms                                                 | 145 ms: 1.65x faster                                                    |
| richards                 | 79.3 ms                                                | 48.2 ms: 1.64x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.38 ms: 1.63x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.61x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 632 ms: 1.61x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 312 us: 1.55x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.66 ms: 1.55x faster                                                   |
| pyflate                  | 716 ms                                                 | 471 ms: 1.52x faster                                                    |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                    |
| float                    | 117 ms                                                 | 79.0 ms: 1.48x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.7 ms: 1.48x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 227 us: 1.45x faster                                                    |
| tornado_http             | 136 ms                                                 | 94.6 ms: 1.44x faster                                                   |
| spectral_norm            | 170 ms                                                 | 118 ms: 1.44x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 41.0 us: 1.43x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.84 us: 1.42x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 2.23 sec: 1.41x faster                                                  |
| logging_format           | 9.09 us                                                | 6.48 us: 1.40x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                  |
| regex_compile            | 188 ms                                                 | 136 ms: 1.39x faster                                                    |
| python_startup           | 14.6 ms                                                | 10.7 ms: 1.37x faster                                                   |
| mako                     | 16.3 ms                                                | 12.0 ms: 1.37x faster                                                   |
| genshi_text              | 31.8 ms                                                | 23.3 ms: 1.36x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                   |
| django_template          | 48.2 ms                                                | 36.1 ms: 1.33x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.58 sec: 1.33x faster                                                  |
| thrift                   | 1.07 ms                                                | 809 us: 1.33x faster                                                    |
| html5lib                 | 88.9 ms                                                | 67.3 ms: 1.32x faster                                                   |
| fannkuch                 | 532 ms                                                 | 406 ms: 1.31x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 780 ms: 1.31x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 61.1 ms: 1.30x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.00 ms: 1.29x faster                                                   |
| nqueens                  | 106 ms                                                 | 82.1 ms: 1.29x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 111 ms: 1.29x faster                                                    |
| deepcopy                 | 479 us                                                 | 373 us: 1.28x faster                                                    |
| 2to3                     | 348 ms                                                 | 272 ms: 1.28x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 66.0 ms: 1.28x faster                                                   |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.26x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 20.5 ms: 1.26x faster                                                   |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 55.6 ms: 1.24x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 3.36 us: 1.24x faster                                                   |
| scimark_fft              | 466 ms                                                 | 376 ms: 1.24x faster                                                    |
| sympy_str                | 346 ms                                                 | 282 ms: 1.23x faster                                                    |
| genshi_xml               | 66.0 ms                                                | 53.9 ms: 1.22x faster                                                   |
| sympy_expand             | 566 ms                                                 | 474 ms: 1.19x faster                                                    |
| dask                     | 441 ms                                                 | 370 ms: 1.19x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.80 sec: 1.18x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 838 us: 1.18x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 87.5 ms: 1.14x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 24.9 ms: 1.12x faster                                                   |
| meteor_contest           | 120 ms                                                 | 111 ms: 1.07x faster                                                    |
| json_loads               | 31.2 us                                                | 29.2 us: 1.07x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 108 ms: 1.07x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 158 ms: 1.06x faster                                                    |
| json                     | 5.69 ms                                                | 5.39 ms: 1.06x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.76 sec: 1.03x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.94 us: 1.03x faster                                                   |
| regex_dna                | 227 ms                                                 | 221 ms: 1.02x faster                                                    |
| bench_mp_pool            | 24.0 ms                                                | 23.9 ms: 1.01x faster                                                   |
| pidigits                 | 191 ms                                                 | 190 ms: 1.00x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 563 ms: 1.01x slower                                                    |
| async_generators         | 444 ms                                                 | 452 ms: 1.02x slower                                                    |
| regex_effbot             | 3.63 ms                                                | 3.70 ms: 1.02x slower                                                   |
| unpickle                 | 14.4 us                                                | 15.1 us: 1.05x slower                                                   |
| pickle_list              | 5.08 us                                                | 5.35 us: 1.05x slower                                                   |
| gc_traversal             | 3.62 ms                                                | 3.95 ms: 1.09x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 1.77 ms: 1.09x slower                                                   |
| pickle                   | 10.7 us                                                | 11.9 us: 1.12x slower                                                   |
| telco                    | 7.27 ms                                                | 8.45 ms: 1.16x slower                                                   |
| coverage                 | 79.4 ms                                                | 92.5 ms: 1.16x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                   |
| pickle_dict              | 29.6 us                                                | 36.2 us: 1.22x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.33x faster                                                            |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240604-3.14.0a0-c73f8ac/bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.11x