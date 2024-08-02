# Results vs. 3.10.4

- fork: python
- ref: e83ce850f433fd8bbf8f
- machine: linux-aarch64
- commit hash: e83ce85
- commit date: 2024-06-05
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 356 ms: 1.07x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.50 sec: 1.01x faster                                                  |
| html5lib       | 86.5 ms                                                               | 72.2 ms: 1.20x faster                                                   |
| tornado_http   | 178 ms                                                                | 138 ms: 1.29x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 504 ms: 1.89x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.25 sec: 1.82x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 663 ms: 1.71x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 811 ms: 1.57x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.74x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 90.4 ms: 1.49x faster                                                   |
| nbody          | 166 ms                                                                | 115 ms: 1.44x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.1 ms: 1.07x faster                                                   |
| regex_dna      | 257 ms                                                                | 250 ms: 1.03x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.87 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 277 us: 1.32x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 413 us: 1.28x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.1 ms: 1.27x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 79.7 ms: 1.25x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 115 ms: 1.07x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.63 us: 1.05x faster                                                   |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| pickle_list          | 5.24 us                                                               | 5.27 us: 1.01x slower                                                   |
| json_loads           | 30.9 us                                                               | 32.1 us: 1.04x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 37.8 us: 1.08x slower                                                   |
| pickle               | 12.5 us                                                               | 13.7 us: 1.10x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.4 us: 1.11x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 15.2 ms: 1.35x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 11.0 ms: 1.60x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.47x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.0 ms: 1.46x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 33.8 ms: 1.04x faster                                                   |
| django_template | 53.3 ms                                                               | 51.2 ms: 1.04x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 83.0 ms: 1.19x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.07x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 207 us: 3.19x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.60 ms: 1.94x faster                                                   |
| async_tree_none          | 950 ms                                                                | 504 ms: 1.89x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.25 sec: 1.82x faster                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 8.23 ms: 1.77x faster                                                   |
| generators               | 68.1 ms                                                               | 38.6 ms: 1.76x faster                                                   |
| raytrace                 | 573 ms                                                                | 326 ms: 1.76x faster                                                    |
| richards_super           | 107 ms                                                                | 62.4 ms: 1.72x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 663 ms: 1.71x faster                                                    |
| richards                 | 91.7 ms                                                               | 56.7 ms: 1.62x faster                                                   |
| logging_silent           | 222 ns                                                                | 138 ns: 1.61x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 811 ms: 1.57x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 614 ms: 1.54x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.59 ms: 1.51x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 89.1 ms: 1.50x faster                                                   |
| float                    | 135 ms                                                                | 90.4 ms: 1.49x faster                                                   |
| go                       | 264 ms                                                                | 179 ms: 1.48x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.23 sec: 1.47x faster                                                  |
| mako                     | 18.9 ms                                                               | 13.0 ms: 1.46x faster                                                   |
| nbody                    | 166 ms                                                                | 115 ms: 1.44x faster                                                    |
| comprehensions           | 33.1 us                                                               | 23.4 us: 1.41x faster                                                   |
| scimark_sor              | 246 ms                                                                | 175 ms: 1.41x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 2.02 ms: 1.41x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 91.3 ms: 1.40x faster                                                   |
| chaos                    | 121 ms                                                                | 90.4 ms: 1.34x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.38 us: 1.32x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 277 us: 1.32x faster                                                    |
| pyflate                  | 795 ms                                                                | 603 ms: 1.32x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.09 us: 1.31x faster                                                   |
| thrift                   | 1.26 ms                                                               | 964 us: 1.31x faster                                                    |
| tornado_http             | 178 ms                                                                | 138 ms: 1.29x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.9 ms: 1.29x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 413 us: 1.28x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| json_dumps               | 16.7 ms                                                               | 13.1 ms: 1.27x faster                                                   |
| spectral_norm            | 186 ms                                                                | 149 ms: 1.25x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 79.7 ms: 1.25x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.36 sec: 1.25x faster                                                  |
| deepcopy_memo            | 61.7 us                                                               | 49.9 us: 1.24x faster                                                   |
| scimark_lu               | 227 ms                                                                | 184 ms: 1.24x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 8.99 ms: 1.21x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.9 ms: 1.20x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 72.2 ms: 1.20x faster                                                   |
| pylint                   | 485 ms                                                                | 408 ms: 1.19x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.34 ms: 1.19x faster                                                   |
| fannkuch                 | 546 ms                                                                | 468 ms: 1.17x faster                                                    |
| dask                     | 450 ms                                                                | 397 ms: 1.13x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.90 ms: 1.10x faster                                                   |
| scimark_fft              | 500 ms                                                                | 459 ms: 1.09x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 144 ms: 1.09x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.41 sec: 1.08x faster                                                  |
| meteor_contest           | 126 ms                                                                | 117 ms: 1.08x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 70.0 ms: 1.08x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 30.1 ms: 1.07x faster                                                   |
| 2to3                     | 381 ms                                                                | 356 ms: 1.07x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 115 ms: 1.07x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.90 us: 1.06x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.63 us: 1.05x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 33.8 ms: 1.04x faster                                                   |
| django_template          | 53.3 ms                                                               | 51.2 ms: 1.04x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 71.2 ms: 1.03x faster                                                   |
| deepcopy                 | 511 us                                                                | 494 us: 1.03x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 25.8 ms: 1.03x faster                                                   |
| json                     | 5.88 ms                                                               | 5.71 ms: 1.03x faster                                                   |
| regex_dna                | 257 ms                                                                | 250 ms: 1.03x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.12 sec: 1.03x faster                                                  |
| sympy_str                | 329 ms                                                                | 322 ms: 1.02x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.32 sec: 1.02x faster                                                  |
| docutils                 | 3.53 sec                                                              | 3.50 sec: 1.01x faster                                                  |
| pickle_list              | 5.24 us                                                               | 5.27 us: 1.01x slower                                                   |
| sympy_expand             | 543 ms                                                                | 546 ms: 1.01x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 661 ms: 1.01x slower                                                    |
| nqueens                  | 117 ms                                                                | 118 ms: 1.01x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.1 us: 1.04x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.35 ms: 1.04x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 37.8 us: 1.08x slower                                                   |
| pickle                   | 12.5 us                                                               | 13.7 us: 1.10x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.4 us: 1.11x slower                                                   |
| async_generators         | 452 ms                                                                | 516 ms: 1.14x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.87 ms: 1.15x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 83.0 ms: 1.19x slower                                                   |
| coverage                 | 83.6 ms                                                               | 100 ms: 1.20x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.07 ms: 1.22x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.4 ms: 1.22x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.2 ms: 1.35x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 11.0 ms: 1.60x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                            |

Benchmark hidden because not significant (4): regex_compile, pidigits, deepcopy_reduce, sympy_sum
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240605-3.14.0a0-e83ce85-JIT/bm-20240605-arminc-aarch64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.25x