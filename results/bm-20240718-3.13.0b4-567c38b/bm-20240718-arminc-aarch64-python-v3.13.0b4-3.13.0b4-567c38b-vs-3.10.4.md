# Results vs. 3.10.4

- fork: python
- ref: v3.13.0b4
- machine: linux-aarch64
- commit hash: 567c38b
- commit date: 2024-07-18
- overall geometric mean: 1.305x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 308 ms: 1.24x faster                                         |
| chameleon      | 10.8 ms                                                               | 8.93 ms: 1.21x faster                                        |
| docutils       | 3.53 sec                                                              | 3.05 sec: 1.15x faster                                       |
| html5lib       | 86.5 ms                                                               | 66.6 ms: 1.30x faster                                        |
| tornado_http   | 178 ms                                                                | 127 ms: 1.40x faster                                         |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 500 ms: 1.90x faster                                         |
| async_tree_io           | 2.28 sec                                                              | 1.21 sec: 1.88x faster                                       |
| async_tree_memoization  | 1.13 sec                                                              | 640 ms: 1.77x faster                                         |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 817 ms: 1.56x faster                                         |
| Geometric mean          | (ref)                                                                 | 1.77x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 110 ms: 1.50x faster                                         |
| float          | 135 ms                                                                | 91.6 ms: 1.47x faster                                        |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 127 ms: 1.39x faster                                         |
| regex_v8       | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                        |
| regex_dna      | 257 ms                                                                | 253 ms: 1.02x faster                                         |
| regex_effbot   | 4.25 ms                                                               | 4.90 ms: 1.15x slower                                        |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 358 us: 1.48x faster                                         |
| unpickle_pure_python | 366 us                                                                | 255 us: 1.43x faster                                         |
| tomli_loads          | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                       |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                        |
| xml_etree_process    | 99.5 ms                                                               | 82.4 ms: 1.21x faster                                        |
| xml_etree_parse      | 212 ms                                                                | 189 ms: 1.12x faster                                         |
| xml_etree_generate   | 123 ms                                                                | 114 ms: 1.08x faster                                         |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.06x faster                                         |
| json_loads           | 30.9 us                                                               | 32.4 us: 1.05x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 12.9 ms: 1.16x slower                                        |
| python_startup_no_site | 6.89 ms                                                               | 8.72 ms: 1.27x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.21x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                        |
| genshi_text     | 35.2 ms                                                               | 27.8 ms: 1.27x faster                                        |
| django_template | 53.3 ms                                                               | 42.2 ms: 1.26x faster                                        |
| genshi_xml      | 69.8 ms                                                               | 59.5 ms: 1.17x faster                                        |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 194 us: 3.41x faster                                         |
| deltablue                | 8.94 ms                                                               | 3.86 ms: 2.32x faster                                        |
| bench_mp_pool            | 14.5 ms                                                               | 7.14 ms: 2.04x faster                                        |
| raytrace                 | 573 ms                                                                | 299 ms: 1.92x faster                                         |
| async_tree_none          | 950 ms                                                                | 500 ms: 1.90x faster                                         |
| async_tree_io            | 2.28 sec                                                              | 1.21 sec: 1.88x faster                                       |
| generators               | 68.1 ms                                                               | 37.3 ms: 1.82x faster                                        |
| richards_super           | 107 ms                                                                | 60.0 ms: 1.79x faster                                        |
| async_tree_memoization   | 1.13 sec                                                              | 640 ms: 1.77x faster                                         |
| chaos                    | 121 ms                                                                | 68.9 ms: 1.76x faster                                        |
| sqlglot_parse            | 2.40 ms                                                               | 1.39 ms: 1.73x faster                                        |
| richards                 | 91.7 ms                                                               | 53.2 ms: 1.72x faster                                        |
| sqlglot_transpile        | 2.84 ms                                                               | 1.71 ms: 1.66x faster                                        |
| scimark_lu               | 227 ms                                                                | 137 ms: 1.65x faster                                         |
| logging_silent           | 222 ns                                                                | 135 ns: 1.65x faster                                         |
| go                       | 264 ms                                                                | 161 ms: 1.64x faster                                         |
| asyncio_tcp              | 944 ms                                                                | 580 ms: 1.63x faster                                         |
| crypto_pyaes             | 134 ms                                                                | 82.5 ms: 1.63x faster                                        |
| comprehensions           | 33.1 us                                                               | 20.7 us: 1.60x faster                                        |
| scimark_monte_carlo      | 128 ms                                                                | 81.8 ms: 1.56x faster                                        |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 817 ms: 1.56x faster                                         |
| scimark_sor              | 246 ms                                                                | 159 ms: 1.54x faster                                         |
| hexiom                   | 10.9 ms                                                               | 7.09 ms: 1.54x faster                                        |
| nbody                    | 166 ms                                                                | 110 ms: 1.50x faster                                         |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.49x faster                                       |
| pickle_pure_python       | 529 us                                                                | 358 us: 1.48x faster                                         |
| float                    | 135 ms                                                                | 91.6 ms: 1.47x faster                                        |
| unpickle_pure_python     | 366 us                                                                | 255 us: 1.43x faster                                         |
| pylint                   | 485 ms                                                                | 341 ms: 1.42x faster                                         |
| pyflate                  | 795 ms                                                                | 560 ms: 1.42x faster                                         |
| mako                     | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                        |
| tornado_http             | 178 ms                                                                | 127 ms: 1.40x faster                                         |
| regex_compile            | 177 ms                                                                | 127 ms: 1.39x faster                                         |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.38x faster                                       |
| logging_simple           | 9.78 us                                                               | 7.13 us: 1.37x faster                                        |
| logging_format           | 10.6 us                                                               | 7.81 us: 1.36x faster                                        |
| tomli_loads              | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                       |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.33x faster                                         |
| thrift                   | 1.26 ms                                                               | 956 us: 1.32x faster                                         |
| html5lib                 | 86.5 ms                                                               | 66.6 ms: 1.30x faster                                        |
| coroutines               | 37.2 ms                                                               | 28.7 ms: 1.30x faster                                        |
| sympy_sum                | 184 ms                                                                | 142 ms: 1.30x faster                                         |
| genshi_text              | 35.2 ms                                                               | 27.8 ms: 1.27x faster                                        |
| django_template          | 53.3 ms                                                               | 42.2 ms: 1.26x faster                                        |
| sympy_integrate          | 26.5 ms                                                               | 21.0 ms: 1.26x faster                                        |
| dulwich_log              | 73.5 ms                                                               | 59.0 ms: 1.25x faster                                        |
| 2to3                     | 381 ms                                                                | 308 ms: 1.24x faster                                         |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                        |
| sympy_str                | 329 ms                                                                | 267 ms: 1.23x faster                                         |
| pprint_pformat           | 2.36 sec                                                              | 1.92 sec: 1.23x faster                                       |
| deepcopy_memo            | 61.7 us                                                               | 50.4 us: 1.22x faster                                        |
| bench_thread_pool        | 1.59 ms                                                               | 1.30 ms: 1.22x faster                                        |
| mypy2                    | 936 ms                                                                | 766 ms: 1.22x faster                                         |
| sqlglot_normalize        | 156 ms                                                                | 128 ms: 1.22x faster                                         |
| pprint_safe_repr         | 1.15 sec                                                              | 941 ms: 1.22x faster                                         |
| chameleon                | 10.8 ms                                                               | 8.93 ms: 1.21x faster                                        |
| sqlglot_optimize         | 75.4 ms                                                               | 62.2 ms: 1.21x faster                                        |
| xml_etree_process        | 99.5 ms                                                               | 82.4 ms: 1.21x faster                                        |
| fannkuch                 | 546 ms                                                                | 455 ms: 1.20x faster                                         |
| dask                     | 450 ms                                                                | 376 ms: 1.20x faster                                         |
| sympy_expand             | 543 ms                                                                | 460 ms: 1.18x faster                                         |
| nqueens                  | 117 ms                                                                | 99.7 ms: 1.18x faster                                        |
| genshi_xml               | 69.8 ms                                                               | 59.5 ms: 1.17x faster                                        |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.52 ms: 1.17x faster                                        |
| docutils                 | 3.53 sec                                                              | 3.05 sec: 1.15x faster                                       |
| pathlib                  | 26.3 ms                                                               | 22.8 ms: 1.15x faster                                        |
| deepcopy                 | 511 us                                                                | 452 us: 1.13x faster                                         |
| scimark_fft              | 500 ms                                                                | 445 ms: 1.12x faster                                         |
| deepcopy_reduce          | 4.60 us                                                               | 4.10 us: 1.12x faster                                        |
| xml_etree_parse          | 212 ms                                                                | 189 ms: 1.12x faster                                         |
| mdp                      | 3.70 sec                                                              | 3.35 sec: 1.10x faster                                       |
| meteor_contest           | 126 ms                                                                | 115 ms: 1.10x faster                                         |
| xml_etree_generate       | 123 ms                                                                | 114 ms: 1.08x faster                                         |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.06x faster                                         |
| regex_v8                 | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                        |
| json                     | 5.88 ms                                                               | 5.70 ms: 1.03x faster                                        |
| regex_dna                | 257 ms                                                                | 253 ms: 1.02x faster                                         |
| asyncio_websockets       | 657 ms                                                                | 661 ms: 1.01x slower                                         |
| create_gc_cycles         | 2.26 ms                                                               | 2.33 ms: 1.03x slower                                        |
| json_loads               | 30.9 us                                                               | 32.4 us: 1.05x slower                                        |
| async_generators         | 452 ms                                                                | 489 ms: 1.08x slower                                         |
| telco                    | 8.49 ms                                                               | 9.64 ms: 1.14x slower                                        |
| regex_effbot             | 4.25 ms                                                               | 4.90 ms: 1.15x slower                                        |
| python_startup           | 11.2 ms                                                               | 12.9 ms: 1.16x slower                                        |
| coverage                 | 83.6 ms                                                               | 99.9 ms: 1.20x slower                                        |
| gc_traversal             | 4.15 ms                                                               | 4.98 ms: 1.20x slower                                        |
| python_startup_no_site   | 6.89 ms                                                               | 8.72 ms: 1.27x slower                                        |
| Geometric mean           | (ref)                                                                 | 1.31x faster                                                 |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240718-3.13.0b4-567c38b/bm-20240718-arminc-aarch64-python-v3.13.0b4-3.13.0b4-567c38b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.305x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.14x