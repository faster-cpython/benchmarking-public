# Results vs. 3.10.4

- fork: colesbury
- ref: gh_100240_freelist
- machine: linux-aarch64
- commit hash: 85453d0
- commit date: 2024-07-17
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 302 ms: 1.26x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.08 sec: 1.15x faster                                                   |
| html5lib       | 86.5 ms                                                               | 66.6 ms: 1.30x faster                                                    |
| tornado_http   | 178 ms                                                                | 126 ms: 1.42x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 439 ms: 2.16x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.08 sec: 2.11x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 550 ms: 2.06x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 724 ms: 1.76x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.02x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 112 ms: 1.49x faster                                                     |
| float          | 135 ms                                                                | 93.0 ms: 1.45x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 129 ms: 1.37x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 31.1 ms: 1.03x faster                                                    |
| regex_dna      | 257 ms                                                                | 250 ms: 1.03x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.87 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 359 us: 1.47x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 252 us: 1.45x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.55 sec: 1.32x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 79.9 ms: 1.25x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.10x faster                                                     |
| xml_etree_parse      | 212 ms                                                                | 196 ms: 1.08x faster                                                     |
| json_loads           | 30.9 us                                                               | 32.3 us: 1.04x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 8.76 ms: 1.27x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.4 ms: 1.42x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.8 ms: 1.26x faster                                                    |
| django_template | 53.3 ms                                                               | 42.8 ms: 1.25x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 200 us: 3.30x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.85 ms: 2.32x faster                                                    |
| async_tree_none          | 950 ms                                                                | 439 ms: 2.16x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.08 sec: 2.11x faster                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 7.01 ms: 2.07x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 550 ms: 2.06x faster                                                     |
| raytrace                 | 573 ms                                                                | 297 ms: 1.93x faster                                                     |
| richards_super           | 107 ms                                                                | 59.0 ms: 1.82x faster                                                    |
| generators               | 68.1 ms                                                               | 37.8 ms: 1.80x faster                                                    |
| chaos                    | 121 ms                                                                | 68.0 ms: 1.78x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 724 ms: 1.76x faster                                                     |
| richards                 | 91.7 ms                                                               | 52.8 ms: 1.74x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.40 ms: 1.71x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 560 ms: 1.68x faster                                                     |
| scimark_lu               | 227 ms                                                                | 136 ms: 1.67x faster                                                     |
| logging_silent           | 222 ns                                                                | 134 ns: 1.66x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 1.72 ms: 1.66x faster                                                    |
| go                       | 264 ms                                                                | 161 ms: 1.65x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 81.6 ms: 1.64x faster                                                    |
| comprehensions           | 33.1 us                                                               | 20.6 us: 1.61x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 38.5 us: 1.60x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.04 ms: 1.55x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 82.4 ms: 1.55x faster                                                    |
| scimark_sor              | 246 ms                                                                | 159 ms: 1.55x faster                                                     |
| deepcopy                 | 511 us                                                                | 331 us: 1.54x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.17 sec: 1.51x faster                                                   |
| nbody                    | 166 ms                                                                | 112 ms: 1.49x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 359 us: 1.47x faster                                                     |
| pylint                   | 485 ms                                                                | 334 ms: 1.45x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 252 us: 1.45x faster                                                     |
| float                    | 135 ms                                                                | 93.0 ms: 1.45x faster                                                    |
| pyflate                  | 795 ms                                                                | 558 ms: 1.42x faster                                                     |
| tornado_http             | 178 ms                                                                | 126 ms: 1.42x faster                                                     |
| mako                     | 18.9 ms                                                               | 13.4 ms: 1.42x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.07 us: 1.38x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.38x faster                                                   |
| regex_compile            | 177 ms                                                                | 129 ms: 1.37x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.76 us: 1.37x faster                                                    |
| spectral_norm            | 186 ms                                                                | 140 ms: 1.33x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.55 sec: 1.32x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.51 us: 1.31x faster                                                    |
| thrift                   | 1.26 ms                                                               | 964 us: 1.31x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 66.6 ms: 1.30x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.8 ms: 1.29x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.23 ms: 1.29x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 21.0 ms: 1.27x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.8 ms: 1.26x faster                                                    |
| 2to3                     | 381 ms                                                                | 302 ms: 1.26x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                                    |
| sympy_sum                | 184 ms                                                                | 147 ms: 1.25x faster                                                     |
| django_template          | 53.3 ms                                                               | 42.8 ms: 1.25x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 79.9 ms: 1.25x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.2 ms: 1.24x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.90 sec: 1.24x faster                                                   |
| sympy_str                | 329 ms                                                                | 266 ms: 1.23x faster                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 931 ms: 1.23x faster                                                     |
| sqlglot_normalize        | 156 ms                                                                | 129 ms: 1.21x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 61.2 ms: 1.20x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.41 ms: 1.19x faster                                                    |
| sympy_expand             | 543 ms                                                                | 457 ms: 1.19x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 63.6 ms: 1.19x faster                                                    |
| fannkuch                 | 546 ms                                                                | 461 ms: 1.18x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.08 sec: 1.15x faster                                                   |
| nqueens                  | 117 ms                                                                | 103 ms: 1.14x faster                                                     |
| scimark_fft              | 500 ms                                                                | 441 ms: 1.13x faster                                                     |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.13x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.31 sec: 1.12x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.10x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 196 ms: 1.08x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 31.1 ms: 1.03x faster                                                    |
| json                     | 5.88 ms                                                               | 5.69 ms: 1.03x faster                                                    |
| regex_dna                | 257 ms                                                                | 250 ms: 1.03x faster                                                     |
| create_gc_cycles         | 2.26 ms                                                               | 2.30 ms: 1.02x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.3 us: 1.04x slower                                                    |
| async_generators         | 452 ms                                                                | 487 ms: 1.08x slower                                                     |
| regex_effbot             | 4.25 ms                                                               | 4.87 ms: 1.15x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.94 ms: 1.17x slower                                                    |
| python_startup           | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 4.93 ms: 1.19x slower                                                    |
| coverage                 | 83.6 ms                                                               | 100.0 ms: 1.20x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.76 ms: 1.27x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.34x faster                                                             |

Benchmark hidden because not significant (3): xml_etree_iterparse, pidigits, asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240717-3.14.0a0-85453d0/bm-20240717-arminc-aarch64-colesbury-gh_100240_freelist-3.14.0a0-85453d0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.14x