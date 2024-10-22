# Results vs. 3.10.4

- fork: mdboom
- ref: accelerate_DJBX33A_m
- machine: linux-aarch64
- commit hash: 04d5e93
- commit date: 2024-08-27
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 294 ms: 1.29x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.07 sec: 1.15x faster                                                  |
| html5lib       | 86.5 ms                                                               | 64.7 ms: 1.34x faster                                                   |
| tornado_http   | 178 ms                                                                | 127 ms: 1.41x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 426 ms: 2.23x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 556 ms: 2.04x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.13 sec: 2.02x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 727 ms: 1.75x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.00x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 109 ms: 1.52x faster                                                    |
| float          | 135 ms                                                                | 92.6 ms: 1.45x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.42x faster                                                    |
| regex_dna      | 257 ms                                                                | 245 ms: 1.05x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.81 ms: 1.13x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 357 us: 1.48x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 252 us: 1.45x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.55 sec: 1.32x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 77.5 ms: 1.28x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.08x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 146 ms: 1.07x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.2 us: 1.04x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.21x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.79 ms: 1.28x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.4 ms: 1.28x faster                                                   |
| django_template | 53.3 ms                                                               | 42.0 ms: 1.27x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 59.1 ms: 1.18x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 191 us: 3.46x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.92 ms: 2.28x faster                                                   |
| async_tree_none          | 950 ms                                                                | 426 ms: 2.23x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 6.98 ms: 2.08x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 556 ms: 2.04x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.13 sec: 2.02x faster                                                  |
| generators               | 68.1 ms                                                               | 35.1 ms: 1.94x faster                                                   |
| raytrace                 | 573 ms                                                                | 300 ms: 1.91x faster                                                    |
| richards_super           | 107 ms                                                                | 59.6 ms: 1.80x faster                                                   |
| chaos                    | 121 ms                                                                | 68.4 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 727 ms: 1.75x faster                                                    |
| richards                 | 91.7 ms                                                               | 53.1 ms: 1.73x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.40 ms: 1.72x faster                                                   |
| scimark_lu               | 227 ms                                                                | 134 ms: 1.69x faster                                                    |
| logging_silent           | 222 ns                                                                | 132 ns: 1.69x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.70 ms: 1.67x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 37.6 us: 1.64x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.3 us: 1.63x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 82.3 ms: 1.63x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 583 ms: 1.62x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 81.2 ms: 1.57x faster                                                   |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.56x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.00 ms: 1.56x faster                                                   |
| deepcopy                 | 511 us                                                                | 329 us: 1.55x faster                                                    |
| nbody                    | 166 ms                                                                | 109 ms: 1.52x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 357 us: 1.48x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.25 sec: 1.46x faster                                                  |
| float                    | 135 ms                                                                | 92.6 ms: 1.45x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 252 us: 1.45x faster                                                    |
| regex_compile            | 177 ms                                                                | 125 ms: 1.42x faster                                                    |
| logging_simple           | 9.78 us                                                               | 6.93 us: 1.41x faster                                                   |
| tornado_http             | 178 ms                                                                | 127 ms: 1.41x faster                                                    |
| go                       | 264 ms                                                                | 190 ms: 1.39x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.69 us: 1.38x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.38x faster                                                  |
| pyflate                  | 795 ms                                                                | 579 ms: 1.37x faster                                                    |
| thrift                   | 1.26 ms                                                               | 928 us: 1.36x faster                                                    |
| pylint                   | 485 ms                                                                | 359 ms: 1.35x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 64.7 ms: 1.34x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.45 us: 1.33x faster                                                   |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.32x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.55 sec: 1.32x faster                                                  |
| sympy_sum                | 184 ms                                                                | 141 ms: 1.31x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.5 ms: 1.30x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.22 ms: 1.30x faster                                                   |
| 2to3                     | 381 ms                                                                | 294 ms: 1.29x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.6 ms: 1.29x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.4 ms: 1.28x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 77.5 ms: 1.28x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 898 ms: 1.28x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.85 sec: 1.27x faster                                                  |
| django_template          | 53.3 ms                                                               | 42.0 ms: 1.27x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                   |
| sympy_str                | 329 ms                                                                | 262 ms: 1.26x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 61.0 ms: 1.24x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.3 ms: 1.23x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 128 ms: 1.22x faster                                                    |
| nqueens                  | 117 ms                                                                | 97.9 ms: 1.20x faster                                                   |
| sympy_expand             | 543 ms                                                                | 453 ms: 1.20x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.41 ms: 1.19x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 59.1 ms: 1.18x faster                                                   |
| fannkuch                 | 546 ms                                                                | 467 ms: 1.17x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.07 sec: 1.15x faster                                                  |
| scimark_fft              | 500 ms                                                                | 440 ms: 1.14x faster                                                    |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.13x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.33 sec: 1.11x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.08x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 146 ms: 1.07x faster                                                    |
| regex_dna                | 257 ms                                                                | 245 ms: 1.05x faster                                                    |
| json                     | 5.88 ms                                                               | 5.59 ms: 1.05x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.31 ms: 1.02x slower                                                   |
| json_loads               | 30.9 us                                                               | 32.2 us: 1.04x slower                                                   |
| async_generators         | 452 ms                                                                | 485 ms: 1.07x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.81 ms: 1.13x slower                                                   |
| coverage                 | 83.6 ms                                                               | 96.9 ms: 1.16x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.0 ms: 1.18x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 4.98 ms: 1.20x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.79 ms: 1.28x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.35x faster                                                            |

Benchmark hidden because not significant (2): pidigits, asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240827-3.14.0a0-04d5e93/bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.15x