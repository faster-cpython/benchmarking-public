# Results vs. 3.10.4

- fork: python
- ref: v3.13.0rc3
- machine: linux-aarch64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.305x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 303 ms: 1.26x faster                                           |
| chameleon      | 10.8 ms                                                               | 9.05 ms: 1.20x faster                                          |
| docutils       | 3.53 sec                                                              | 2.88 sec: 1.22x faster                                         |
| html5lib       | 86.5 ms                                                               | 64.7 ms: 1.34x faster                                          |
| tornado_http   | 178 ms                                                                | 131 ms: 1.36x faster                                           |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.11 sec: 2.07x faster                                         |
| async_tree_none         | 950 ms                                                                | 489 ms: 1.94x faster                                           |
| async_tree_memoization  | 1.13 sec                                                              | 614 ms: 1.84x faster                                           |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 761 ms: 1.67x faster                                           |
| Geometric mean          | (ref)                                                                 | 1.88x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 114 ms: 1.46x faster                                           |
| float          | 135 ms                                                                | 93.7 ms: 1.44x faster                                          |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.38x faster                                           |
| regex_v8       | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                          |
| regex_dna      | 257 ms                                                                | 252 ms: 1.02x faster                                           |
| regex_effbot   | 4.25 ms                                                               | 4.90 ms: 1.15x slower                                          |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 363 us: 1.46x faster                                           |
| unpickle_pure_python | 366 us                                                                | 256 us: 1.43x faster                                           |
| tomli_loads          | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                         |
| xml_etree_process    | 99.5 ms                                                               | 80.1 ms: 1.24x faster                                          |
| json_dumps           | 16.7 ms                                                               | 13.6 ms: 1.22x faster                                          |
| xml_etree_parse      | 212 ms                                                                | 191 ms: 1.11x faster                                           |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                           |
| xml_etree_iterparse  | 156 ms                                                                | 146 ms: 1.07x faster                                           |
| unpickle_list        | 6.99 us                                                               | 6.92 us: 1.01x faster                                          |
| json_loads           | 30.9 us                                                               | 31.3 us: 1.01x slower                                          |
| pickle_list          | 5.24 us                                                               | 5.36 us: 1.02x slower                                          |
| pickle               | 12.5 us                                                               | 13.5 us: 1.09x slower                                          |
| pickle_dict          | 35.1 us                                                               | 38.1 us: 1.09x slower                                          |
| unpickle             | 17.5 us                                                               | 20.0 us: 1.14x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                          |
| python_startup_no_site | 6.89 ms                                                               | 8.74 ms: 1.27x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.3 ms: 1.43x faster                                          |
| django_template | 53.3 ms                                                               | 41.5 ms: 1.28x faster                                          |
| genshi_text     | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                          |
| genshi_xml      | 69.8 ms                                                               | 61.2 ms: 1.14x faster                                          |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 193 us: 3.42x faster                                           |
| deltablue                | 8.94 ms                                                               | 3.82 ms: 2.34x faster                                          |
| async_tree_io            | 2.28 sec                                                              | 1.11 sec: 2.07x faster                                         |
| bench_mp_pool            | 14.5 ms                                                               | 7.33 ms: 1.98x faster                                          |
| async_tree_none          | 950 ms                                                                | 489 ms: 1.94x faster                                           |
| raytrace                 | 573 ms                                                                | 296 ms: 1.94x faster                                           |
| async_tree_memoization   | 1.13 sec                                                              | 614 ms: 1.84x faster                                           |
| generators               | 68.1 ms                                                               | 37.8 ms: 1.80x faster                                          |
| chaos                    | 121 ms                                                                | 68.4 ms: 1.77x faster                                          |
| richards_super           | 107 ms                                                                | 61.1 ms: 1.76x faster                                          |
| sqlglot_parse            | 2.40 ms                                                               | 1.38 ms: 1.74x faster                                          |
| richards                 | 91.7 ms                                                               | 53.6 ms: 1.71x faster                                          |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 761 ms: 1.67x faster                                           |
| asyncio_tcp              | 944 ms                                                                | 565 ms: 1.67x faster                                           |
| logging_silent           | 222 ns                                                                | 134 ns: 1.66x faster                                           |
| sqlglot_transpile        | 2.84 ms                                                               | 1.72 ms: 1.65x faster                                          |
| crypto_pyaes             | 134 ms                                                                | 81.9 ms: 1.64x faster                                          |
| scimark_lu               | 227 ms                                                                | 140 ms: 1.63x faster                                           |
| comprehensions           | 33.1 us                                                               | 20.4 us: 1.62x faster                                          |
| go                       | 264 ms                                                                | 163 ms: 1.62x faster                                           |
| scimark_sor              | 246 ms                                                                | 159 ms: 1.55x faster                                           |
| hexiom                   | 10.9 ms                                                               | 7.04 ms: 1.55x faster                                          |
| scimark_monte_carlo      | 128 ms                                                                | 82.7 ms: 1.54x faster                                          |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.19 sec: 1.50x faster                                         |
| pickle_pure_python       | 529 us                                                                | 363 us: 1.46x faster                                           |
| nbody                    | 166 ms                                                                | 114 ms: 1.46x faster                                           |
| float                    | 135 ms                                                                | 93.7 ms: 1.44x faster                                          |
| mako                     | 18.9 ms                                                               | 13.3 ms: 1.43x faster                                          |
| unpickle_pure_python     | 366 us                                                                | 256 us: 1.43x faster                                           |
| pylint                   | 485 ms                                                                | 341 ms: 1.42x faster                                           |
| pyflate                  | 795 ms                                                                | 561 ms: 1.42x faster                                           |
| logging_simple           | 9.78 us                                                               | 7.02 us: 1.39x faster                                          |
| logging_format           | 10.6 us                                                               | 7.67 us: 1.38x faster                                          |
| regex_compile            | 177 ms                                                                | 128 ms: 1.38x faster                                           |
| tornado_http             | 178 ms                                                                | 131 ms: 1.36x faster                                           |
| pycparser                | 1.69 sec                                                              | 1.26 sec: 1.35x faster                                         |
| html5lib                 | 86.5 ms                                                               | 64.7 ms: 1.34x faster                                          |
| thrift                   | 1.26 ms                                                               | 947 us: 1.33x faster                                           |
| tomli_loads              | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                         |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.32x faster                                           |
| coroutines               | 37.2 ms                                                               | 28.4 ms: 1.31x faster                                          |
| sympy_sum                | 184 ms                                                                | 142 ms: 1.30x faster                                           |
| django_template          | 53.3 ms                                                               | 41.5 ms: 1.28x faster                                          |
| dask                     | 450 ms                                                                | 350 ms: 1.28x faster                                           |
| sympy_integrate          | 26.5 ms                                                               | 21.0 ms: 1.26x faster                                          |
| genshi_text              | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                          |
| 2to3                     | 381 ms                                                                | 303 ms: 1.26x faster                                           |
| bench_thread_pool        | 1.59 ms                                                               | 1.27 ms: 1.25x faster                                          |
| sympy_str                | 329 ms                                                                | 264 ms: 1.24x faster                                           |
| pprint_pformat           | 2.36 sec                                                              | 1.90 sec: 1.24x faster                                         |
| xml_etree_process        | 99.5 ms                                                               | 80.1 ms: 1.24x faster                                          |
| pprint_safe_repr         | 1.15 sec                                                              | 928 ms: 1.24x faster                                           |
| gunicorn                 | 1.45 ms                                                               | 1.17 ms: 1.24x faster                                          |
| json_dumps               | 16.7 ms                                                               | 13.6 ms: 1.22x faster                                          |
| sqlglot_normalize        | 156 ms                                                                | 128 ms: 1.22x faster                                           |
| docutils                 | 3.53 sec                                                              | 2.88 sec: 1.22x faster                                         |
| fannkuch                 | 546 ms                                                                | 452 ms: 1.21x faster                                           |
| sqlglot_optimize         | 75.4 ms                                                               | 62.9 ms: 1.20x faster                                          |
| chameleon                | 10.8 ms                                                               | 9.05 ms: 1.20x faster                                          |
| aiohttp                  | 1.39 ms                                                               | 1.16 ms: 1.20x faster                                          |
| deepcopy_memo            | 61.7 us                                                               | 51.7 us: 1.19x faster                                          |
| nqueens                  | 117 ms                                                                | 98.6 ms: 1.19x faster                                          |
| sympy_expand             | 543 ms                                                                | 458 ms: 1.19x faster                                           |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.54 ms: 1.17x faster                                          |
| pathlib                  | 26.3 ms                                                               | 22.8 ms: 1.16x faster                                          |
| genshi_xml               | 69.8 ms                                                               | 61.2 ms: 1.14x faster                                          |
| scimark_fft              | 500 ms                                                                | 447 ms: 1.12x faster                                           |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                           |
| deepcopy                 | 511 us                                                                | 459 us: 1.11x faster                                           |
| deepcopy_reduce          | 4.60 us                                                               | 4.14 us: 1.11x faster                                          |
| xml_etree_parse          | 212 ms                                                                | 191 ms: 1.11x faster                                           |
| mdp                      | 3.70 sec                                                              | 3.35 sec: 1.10x faster                                         |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                           |
| xml_etree_iterparse      | 156 ms                                                                | 146 ms: 1.07x faster                                           |
| flaskblogging            | 4.83 ms                                                               | 4.54 ms: 1.07x faster                                          |
| json                     | 5.88 ms                                                               | 5.53 ms: 1.06x faster                                          |
| regex_v8                 | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                          |
| create_gc_cycles         | 2.26 ms                                                               | 2.14 ms: 1.05x faster                                          |
| sqlite_synth             | 4.12 us                                                               | 3.92 us: 1.05x faster                                          |
| regex_dna                | 257 ms                                                                | 252 ms: 1.02x faster                                           |
| unpickle_list            | 6.99 us                                                               | 6.92 us: 1.01x faster                                          |
| json_loads               | 30.9 us                                                               | 31.3 us: 1.01x slower                                          |
| pickle_list              | 5.24 us                                                               | 5.36 us: 1.02x slower                                          |
| pickle                   | 12.5 us                                                               | 13.5 us: 1.09x slower                                          |
| pickle_dict              | 35.1 us                                                               | 38.1 us: 1.09x slower                                          |
| async_generators         | 452 ms                                                                | 492 ms: 1.09x slower                                           |
| gc_traversal             | 4.15 ms                                                               | 4.56 ms: 1.10x slower                                          |
| telco                    | 8.49 ms                                                               | 9.69 ms: 1.14x slower                                          |
| unpickle                 | 17.5 us                                                               | 20.0 us: 1.14x slower                                          |
| regex_effbot             | 4.25 ms                                                               | 4.90 ms: 1.15x slower                                          |
| coverage                 | 83.6 ms                                                               | 98.0 ms: 1.17x slower                                          |
| python_startup           | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                          |
| mypy2                    | 936 ms                                                                | 1.18 sec: 1.26x slower                                         |
| python_startup_no_site   | 6.89 ms                                                               | 8.74 ms: 1.27x slower                                          |
| Geometric mean           | (ref)                                                                 | 1.28x faster                                                   |

Benchmark hidden because not significant (2): pidigits, asyncio_websockets
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: dulwich_log, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241001-3.13.0rc3-fae84c7/bm-20241001-arminc-aarch64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.305x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.14x