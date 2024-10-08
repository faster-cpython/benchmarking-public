# Results vs. 3.10.4

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.44x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                  |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.24x faster                                                |
| html5lib       | 88.9 ms                                                | 64.0 ms: 1.39x faster                                                 |
| tornado_http   | 136 ms                                                 | 89.9 ms: 1.52x faster                                                 |
| Geometric mean | (ref)                                                  | 1.37x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 322 ms: 2.26x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 389 ms: 2.24x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 920 ms: 1.92x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 557 ms: 1.82x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.05x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 89.8 ms: 1.71x faster                                                 |
| float          | 117 ms                                                 | 78.3 ms: 1.50x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.38x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                  |
| regex_v8       | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                 |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 301 us: 1.61x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 84.6 ms: 1.18x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                                  |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 154 ms: 1.09x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                 |
| django_template | 48.2 ms                                                | 33.8 ms: 1.42x faster                                                 |
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 49.1 ms: 1.35x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.43x faster                                                  |
| generators               | 80.1 ms                                                | 27.8 ms: 2.88x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.20 ms: 2.47x faster                                                 |
| async_tree_none          | 728 ms                                                 | 322 ms: 2.26x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 389 ms: 2.24x faster                                                  |
| go                       | 240 ms                                                 | 119 ms: 2.03x faster                                                  |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 473 ms: 1.95x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 30.1 us: 1.94x faster                                                 |
| raytrace                 | 507 ms                                                 | 262 ms: 1.94x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 920 ms: 1.92x faster                                                  |
| logging_silent           | 190 ns                                                 | 101 ns: 1.87x faster                                                  |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                                  |
| richards_super           | 94.7 ms                                                | 51.9 ms: 1.83x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 557 ms: 1.82x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 71.4 ms: 1.79x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 66.7 ms: 1.77x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                 |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                                  |
| pylint                   | 551 ms                                                 | 319 ms: 1.73x faster                                                  |
| richards                 | 79.3 ms                                                | 45.9 ms: 1.73x faster                                                 |
| nbody                    | 154 ms                                                 | 89.8 ms: 1.71x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.11 ms: 1.70x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.63x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 301 us: 1.61x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                 |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.55x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                                  |
| tornado_http             | 136 ms                                                 | 89.9 ms: 1.52x faster                                                 |
| pyflate                  | 716 ms                                                 | 474 ms: 1.51x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.51x faster                                                  |
| float                    | 117 ms                                                 | 78.3 ms: 1.50x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.55 us: 1.49x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.47x faster                                                 |
| logging_format           | 9.09 us                                                | 6.18 us: 1.47x faster                                                 |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.8 ms: 1.46x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                |
| django_template          | 48.2 ms                                                | 33.8 ms: 1.42x faster                                                 |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 716 ms: 1.42x faster                                                  |
| thrift                   | 1.07 ms                                                | 767 us: 1.40x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| html5lib                 | 88.9 ms                                                | 64.0 ms: 1.39x faster                                                 |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 49.1 ms: 1.35x faster                                                 |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.34x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.83 ms: 1.34x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                                 |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.32x faster                                                  |
| nqueens                  | 106 ms                                                 | 80.4 ms: 1.32x faster                                                 |
| pathlib                  | 20.5 ms                                                | 15.7 ms: 1.30x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 53.7 ms: 1.29x faster                                                 |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                                  |
| scimark_fft              | 466 ms                                                 | 369 ms: 1.26x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 784 us: 1.26x faster                                                  |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.24x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 84.6 ms: 1.18x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.50 sec: 1.14x faster                                                |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                                  |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 154 ms: 1.09x faster                                                  |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                 |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                  |
| async_generators         | 444 ms                                                 | 439 ms: 1.01x faster                                                  |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                                  |
| gc_traversal             | 3.62 ms                                                | 3.71 ms: 1.02x slower                                                 |
| regex_effbot             | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.75 ms: 1.08x slower                                                 |
| coverage                 | 79.4 ms                                                | 86.2 ms: 1.09x slower                                                 |
| telco                    | 7.27 ms                                                | 8.32 ms: 1.14x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240829-3.14.0a0-15b187e/bm-20240829-linux-x86_64-mdboom-simplify_richcompare-3.14.0a0-15b187e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.12x