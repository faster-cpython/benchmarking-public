# Results vs. 3.10.4

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.45x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 253 ms: 1.38x faster                                                  |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                |
| html5lib       | 88.9 ms                                                | 63.8 ms: 1.39x faster                                                 |
| tornado_http   | 136 ms                                                 | 89.5 ms: 1.52x faster                                                 |
| Geometric mean | (ref)                                                  | 1.38x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 322 ms: 2.26x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 389 ms: 2.24x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 926 ms: 1.91x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 561 ms: 1.81x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 85.3 ms: 1.80x faster                                                 |
| float          | 117 ms                                                 | 76.5 ms: 1.53x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.41x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                 |
| regex_dna      | 227 ms                                                 | 218 ms: 1.04x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.54 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 301 us: 1.61x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 212 us: 1.56x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.05 sec: 1.53x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 58.8 ms: 1.35x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 85.2 ms: 1.17x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                                  |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                 |
| django_template | 48.2 ms                                                | 33.7 ms: 1.43x faster                                                 |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 48.2 ms: 1.37x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.39x faster                                                  |
| generators               | 80.1 ms                                                | 27.7 ms: 2.89x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.22 ms: 2.46x faster                                                 |
| async_tree_none          | 728 ms                                                 | 322 ms: 2.26x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 389 ms: 2.24x faster                                                  |
| go                       | 240 ms                                                 | 117 ms: 2.04x faster                                                  |
| chaos                    | 115 ms                                                 | 58.2 ms: 1.99x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 29.6 us: 1.97x faster                                                 |
| raytrace                 | 507 ms                                                 | 261 ms: 1.94x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 926 ms: 1.91x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 486 ms: 1.90x faster                                                  |
| logging_silent           | 190 ns                                                 | 100 ns: 1.89x faster                                                  |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                  |
| richards_super           | 94.7 ms                                                | 51.6 ms: 1.83x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 561 ms: 1.81x faster                                                  |
| nbody                    | 154 ms                                                 | 85.3 ms: 1.80x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 66.4 ms: 1.78x faster                                                 |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.78x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 72.9 ms: 1.75x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                 |
| richards                 | 79.3 ms                                                | 45.9 ms: 1.73x faster                                                 |
| pylint                   | 551 ms                                                 | 319 ms: 1.73x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.19 ms: 1.68x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 301 us: 1.61x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                 |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 212 us: 1.56x faster                                                  |
| pyflate                  | 716 ms                                                 | 461 ms: 1.56x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.05 sec: 1.53x faster                                                |
| float                    | 117 ms                                                 | 76.5 ms: 1.53x faster                                                 |
| tornado_http             | 136 ms                                                 | 89.5 ms: 1.52x faster                                                 |
| spectral_norm            | 170 ms                                                 | 112 ms: 1.51x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                 |
| logging_format           | 9.09 us                                                | 6.10 us: 1.49x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.58 us: 1.49x faster                                                 |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                 |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.44 sec: 1.46x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 702 ms: 1.45x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                |
| django_template          | 48.2 ms                                                | 33.7 ms: 1.43x faster                                                 |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                 |
| thrift                   | 1.07 ms                                                | 762 us: 1.41x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                                |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| html5lib                 | 88.9 ms                                                | 63.8 ms: 1.39x faster                                                 |
| 2to3                     | 348 ms                                                 | 253 ms: 1.38x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 48.2 ms: 1.37x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.77 ms: 1.36x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 58.8 ms: 1.35x faster                                                 |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                  |
| nqueens                  | 106 ms                                                 | 79.8 ms: 1.33x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                                 |
| fannkuch                 | 532 ms                                                 | 402 ms: 1.32x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.32x faster                                                  |
| sympy_str                | 346 ms                                                 | 267 ms: 1.30x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 53.5 ms: 1.29x faster                                                 |
| scimark_fft              | 466 ms                                                 | 363 ms: 1.28x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 783 us: 1.26x faster                                                  |
| sympy_expand             | 566 ms                                                 | 452 ms: 1.25x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 85.2 ms: 1.17x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.50 sec: 1.14x faster                                                |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                                  |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                                 |
| regex_dna                | 227 ms                                                 | 218 ms: 1.04x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.54 ms: 1.03x faster                                                 |
| gc_traversal             | 3.62 ms                                                | 3.54 ms: 1.02x faster                                                 |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| async_generators         | 444 ms                                                 | 439 ms: 1.01x faster                                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.73 ms: 1.07x slower                                                 |
| coverage                 | 79.4 ms                                                | 85.7 ms: 1.08x slower                                                 |
| telco                    | 7.27 ms                                                | 8.34 ms: 1.15x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.45x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240829-3.14.0a0-c9a5962/bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.12x