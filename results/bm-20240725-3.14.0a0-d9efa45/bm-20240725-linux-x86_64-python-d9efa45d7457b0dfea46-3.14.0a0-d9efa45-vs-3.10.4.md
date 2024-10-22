# Results vs. 3.10.4

- fork: python
- ref: d9efa45d7457b0dfea46
- machine: linux-x86_64
- commit hash: d9efa45
- commit date: 2024-07-25
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 263 ms: 1.33x faster                                                  |
| docutils       | 3.30 sec                                               | 2.72 sec: 1.21x faster                                                |
| html5lib       | 88.9 ms                                                | 63.9 ms: 1.39x faster                                                 |
| tornado_http   | 136 ms                                                 | 89.9 ms: 1.52x faster                                                 |
| Geometric mean | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 324 ms: 2.24x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 399 ms: 2.18x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 904 ms: 1.96x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 560 ms: 1.81x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.04x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.5 ms: 1.73x faster                                                 |
| float          | 117 ms                                                 | 78.0 ms: 1.50x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 131 ms: 1.43x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                 |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.78 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 301 us: 1.61x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.55x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.04 sec: 1.54x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 59.0 ms: 1.34x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 85.3 ms: 1.17x faster                                                 |
| json_loads           | 31.2 us                                                | 27.7 us: 1.13x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 155 ms: 1.08x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                 |
| django_template | 48.2 ms                                                | 34.1 ms: 1.41x faster                                                 |
| genshi_text     | 31.8 ms                                                | 23.8 ms: 1.34x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 51.6 ms: 1.28x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                                  |
| generators               | 80.1 ms                                                | 28.1 ms: 2.85x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.17 ms: 2.50x faster                                                 |
| async_tree_none          | 728 ms                                                 | 324 ms: 2.24x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 399 ms: 2.18x faster                                                  |
| chaos                    | 115 ms                                                 | 58.4 ms: 1.98x faster                                                 |
| raytrace                 | 507 ms                                                 | 257 ms: 1.97x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 904 ms: 1.96x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.9 us: 1.95x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 482 ms: 1.91x faster                                                  |
| logging_silent           | 190 ns                                                 | 99.6 ns: 1.90x faster                                                 |
| richards_super           | 94.7 ms                                                | 51.2 ms: 1.85x faster                                                 |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 560 ms: 1.81x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 72.1 ms: 1.77x faster                                                 |
| richards                 | 79.3 ms                                                | 45.1 ms: 1.76x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.76x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 67.7 ms: 1.75x faster                                                 |
| pylint                   | 551 ms                                                 | 317 ms: 1.74x faster                                                  |
| nbody                    | 154 ms                                                 | 88.5 ms: 1.73x faster                                                 |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.73x faster                                                  |
| go                       | 240 ms                                                 | 140 ms: 1.72x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.21 ms: 1.68x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 301 us: 1.61x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.62 us: 1.59x faster                                                 |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.55x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.04 sec: 1.54x faster                                                |
| spectral_norm            | 170 ms                                                 | 111 ms: 1.53x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.52x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.45 us: 1.52x faster                                                 |
| tornado_http             | 136 ms                                                 | 89.9 ms: 1.52x faster                                                 |
| float                    | 117 ms                                                 | 78.0 ms: 1.50x faster                                                 |
| logging_format           | 9.09 us                                                | 6.07 us: 1.50x faster                                                 |
| pyflate                  | 716 ms                                                 | 483 ms: 1.48x faster                                                  |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                                 |
| regex_compile            | 188 ms                                                 | 131 ms: 1.43x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.43x faster                                                |
| django_template          | 48.2 ms                                                | 34.1 ms: 1.41x faster                                                 |
| html5lib                 | 88.9 ms                                                | 63.9 ms: 1.39x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                |
| thrift                   | 1.07 ms                                                | 773 us: 1.39x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 739 ms: 1.38x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 59.0 ms: 1.34x faster                                                 |
| genshi_text              | 31.8 ms                                                | 23.8 ms: 1.34x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.33x faster                                                  |
| nqueens                  | 106 ms                                                 | 79.7 ms: 1.33x faster                                                 |
| 2to3                     | 348 ms                                                 | 263 ms: 1.33x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                                 |
| fannkuch                 | 532 ms                                                 | 406 ms: 1.31x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.94 ms: 1.31x faster                                                 |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 53.6 ms: 1.29x faster                                                 |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 51.6 ms: 1.28x faster                                                 |
| sympy_str                | 346 ms                                                 | 271 ms: 1.27x faster                                                  |
| scimark_fft              | 466 ms                                                 | 366 ms: 1.27x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 784 us: 1.26x faster                                                  |
| dask                     | 441 ms                                                 | 354 ms: 1.25x faster                                                  |
| sympy_expand             | 566 ms                                                 | 462 ms: 1.22x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.72 sec: 1.21x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 85.3 ms: 1.17x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                                |
| json_loads               | 31.2 us                                                | 27.7 us: 1.13x faster                                                 |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                  |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 155 ms: 1.08x faster                                                  |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                  |
| async_generators         | 444 ms                                                 | 432 ms: 1.03x faster                                                  |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| gc_traversal             | 3.62 ms                                                | 3.72 ms: 1.03x slower                                                 |
| regex_effbot             | 3.63 ms                                                | 3.78 ms: 1.04x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                                 |
| telco                    | 7.27 ms                                                | 8.16 ms: 1.12x slower                                                 |
| coverage                 | 79.4 ms                                                | 92.6 ms: 1.17x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240725-3.14.0a0-d9efa45/bm-20240725-linux-x86_64-python-d9efa45d7457b0dfea46-3.14.0a0-d9efa45.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.12x