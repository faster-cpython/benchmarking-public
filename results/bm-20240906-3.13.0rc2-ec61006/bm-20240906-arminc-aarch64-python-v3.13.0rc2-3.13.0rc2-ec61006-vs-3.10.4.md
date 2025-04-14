# Results vs. 3.10.4

- fork: python
- ref: v3.13.0rc2
- machine: linux-aarch64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.297x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 304 ms: 1.25x faster                                           |
| chameleon      | 10.8 ms                                                               | 8.94 ms: 1.21x faster                                          |
| docutils       | 3.53 sec                                                              | 3.10 sec: 1.14x faster                                         |
| html5lib       | 86.5 ms                                                               | 67.6 ms: 1.28x faster                                          |
| tornado_http   | 178 ms                                                                | 130 ms: 1.37x faster                                           |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 488 ms: 1.95x faster                                           |
| async_tree_io           | 2.28 sec                                                              | 1.20 sec: 1.90x faster                                         |
| async_tree_memoization  | 1.13 sec                                                              | 644 ms: 1.76x faster                                           |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 790 ms: 1.61x faster                                           |
| Geometric mean          | (ref)                                                                 | 1.80x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 135 ms                                                                | 91.5 ms: 1.47x faster                                          |
| nbody          | 166 ms                                                                | 113 ms: 1.46x faster                                           |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.37x faster                                           |
| regex_v8       | 32.2 ms                                                               | 31.1 ms: 1.03x faster                                          |
| regex_dna      | 257 ms                                                                | 252 ms: 1.02x faster                                           |
| regex_effbot   | 4.25 ms                                                               | 4.88 ms: 1.15x slower                                          |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 354 us: 1.49x faster                                           |
| unpickle_pure_python | 366 us                                                                | 251 us: 1.45x faster                                           |
| tomli_loads          | 3.36 sec                                                              | 2.55 sec: 1.32x faster                                         |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                          |
| xml_etree_process    | 99.5 ms                                                               | 79.7 ms: 1.25x faster                                          |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                           |
| xml_etree_parse      | 212 ms                                                                | 195 ms: 1.09x faster                                           |
| unpickle_list        | 6.99 us                                                               | 6.58 us: 1.06x faster                                          |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.05x faster                                           |
| json_loads           | 30.9 us                                                               | 31.4 us: 1.02x slower                                          |
| pickle_list          | 5.24 us                                                               | 5.33 us: 1.02x slower                                          |
| pickle_dict          | 35.1 us                                                               | 37.9 us: 1.08x slower                                          |
| pickle               | 12.5 us                                                               | 13.6 us: 1.09x slower                                          |
| unpickle             | 17.5 us                                                               | 20.3 us: 1.16x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                          |
| python_startup_no_site | 6.89 ms                                                               | 8.63 ms: 1.25x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.21x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                          |
| genshi_text     | 35.2 ms                                                               | 27.8 ms: 1.27x faster                                          |
| django_template | 53.3 ms                                                               | 42.6 ms: 1.25x faster                                          |
| genshi_xml      | 69.8 ms                                                               | 61.1 ms: 1.14x faster                                          |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 193 us: 3.43x faster                                           |
| deltablue                | 8.94 ms                                                               | 3.86 ms: 2.32x faster                                          |
| async_tree_none          | 950 ms                                                                | 488 ms: 1.95x faster                                           |
| raytrace                 | 573 ms                                                                | 300 ms: 1.91x faster                                           |
| async_tree_io            | 2.28 sec                                                              | 1.20 sec: 1.90x faster                                         |
| bench_mp_pool            | 14.5 ms                                                               | 7.75 ms: 1.88x faster                                          |
| richards_super           | 107 ms                                                                | 59.5 ms: 1.80x faster                                          |
| generators               | 68.1 ms                                                               | 38.0 ms: 1.79x faster                                          |
| chaos                    | 121 ms                                                                | 68.4 ms: 1.77x faster                                          |
| async_tree_memoization   | 1.13 sec                                                              | 644 ms: 1.76x faster                                           |
| richards                 | 91.7 ms                                                               | 52.9 ms: 1.73x faster                                          |
| sqlglot_parse            | 2.40 ms                                                               | 1.42 ms: 1.69x faster                                          |
| sqlglot_transpile        | 2.84 ms                                                               | 1.72 ms: 1.65x faster                                          |
| go                       | 264 ms                                                                | 161 ms: 1.65x faster                                           |
| crypto_pyaes             | 134 ms                                                                | 82.2 ms: 1.63x faster                                          |
| comprehensions           | 33.1 us                                                               | 20.4 us: 1.62x faster                                          |
| scimark_lu               | 227 ms                                                                | 140 ms: 1.62x faster                                           |
| logging_silent           | 222 ns                                                                | 137 ns: 1.62x faster                                           |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 790 ms: 1.61x faster                                           |
| asyncio_tcp              | 944 ms                                                                | 592 ms: 1.59x faster                                           |
| hexiom                   | 10.9 ms                                                               | 7.00 ms: 1.56x faster                                          |
| scimark_monte_carlo      | 128 ms                                                                | 82.3 ms: 1.55x faster                                          |
| scimark_sor              | 246 ms                                                                | 160 ms: 1.54x faster                                           |
| pickle_pure_python       | 529 us                                                                | 354 us: 1.49x faster                                           |
| float                    | 135 ms                                                                | 91.5 ms: 1.47x faster                                          |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.24 sec: 1.47x faster                                         |
| nbody                    | 166 ms                                                                | 113 ms: 1.46x faster                                           |
| unpickle_pure_python     | 366 us                                                                | 251 us: 1.45x faster                                           |
| pyflate                  | 795 ms                                                                | 550 ms: 1.45x faster                                           |
| mako                     | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                          |
| logging_simple           | 9.78 us                                                               | 6.96 us: 1.40x faster                                          |
| pycparser                | 1.69 sec                                                              | 1.21 sec: 1.40x faster                                         |
| regex_compile            | 177 ms                                                                | 128 ms: 1.37x faster                                           |
| tornado_http             | 178 ms                                                                | 130 ms: 1.37x faster                                           |
| logging_format           | 10.6 us                                                               | 7.76 us: 1.37x faster                                          |
| pylint                   | 485 ms                                                                | 360 ms: 1.35x faster                                           |
| thrift                   | 1.26 ms                                                               | 956 us: 1.32x faster                                           |
| tomli_loads              | 3.36 sec                                                              | 2.55 sec: 1.32x faster                                         |
| spectral_norm            | 186 ms                                                                | 145 ms: 1.29x faster                                           |
| sympy_sum                | 184 ms                                                                | 143 ms: 1.29x faster                                           |
| html5lib                 | 86.5 ms                                                               | 67.6 ms: 1.28x faster                                          |
| coroutines               | 37.2 ms                                                               | 29.2 ms: 1.27x faster                                          |
| genshi_text              | 35.2 ms                                                               | 27.8 ms: 1.27x faster                                          |
| sympy_integrate          | 26.5 ms                                                               | 20.9 ms: 1.27x faster                                          |
| 2to3                     | 381 ms                                                                | 304 ms: 1.25x faster                                           |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                          |
| django_template          | 53.3 ms                                                               | 42.6 ms: 1.25x faster                                          |
| xml_etree_process        | 99.5 ms                                                               | 79.7 ms: 1.25x faster                                          |
| bench_thread_pool        | 1.59 ms                                                               | 1.27 ms: 1.25x faster                                          |
| sympy_str                | 329 ms                                                                | 266 ms: 1.24x faster                                           |
| mypy2                    | 936 ms                                                                | 761 ms: 1.23x faster                                           |
| pprint_pformat           | 2.36 sec                                                              | 1.92 sec: 1.23x faster                                         |
| pprint_safe_repr         | 1.15 sec                                                              | 942 ms: 1.22x faster                                           |
| chameleon                | 10.8 ms                                                               | 8.94 ms: 1.21x faster                                          |
| sqlglot_normalize        | 156 ms                                                                | 129 ms: 1.21x faster                                           |
| dask                     | 450 ms                                                                | 373 ms: 1.20x faster                                           |
| sqlglot_optimize         | 75.4 ms                                                               | 62.6 ms: 1.20x faster                                          |
| deepcopy_memo            | 61.7 us                                                               | 51.4 us: 1.20x faster                                          |
| fannkuch                 | 546 ms                                                                | 458 ms: 1.19x faster                                           |
| sympy_expand             | 543 ms                                                                | 456 ms: 1.19x faster                                           |
| nqueens                  | 117 ms                                                                | 98.9 ms: 1.19x faster                                          |
| gunicorn                 | 1.45 ms                                                               | 1.23 ms: 1.18x faster                                          |
| pathlib                  | 26.3 ms                                                               | 22.7 ms: 1.16x faster                                          |
| aiohttp                  | 1.39 ms                                                               | 1.20 ms: 1.16x faster                                          |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.67 ms: 1.14x faster                                          |
| genshi_xml               | 69.8 ms                                                               | 61.1 ms: 1.14x faster                                          |
| docutils                 | 3.53 sec                                                              | 3.10 sec: 1.14x faster                                         |
| deepcopy                 | 511 us                                                                | 453 us: 1.13x faster                                           |
| scimark_fft              | 500 ms                                                                | 446 ms: 1.12x faster                                           |
| deepcopy_reduce          | 4.60 us                                                               | 4.12 us: 1.12x faster                                          |
| meteor_contest           | 126 ms                                                                | 114 ms: 1.11x faster                                           |
| mdp                      | 3.70 sec                                                              | 3.38 sec: 1.10x faster                                         |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                           |
| xml_etree_parse          | 212 ms                                                                | 195 ms: 1.09x faster                                           |
| unpickle_list            | 6.99 us                                                               | 6.58 us: 1.06x faster                                          |
| sqlite_synth             | 4.12 us                                                               | 3.88 us: 1.06x faster                                          |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.05x faster                                           |
| json                     | 5.88 ms                                                               | 5.60 ms: 1.05x faster                                          |
| regex_v8                 | 32.2 ms                                                               | 31.1 ms: 1.03x faster                                          |
| regex_dna                | 257 ms                                                                | 252 ms: 1.02x faster                                           |
| json_loads               | 30.9 us                                                               | 31.4 us: 1.02x slower                                          |
| pickle_list              | 5.24 us                                                               | 5.33 us: 1.02x slower                                          |
| create_gc_cycles         | 2.26 ms                                                               | 2.33 ms: 1.03x slower                                          |
| async_generators         | 452 ms                                                                | 483 ms: 1.07x slower                                           |
| pickle_dict              | 35.1 us                                                               | 37.9 us: 1.08x slower                                          |
| pickle                   | 12.5 us                                                               | 13.6 us: 1.09x slower                                          |
| regex_effbot             | 4.25 ms                                                               | 4.88 ms: 1.15x slower                                          |
| unpickle                 | 17.5 us                                                               | 20.3 us: 1.16x slower                                          |
| python_startup           | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                          |
| coverage                 | 83.6 ms                                                               | 98.7 ms: 1.18x slower                                          |
| gc_traversal             | 4.15 ms                                                               | 4.92 ms: 1.18x slower                                          |
| telco                    | 8.49 ms                                                               | 10.1 ms: 1.19x slower                                          |
| python_startup_no_site   | 6.89 ms                                                               | 8.63 ms: 1.25x slower                                          |
| Geometric mean           | (ref)                                                                 | 1.28x faster                                                   |

Benchmark hidden because not significant (3): flaskblogging, pidigits, asyncio_websockets
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: dulwich_log, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240906-3.13.0rc2-ec61006/bm-20240906-arminc-aarch64-python-v3.13.0rc2-3.13.0rc2-ec61006.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.297x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.15x