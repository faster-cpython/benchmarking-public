# Results vs. 3.10.4

- fork: python
- ref: e256a7590a0149feadfe
- machine: linux-aarch64
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.32x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 295 ms: 1.29x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.03 sec: 1.17x faster                                                  |
| html5lib       | 86.5 ms                                                               | 66.4 ms: 1.30x faster                                                   |
| tornado_http   | 178 ms                                                                | 124 ms: 1.44x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 417 ms: 2.27x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 555 ms: 2.04x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.14 sec: 2.00x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 722 ms: 1.76x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.01x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 111 ms: 1.50x faster                                                    |
| float          | 135 ms                                                                | 92.9 ms: 1.45x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.41x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                   |
| regex_dna      | 257 ms                                                                | 247 ms: 1.04x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.93 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 361 us: 1.47x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 255 us: 1.44x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 13.1 ms: 1.27x faster                                                   |
| tomli_loads          | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 80.0 ms: 1.24x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.10x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 193 ms: 1.10x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.63 us: 1.05x faster                                                   |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.05x faster                                                    |
| json_loads           | 30.9 us                                                               | 31.5 us: 1.02x slower                                                   |
| pickle               | 12.5 us                                                               | 13.6 us: 1.09x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 38.3 us: 1.09x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.4 us: 1.11x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                            |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 12.9 ms: 1.16x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.57 ms: 1.24x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.20x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.5 ms: 1.40x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 26.9 ms: 1.31x faster                                                   |
| django_template | 53.3 ms                                                               | 41.5 ms: 1.28x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.0 ms: 1.16x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.29x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 196 us: 3.38x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.88 ms: 2.30x faster                                                   |
| async_tree_none          | 950 ms                                                                | 417 ms: 2.27x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 555 ms: 2.04x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.20 ms: 2.02x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.14 sec: 2.00x faster                                                  |
| generators               | 68.1 ms                                                               | 34.7 ms: 1.96x faster                                                   |
| go                       | 264 ms                                                                | 138 ms: 1.92x faster                                                    |
| raytrace                 | 573 ms                                                                | 303 ms: 1.89x faster                                                    |
| richards_super           | 107 ms                                                                | 58.9 ms: 1.82x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 722 ms: 1.76x faster                                                    |
| chaos                    | 121 ms                                                                | 68.7 ms: 1.76x faster                                                   |
| richards                 | 91.7 ms                                                               | 52.4 ms: 1.75x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 556 ms: 1.70x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.42 ms: 1.69x faster                                                   |
| scimark_lu               | 227 ms                                                                | 134 ms: 1.69x faster                                                    |
| logging_silent           | 222 ns                                                                | 133 ns: 1.67x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.64x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 37.6 us: 1.64x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 82.4 ms: 1.63x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.7 us: 1.60x faster                                                   |
| scimark_sor              | 246 ms                                                                | 158 ms: 1.56x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 82.2 ms: 1.55x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.10 ms: 1.54x faster                                                   |
| deepcopy                 | 511 us                                                                | 334 us: 1.53x faster                                                    |
| nbody                    | 166 ms                                                                | 111 ms: 1.50x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.20 sec: 1.49x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 361 us: 1.47x faster                                                    |
| float                    | 135 ms                                                                | 92.9 ms: 1.45x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 255 us: 1.44x faster                                                    |
| tornado_http             | 178 ms                                                                | 124 ms: 1.44x faster                                                    |
| logging_simple           | 9.78 us                                                               | 6.89 us: 1.42x faster                                                   |
| regex_compile            | 177 ms                                                                | 125 ms: 1.41x faster                                                    |
| pyflate                  | 795 ms                                                                | 564 ms: 1.41x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.56 us: 1.40x faster                                                   |
| mako                     | 18.9 ms                                                               | 13.5 ms: 1.40x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.22 sec: 1.39x faster                                                  |
| thrift                   | 1.26 ms                                                               | 928 us: 1.36x faster                                                    |
| pylint                   | 485 ms                                                                | 360 ms: 1.35x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.48 us: 1.32x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.3 ms: 1.31x faster                                                   |
| sympy_sum                | 184 ms                                                                | 140 ms: 1.31x faster                                                    |
| spectral_norm            | 186 ms                                                                | 142 ms: 1.31x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 26.9 ms: 1.31x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 66.4 ms: 1.30x faster                                                   |
| 2to3                     | 381 ms                                                                | 295 ms: 1.29x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.23 ms: 1.29x faster                                                   |
| django_template          | 53.3 ms                                                               | 41.5 ms: 1.28x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.8 ms: 1.27x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.1 ms: 1.27x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                                  |
| pathlib                  | 26.3 ms                                                               | 20.9 ms: 1.26x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 58.9 ms: 1.25x faster                                                   |
| sympy_str                | 329 ms                                                                | 264 ms: 1.25x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.89 sec: 1.25x faster                                                  |
| xml_etree_process        | 99.5 ms                                                               | 80.0 ms: 1.24x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 923 ms: 1.24x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 127 ms: 1.23x faster                                                    |
| fannkuch                 | 546 ms                                                                | 458 ms: 1.19x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 63.6 ms: 1.19x faster                                                   |
| sympy_expand             | 543 ms                                                                | 460 ms: 1.18x faster                                                    |
| nqueens                  | 117 ms                                                                | 100 ms: 1.17x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.03 sec: 1.17x faster                                                  |
| genshi_xml               | 69.8 ms                                                               | 60.0 ms: 1.16x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.56 ms: 1.16x faster                                                   |
| meteor_contest           | 126 ms                                                                | 111 ms: 1.13x faster                                                    |
| scimark_fft              | 500 ms                                                                | 443 ms: 1.13x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.35 sec: 1.10x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.10x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 193 ms: 1.10x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.87 us: 1.06x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.63 us: 1.05x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.05x faster                                                    |
| json                     | 5.88 ms                                                               | 5.58 ms: 1.05x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                   |
| regex_dna                | 257 ms                                                                | 247 ms: 1.04x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 660 ms: 1.01x slower                                                    |
| json_loads               | 30.9 us                                                               | 31.5 us: 1.02x slower                                                   |
| async_generators         | 452 ms                                                                | 485 ms: 1.07x slower                                                    |
| pickle                   | 12.5 us                                                               | 13.6 us: 1.09x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 38.3 us: 1.09x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.4 us: 1.11x slower                                                   |
| python_startup           | 11.2 ms                                                               | 12.9 ms: 1.16x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.93 ms: 1.16x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.97 ms: 1.17x slower                                                   |
| coverage                 | 83.6 ms                                                               | 98.5 ms: 1.18x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.13 ms: 1.23x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.57 ms: 1.24x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.32x faster                                                            |

Benchmark hidden because not significant (3): pidigits, create_gc_cycles, pickle_list
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240924-3.14.0a0-e256a75/bm-20240924-arminc-aarch64-python-e256a7590a0149feadfe-3.14.0a0-e256a75.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.14x