# Results vs. 3.10.4

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-x86_64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 271 ms: 1.29x faster                                                  |
| chameleon      | 9.68 ms                                                | 7.01 ms: 1.38x faster                                                 |
| docutils       | 3.30 sec                                               | 2.78 sec: 1.18x faster                                                |
| html5lib       | 88.9 ms                                                | 67.1 ms: 1.33x faster                                                 |
| tornado_http   | 136 ms                                                 | 93.9 ms: 1.45x faster                                                 |
| Geometric mean | (ref)                                                  | 1.32x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 381 ms: 1.91x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 464 ms: 1.88x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 947 ms: 1.87x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 617 ms: 1.65x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.82x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 84.6 ms: 1.81x faster                                                 |
| float          | 117 ms                                                 | 77.2 ms: 1.52x faster                                                 |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.40x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.40x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                 |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 300 us: 1.62x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.15 sec: 1.46x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.8 ms: 1.31x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 86.2 ms: 1.15x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                                  |
| json_loads           | 31.2 us                                                | 28.9 us: 1.08x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 159 ms: 1.06x faster                                                  |
| pickle_list          | 5.08 us                                                | 5.20 us: 1.02x slower                                                 |
| unpickle_list        | 5.20 us                                                | 5.35 us: 1.03x slower                                                 |
| unpickle             | 14.4 us                                                | 15.4 us: 1.07x slower                                                 |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                                 |
| pickle_dict          | 29.6 us                                                | 35.7 us: 1.21x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.0 ms: 1.48x faster                                                 |
| django_template | 48.2 ms                                                | 35.3 ms: 1.36x faster                                                 |
| genshi_text     | 31.8 ms                                                | 23.7 ms: 1.34x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 51.3 ms: 1.29x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.27x faster                                                  |
| generators               | 80.1 ms                                                | 28.6 ms: 2.80x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.26 ms: 2.43x faster                                                 |
| raytrace                 | 507 ms                                                 | 262 ms: 1.93x faster                                                  |
| chaos                    | 115 ms                                                 | 60.4 ms: 1.91x faster                                                 |
| async_tree_none          | 728 ms                                                 | 381 ms: 1.91x faster                                                  |
| logging_silent           | 190 ns                                                 | 101 ns: 1.89x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 464 ms: 1.88x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 947 ms: 1.87x faster                                                  |
| nbody                    | 154 ms                                                 | 84.6 ms: 1.81x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 508 ms: 1.81x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 67.0 ms: 1.76x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.75x faster                                                 |
| pylint                   | 551 ms                                                 | 318 ms: 1.74x faster                                                  |
| richards_super           | 94.7 ms                                                | 54.8 ms: 1.73x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 74.4 ms: 1.72x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.12 ms: 1.70x faster                                                 |
| go                       | 240 ms                                                 | 144 ms: 1.67x faster                                                  |
| scimark_sor              | 220 ms                                                 | 133 ms: 1.65x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 617 ms: 1.65x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                                 |
| richards                 | 79.3 ms                                                | 48.6 ms: 1.63x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.62x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                 |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.55x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                                  |
| pyflate                  | 716 ms                                                 | 472 ms: 1.52x faster                                                  |
| float                    | 117 ms                                                 | 77.2 ms: 1.52x faster                                                 |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.50x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 39.0 us: 1.50x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                 |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.48x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 2.15 sec: 1.46x faster                                                |
| tornado_http             | 136 ms                                                 | 93.9 ms: 1.45x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.80 us: 1.43x faster                                                 |
| logging_format           | 9.09 us                                                | 6.43 us: 1.41x faster                                                 |
| regex_compile            | 188 ms                                                 | 134 ms: 1.40x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.39x faster                                                |
| chameleon                | 9.68 ms                                                | 7.01 ms: 1.38x faster                                                 |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 741 ms: 1.37x faster                                                  |
| django_template          | 48.2 ms                                                | 35.3 ms: 1.36x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                |
| fannkuch                 | 532 ms                                                 | 394 ms: 1.35x faster                                                  |
| genshi_text              | 31.8 ms                                                | 23.7 ms: 1.34x faster                                                 |
| thrift                   | 1.07 ms                                                | 805 us: 1.33x faster                                                  |
| html5lib                 | 88.9 ms                                                | 67.1 ms: 1.33x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 59.9 ms: 1.32x faster                                                 |
| deepcopy                 | 479 us                                                 | 364 us: 1.32x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.8 ms: 1.31x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                                  |
| scimark_fft              | 466 ms                                                 | 359 ms: 1.30x faster                                                  |
| nqueens                  | 106 ms                                                 | 81.8 ms: 1.29x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 51.3 ms: 1.29x faster                                                 |
| 2to3                     | 348 ms                                                 | 271 ms: 1.29x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 65.7 ms: 1.28x faster                                                 |
| sympy_sum                | 196 ms                                                 | 154 ms: 1.27x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 3.28 us: 1.27x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.09 ms: 1.27x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 20.4 ms: 1.27x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 55.0 ms: 1.26x faster                                                 |
| sympy_str                | 346 ms                                                 | 281 ms: 1.23x faster                                                  |
| dask                     | 441 ms                                                 | 368 ms: 1.20x faster                                                  |
| sympy_expand             | 566 ms                                                 | 474 ms: 1.19x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 830 us: 1.19x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.78 sec: 1.18x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 86.2 ms: 1.15x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                 |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                                  |
| json_loads               | 31.2 us                                                | 28.9 us: 1.08x faster                                                 |
| json                     | 5.69 ms                                                | 5.28 ms: 1.08x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 159 ms: 1.06x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.76 sec: 1.03x faster                                                |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.98 us: 1.01x faster                                                 |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 566 ms: 1.01x slower                                                  |
| async_generators         | 444 ms                                                 | 452 ms: 1.02x slower                                                  |
| pickle_list              | 5.08 us                                                | 5.20 us: 1.02x slower                                                 |
| unpickle_list            | 5.20 us                                                | 5.35 us: 1.03x slower                                                 |
| regex_effbot             | 3.63 ms                                                | 3.75 ms: 1.03x slower                                                 |
| flaskblogging            | 8.58 ms                                                | 8.92 ms: 1.04x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 3.81 ms: 1.05x slower                                                 |
| unpickle                 | 14.4 us                                                | 15.4 us: 1.07x slower                                                 |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.79 ms: 1.10x slower                                                 |
| coverage                 | 79.4 ms                                                | 91.1 ms: 1.15x slower                                                 |
| telco                    | 7.27 ms                                                | 8.59 ms: 1.18x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                 |
| pickle_dict              | 29.6 us                                                | 35.7 us: 1.21x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-linux-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.11x