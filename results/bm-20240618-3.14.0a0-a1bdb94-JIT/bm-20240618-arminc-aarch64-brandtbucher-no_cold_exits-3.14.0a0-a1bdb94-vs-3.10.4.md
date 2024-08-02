# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-aarch64
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 360 ms: 1.06x faster                                                   |
| docutils       | 3.53 sec                                                              | 3.56 sec: 1.01x slower                                                 |
| html5lib       | 86.5 ms                                                               | 73.3 ms: 1.18x faster                                                  |
| tornado_http   | 178 ms                                                                | 141 ms: 1.27x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 506 ms: 1.88x faster                                                   |
| async_tree_io           | 2.28 sec                                                              | 1.25 sec: 1.83x faster                                                 |
| async_tree_memoization  | 1.13 sec                                                              | 667 ms: 1.70x faster                                                   |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 811 ms: 1.57x faster                                                   |
| Geometric mean          | (ref)                                                                 | 1.74x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 90.5 ms: 1.49x faster                                                  |
| nbody          | 166 ms                                                                | 116 ms: 1.43x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.5 ms: 1.05x faster                                                  |
| regex_dna      | 257 ms                                                                | 252 ms: 1.02x faster                                                   |
| regex_compile  | 177 ms                                                                | 175 ms: 1.01x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.90 ms: 1.15x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 393 us: 1.35x faster                                                   |
| unpickle_pure_python | 366 us                                                                | 278 us: 1.31x faster                                                   |
| tomli_loads          | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                 |
| json_dumps           | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 79.2 ms: 1.26x faster                                                  |
| xml_etree_parse      | 212 ms                                                                | 190 ms: 1.11x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                   |
| unpickle_list        | 6.99 us                                                               | 6.61 us: 1.06x faster                                                  |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.06x faster                                                   |
| json_loads           | 30.9 us                                                               | 32.8 us: 1.06x slower                                                  |
| pickle_dict          | 35.1 us                                                               | 37.3 us: 1.06x slower                                                  |
| pickle               | 12.5 us                                                               | 13.6 us: 1.09x slower                                                  |
| unpickle             | 17.5 us                                                               | 19.7 us: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.09x faster                                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                  |
| python_startup_no_site | 6.89 ms                                                               | 8.79 ms: 1.28x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                  |
| django_template | 53.3 ms                                                               | 49.8 ms: 1.07x faster                                                  |
| genshi_xml      | 69.8 ms                                                               | 82.2 ms: 1.18x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.07x faster                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 212 us: 3.12x faster                                                   |
| deltablue                | 8.94 ms                                                               | 4.48 ms: 1.99x faster                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 7.66 ms: 1.90x faster                                                  |
| async_tree_none          | 950 ms                                                                | 506 ms: 1.88x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.25 sec: 1.83x faster                                                 |
| raytrace                 | 573 ms                                                                | 324 ms: 1.77x faster                                                   |
| generators               | 68.1 ms                                                               | 38.8 ms: 1.75x faster                                                  |
| richards_super           | 107 ms                                                                | 61.4 ms: 1.75x faster                                                  |
| richards                 | 91.7 ms                                                               | 53.8 ms: 1.70x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 667 ms: 1.70x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 37.7 us: 1.64x faster                                                  |
| logging_silent           | 222 ns                                                                | 141 ns: 1.58x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 811 ms: 1.57x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 617 ms: 1.53x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 88.0 ms: 1.52x faster                                                  |
| sqlglot_parse            | 2.40 ms                                                               | 1.59 ms: 1.51x faster                                                  |
| float                    | 135 ms                                                                | 90.5 ms: 1.49x faster                                                  |
| go                       | 264 ms                                                                | 178 ms: 1.48x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.26 sec: 1.45x faster                                                 |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                  |
| nbody                    | 166 ms                                                                | 116 ms: 1.43x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 89.2 ms: 1.43x faster                                                  |
| comprehensions           | 33.1 us                                                               | 23.1 us: 1.43x faster                                                  |
| sqlglot_transpile        | 2.84 ms                                                               | 2.01 ms: 1.41x faster                                                  |
| scimark_sor              | 246 ms                                                                | 178 ms: 1.39x faster                                                   |
| chaos                    | 121 ms                                                                | 89.5 ms: 1.35x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 393 us: 1.35x faster                                                   |
| deepcopy                 | 511 us                                                                | 381 us: 1.34x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.32 us: 1.34x faster                                                  |
| logging_format           | 10.6 us                                                               | 8.02 us: 1.32x faster                                                  |
| thrift                   | 1.26 ms                                                               | 958 us: 1.31x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 278 us: 1.31x faster                                                   |
| pyflate                  | 795 ms                                                                | 619 ms: 1.28x faster                                                   |
| coroutines               | 37.2 ms                                                               | 29.1 ms: 1.28x faster                                                  |
| tomli_loads              | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                 |
| spectral_norm            | 186 ms                                                                | 147 ms: 1.27x faster                                                   |
| tornado_http             | 178 ms                                                                | 141 ms: 1.27x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                  |
| xml_etree_process        | 99.5 ms                                                               | 79.2 ms: 1.26x faster                                                  |
| pycparser                | 1.69 sec                                                              | 1.36 sec: 1.24x faster                                                 |
| scimark_lu               | 227 ms                                                                | 183 ms: 1.24x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 8.96 ms: 1.22x faster                                                  |
| pathlib                  | 26.3 ms                                                               | 22.1 ms: 1.19x faster                                                  |
| fannkuch                 | 546 ms                                                                | 459 ms: 1.19x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.34 ms: 1.19x faster                                                  |
| pylint                   | 485 ms                                                                | 410 ms: 1.18x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 73.3 ms: 1.18x faster                                                  |
| dask                     | 450 ms                                                                | 385 ms: 1.17x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 190 ms: 1.11x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.90 ms: 1.11x faster                                                  |
| deepcopy_reduce          | 4.60 us                                                               | 4.21 us: 1.09x faster                                                  |
| sqlglot_optimize         | 75.4 ms                                                               | 69.2 ms: 1.09x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 144 ms: 1.08x faster                                                   |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.08x faster                                                   |
| scimark_fft              | 500 ms                                                                | 463 ms: 1.08x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.44 sec: 1.07x faster                                                 |
| django_template          | 53.3 ms                                                               | 49.8 ms: 1.07x faster                                                  |
| sqlite_synth             | 4.12 us                                                               | 3.87 us: 1.06x faster                                                  |
| 2to3                     | 381 ms                                                                | 360 ms: 1.06x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.61 us: 1.06x faster                                                  |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.06x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 30.5 ms: 1.05x faster                                                  |
| regex_dna                | 257 ms                                                                | 252 ms: 1.02x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.12 sec: 1.02x faster                                                 |
| dulwich_log              | 73.5 ms                                                               | 72.4 ms: 1.02x faster                                                  |
| regex_compile            | 177 ms                                                                | 175 ms: 1.01x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.56 sec: 1.01x slower                                                 |
| nqueens                  | 117 ms                                                                | 119 ms: 1.01x slower                                                   |
| sympy_sum                | 184 ms                                                                | 187 ms: 1.01x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.32 ms: 1.03x slower                                                  |
| json_loads               | 30.9 us                                                               | 32.8 us: 1.06x slower                                                  |
| pickle_dict              | 35.1 us                                                               | 37.3 us: 1.06x slower                                                  |
| pickle                   | 12.5 us                                                               | 13.6 us: 1.09x slower                                                  |
| unpickle                 | 17.5 us                                                               | 19.7 us: 1.13x slower                                                  |
| async_generators         | 452 ms                                                                | 512 ms: 1.13x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.90 ms: 1.15x slower                                                  |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                  |
| gc_traversal             | 4.15 ms                                                               | 4.85 ms: 1.17x slower                                                  |
| genshi_xml               | 69.8 ms                                                               | 82.2 ms: 1.18x slower                                                  |
| telco                    | 8.49 ms                                                               | 10.1 ms: 1.19x slower                                                  |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.79 ms: 1.28x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                           |

Benchmark hidden because not significant (9): sympy_str, pprint_pformat, pidigits, sympy_integrate, genshi_text, sympy_expand, pickle_list, asyncio_websockets, json
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240618-3.14.0a0-a1bdb94-JIT/bm-20240618-arminc-aarch64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.23x