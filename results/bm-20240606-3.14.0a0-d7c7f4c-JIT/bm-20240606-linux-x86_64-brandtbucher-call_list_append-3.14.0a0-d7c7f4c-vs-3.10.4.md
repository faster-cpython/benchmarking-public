# Results vs. 3.10.4

- fork: brandtbucher
- ref: call_list_append
- machine: linux-x86_64
- commit hash: d7c7f4c
- commit date: 2024-06-06
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 281 ms: 1.24x faster                                                    |
| docutils       | 3.30 sec                                               | 2.95 sec: 1.12x faster                                                  |
| html5lib       | 88.9 ms                                                | 68.4 ms: 1.30x faster                                                   |
| tornado_http   | 136 ms                                                 | 97.1 ms: 1.40x faster                                                   |
| Geometric mean | (ref)                                                  | 1.26x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 384 ms: 1.90x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 474 ms: 1.83x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 999 ms: 1.77x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 640 ms: 1.59x faster                                                    |
| Geometric mean          | (ref)                                                  | 1.77x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.5 ms: 1.86x faster                                                   |
| float          | 117 ms                                                 | 72.6 ms: 1.61x faster                                                   |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.45x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.36x faster                                                    |
| regex_v8       | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                   |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                                    |
| regex_effbot   | 3.63 ms                                                | 3.56 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.12x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.61x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 306 us: 1.58x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 225 us: 1.47x faster                                                    |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.38x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 57.7 ms: 1.37x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 82.0 ms: 1.21x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.15x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                                    |
| json_loads           | 31.2 us                                                | 28.9 us: 1.08x faster                                                   |
| pickle_list          | 5.08 us                                                | 5.14 us: 1.01x slower                                                   |
| unpickle_list        | 5.20 us                                                | 5.37 us: 1.03x slower                                                   |
| unpickle             | 14.4 us                                                | 15.6 us: 1.09x slower                                                   |
| pickle               | 10.7 us                                                | 12.0 us: 1.13x slower                                                   |
| pickle_dict          | 29.6 us                                                | 34.7 us: 1.17x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.1 ms: 1.31x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.60 ms: 1.28x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                   |
| django_template | 48.2 ms                                                | 37.3 ms: 1.29x faster                                                   |
| genshi_text     | 31.8 ms                                                | 25.0 ms: 1.28x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 58.9 ms: 1.12x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 174 us: 3.13x faster                                                    |
| generators               | 80.1 ms                                                | 30.9 ms: 2.59x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.77 ms: 2.10x faster                                                   |
| richards_super           | 94.7 ms                                                | 48.4 ms: 1.96x faster                                                   |
| chaos                    | 115 ms                                                 | 60.3 ms: 1.91x faster                                                   |
| richards                 | 79.3 ms                                                | 41.8 ms: 1.90x faster                                                   |
| async_tree_none          | 728 ms                                                 | 384 ms: 1.90x faster                                                    |
| scimark_monte_carlo      | 118 ms                                                 | 62.8 ms: 1.88x faster                                                   |
| nbody                    | 154 ms                                                 | 82.5 ms: 1.86x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 474 ms: 1.83x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 70.2 ms: 1.82x faster                                                   |
| raytrace                 | 507 ms                                                 | 279 ms: 1.82x faster                                                    |
| asyncio_tcp              | 922 ms                                                 | 518 ms: 1.78x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 999 ms: 1.77x faster                                                    |
| logging_silent           | 190 ns                                                 | 107 ns: 1.77x faster                                                    |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                                   |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.70x faster                                                    |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                   |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                   |
| float                    | 117 ms                                                 | 72.6 ms: 1.61x faster                                                   |
| go                       | 240 ms                                                 | 149 ms: 1.61x faster                                                    |
| pyflate                  | 716 ms                                                 | 446 ms: 1.61x faster                                                    |
| spectral_norm            | 170 ms                                                 | 106 ms: 1.61x faster                                                    |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.61x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 640 ms: 1.59x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 306 us: 1.58x faster                                                    |
| pylint                   | 551 ms                                                 | 352 ms: 1.56x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.66 ms: 1.56x faster                                                   |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 38.4 us: 1.52x faster                                                   |
| fannkuch                 | 532 ms                                                 | 356 ms: 1.49x faster                                                    |
| unpickle_pure_python     | 331 us                                                 | 225 us: 1.47x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.71 us: 1.46x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                  |
| scimark_fft              | 466 ms                                                 | 324 ms: 1.44x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 712 ms: 1.43x faster                                                    |
| logging_format           | 9.09 us                                                | 6.42 us: 1.42x faster                                                   |
| tornado_http             | 136 ms                                                 | 97.1 ms: 1.40x faster                                                   |
| scimark_lu               | 176 ms                                                 | 126 ms: 1.40x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.64 ms: 1.39x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.38x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.87 sec: 1.38x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 57.7 ms: 1.37x faster                                                   |
| regex_compile            | 188 ms                                                 | 138 ms: 1.36x faster                                                    |
| python_startup           | 14.6 ms                                                | 11.1 ms: 1.31x faster                                                   |
| html5lib                 | 88.9 ms                                                | 68.4 ms: 1.30x faster                                                   |
| thrift                   | 1.07 ms                                                | 826 us: 1.30x faster                                                    |
| django_template          | 48.2 ms                                                | 37.3 ms: 1.29x faster                                                   |
| genshi_text              | 31.8 ms                                                | 25.0 ms: 1.28x faster                                                   |
| deepcopy                 | 479 us                                                 | 378 us: 1.27x faster                                                    |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.27x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 3.34 us: 1.25x faster                                                   |
| nqueens                  | 106 ms                                                 | 85.0 ms: 1.24x faster                                                   |
| 2to3                     | 348 ms                                                 | 281 ms: 1.24x faster                                                    |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 68.9 ms: 1.22x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 57.0 ms: 1.21x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 82.0 ms: 1.21x faster                                                   |
| dask                     | 441 ms                                                 | 381 ms: 1.16x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 22.5 ms: 1.15x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.15x faster                                                    |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                    |
| sympy_str                | 346 ms                                                 | 301 ms: 1.15x faster                                                    |
| genshi_xml               | 66.0 ms                                                | 58.9 ms: 1.12x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 881 us: 1.12x faster                                                    |
| docutils                 | 3.30 sec                                               | 2.95 sec: 1.12x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                   |
| sympy_expand             | 566 ms                                                 | 512 ms: 1.11x faster                                                    |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.10x faster                                                  |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                    |
| json_loads               | 31.2 us                                                | 28.9 us: 1.08x faster                                                   |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.06x faster                                                   |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                                    |
| regex_effbot             | 3.63 ms                                                | 3.56 ms: 1.02x faster                                                   |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                                    |
| pickle_list              | 5.08 us                                                | 5.14 us: 1.01x slower                                                   |
| asyncio_websockets       | 559 ms                                                 | 568 ms: 1.02x slower                                                    |
| unpickle_list            | 5.20 us                                                | 5.37 us: 1.03x slower                                                   |
| async_generators         | 444 ms                                                 | 469 ms: 1.06x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 3.87 ms: 1.07x slower                                                   |
| unpickle                 | 14.4 us                                                | 15.6 us: 1.09x slower                                                   |
| telco                    | 7.27 ms                                                | 8.06 ms: 1.11x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 1.80 ms: 1.11x slower                                                   |
| pickle                   | 10.7 us                                                | 12.0 us: 1.13x slower                                                   |
| pickle_dict              | 29.6 us                                                | 34.7 us: 1.17x slower                                                   |
| coverage                 | 79.4 ms                                                | 93.5 ms: 1.18x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.60 ms: 1.28x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                            |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240606-3.14.0a0-d7c7f4c-JIT/bm-20240606-linux-x86_64-brandtbucher-call_list_append-3.14.0a0-d7c7f4c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.21x