# Results vs. 3.10.4

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.36x faster                                                  |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                |
| html5lib       | 88.9 ms                                                | 61.8 ms: 1.44x faster                                                 |
| tornado_http   | 136 ms                                                 | 90.8 ms: 1.50x faster                                                 |
| Geometric mean | (ref)                                                  | 1.38x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 321 ms: 2.27x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 390 ms: 2.23x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 928 ms: 1.91x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 560 ms: 1.82x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 85.8 ms: 1.79x faster                                                 |
| float          | 117 ms                                                 | 77.8 ms: 1.51x faster                                                 |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.40x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                  |
| regex_v8       | 27.8 ms                                                | 26.8 ms: 1.04x faster                                                 |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.76 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.05 sec: 1.53x faster                                                |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                  |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 58.8 ms: 1.35x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 84.9 ms: 1.17x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 154 ms: 1.09x faster                                                  |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                 |
| django_template | 48.2 ms                                                | 33.5 ms: 1.44x faster                                                 |
| genshi_text     | 31.8 ms                                                | 23.0 ms: 1.38x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 51.5 ms: 1.28x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.29x faster                                                  |
| generators               | 80.1 ms                                                | 27.8 ms: 2.88x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.20 ms: 2.47x faster                                                 |
| async_tree_none          | 728 ms                                                 | 321 ms: 2.27x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 390 ms: 2.23x faster                                                  |
| go                       | 240 ms                                                 | 119 ms: 2.02x faster                                                  |
| chaos                    | 115 ms                                                 | 58.7 ms: 1.97x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.96x faster                                                 |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 482 ms: 1.91x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 928 ms: 1.91x faster                                                  |
| logging_silent           | 190 ns                                                 | 102 ns: 1.85x faster                                                  |
| richards_super           | 94.7 ms                                                | 51.7 ms: 1.83x faster                                                 |
| deepcopy                 | 479 us                                                 | 264 us: 1.82x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 560 ms: 1.82x faster                                                  |
| nbody                    | 154 ms                                                 | 85.8 ms: 1.79x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 72.4 ms: 1.76x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                 |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 68.2 ms: 1.73x faster                                                 |
| richards                 | 79.3 ms                                                | 46.0 ms: 1.72x faster                                                 |
| pylint                   | 551 ms                                                 | 321 ms: 1.72x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.19 ms: 1.68x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                                  |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.55x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.05 sec: 1.53x faster                                                |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.52x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                                 |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.51x faster                                                  |
| float                    | 117 ms                                                 | 77.8 ms: 1.51x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.50x faster                                                 |
| tornado_http             | 136 ms                                                 | 90.8 ms: 1.50x faster                                                 |
| pyflate                  | 716 ms                                                 | 478 ms: 1.50x faster                                                  |
| logging_format           | 9.09 us                                                | 6.17 us: 1.47x faster                                                 |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                 |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                  |
| html5lib                 | 88.9 ms                                                | 61.8 ms: 1.44x faster                                                 |
| django_template          | 48.2 ms                                                | 33.5 ms: 1.44x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.43x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 714 ms: 1.43x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| genshi_text              | 31.8 ms                                                | 23.0 ms: 1.38x faster                                                 |
| thrift                   | 1.07 ms                                                | 778 us: 1.38x faster                                                  |
| 2to3                     | 348 ms                                                 | 257 ms: 1.36x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.77 ms: 1.36x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 58.8 ms: 1.35x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.33x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                                 |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                  |
| nqueens                  | 106 ms                                                 | 80.4 ms: 1.32x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                                |
| fannkuch                 | 532 ms                                                 | 407 ms: 1.31x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 53.4 ms: 1.30x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 51.5 ms: 1.28x faster                                                 |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                                  |
| scimark_fft              | 466 ms                                                 | 363 ms: 1.28x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 787 us: 1.25x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                |
| sympy_expand             | 566 ms                                                 | 459 ms: 1.23x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 84.9 ms: 1.17x faster                                                 |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 154 ms: 1.09x faster                                                  |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                 |
| json                     | 5.69 ms                                                | 5.27 ms: 1.08x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 26.8 ms: 1.04x faster                                                 |
| async_generators         | 444 ms                                                 | 431 ms: 1.03x faster                                                  |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.76 ms: 1.04x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 3.78 ms: 1.04x slower                                                 |
| coverage                 | 79.4 ms                                                | 84.9 ms: 1.07x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                                 |
| telco                    | 7.27 ms                                                | 8.31 ms: 1.14x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240903-3.14.0a0-6d5be6d/bm-20240903-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.12x