# Results vs. 3.10.4

- fork: python
- ref: 58ce131037ecb34d506a
- machine: linux-aarch64
- commit hash: 58ce131
- commit date: 2024-08-29
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 297 ms: 1.28x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                  |
| html5lib       | 86.5 ms                                                               | 63.5 ms: 1.36x faster                                                   |
| tornado_http   | 178 ms                                                                | 127 ms: 1.40x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 424 ms: 2.24x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 555 ms: 2.04x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.15 sec: 1.99x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 731 ms: 1.74x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.00x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 110 ms: 1.51x faster                                                    |
| float          | 135 ms                                                                | 92.6 ms: 1.46x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.41x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| regex_dna      | 257 ms                                                                | 247 ms: 1.04x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.84 ms: 1.14x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 363 us: 1.46x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 253 us: 1.44x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 79.8 ms: 1.25x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 188 ms: 1.12x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.6 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.81 ms: 1.28x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.5 ms: 1.41x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                   |
| django_template | 53.3 ms                                                               | 42.8 ms: 1.25x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 61.4 ms: 1.14x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.26x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 194 us: 3.40x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.91 ms: 2.29x faster                                                   |
| async_tree_none          | 950 ms                                                                | 424 ms: 2.24x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.04 ms: 2.06x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 555 ms: 2.04x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.15 sec: 1.99x faster                                                  |
| generators               | 68.1 ms                                                               | 34.8 ms: 1.96x faster                                                   |
| go                       | 264 ms                                                                | 137 ms: 1.93x faster                                                    |
| raytrace                 | 573 ms                                                                | 301 ms: 1.90x faster                                                    |
| richards_super           | 107 ms                                                                | 59.6 ms: 1.80x faster                                                   |
| chaos                    | 121 ms                                                                | 68.4 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 731 ms: 1.74x faster                                                    |
| richards                 | 91.7 ms                                                               | 53.6 ms: 1.71x faster                                                   |
| scimark_lu               | 227 ms                                                                | 134 ms: 1.70x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.42 ms: 1.69x faster                                                   |
| logging_silent           | 222 ns                                                                | 132 ns: 1.68x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 564 ms: 1.67x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.72 ms: 1.65x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 82.3 ms: 1.63x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.4 us: 1.63x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 38.1 us: 1.62x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 81.4 ms: 1.57x faster                                                   |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.57x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.02 ms: 1.55x faster                                                   |
| deepcopy                 | 511 us                                                                | 334 us: 1.53x faster                                                    |
| nbody                    | 166 ms                                                                | 110 ms: 1.51x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.49x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 363 us: 1.46x faster                                                    |
| float                    | 135 ms                                                                | 92.6 ms: 1.46x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 253 us: 1.44x faster                                                    |
| pyflate                  | 795 ms                                                                | 560 ms: 1.42x faster                                                    |
| regex_compile            | 177 ms                                                                | 125 ms: 1.41x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.5 ms: 1.41x faster                                                   |
| tornado_http             | 178 ms                                                                | 127 ms: 1.40x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.22 sec: 1.39x faster                                                  |
| logging_simple           | 9.78 us                                                               | 7.06 us: 1.39x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.66 us: 1.38x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 63.5 ms: 1.36x faster                                                   |
| pylint                   | 485 ms                                                                | 357 ms: 1.36x faster                                                    |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.32x faster                                                    |
| thrift                   | 1.26 ms                                                               | 954 us: 1.32x faster                                                    |
| sympy_sum                | 184 ms                                                                | 141 ms: 1.30x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.7 ms: 1.30x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.56 us: 1.29x faster                                                   |
| 2to3                     | 381 ms                                                                | 297 ms: 1.28x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                  |
| bench_thread_pool        | 1.59 ms                                                               | 1.24 ms: 1.28x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.8 ms: 1.27x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 79.8 ms: 1.25x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.1 ms: 1.25x faster                                                   |
| django_template          | 53.3 ms                                                               | 42.8 ms: 1.25x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 125 ms: 1.24x faster                                                    |
| sympy_str                | 329 ms                                                                | 265 ms: 1.24x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.91 sec: 1.23x faster                                                  |
| json_dumps               | 16.7 ms                                                               | 13.6 ms: 1.23x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 942 ms: 1.22x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 61.9 ms: 1.22x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.33 ms: 1.20x faster                                                   |
| fannkuch                 | 546 ms                                                                | 460 ms: 1.19x faster                                                    |
| sympy_expand             | 543 ms                                                                | 459 ms: 1.18x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                  |
| nqueens                  | 117 ms                                                                | 101 ms: 1.16x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 61.4 ms: 1.14x faster                                                   |
| scimark_fft              | 500 ms                                                                | 440 ms: 1.14x faster                                                    |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.13x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 188 ms: 1.12x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.34 sec: 1.11x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| regex_dna                | 257 ms                                                                | 247 ms: 1.04x faster                                                    |
| json                     | 5.88 ms                                                               | 5.69 ms: 1.03x faster                                                   |
| json_loads               | 30.9 us                                                               | 32.6 us: 1.05x slower                                                   |
| async_generators         | 452 ms                                                                | 482 ms: 1.06x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.84 ms: 1.14x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 4.84 ms: 1.16x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| coverage                 | 83.6 ms                                                               | 98.7 ms: 1.18x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.1 ms: 1.19x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.81 ms: 1.28x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.35x faster                                                            |

Benchmark hidden because not significant (3): pidigits, asyncio_websockets, create_gc_cycles
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240829-3.14.0a0-58ce131/bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.15x