# Results vs. 3.10.4

- fork: python
- ref: 6b280a84988ca221b5bd
- machine: linux-aarch64
- commit hash: 6b280a8
- commit date: 2024-06-29
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 360 ms: 1.06x faster                                                    |
| html5lib       | 86.5 ms                                                               | 71.9 ms: 1.20x faster                                                   |
| tornado_http   | 178 ms                                                                | 137 ms: 1.31x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 443 ms: 2.14x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.07 sec: 2.14x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 569 ms: 1.99x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 731 ms: 1.74x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.00x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 89.4 ms: 1.51x faster                                                   |
| nbody          | 166 ms                                                                | 115 ms: 1.44x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.9 ms: 1.04x faster                                                   |
| regex_dna      | 257 ms                                                                | 251 ms: 1.03x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.87 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 397 us: 1.33x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 278 us: 1.31x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.62 sec: 1.28x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 79.0 ms: 1.26x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.24x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 191 ms: 1.11x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                    |
| json_loads           | 30.9 us                                                               | 33.4 us: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.17x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 15.6 ms: 1.39x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 11.0 ms: 1.60x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.49x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                                   |
| django_template | 53.3 ms                                                               | 50.8 ms: 1.05x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 33.6 ms: 1.05x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 80.1 ms: 1.15x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.08x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 207 us: 3.19x faster                                                    |
| async_tree_none          | 950 ms                                                                | 443 ms: 2.14x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.07 sec: 2.14x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 569 ms: 1.99x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.61 ms: 1.94x faster                                                   |
| raytrace                 | 573 ms                                                                | 325 ms: 1.76x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 731 ms: 1.74x faster                                                    |
| generators               | 68.1 ms                                                               | 39.3 ms: 1.73x faster                                                   |
| richards_super           | 107 ms                                                                | 62.1 ms: 1.73x faster                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 8.57 ms: 1.70x faster                                                   |
| richards                 | 91.7 ms                                                               | 55.6 ms: 1.65x faster                                                   |
| logging_silent           | 222 ns                                                                | 138 ns: 1.61x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 38.9 us: 1.58x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 86.3 ms: 1.55x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.58 ms: 1.52x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 623 ms: 1.52x faster                                                    |
| float                    | 135 ms                                                                | 89.4 ms: 1.51x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.49x faster                                                  |
| go                       | 264 ms                                                                | 179 ms: 1.48x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 87.5 ms: 1.46x faster                                                   |
| nbody                    | 166 ms                                                                | 115 ms: 1.44x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 1.99 ms: 1.43x faster                                                   |
| comprehensions           | 33.1 us                                                               | 23.4 us: 1.42x faster                                                   |
| scimark_sor              | 246 ms                                                                | 176 ms: 1.40x faster                                                    |
| chaos                    | 121 ms                                                                | 87.0 ms: 1.39x faster                                                   |
| deepcopy                 | 511 us                                                                | 375 us: 1.36x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.28 us: 1.34x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.90 us: 1.34x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 397 us: 1.33x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 278 us: 1.31x faster                                                    |
| thrift                   | 1.26 ms                                                               | 962 us: 1.31x faster                                                    |
| tornado_http             | 178 ms                                                                | 137 ms: 1.31x faster                                                    |
| pyflate                  | 795 ms                                                                | 618 ms: 1.29x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.62 sec: 1.28x faster                                                  |
| spectral_norm            | 186 ms                                                                | 147 ms: 1.27x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.34 sec: 1.26x faster                                                  |
| xml_etree_process        | 99.5 ms                                                               | 79.0 ms: 1.26x faster                                                   |
| coroutines               | 37.2 ms                                                               | 29.8 ms: 1.25x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.24x faster                                                   |
| scimark_lu               | 227 ms                                                                | 183 ms: 1.24x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 8.99 ms: 1.21x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.32 ms: 1.21x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 71.9 ms: 1.20x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 22.1 ms: 1.19x faster                                                   |
| pylint                   | 485 ms                                                                | 412 ms: 1.18x faster                                                    |
| dask                     | 450 ms                                                                | 387 ms: 1.16x faster                                                    |
| fannkuch                 | 546 ms                                                                | 472 ms: 1.16x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.07 us: 1.13x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 191 ms: 1.11x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 142 ms: 1.10x faster                                                    |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.09x faster                                                    |
| scimark_fft              | 500 ms                                                                | 461 ms: 1.09x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.03 ms: 1.08x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 70.1 ms: 1.08x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.46 sec: 1.07x faster                                                  |
| 2to3                     | 381 ms                                                                | 360 ms: 1.06x faster                                                    |
| django_template          | 53.3 ms                                                               | 50.8 ms: 1.05x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 25.3 ms: 1.05x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 33.6 ms: 1.05x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.9 ms: 1.04x faster                                                   |
| sympy_str                | 329 ms                                                                | 316 ms: 1.04x faster                                                    |
| regex_dna                | 257 ms                                                                | 251 ms: 1.03x faster                                                    |
| sympy_sum                | 184 ms                                                                | 180 ms: 1.02x faster                                                    |
| sympy_expand             | 543 ms                                                                | 534 ms: 1.02x faster                                                    |
| nqueens                  | 117 ms                                                                | 116 ms: 1.01x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.14 sec: 1.01x faster                                                  |
| asyncio_websockets       | 657 ms                                                                | 661 ms: 1.01x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.38 sec: 1.01x slower                                                  |
| create_gc_cycles         | 2.26 ms                                                               | 2.35 ms: 1.04x slower                                                   |
| json_loads               | 30.9 us                                                               | 33.4 us: 1.08x slower                                                   |
| async_generators         | 452 ms                                                                | 510 ms: 1.13x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.87 ms: 1.15x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 80.1 ms: 1.15x slower                                                   |
| coverage                 | 83.6 ms                                                               | 100 ms: 1.20x slower                                                    |
| telco                    | 8.49 ms                                                               | 10.3 ms: 1.22x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.15 ms: 1.24x slower                                                   |
| python_startup           | 11.2 ms                                                               | 15.6 ms: 1.39x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 11.0 ms: 1.60x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.23x faster                                                            |

Benchmark hidden because not significant (5): regex_compile, dulwich_log, pidigits, docutils, json
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240629-3.14.0a0-6b280a8-JIT/bm-20240629-arminc-aarch64-python-6b280a84988ca221b5bd-3.14.0a0-6b280a8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.24x