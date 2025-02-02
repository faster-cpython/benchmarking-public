# Results vs. 3.10.4

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: linux-aarch64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.329x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 297 ms: 1.28x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.05 sec: 1.16x faster                                                  |
| html5lib       | 86.5 ms                                                               | 65.6 ms: 1.32x faster                                                   |
| tornado_http   | 178 ms                                                                | 129 ms: 1.38x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 421 ms: 2.26x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 562 ms: 2.02x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.14 sec: 2.01x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 720 ms: 1.77x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.00x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 110 ms: 1.50x faster                                                    |
| float          | 135 ms                                                                | 92.9 ms: 1.45x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 127 ms: 1.39x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.5 ms: 1.05x faster                                                   |
| regex_dna      | 257 ms                                                                | 255 ms: 1.01x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.95 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 253 us: 1.45x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 373 us: 1.42x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 81.6 ms: 1.22x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 191 ms: 1.11x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.09x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.40 us: 1.09x faster                                                   |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| pickle_list          | 5.24 us                                                               | 5.20 us: 1.01x faster                                                   |
| json_loads           | 30.9 us                                                               | 31.7 us: 1.02x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 38.0 us: 1.08x slower                                                   |
| pickle               | 12.5 us                                                               | 13.7 us: 1.10x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.5 us: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.69 ms: 1.26x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.5 ms: 1.40x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.4 ms: 1.29x faster                                                   |
| django_template | 53.3 ms                                                               | 42.3 ms: 1.26x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 192 us: 3.45x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.87 ms: 2.31x faster                                                   |
| async_tree_none          | 950 ms                                                                | 421 ms: 2.26x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.11 ms: 2.04x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 562 ms: 2.02x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.14 sec: 2.01x faster                                                  |
| generators               | 68.1 ms                                                               | 34.9 ms: 1.95x faster                                                   |
| go                       | 264 ms                                                                | 139 ms: 1.91x faster                                                    |
| raytrace                 | 573 ms                                                                | 301 ms: 1.90x faster                                                    |
| richards_super           | 107 ms                                                                | 60.1 ms: 1.78x faster                                                   |
| chaos                    | 121 ms                                                                | 68.4 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 720 ms: 1.77x faster                                                    |
| richards                 | 91.7 ms                                                               | 52.8 ms: 1.73x faster                                                   |
| scimark_lu               | 227 ms                                                                | 135 ms: 1.69x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.43 ms: 1.68x faster                                                   |
| logging_silent           | 222 ns                                                                | 133 ns: 1.67x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 567 ms: 1.67x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.5 us: 1.64x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 81.9 ms: 1.64x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 1.75 ms: 1.63x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.5 us: 1.62x faster                                                   |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.56x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 82.1 ms: 1.56x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.17 ms: 1.52x faster                                                   |
| deepcopy                 | 511 us                                                                | 337 us: 1.52x faster                                                    |
| nbody                    | 166 ms                                                                | 110 ms: 1.50x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.48x faster                                                  |
| float                    | 135 ms                                                                | 92.9 ms: 1.45x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 253 us: 1.45x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 373 us: 1.42x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.5 ms: 1.40x faster                                                   |
| regex_compile            | 177 ms                                                                | 127 ms: 1.39x faster                                                    |
| tornado_http             | 178 ms                                                                | 129 ms: 1.38x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.37x faster                                                  |
| pyflate                  | 795 ms                                                                | 580 ms: 1.37x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.18 us: 1.36x faster                                                   |
| thrift                   | 1.26 ms                                                               | 931 us: 1.35x faster                                                    |
| pylint                   | 485 ms                                                                | 360 ms: 1.35x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.90 us: 1.34x faster                                                   |
| spectral_norm            | 186 ms                                                                | 140 ms: 1.33x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 65.6 ms: 1.32x faster                                                   |
| sympy_sum                | 184 ms                                                                | 142 ms: 1.29x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.23 ms: 1.29x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.9 ms: 1.29x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.57 us: 1.29x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.4 ms: 1.29x faster                                                   |
| 2to3                     | 381 ms                                                                | 297 ms: 1.28x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.7 ms: 1.28x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                                  |
| django_template          | 53.3 ms                                                               | 42.3 ms: 1.26x faster                                                   |
| sympy_str                | 329 ms                                                                | 263 ms: 1.25x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.1 ms: 1.24x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 59.2 ms: 1.24x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 926 ms: 1.24x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.91 sec: 1.24x faster                                                  |
| sqlglot_normalize        | 156 ms                                                                | 127 ms: 1.23x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 81.6 ms: 1.22x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 62.4 ms: 1.21x faster                                                   |
| nqueens                  | 117 ms                                                                | 98.4 ms: 1.19x faster                                                   |
| fannkuch                 | 546 ms                                                                | 462 ms: 1.18x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.47 ms: 1.18x faster                                                   |
| sympy_expand             | 543 ms                                                                | 462 ms: 1.17x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.05 sec: 1.16x faster                                                  |
| genshi_xml               | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                                   |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.13x faster                                                    |
| scimark_fft              | 500 ms                                                                | 445 ms: 1.12x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 191 ms: 1.11x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.37 sec: 1.10x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.09x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.40 us: 1.09x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.81 us: 1.08x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 30.5 ms: 1.05x faster                                                   |
| json                     | 5.88 ms                                                               | 5.59 ms: 1.05x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| regex_dna                | 257 ms                                                                | 255 ms: 1.01x faster                                                    |
| pickle_list              | 5.24 us                                                               | 5.20 us: 1.01x faster                                                   |
| json_loads               | 30.9 us                                                               | 31.7 us: 1.02x slower                                                   |
| async_generators         | 452 ms                                                                | 479 ms: 1.06x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 38.0 us: 1.08x slower                                                   |
| pickle                   | 12.5 us                                                               | 13.7 us: 1.10x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.5 us: 1.12x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.95 ms: 1.16x slower                                                   |
| coverage                 | 83.6 ms                                                               | 97.6 ms: 1.17x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.2 ms: 1.21x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.09 ms: 1.22x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.69 ms: 1.26x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.31x faster                                                            |

Benchmark hidden because not significant (3): pidigits, create_gc_cycles, asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-arminc-aarch64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.329x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.14x