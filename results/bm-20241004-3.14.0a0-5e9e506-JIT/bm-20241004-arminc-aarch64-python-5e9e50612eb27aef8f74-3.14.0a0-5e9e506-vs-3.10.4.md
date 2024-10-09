# Results vs. 3.10.4

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: linux-aarch64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.11x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 385 ms: 1.01x slower                                                    |
| docutils       | 3.53 sec                                                              | 3.72 sec: 1.05x slower                                                  |
| html5lib       | 86.5 ms                                                               | 71.9 ms: 1.20x faster                                                   |
| tornado_http   | 178 ms                                                                | 145 ms: 1.23x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 444 ms: 2.14x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.15 sec: 1.99x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 588 ms: 1.93x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 763 ms: 1.67x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.92x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 89.8 ms: 1.50x faster                                                   |
| nbody          | 166 ms                                                                | 111 ms: 1.49x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 31.4 ms: 1.02x faster                                                   |
| regex_dna      | 257 ms                                                                | 253 ms: 1.02x faster                                                    |
| regex_compile  | 177 ms                                                                | 185 ms: 1.05x slower                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.91 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 264 us: 1.38x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 397 us: 1.33x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 13.1 ms: 1.27x faster                                                   |
| tomli_loads          | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 82.5 ms: 1.21x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 187 ms: 1.14x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.33 us: 1.10x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.05x faster                                                    |
| pickle_list          | 5.24 us                                                               | 5.21 us: 1.01x faster                                                   |
| pickle_dict          | 35.1 us                                                               | 37.8 us: 1.08x slower                                                   |
| pickle               | 12.5 us                                                               | 13.7 us: 1.09x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.2 us: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                            |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.73 ms: 1.27x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.21x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.0 ms: 1.45x faster                                                   |
| django_template | 53.3 ms                                                               | 51.0 ms: 1.05x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 84.1 ms: 1.20x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.06x faster                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 208 us: 3.17x faster                                                    |
| async_tree_none          | 950 ms                                                                | 444 ms: 2.14x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.35 ms: 2.06x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.15 sec: 1.99x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 588 ms: 1.93x faster                                                    |
| logging_silent           | 222 ns                                                                | 131 ns: 1.70x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 763 ms: 1.67x faster                                                    |
| raytrace                 | 573 ms                                                                | 349 ms: 1.64x faster                                                    |
| scimark_sor              | 246 ms                                                                | 152 ms: 1.62x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 38.3 us: 1.61x faster                                                   |
| scimark_lu               | 227 ms                                                                | 150 ms: 1.51x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 628 ms: 1.50x faster                                                    |
| float                    | 135 ms                                                                | 89.8 ms: 1.50x faster                                                   |
| richards_super           | 107 ms                                                                | 71.8 ms: 1.49x faster                                                   |
| nbody                    | 166 ms                                                                | 111 ms: 1.49x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 90.1 ms: 1.49x faster                                                   |
| mako                     | 18.9 ms                                                               | 13.0 ms: 1.45x faster                                                   |
| richards                 | 91.7 ms                                                               | 64.1 ms: 1.43x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.29 sec: 1.43x faster                                                  |
| go                       | 264 ms                                                                | 186 ms: 1.42x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 89.9 ms: 1.42x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.71 ms: 1.40x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 264 us: 1.38x faster                                                    |
| chaos                    | 121 ms                                                                | 88.8 ms: 1.36x faster                                                   |
| comprehensions           | 33.1 us                                                               | 24.5 us: 1.35x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 397 us: 1.33x faster                                                    |
| thrift                   | 1.26 ms                                                               | 966 us: 1.30x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.51 us: 1.30x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.6 ms: 1.30x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 2.20 ms: 1.29x faster                                                   |
| logging_format           | 10.6 us                                                               | 8.27 us: 1.28x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.1 ms: 1.27x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| spectral_norm            | 186 ms                                                                | 147 ms: 1.27x faster                                                    |
| deepcopy                 | 511 us                                                                | 402 us: 1.27x faster                                                    |
| pyflate                  | 795 ms                                                                | 638 ms: 1.25x faster                                                    |
| tornado_http             | 178 ms                                                                | 145 ms: 1.23x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 82.5 ms: 1.21x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.9 ms: 1.20x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 71.9 ms: 1.20x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.37 ms: 1.16x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 4.01 us: 1.15x faster                                                   |
| generators               | 68.1 ms                                                               | 59.5 ms: 1.14x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.49 sec: 1.14x faster                                                  |
| xml_etree_parse          | 212 ms                                                                | 187 ms: 1.14x faster                                                    |
| scimark_fft              | 500 ms                                                                | 449 ms: 1.11x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.33 us: 1.10x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.91 ms: 1.10x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.78 us: 1.09x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 10.1 ms: 1.08x faster                                                   |
| fannkuch                 | 546 ms                                                                | 505 ms: 1.08x faster                                                    |
| json                     | 5.88 ms                                                               | 5.50 ms: 1.07x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.48 sec: 1.06x faster                                                  |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.05x faster                                                    |
| django_template          | 53.3 ms                                                               | 51.0 ms: 1.05x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 31.4 ms: 1.02x faster                                                   |
| meteor_contest           | 126 ms                                                                | 124 ms: 1.02x faster                                                    |
| regex_dna                | 257 ms                                                                | 253 ms: 1.02x faster                                                    |
| pickle_list              | 5.24 us                                                               | 5.21 us: 1.01x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 663 ms: 1.01x slower                                                    |
| 2to3                     | 381 ms                                                                | 385 ms: 1.01x slower                                                    |
| regex_compile            | 177 ms                                                                | 185 ms: 1.05x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.72 sec: 1.05x slower                                                  |
| nqueens                  | 117 ms                                                                | 125 ms: 1.07x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 37.8 us: 1.08x slower                                                   |
| sympy_expand             | 543 ms                                                                | 587 ms: 1.08x slower                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.25 sec: 1.09x slower                                                  |
| sqlglot_optimize         | 75.4 ms                                                               | 82.1 ms: 1.09x slower                                                   |
| pickle                   | 12.5 us                                                               | 13.7 us: 1.09x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.2 us: 1.10x slower                                                   |
| dulwich_log              | 73.5 ms                                                               | 80.8 ms: 1.10x slower                                                   |
| sympy_integrate          | 26.5 ms                                                               | 29.2 ms: 1.10x slower                                                   |
| sympy_str                | 329 ms                                                                | 363 ms: 1.10x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.61 sec: 1.10x slower                                                  |
| telco                    | 8.49 ms                                                               | 9.41 ms: 1.11x slower                                                   |
| async_generators         | 452 ms                                                                | 507 ms: 1.12x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.91 ms: 1.16x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| coverage                 | 83.6 ms                                                               | 97.8 ms: 1.17x slower                                                   |
| sympy_sum                | 184 ms                                                                | 215 ms: 1.17x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 84.1 ms: 1.20x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.02 ms: 1.21x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.73 ms: 1.27x slower                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 2.04 sec: 140.58x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.11x faster                                                            |

Benchmark hidden because not significant (6): genshi_text, pidigits, sqlglot_normalize, pylint, json_loads, create_gc_cycles
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.21x