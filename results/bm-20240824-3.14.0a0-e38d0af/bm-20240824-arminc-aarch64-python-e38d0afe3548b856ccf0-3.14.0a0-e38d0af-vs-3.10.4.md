# Results vs. 3.10.4

- fork: python
- ref: e38d0afe3548b856ccf0
- machine: linux-aarch64
- commit hash: e38d0af
- commit date: 2024-08-24
- overall geometric mean: 1.329x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 295 ms: 1.29x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.06 sec: 1.15x faster                                                  |
| html5lib       | 86.5 ms                                                               | 67.0 ms: 1.29x faster                                                   |
| tornado_http   | 178 ms                                                                | 129 ms: 1.39x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 427 ms: 2.22x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.13 sec: 2.02x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 563 ms: 2.01x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 729 ms: 1.75x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.99x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 109 ms: 1.52x faster                                                    |
| float          | 135 ms                                                                | 91.9 ms: 1.47x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 127 ms: 1.39x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.6 ms: 1.05x faster                                                   |
| regex_dna      | 257 ms                                                                | 247 ms: 1.04x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.83 ms: 1.14x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 363 us: 1.46x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 255 us: 1.43x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.3 ms: 1.24x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 190 ms: 1.12x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.05x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.9 us: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.68 ms: 1.26x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.21x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                   |
| django_template | 53.3 ms                                                               | 42.1 ms: 1.27x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.6 ms: 1.15x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 193 us: 3.42x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.91 ms: 2.29x faster                                                   |
| async_tree_none          | 950 ms                                                                | 427 ms: 2.22x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.13 ms: 2.04x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.13 sec: 2.02x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 563 ms: 2.01x faster                                                    |
| generators               | 68.1 ms                                                               | 35.2 ms: 1.94x faster                                                   |
| raytrace                 | 573 ms                                                                | 303 ms: 1.89x faster                                                    |
| richards_super           | 107 ms                                                                | 59.4 ms: 1.81x faster                                                   |
| chaos                    | 121 ms                                                                | 68.6 ms: 1.76x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 729 ms: 1.75x faster                                                    |
| richards                 | 91.7 ms                                                               | 53.3 ms: 1.72x faster                                                   |
| logging_silent           | 222 ns                                                                | 131 ns: 1.70x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.43 ms: 1.69x faster                                                   |
| scimark_lu               | 227 ms                                                                | 136 ms: 1.66x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 572 ms: 1.65x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.75 ms: 1.63x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 38.0 us: 1.63x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.4 us: 1.62x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 83.1 ms: 1.61x faster                                                   |
| scimark_sor              | 246 ms                                                                | 156 ms: 1.58x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 82.3 ms: 1.55x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.10 ms: 1.54x faster                                                   |
| nbody                    | 166 ms                                                                | 109 ms: 1.52x faster                                                    |
| deepcopy                 | 511 us                                                                | 338 us: 1.51x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.49x faster                                                  |
| float                    | 135 ms                                                                | 91.9 ms: 1.47x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 363 us: 1.46x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 255 us: 1.43x faster                                                    |
| pyflate                  | 795 ms                                                                | 562 ms: 1.41x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                   |
| logging_simple           | 9.78 us                                                               | 6.96 us: 1.40x faster                                                   |
| regex_compile            | 177 ms                                                                | 127 ms: 1.39x faster                                                    |
| tornado_http             | 178 ms                                                                | 129 ms: 1.39x faster                                                    |
| go                       | 264 ms                                                                | 192 ms: 1.37x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.74 us: 1.37x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.24 sec: 1.36x faster                                                  |
| thrift                   | 1.26 ms                                                               | 931 us: 1.35x faster                                                    |
| pylint                   | 485 ms                                                                | 361 ms: 1.35x faster                                                    |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.32x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.6 ms: 1.30x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.54 us: 1.30x faster                                                   |
| 2to3                     | 381 ms                                                                | 295 ms: 1.29x faster                                                    |
| sympy_sum                | 184 ms                                                                | 142 ms: 1.29x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 67.0 ms: 1.29x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.24 ms: 1.29x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.8 ms: 1.28x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| genshi_text              | 35.2 ms                                                               | 27.7 ms: 1.27x faster                                                   |
| django_template          | 53.3 ms                                                               | 42.1 ms: 1.27x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                   |
| sympy_str                | 329 ms                                                                | 264 ms: 1.24x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 80.3 ms: 1.24x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.3 ms: 1.23x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 936 ms: 1.23x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.93 sec: 1.22x faster                                                  |
| sqlglot_normalize        | 156 ms                                                                | 128 ms: 1.21x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 62.3 ms: 1.21x faster                                                   |
| fannkuch                 | 546 ms                                                                | 460 ms: 1.19x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.44 ms: 1.18x faster                                                   |
| sympy_expand             | 543 ms                                                                | 462 ms: 1.18x faster                                                    |
| nqueens                  | 117 ms                                                                | 100 ms: 1.17x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.06 sec: 1.15x faster                                                  |
| genshi_xml               | 69.8 ms                                                               | 60.6 ms: 1.15x faster                                                   |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.13x faster                                                    |
| scimark_fft              | 500 ms                                                                | 444 ms: 1.13x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 190 ms: 1.12x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.34 sec: 1.11x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.6 ms: 1.05x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.05x faster                                                    |
| regex_dna                | 257 ms                                                                | 247 ms: 1.04x faster                                                    |
| json                     | 5.88 ms                                                               | 5.72 ms: 1.03x faster                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.31 ms: 1.02x slower                                                   |
| json_loads               | 30.9 us                                                               | 32.9 us: 1.06x slower                                                   |
| async_generators         | 452 ms                                                                | 485 ms: 1.07x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.83 ms: 1.14x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.84 ms: 1.16x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 4.89 ms: 1.18x slower                                                   |
| coverage                 | 83.6 ms                                                               | 98.9 ms: 1.18x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.68 ms: 1.26x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.34x faster                                                            |

Benchmark hidden because not significant (2): pidigits, asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240824-3.14.0a0-e38d0af/bm-20240824-arminc-aarch64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.329x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.15x