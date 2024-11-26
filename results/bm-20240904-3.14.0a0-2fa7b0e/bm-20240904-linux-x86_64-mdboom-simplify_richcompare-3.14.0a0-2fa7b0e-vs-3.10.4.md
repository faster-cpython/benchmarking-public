# Results vs. 3.10.4

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.430x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.36x faster                                                  |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                |
| html5lib       | 88.9 ms                                                | 63.5 ms: 1.40x faster                                                 |
| tornado_http   | 136 ms                                                 | 90.7 ms: 1.50x faster                                                 |
| Geometric mean | (ref)                                                  | 1.37x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 327 ms: 2.23x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 394 ms: 2.21x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 937 ms: 1.89x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 567 ms: 1.79x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.0 ms: 1.78x faster                                                 |
| float          | 117 ms                                                 | 77.5 ms: 1.51x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.40x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 131 ms: 1.44x faster                                                  |
| regex_v8       | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                 |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 301 us: 1.61x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 210 us: 1.57x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.10 sec: 1.49x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 59.4 ms: 1.33x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 86.0 ms: 1.16x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                                  |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 155 ms: 1.08x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.2 ms: 1.45x faster                                                 |
| django_template | 48.2 ms                                                | 34.0 ms: 1.42x faster                                                 |
| genshi_text     | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 50.9 ms: 1.30x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.37x faster                                                  |
| generators               | 80.1 ms                                                | 27.7 ms: 2.89x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.21 ms: 2.47x faster                                                 |
| async_tree_none          | 728 ms                                                 | 327 ms: 2.23x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 394 ms: 2.21x faster                                                  |
| go                       | 240 ms                                                 | 119 ms: 2.02x faster                                                  |
| chaos                    | 115 ms                                                 | 58.7 ms: 1.97x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 30.3 us: 1.93x faster                                                 |
| raytrace                 | 507 ms                                                 | 263 ms: 1.93x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 479 ms: 1.93x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 937 ms: 1.89x faster                                                  |
| logging_silent           | 190 ns                                                 | 101 ns: 1.87x faster                                                  |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                  |
| richards_super           | 94.7 ms                                                | 51.8 ms: 1.83x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 567 ms: 1.79x faster                                                  |
| nbody                    | 154 ms                                                 | 86.0 ms: 1.78x faster                                                 |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 73.6 ms: 1.74x faster                                                 |
| richards                 | 79.3 ms                                                | 45.7 ms: 1.73x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 68.7 ms: 1.72x faster                                                 |
| pylint                   | 551 ms                                                 | 321 ms: 1.72x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.29 ms: 1.65x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 301 us: 1.61x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 210 us: 1.57x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                                 |
| spectral_norm            | 170 ms                                                 | 108 ms: 1.57x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                                 |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                  |
| pyflate                  | 716 ms                                                 | 471 ms: 1.52x faster                                                  |
| float                    | 117 ms                                                 | 77.5 ms: 1.51x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.51 us: 1.51x faster                                                 |
| tornado_http             | 136 ms                                                 | 90.7 ms: 1.50x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 2.10 sec: 1.49x faster                                                |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                 |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.45x faster                                                 |
| regex_compile            | 188 ms                                                 | 131 ms: 1.44x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.43x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 717 ms: 1.42x faster                                                  |
| django_template          | 48.2 ms                                                | 34.0 ms: 1.42x faster                                                 |
| html5lib                 | 88.9 ms                                                | 63.5 ms: 1.40x faster                                                 |
| thrift                   | 1.07 ms                                                | 771 us: 1.39x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| genshi_text              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.74 ms: 1.37x faster                                                 |
| 2to3                     | 348 ms                                                 | 257 ms: 1.36x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 59.4 ms: 1.33x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.32x faster                                                  |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.32x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                  |
| nqueens                  | 106 ms                                                 | 80.7 ms: 1.31x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 50.9 ms: 1.30x faster                                                 |
| scimark_fft              | 466 ms                                                 | 360 ms: 1.29x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 53.8 ms: 1.29x faster                                                 |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 787 us: 1.25x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                |
| sympy_expand             | 566 ms                                                 | 461 ms: 1.23x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 86.0 ms: 1.16x faster                                                 |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                                  |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 155 ms: 1.08x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.64 sec: 1.08x faster                                                |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                 |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                                  |
| gc_traversal             | 3.62 ms                                                | 3.72 ms: 1.03x slower                                                 |
| regex_effbot             | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                 |
| coverage                 | 79.4 ms                                                | 85.7 ms: 1.08x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.08x slower                                                 |
| telco                    | 7.27 ms                                                | 8.34 ms: 1.15x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                          |

Benchmark hidden because not significant (3): bench_mp_pool, asyncio_websockets, async_generators
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240904-3.14.0a0-2fa7b0e/bm-20240904-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.430x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.12x