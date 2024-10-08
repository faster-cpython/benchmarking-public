# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a5
- machine: linux-aarch64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 306 ms: 1.24x faster                                         |
| chameleon      | 10.8 ms                                                               | 8.86 ms: 1.22x faster                                        |
| docutils       | 3.53 sec                                                              | 2.92 sec: 1.21x faster                                       |
| html5lib       | 86.5 ms                                                               | 65.9 ms: 1.31x faster                                        |
| tornado_http   | 178 ms                                                                | 136 ms: 1.31x faster                                         |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 573 ms: 1.66x faster                                         |
| async_tree_io           | 2.28 sec                                                              | 1.44 sec: 1.59x faster                                       |
| async_tree_memoization  | 1.13 sec                                                              | 737 ms: 1.54x faster                                         |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 893 ms: 1.43x faster                                         |
| Geometric mean          | (ref)                                                                 | 1.55x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 103 ms: 1.61x faster                                         |
| float          | 135 ms                                                                | 93.1 ms: 1.45x faster                                        |
| Geometric mean | (ref)                                                                 | 1.33x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 126 ms: 1.40x faster                                         |
| regex_v8       | 32.2 ms                                                               | 30.4 ms: 1.06x faster                                        |
| regex_dna      | 257 ms                                                                | 251 ms: 1.03x faster                                         |
| regex_effbot   | 4.25 ms                                                               | 4.94 ms: 1.16x slower                                        |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 349 us: 1.52x faster                                         |
| unpickle_pure_python | 366 us                                                                | 256 us: 1.43x faster                                         |
| json_dumps           | 16.7 ms                                                               | 12.8 ms: 1.31x faster                                        |
| tomli_loads          | 3.36 sec                                                              | 2.59 sec: 1.30x faster                                       |
| xml_etree_process    | 99.5 ms                                                               | 80.4 ms: 1.24x faster                                        |
| unpickle_list        | 6.99 us                                                               | 6.25 us: 1.12x faster                                        |
| xml_etree_parse      | 212 ms                                                                | 191 ms: 1.11x faster                                         |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.05x faster                                         |
| pickle_list          | 5.24 us                                                               | 5.26 us: 1.00x slower                                        |
| json_loads           | 30.9 us                                                               | 32.2 us: 1.04x slower                                        |
| pickle               | 12.5 us                                                               | 13.3 us: 1.06x slower                                        |
| pickle_dict          | 35.1 us                                                               | 37.6 us: 1.07x slower                                        |
| unpickle             | 17.5 us                                                               | 19.3 us: 1.11x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.12x faster                                                 |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 12.2 ms: 1.09x slower                                        |
| python_startup_no_site | 6.89 ms                                                               | 10.5 ms: 1.52x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.29x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.9 ms: 1.46x faster                                        |
| django_template | 53.3 ms                                                               | 40.5 ms: 1.32x faster                                        |
| genshi_text     | 35.2 ms                                                               | 27.8 ms: 1.27x faster                                        |
| genshi_xml      | 69.8 ms                                                               | 60.5 ms: 1.15x faster                                        |
| Geometric mean  | (ref)                                                                 | 1.30x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 133 us: 4.96x faster                                         |
| deltablue                | 8.94 ms                                                               | 4.00 ms: 2.24x faster                                        |
| bench_mp_pool            | 14.5 ms                                                               | 7.02 ms: 2.07x faster                                        |
| raytrace                 | 573 ms                                                                | 296 ms: 1.93x faster                                         |
| generators               | 68.1 ms                                                               | 35.9 ms: 1.89x faster                                        |
| richards_super           | 107 ms                                                                | 59.1 ms: 1.82x faster                                        |
| chaos                    | 121 ms                                                                | 67.6 ms: 1.79x faster                                        |
| richards                 | 91.7 ms                                                               | 51.8 ms: 1.77x faster                                        |
| sqlglot_parse            | 2.40 ms                                                               | 1.37 ms: 1.75x faster                                        |
| logging_silent           | 222 ns                                                                | 130 ns: 1.71x faster                                         |
| crypto_pyaes             | 134 ms                                                                | 79.2 ms: 1.69x faster                                        |
| asyncio_tcp              | 944 ms                                                                | 559 ms: 1.69x faster                                         |
| comprehensions           | 33.1 us                                                               | 19.9 us: 1.67x faster                                        |
| async_tree_none          | 950 ms                                                                | 573 ms: 1.66x faster                                         |
| scimark_lu               | 227 ms                                                                | 137 ms: 1.65x faster                                         |
| go                       | 264 ms                                                                | 161 ms: 1.64x faster                                         |
| sqlglot_transpile        | 2.84 ms                                                               | 1.75 ms: 1.62x faster                                        |
| nbody                    | 166 ms                                                                | 103 ms: 1.61x faster                                         |
| async_tree_io            | 2.28 sec                                                              | 1.44 sec: 1.59x faster                                       |
| hexiom                   | 10.9 ms                                                               | 6.92 ms: 1.58x faster                                        |
| scimark_monte_carlo      | 128 ms                                                                | 82.1 ms: 1.56x faster                                        |
| async_tree_memoization   | 1.13 sec                                                              | 737 ms: 1.54x faster                                         |
| pickle_pure_python       | 529 us                                                                | 349 us: 1.52x faster                                         |
| scimark_sor              | 246 ms                                                                | 165 ms: 1.49x faster                                         |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.22 sec: 1.48x faster                                       |
| mako                     | 18.9 ms                                                               | 12.9 ms: 1.46x faster                                        |
| pylint                   | 485 ms                                                                | 335 ms: 1.45x faster                                         |
| float                    | 135 ms                                                                | 93.1 ms: 1.45x faster                                        |
| unpickle_pure_python     | 366 us                                                                | 256 us: 1.43x faster                                         |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 893 ms: 1.43x faster                                         |
| regex_compile            | 177 ms                                                                | 126 ms: 1.40x faster                                         |
| spectral_norm            | 186 ms                                                                | 135 ms: 1.38x faster                                         |
| logging_simple           | 9.78 us                                                               | 7.18 us: 1.36x faster                                        |
| thrift                   | 1.26 ms                                                               | 929 us: 1.36x faster                                         |
| logging_format           | 10.6 us                                                               | 7.83 us: 1.36x faster                                        |
| pyflate                  | 795 ms                                                                | 591 ms: 1.35x faster                                         |
| pycparser                | 1.69 sec                                                              | 1.28 sec: 1.32x faster                                       |
| sympy_sum                | 184 ms                                                                | 140 ms: 1.32x faster                                         |
| django_template          | 53.3 ms                                                               | 40.5 ms: 1.32x faster                                        |
| html5lib                 | 86.5 ms                                                               | 65.9 ms: 1.31x faster                                        |
| tornado_http             | 178 ms                                                                | 136 ms: 1.31x faster                                         |
| json_dumps               | 16.7 ms                                                               | 12.8 ms: 1.31x faster                                        |
| sympy_integrate          | 26.5 ms                                                               | 20.4 ms: 1.30x faster                                        |
| tomli_loads              | 3.36 sec                                                              | 2.59 sec: 1.30x faster                                       |
| coroutines               | 37.2 ms                                                               | 28.8 ms: 1.29x faster                                        |
| deepcopy_memo            | 61.7 us                                                               | 48.2 us: 1.28x faster                                        |
| pprint_safe_repr         | 1.15 sec                                                              | 903 ms: 1.27x faster                                         |
| pprint_pformat           | 2.36 sec                                                              | 1.86 sec: 1.27x faster                                       |
| genshi_text              | 35.2 ms                                                               | 27.8 ms: 1.27x faster                                        |
| sympy_str                | 329 ms                                                                | 260 ms: 1.26x faster                                         |
| 2to3                     | 381 ms                                                                | 306 ms: 1.24x faster                                         |
| sqlglot_normalize        | 156 ms                                                                | 126 ms: 1.24x faster                                         |
| xml_etree_process        | 99.5 ms                                                               | 80.4 ms: 1.24x faster                                        |
| bench_thread_pool        | 1.59 ms                                                               | 1.29 ms: 1.24x faster                                        |
| sqlglot_optimize         | 75.4 ms                                                               | 61.2 ms: 1.23x faster                                        |
| dulwich_log              | 73.5 ms                                                               | 59.7 ms: 1.23x faster                                        |
| chameleon                | 10.8 ms                                                               | 8.86 ms: 1.22x faster                                        |
| nqueens                  | 117 ms                                                                | 96.0 ms: 1.22x faster                                        |
| docutils                 | 3.53 sec                                                              | 2.92 sec: 1.21x faster                                       |
| sympy_expand             | 543 ms                                                                | 451 ms: 1.20x faster                                         |
| fannkuch                 | 546 ms                                                                | 459 ms: 1.19x faster                                         |
| deepcopy                 | 511 us                                                                | 431 us: 1.18x faster                                         |
| aiohttp                  | 1.39 ms                                                               | 1.18 ms: 1.18x faster                                        |
| gunicorn                 | 1.45 ms                                                               | 1.23 ms: 1.17x faster                                        |
| dask                     | 450 ms                                                                | 383 ms: 1.17x faster                                         |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.51 ms: 1.17x faster                                        |
| deepcopy_reduce          | 4.60 us                                                               | 3.95 us: 1.16x faster                                        |
| genshi_xml               | 69.8 ms                                                               | 60.5 ms: 1.15x faster                                        |
| scimark_fft              | 500 ms                                                                | 441 ms: 1.14x faster                                         |
| create_gc_cycles         | 2.26 ms                                                               | 1.99 ms: 1.13x faster                                        |
| unpickle_list            | 6.99 us                                                               | 6.25 us: 1.12x faster                                        |
| mdp                      | 3.70 sec                                                              | 3.32 sec: 1.11x faster                                       |
| xml_etree_parse          | 212 ms                                                                | 191 ms: 1.11x faster                                         |
| pathlib                  | 26.3 ms                                                               | 24.2 ms: 1.09x faster                                        |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.09x faster                                         |
| sqlite_synth             | 4.12 us                                                               | 3.88 us: 1.06x faster                                        |
| regex_v8                 | 32.2 ms                                                               | 30.4 ms: 1.06x faster                                        |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.05x faster                                         |
| json                     | 5.88 ms                                                               | 5.71 ms: 1.03x faster                                        |
| regex_dna                | 257 ms                                                                | 251 ms: 1.03x faster                                         |
| pickle_list              | 5.24 us                                                               | 5.26 us: 1.00x slower                                        |
| asyncio_websockets       | 657 ms                                                                | 664 ms: 1.01x slower                                         |
| json_loads               | 30.9 us                                                               | 32.2 us: 1.04x slower                                        |
| pickle                   | 12.5 us                                                               | 13.3 us: 1.06x slower                                        |
| pickle_dict              | 35.1 us                                                               | 37.6 us: 1.07x slower                                        |
| gc_traversal             | 4.15 ms                                                               | 4.45 ms: 1.07x slower                                        |
| async_generators         | 452 ms                                                                | 487 ms: 1.08x slower                                         |
| python_startup           | 11.2 ms                                                               | 12.2 ms: 1.09x slower                                        |
| unpickle                 | 17.5 us                                                               | 19.3 us: 1.11x slower                                        |
| regex_effbot             | 4.25 ms                                                               | 4.94 ms: 1.16x slower                                        |
| telco                    | 8.49 ms                                                               | 10.2 ms: 1.20x slower                                        |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                         |
| python_startup_no_site   | 6.89 ms                                                               | 10.5 ms: 1.52x slower                                        |
| Geometric mean           | (ref)                                                                 | 1.29x faster                                                 |

Benchmark hidden because not significant (4): xml_etree_generate, flaskblogging, mypy2, pidigits
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240312-3.13.0a5-076d169/bm-20240312-arminc-aarch64-python-v3.13.0a5-3.13.0a5-076d169.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.09x