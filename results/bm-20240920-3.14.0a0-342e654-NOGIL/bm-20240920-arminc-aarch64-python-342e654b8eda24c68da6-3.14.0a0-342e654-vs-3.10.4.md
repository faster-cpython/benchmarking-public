# Results vs. 3.10.4

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-aarch64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.169x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x slower
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 508 ms: 1.33x slower                                                    |
| docutils       | 3.53 sec                                                              | 3.93 sec: 1.11x slower                                                  |
| html5lib       | 86.5 ms                                                               | 118 ms: 1.37x slower                                                    |
| tornado_http   | 178 ms                                                                | 203 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.23x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.37 sec: 1.67x faster                                                  |
| async_tree_none         | 950 ms                                                                | 604 ms: 1.57x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 735 ms: 1.54x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 897 ms: 1.42x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.55x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 205 ms: 1.52x slower                                                    |
| nbody          | 166 ms                                                                | 279 ms: 1.68x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.37x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 254 ms: 1.01x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.42 ms: 1.04x slower                                                   |
| regex_compile  | 177 ms                                                                | 248 ms: 1.40x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 182 ms: 1.17x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 152 ms: 1.02x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 7.12 us: 1.02x slower                                                   |
| pickle_list          | 5.24 us                                                               | 5.41 us: 1.03x slower                                                   |
| pickle               | 12.5 us                                                               | 13.1 us: 1.05x slower                                                   |
| json_dumps           | 16.7 ms                                                               | 17.8 ms: 1.07x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 39.4 us: 1.12x slower                                                   |
| unpickle             | 17.5 us                                                               | 21.3 us: 1.22x slower                                                   |
| tomli_loads          | 3.36 sec                                                              | 4.11 sec: 1.22x slower                                                  |
| json_loads           | 30.9 us                                                               | 37.9 us: 1.23x slower                                                   |
| xml_etree_process    | 99.5 ms                                                               | 125 ms: 1.26x slower                                                    |
| xml_etree_generate   | 123 ms                                                                | 155 ms: 1.26x slower                                                    |
| pickle_pure_python   | 529 us                                                                | 754 us: 1.43x slower                                                    |
| unpickle_pure_python | 366 us                                                                | 526 us: 1.44x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.14x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 18.1 ms: 1.62x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 12.1 ms: 1.76x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.69x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 69.8 ms                                                               | 101 ms: 1.44x slower                                                    |
| genshi_text     | 35.2 ms                                                               | 52.1 ms: 1.48x slower                                                   |
| django_template | 53.3 ms                                                               | 79.0 ms: 1.48x slower                                                   |
| mako            | 18.9 ms                                                               | 28.4 ms: 1.50x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.48x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| bench_mp_pool            | 14.5 ms                                                               | 6.69 ms: 2.17x faster                                                   |
| typing_runtime_protocols | 661 us                                                                | 324 us: 2.04x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.37 sec: 1.67x faster                                                  |
| async_tree_none          | 950 ms                                                                | 604 ms: 1.57x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 735 ms: 1.54x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 897 ms: 1.42x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 668 ms: 1.41x faster                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 1.61 ms: 1.40x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.59 sec: 1.27x faster                                                  |
| gc_traversal             | 4.15 ms                                                               | 3.44 ms: 1.21x faster                                                   |
| generators               | 68.1 ms                                                               | 57.8 ms: 1.18x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 182 ms: 1.17x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 152 ms: 1.02x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 25.7 ms: 1.02x faster                                                   |
| regex_dna                | 257 ms                                                                | 254 ms: 1.01x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 7.12 us: 1.02x slower                                                   |
| asyncio_websockets       | 657 ms                                                                | 676 ms: 1.03x slower                                                    |
| pickle_list              | 5.24 us                                                               | 5.41 us: 1.03x slower                                                   |
| crypto_pyaes             | 134 ms                                                                | 139 ms: 1.03x slower                                                    |
| deepcopy                 | 511 us                                                                | 531 us: 1.04x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.42 ms: 1.04x slower                                                   |
| pickle                   | 12.5 us                                                               | 13.1 us: 1.05x slower                                                   |
| coroutines               | 37.2 ms                                                               | 39.3 ms: 1.06x slower                                                   |
| json_dumps               | 16.7 ms                                                               | 17.8 ms: 1.07x slower                                                   |
| deepcopy_memo            | 61.7 us                                                               | 67.9 us: 1.10x slower                                                   |
| docutils                 | 3.53 sec                                                              | 3.93 sec: 1.11x slower                                                  |
| pickle_dict              | 35.1 us                                                               | 39.4 us: 1.12x slower                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.66 ms: 1.14x slower                                                   |
| tornado_http             | 178 ms                                                                | 203 ms: 1.14x slower                                                    |
| scimark_fft              | 500 ms                                                                | 574 ms: 1.15x slower                                                    |
| json                     | 5.88 ms                                                               | 6.77 ms: 1.15x slower                                                   |
| mdp                      | 3.70 sec                                                              | 4.28 sec: 1.16x slower                                                  |
| pycparser                | 1.69 sec                                                              | 2.00 sec: 1.18x slower                                                  |
| spectral_norm            | 186 ms                                                                | 225 ms: 1.21x slower                                                    |
| comprehensions           | 33.1 us                                                               | 40.2 us: 1.21x slower                                                   |
| unpickle                 | 17.5 us                                                               | 21.3 us: 1.22x slower                                                   |
| tomli_loads              | 3.36 sec                                                              | 4.11 sec: 1.22x slower                                                  |
| json_loads               | 30.9 us                                                               | 37.9 us: 1.23x slower                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 5.76 us: 1.25x slower                                                   |
| richards                 | 91.7 ms                                                               | 115 ms: 1.26x slower                                                    |
| richards_super           | 107 ms                                                                | 135 ms: 1.26x slower                                                    |
| xml_etree_process        | 99.5 ms                                                               | 125 ms: 1.26x slower                                                    |
| xml_etree_generate       | 123 ms                                                                | 155 ms: 1.26x slower                                                    |
| pyflate                  | 795 ms                                                                | 1.00 sec: 1.26x slower                                                  |
| bench_thread_pool        | 1.59 ms                                                               | 2.01 ms: 1.27x slower                                                   |
| nqueens                  | 117 ms                                                                | 149 ms: 1.27x slower                                                    |
| dulwich_log              | 73.5 ms                                                               | 93.6 ms: 1.27x slower                                                   |
| logging_silent           | 222 ns                                                                | 284 ns: 1.28x slower                                                    |
| thrift                   | 1.26 ms                                                               | 1.62 ms: 1.29x slower                                                   |
| sympy_integrate          | 26.5 ms                                                               | 34.6 ms: 1.30x slower                                                   |
| meteor_contest           | 126 ms                                                                | 166 ms: 1.31x slower                                                    |
| chaos                    | 121 ms                                                                | 161 ms: 1.33x slower                                                    |
| 2to3                     | 381 ms                                                                | 508 ms: 1.33x slower                                                    |
| html5lib                 | 86.5 ms                                                               | 118 ms: 1.37x slower                                                    |
| scimark_sor              | 246 ms                                                                | 337 ms: 1.37x slower                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 176 ms: 1.38x slower                                                    |
| fannkuch                 | 546 ms                                                                | 753 ms: 1.38x slower                                                    |
| deltablue                | 8.94 ms                                                               | 12.4 ms: 1.39x slower                                                   |
| sqlglot_normalize        | 156 ms                                                                | 217 ms: 1.39x slower                                                    |
| regex_compile            | 177 ms                                                                | 248 ms: 1.40x slower                                                    |
| hexiom                   | 10.9 ms                                                               | 15.4 ms: 1.41x slower                                                   |
| pickle_pure_python       | 529 us                                                                | 754 us: 1.43x slower                                                    |
| raytrace                 | 573 ms                                                                | 821 ms: 1.43x slower                                                    |
| logging_simple           | 9.78 us                                                               | 14.1 us: 1.44x slower                                                   |
| unpickle_pure_python     | 366 us                                                                | 526 us: 1.44x slower                                                    |
| async_generators         | 452 ms                                                                | 653 ms: 1.44x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 101 ms: 1.44x slower                                                    |
| logging_format           | 10.6 us                                                               | 15.4 us: 1.45x slower                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.67 sec: 1.45x slower                                                  |
| go                       | 264 ms                                                                | 384 ms: 1.45x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 3.43 sec: 1.46x slower                                                  |
| scimark_lu               | 227 ms                                                                | 330 ms: 1.46x slower                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 110 ms: 1.46x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 52.1 ms: 1.48x slower                                                   |
| django_template          | 53.3 ms                                                               | 79.0 ms: 1.48x slower                                                   |
| mako                     | 18.9 ms                                                               | 28.4 ms: 1.50x slower                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 4.28 ms: 1.51x slower                                                   |
| telco                    | 8.49 ms                                                               | 12.9 ms: 1.52x slower                                                   |
| float                    | 135 ms                                                                | 205 ms: 1.52x slower                                                    |
| sympy_str                | 329 ms                                                                | 504 ms: 1.53x slower                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 3.72 ms: 1.55x slower                                                   |
| coverage                 | 83.6 ms                                                               | 133 ms: 1.60x slower                                                    |
| python_startup           | 11.2 ms                                                               | 18.1 ms: 1.62x slower                                                   |
| nbody                    | 166 ms                                                                | 279 ms: 1.68x slower                                                    |
| sympy_sum                | 184 ms                                                                | 310 ms: 1.68x slower                                                    |
| sympy_expand             | 543 ms                                                                | 936 ms: 1.72x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 12.1 ms: 1.76x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.18x slower                                                            |

Benchmark hidden because not significant (4): sqlite_synth, pidigits, regex_v8, pylint
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240920-3.14.0a0-342e654-NOGIL/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.169x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.21x
- 95% likely to have a slowdown of 1.19x
- 99% likely to have a slowdown of 1.16x

# Memory
- memory change: 1.33x