# Results vs. 3.10.4

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: linux-aarch64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.333x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 293 ms: 1.30x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.05 sec: 1.16x faster                                                  |
| html5lib       | 86.5 ms                                                               | 63.1 ms: 1.37x faster                                                   |
| tornado_http   | 178 ms                                                                | 124 ms: 1.43x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 423 ms: 2.24x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 556 ms: 2.04x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.13 sec: 2.02x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 733 ms: 1.73x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.00x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 109 ms: 1.52x faster                                                    |
| float          | 135 ms                                                                | 92.7 ms: 1.45x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.41x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| regex_dna      | 257 ms                                                                | 252 ms: 1.02x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 361 us: 1.46x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 255 us: 1.43x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 78.5 ms: 1.27x faster                                                   |
| tomli_loads          | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 186 ms: 1.14x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.28 us: 1.11x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.11x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.06x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.5 us: 1.05x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 37.5 us: 1.07x slower                                                   |
| pickle               | 12.5 us                                                               | 13.5 us: 1.08x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.6 us: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                            |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.83 ms: 1.28x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.23x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                   |
| django_template | 53.3 ms                                                               | 41.7 ms: 1.28x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.6 ms: 1.15x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 192 us: 3.44x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.91 ms: 2.29x faster                                                   |
| async_tree_none          | 950 ms                                                                | 423 ms: 2.24x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.02 ms: 2.07x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 556 ms: 2.04x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.13 sec: 2.02x faster                                                  |
| generators               | 68.1 ms                                                               | 35.1 ms: 1.94x faster                                                   |
| go                       | 264 ms                                                                | 138 ms: 1.92x faster                                                    |
| raytrace                 | 573 ms                                                                | 301 ms: 1.90x faster                                                    |
| richards_super           | 107 ms                                                                | 59.5 ms: 1.80x faster                                                   |
| chaos                    | 121 ms                                                                | 68.5 ms: 1.77x faster                                                   |
| richards                 | 91.7 ms                                                               | 52.8 ms: 1.74x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 733 ms: 1.73x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.42 ms: 1.69x faster                                                   |
| scimark_lu               | 227 ms                                                                | 134 ms: 1.69x faster                                                    |
| logging_silent           | 222 ns                                                                | 133 ns: 1.68x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 574 ms: 1.65x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.64x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 38.0 us: 1.62x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.4 us: 1.62x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 83.4 ms: 1.61x faster                                                   |
| scimark_sor              | 246 ms                                                                | 158 ms: 1.56x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 82.0 ms: 1.56x faster                                                   |
| deepcopy                 | 511 us                                                                | 332 us: 1.54x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.17 ms: 1.52x faster                                                   |
| nbody                    | 166 ms                                                                | 109 ms: 1.52x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.20 sec: 1.49x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 361 us: 1.46x faster                                                    |
| float                    | 135 ms                                                                | 92.7 ms: 1.45x faster                                                   |
| tornado_http             | 178 ms                                                                | 124 ms: 1.43x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 255 us: 1.43x faster                                                    |
| regex_compile            | 177 ms                                                                | 125 ms: 1.41x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                   |
| logging_simple           | 9.78 us                                                               | 6.95 us: 1.41x faster                                                   |
| pyflate                  | 795 ms                                                                | 566 ms: 1.40x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.62 us: 1.39x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.37x faster                                                  |
| html5lib                 | 86.5 ms                                                               | 63.1 ms: 1.37x faster                                                   |
| thrift                   | 1.26 ms                                                               | 931 us: 1.35x faster                                                    |
| pylint                   | 485 ms                                                                | 359 ms: 1.35x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.45 us: 1.33x faster                                                   |
| spectral_norm            | 186 ms                                                                | 140 ms: 1.33x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.6 ms: 1.30x faster                                                   |
| 2to3                     | 381 ms                                                                | 293 ms: 1.30x faster                                                    |
| sympy_sum                | 184 ms                                                                | 143 ms: 1.29x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.24 ms: 1.28x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.8 ms: 1.28x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                   |
| django_template          | 53.3 ms                                                               | 41.7 ms: 1.28x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 78.5 ms: 1.27x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 914 ms: 1.26x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.0 ms: 1.25x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 58.8 ms: 1.25x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.89 sec: 1.25x faster                                                  |
| sympy_str                | 329 ms                                                                | 265 ms: 1.24x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 127 ms: 1.23x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 62.5 ms: 1.21x faster                                                   |
| fannkuch                 | 546 ms                                                                | 456 ms: 1.20x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.38 ms: 1.19x faster                                                   |
| nqueens                  | 117 ms                                                                | 98.6 ms: 1.19x faster                                                   |
| sympy_expand             | 543 ms                                                                | 464 ms: 1.17x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.05 sec: 1.16x faster                                                  |
| genshi_xml               | 69.8 ms                                                               | 60.6 ms: 1.15x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 186 ms: 1.14x faster                                                    |
| scimark_fft              | 500 ms                                                                | 443 ms: 1.13x faster                                                    |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.13x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.28 us: 1.11x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.34 sec: 1.11x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.11x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.90 us: 1.06x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.06x faster                                                    |
| json                     | 5.88 ms                                                               | 5.70 ms: 1.03x faster                                                   |
| regex_dna                | 257 ms                                                                | 252 ms: 1.02x faster                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.30 ms: 1.02x slower                                                   |
| json_loads               | 30.9 us                                                               | 32.5 us: 1.05x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 37.5 us: 1.07x slower                                                   |
| async_generators         | 452 ms                                                                | 487 ms: 1.08x slower                                                    |
| pickle                   | 12.5 us                                                               | 13.5 us: 1.08x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.6 us: 1.12x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.99 ms: 1.18x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 4.91 ms: 1.18x slower                                                   |
| coverage                 | 83.6 ms                                                               | 99.5 ms: 1.19x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.83 ms: 1.28x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.32x faster                                                            |

Benchmark hidden because not significant (3): pidigits, asyncio_websockets, pickle_list
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240907-3.14.0a0-11fa119/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.333x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.15x