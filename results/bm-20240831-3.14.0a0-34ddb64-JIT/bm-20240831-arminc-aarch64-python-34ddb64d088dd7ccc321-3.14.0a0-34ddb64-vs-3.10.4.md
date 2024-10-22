# Results vs. 3.10.4

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-aarch64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.19x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.53 sec                                                              | 3.93 sec: 1.11x slower                                                  |
| html5lib       | 86.5 ms                                                               | 70.5 ms: 1.23x faster                                                   |
| tornado_http   | 178 ms                                                                | 151 ms: 1.18x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 451 ms: 2.10x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 571 ms: 1.98x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.19 sec: 1.92x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 743 ms: 1.71x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.93x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 88.0 ms: 1.53x faster                                                   |
| nbody          | 166 ms                                                                | 116 ms: 1.43x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| regex_dna      | 257 ms                                                                | 246 ms: 1.05x faster                                                    |
| regex_compile  | 177 ms                                                                | 194 ms: 1.10x slower                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.87 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 382 us: 1.39x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 266 us: 1.37x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 79.4 ms: 1.25x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 114 ms: 1.08x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 198 ms: 1.07x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.7 us: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.3 ms: 1.19x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.96 ms: 1.30x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.24x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.1 ms: 1.45x faster                                                   |
| django_template | 53.3 ms                                                               | 51.0 ms: 1.05x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 34.4 ms: 1.02x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 81.1 ms: 1.16x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.07x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 207 us: 3.20x faster                                                    |
| async_tree_none          | 950 ms                                                                | 451 ms: 2.10x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.34 ms: 2.06x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 571 ms: 1.98x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.19 sec: 1.92x faster                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 7.59 ms: 1.92x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 743 ms: 1.71x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.4 us: 1.65x faster                                                   |
| scimark_sor              | 246 ms                                                                | 150 ms: 1.64x faster                                                    |
| raytrace                 | 573 ms                                                                | 353 ms: 1.62x faster                                                    |
| logging_silent           | 222 ns                                                                | 137 ns: 1.62x faster                                                    |
| float                    | 135 ms                                                                | 88.0 ms: 1.53x faster                                                   |
| scimark_lu               | 227 ms                                                                | 149 ms: 1.52x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 89.4 ms: 1.50x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 635 ms: 1.49x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.1 ms: 1.45x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.29 sec: 1.43x faster                                                  |
| nbody                    | 166 ms                                                                | 116 ms: 1.43x faster                                                    |
| richards_super           | 107 ms                                                                | 76.3 ms: 1.41x faster                                                   |
| go                       | 264 ms                                                                | 188 ms: 1.41x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 382 us: 1.39x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 92.2 ms: 1.39x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 266 us: 1.37x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.77 ms: 1.36x faster                                                   |
| richards                 | 91.7 ms                                                               | 67.9 ms: 1.35x faster                                                   |
| comprehensions           | 33.1 us                                                               | 25.0 us: 1.33x faster                                                   |
| thrift                   | 1.26 ms                                                               | 950 us: 1.33x faster                                                    |
| chaos                    | 121 ms                                                                | 91.5 ms: 1.32x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.41 us: 1.32x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.3 ms: 1.31x faster                                                   |
| logging_format           | 10.6 us                                                               | 8.13 us: 1.30x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 2.19 ms: 1.30x faster                                                   |
| spectral_norm            | 186 ms                                                                | 146 ms: 1.28x faster                                                    |
| deepcopy                 | 511 us                                                                | 400 us: 1.28x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| pyflate                  | 795 ms                                                                | 630 ms: 1.26x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 79.4 ms: 1.25x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 70.5 ms: 1.23x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.8 ms: 1.21x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.83 us: 1.20x faster                                                   |
| generators               | 68.1 ms                                                               | 56.9 ms: 1.20x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.19x faster                                                   |
| tornado_http             | 178 ms                                                                | 151 ms: 1.18x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.81 ms: 1.12x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.52 sec: 1.11x faster                                                  |
| scimark_fft              | 500 ms                                                                | 463 ms: 1.08x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 114 ms: 1.08x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.45 sec: 1.07x faster                                                  |
| xml_etree_parse          | 212 ms                                                                | 198 ms: 1.07x faster                                                    |
| fannkuch                 | 546 ms                                                                | 511 ms: 1.07x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 10.3 ms: 1.06x faster                                                   |
| regex_dna                | 257 ms                                                                | 246 ms: 1.05x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| django_template          | 53.3 ms                                                               | 51.0 ms: 1.05x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 151 ms: 1.03x faster                                                    |
| meteor_contest           | 126 ms                                                                | 123 ms: 1.02x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 34.4 ms: 1.02x faster                                                   |
| json                     | 5.88 ms                                                               | 5.76 ms: 1.02x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 663 ms: 1.01x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.36 ms: 1.05x slower                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 79.4 ms: 1.05x slower                                                   |
| json_loads               | 30.9 us                                                               | 32.7 us: 1.06x slower                                                   |
| nqueens                  | 117 ms                                                                | 125 ms: 1.06x slower                                                    |
| regex_compile            | 177 ms                                                                | 194 ms: 1.10x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 29.2 ms: 1.10x slower                                                   |
| sympy_str                | 329 ms                                                                | 364 ms: 1.11x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.93 sec: 1.11x slower                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 1.28 sec: 1.12x slower                                                  |
| pprint_pformat           | 2.36 sec                                                              | 2.64 sec: 1.12x slower                                                  |
| async_generators         | 452 ms                                                                | 507 ms: 1.12x slower                                                    |
| sympy_expand             | 543 ms                                                                | 619 ms: 1.14x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.87 ms: 1.15x slower                                                   |
| dulwich_log              | 73.5 ms                                                               | 85.3 ms: 1.16x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 81.1 ms: 1.16x slower                                                   |
| sympy_sum                | 184 ms                                                                | 215 ms: 1.17x slower                                                    |
| python_startup           | 11.2 ms                                                               | 13.3 ms: 1.19x slower                                                   |
| coverage                 | 83.6 ms                                                               | 99.6 ms: 1.19x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.00 ms: 1.20x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.4 ms: 1.22x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.96 ms: 1.30x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                            |

Benchmark hidden because not significant (3): pidigits, 2to3, pylint
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.27x