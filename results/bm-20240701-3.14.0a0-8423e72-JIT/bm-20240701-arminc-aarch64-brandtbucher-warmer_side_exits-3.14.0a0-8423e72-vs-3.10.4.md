# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmer_side_exits
- machine: linux-aarch64
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 363 ms: 1.05x faster                                                       |
| html5lib       | 86.5 ms                                                               | 69.4 ms: 1.25x faster                                                      |
| tornado_http   | 178 ms                                                                | 135 ms: 1.32x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.07 sec: 2.14x faster                                                     |
| async_tree_none         | 950 ms                                                                | 448 ms: 2.12x faster                                                       |
| async_tree_memoization  | 1.13 sec                                                              | 582 ms: 1.95x faster                                                       |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 740 ms: 1.72x faster                                                       |
| Geometric mean          | (ref)                                                                 | 1.97x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 90.1 ms: 1.49x faster                                                      |
| nbody          | 166 ms                                                                | 115 ms: 1.44x faster                                                       |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.8 ms: 1.04x faster                                                      |
| regex_compile  | 177 ms                                                                | 173 ms: 1.02x faster                                                       |
| regex_effbot   | 4.25 ms                                                               | 4.99 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 261 us: 1.40x faster                                                       |
| pickle_pure_python   | 529 us                                                                | 393 us: 1.35x faster                                                       |
| tomli_loads          | 3.36 sec                                                              | 2.58 sec: 1.30x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                                      |
| xml_etree_process    | 99.5 ms                                                               | 80.1 ms: 1.24x faster                                                      |
| xml_etree_parse      | 212 ms                                                                | 192 ms: 1.11x faster                                                       |
| xml_etree_generate   | 123 ms                                                                | 116 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.05x faster                                                       |
| json_loads           | 30.9 us                                                               | 32.9 us: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                      |
| python_startup_no_site | 6.89 ms                                                               | 8.85 ms: 1.28x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.23x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.0 ms: 1.46x faster                                                      |
| genshi_text     | 35.2 ms                                                               | 32.6 ms: 1.08x faster                                                      |
| django_template | 53.3 ms                                                               | 50.0 ms: 1.07x faster                                                      |
| genshi_xml      | 69.8 ms                                                               | 75.7 ms: 1.08x slower                                                      |
| Geometric mean  | (ref)                                                                 | 1.12x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 208 us: 3.18x faster                                                       |
| async_tree_io            | 2.28 sec                                                              | 1.07 sec: 2.14x faster                                                     |
| async_tree_none          | 950 ms                                                                | 448 ms: 2.12x faster                                                       |
| async_tree_memoization   | 1.13 sec                                                              | 582 ms: 1.95x faster                                                       |
| deltablue                | 8.94 ms                                                               | 4.70 ms: 1.90x faster                                                      |
| richards_super           | 107 ms                                                                | 58.7 ms: 1.83x faster                                                      |
| richards                 | 91.7 ms                                                               | 51.4 ms: 1.78x faster                                                      |
| raytrace                 | 573 ms                                                                | 324 ms: 1.77x faster                                                       |
| bench_mp_pool            | 14.5 ms                                                               | 8.33 ms: 1.74x faster                                                      |
| generators               | 68.1 ms                                                               | 39.2 ms: 1.74x faster                                                      |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 740 ms: 1.72x faster                                                       |
| logging_silent           | 222 ns                                                                | 137 ns: 1.63x faster                                                       |
| deepcopy_memo            | 61.7 us                                                               | 38.4 us: 1.61x faster                                                      |
| crypto_pyaes             | 134 ms                                                                | 86.5 ms: 1.55x faster                                                      |
| asyncio_tcp              | 944 ms                                                                | 610 ms: 1.55x faster                                                       |
| sqlglot_parse            | 2.40 ms                                                               | 1.59 ms: 1.51x faster                                                      |
| float                    | 135 ms                                                                | 90.1 ms: 1.49x faster                                                      |
| scimark_monte_carlo      | 128 ms                                                                | 85.8 ms: 1.49x faster                                                      |
| go                       | 264 ms                                                                | 178 ms: 1.48x faster                                                       |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.25 sec: 1.46x faster                                                     |
| mako                     | 18.9 ms                                                               | 13.0 ms: 1.46x faster                                                      |
| nbody                    | 166 ms                                                                | 115 ms: 1.44x faster                                                       |
| sqlglot_transpile        | 2.84 ms                                                               | 2.00 ms: 1.42x faster                                                      |
| comprehensions           | 33.1 us                                                               | 23.4 us: 1.42x faster                                                      |
| scimark_sor              | 246 ms                                                                | 175 ms: 1.40x faster                                                       |
| unpickle_pure_python     | 366 us                                                                | 261 us: 1.40x faster                                                       |
| chaos                    | 121 ms                                                                | 87.0 ms: 1.39x faster                                                      |
| deepcopy                 | 511 us                                                                | 377 us: 1.35x faster                                                       |
| logging_simple           | 9.78 us                                                               | 7.24 us: 1.35x faster                                                      |
| pickle_pure_python       | 529 us                                                                | 393 us: 1.35x faster                                                       |
| logging_format           | 10.6 us                                                               | 7.94 us: 1.34x faster                                                      |
| tornado_http             | 178 ms                                                                | 135 ms: 1.32x faster                                                       |
| thrift                   | 1.26 ms                                                               | 966 us: 1.30x faster                                                       |
| tomli_loads              | 3.36 sec                                                              | 2.58 sec: 1.30x faster                                                     |
| pyflate                  | 795 ms                                                                | 612 ms: 1.30x faster                                                       |
| spectral_norm            | 186 ms                                                                | 147 ms: 1.27x faster                                                       |
| pycparser                | 1.69 sec                                                              | 1.34 sec: 1.26x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                                      |
| html5lib                 | 86.5 ms                                                               | 69.4 ms: 1.25x faster                                                      |
| coroutines               | 37.2 ms                                                               | 29.9 ms: 1.24x faster                                                      |
| xml_etree_process        | 99.5 ms                                                               | 80.1 ms: 1.24x faster                                                      |
| scimark_lu               | 227 ms                                                                | 184 ms: 1.23x faster                                                       |
| bench_thread_pool        | 1.59 ms                                                               | 1.32 ms: 1.20x faster                                                      |
| pathlib                  | 26.3 ms                                                               | 21.9 ms: 1.20x faster                                                      |
| hexiom                   | 10.9 ms                                                               | 9.17 ms: 1.19x faster                                                      |
| fannkuch                 | 546 ms                                                                | 468 ms: 1.17x faster                                                       |
| pylint                   | 485 ms                                                                | 418 ms: 1.16x faster                                                       |
| dask                     | 450 ms                                                                | 392 ms: 1.15x faster                                                       |
| xml_etree_parse          | 212 ms                                                                | 192 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.91 ms: 1.10x faster                                                      |
| meteor_contest           | 126 ms                                                                | 115 ms: 1.10x faster                                                       |
| sqlglot_normalize        | 156 ms                                                                | 142 ms: 1.10x faster                                                       |
| deepcopy_reduce          | 4.60 us                                                               | 4.19 us: 1.10x faster                                                      |
| sqlglot_optimize         | 75.4 ms                                                               | 69.2 ms: 1.09x faster                                                      |
| scimark_fft              | 500 ms                                                                | 462 ms: 1.08x faster                                                       |
| genshi_text              | 35.2 ms                                                               | 32.6 ms: 1.08x faster                                                      |
| django_template          | 53.3 ms                                                               | 50.0 ms: 1.07x faster                                                      |
| mdp                      | 3.70 sec                                                              | 3.46 sec: 1.07x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 116 ms: 1.06x faster                                                       |
| 2to3                     | 381 ms                                                                | 363 ms: 1.05x faster                                                       |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.05x faster                                                       |
| regex_v8                 | 32.2 ms                                                               | 30.8 ms: 1.04x faster                                                      |
| dulwich_log              | 73.5 ms                                                               | 70.6 ms: 1.04x faster                                                      |
| pprint_safe_repr         | 1.15 sec                                                              | 1.11 sec: 1.03x faster                                                     |
| json                     | 5.88 ms                                                               | 5.72 ms: 1.03x faster                                                      |
| regex_compile            | 177 ms                                                                | 173 ms: 1.02x faster                                                       |
| pprint_pformat           | 2.36 sec                                                              | 2.32 sec: 1.02x faster                                                     |
| sympy_str                | 329 ms                                                                | 324 ms: 1.02x faster                                                       |
| sympy_integrate          | 26.5 ms                                                               | 26.2 ms: 1.01x faster                                                      |
| nqueens                  | 117 ms                                                                | 118 ms: 1.01x slower                                                       |
| asyncio_websockets       | 657 ms                                                                | 662 ms: 1.01x slower                                                       |
| create_gc_cycles         | 2.26 ms                                                               | 2.34 ms: 1.04x slower                                                      |
| json_loads               | 30.9 us                                                               | 32.9 us: 1.06x slower                                                      |
| genshi_xml               | 69.8 ms                                                               | 75.7 ms: 1.08x slower                                                      |
| async_generators         | 452 ms                                                                | 515 ms: 1.14x slower                                                       |
| python_startup           | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                      |
| regex_effbot             | 4.25 ms                                                               | 4.99 ms: 1.18x slower                                                      |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                                       |
| gc_traversal             | 4.15 ms                                                               | 5.06 ms: 1.22x slower                                                      |
| telco                    | 8.49 ms                                                               | 10.4 ms: 1.22x slower                                                      |
| python_startup_no_site   | 6.89 ms                                                               | 8.85 ms: 1.28x slower                                                      |
| Geometric mean           | (ref)                                                                 | 1.24x faster                                                               |

Benchmark hidden because not significant (5): pidigits, regex_dna, sympy_sum, docutils, sympy_expand
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240701-3.14.0a0-8423e72-JIT/bm-20240701-arminc-aarch64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.25x