# Results vs. 3.10.4

- fork: python
- ref: 52caaef6d01a94962576
- machine: linux-aarch64
- commit hash: 52caaef
- commit date: 2024-08-24
- overall geometric mean: 1.19x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.53 sec                                                              | 4.10 sec: 1.16x slower                                                  |
| html5lib       | 86.5 ms                                                               | 72.5 ms: 1.19x faster                                                   |
| tornado_http   | 178 ms                                                                | 149 ms: 1.20x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 457 ms: 2.08x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 574 ms: 1.98x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.19 sec: 1.92x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 742 ms: 1.71x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.92x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 88.4 ms: 1.52x faster                                                   |
| nbody          | 166 ms                                                                | 115 ms: 1.45x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| regex_compile  | 177 ms                                                                | 190 ms: 1.08x slower                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.91 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 382 us: 1.39x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 266 us: 1.37x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 81.0 ms: 1.23x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.11x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 147 ms: 1.06x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.6 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.19x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 12.9 ms: 1.15x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.85 ms: 1.28x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                                   |
| django_template | 53.3 ms                                                               | 51.1 ms: 1.04x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 34.4 ms: 1.02x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 82.0 ms: 1.17x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.07x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 209 us: 3.16x faster                                                    |
| async_tree_none          | 950 ms                                                                | 457 ms: 2.08x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.34 ms: 2.06x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 574 ms: 1.98x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.56 ms: 1.92x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.19 sec: 1.92x faster                                                  |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 742 ms: 1.71x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.3 us: 1.66x faster                                                   |
| logging_silent           | 222 ns                                                                | 136 ns: 1.63x faster                                                    |
| raytrace                 | 573 ms                                                                | 353 ms: 1.62x faster                                                    |
| scimark_sor              | 246 ms                                                                | 154 ms: 1.59x faster                                                    |
| float                    | 135 ms                                                                | 88.4 ms: 1.52x faster                                                   |
| scimark_lu               | 227 ms                                                                | 149 ms: 1.52x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 89.0 ms: 1.51x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 638 ms: 1.48x faster                                                    |
| nbody                    | 166 ms                                                                | 115 ms: 1.45x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.29 sec: 1.43x faster                                                  |
| richards_super           | 107 ms                                                                | 77.3 ms: 1.39x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 92.1 ms: 1.39x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 382 us: 1.39x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 266 us: 1.37x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.76 ms: 1.36x faster                                                   |
| richards                 | 91.7 ms                                                               | 67.5 ms: 1.36x faster                                                   |
| comprehensions           | 33.1 us                                                               | 24.6 us: 1.35x faster                                                   |
| chaos                    | 121 ms                                                                | 90.9 ms: 1.33x faster                                                   |
| thrift                   | 1.26 ms                                                               | 955 us: 1.32x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.47 us: 1.31x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.5 ms: 1.30x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 2.19 ms: 1.30x faster                                                   |
| deepcopy                 | 511 us                                                                | 396 us: 1.29x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.24 us: 1.29x faster                                                   |
| pyflate                  | 795 ms                                                                | 622 ms: 1.28x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                  |
| spectral_norm            | 186 ms                                                                | 147 ms: 1.27x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 81.0 ms: 1.23x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.78 us: 1.21x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.9 ms: 1.20x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.32 ms: 1.20x faster                                                   |
| tornado_http             | 178 ms                                                                | 149 ms: 1.20x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 72.5 ms: 1.19x faster                                                   |
| generators               | 68.1 ms                                                               | 57.6 ms: 1.18x faster                                                   |
| go                       | 264 ms                                                                | 226 ms: 1.17x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.76 ms: 1.13x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.11x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.53 sec: 1.11x faster                                                  |
| scimark_fft              | 500 ms                                                                | 459 ms: 1.09x faster                                                    |
| fannkuch                 | 546 ms                                                                | 502 ms: 1.09x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 10.2 ms: 1.07x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.48 sec: 1.06x faster                                                  |
| regex_v8                 | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 147 ms: 1.06x faster                                                    |
| django_template          | 53.3 ms                                                               | 51.1 ms: 1.04x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 152 ms: 1.03x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 34.4 ms: 1.02x faster                                                   |
| meteor_contest           | 126 ms                                                                | 124 ms: 1.02x faster                                                    |
| json                     | 5.88 ms                                                               | 5.78 ms: 1.02x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 662 ms: 1.01x slower                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 77.7 ms: 1.03x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.33 ms: 1.03x slower                                                   |
| json_loads               | 30.9 us                                                               | 32.6 us: 1.05x slower                                                   |
| nqueens                  | 117 ms                                                                | 124 ms: 1.06x slower                                                    |
| regex_compile            | 177 ms                                                                | 190 ms: 1.08x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 29.0 ms: 1.09x slower                                                   |
| sympy_str                | 329 ms                                                                | 361 ms: 1.10x slower                                                    |
| sympy_expand             | 543 ms                                                                | 603 ms: 1.11x slower                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.28 sec: 1.12x slower                                                  |
| pprint_pformat           | 2.36 sec                                                              | 2.65 sec: 1.12x slower                                                  |
| async_generators         | 452 ms                                                                | 511 ms: 1.13x slower                                                    |
| sympy_sum                | 184 ms                                                                | 211 ms: 1.14x slower                                                    |
| python_startup           | 11.2 ms                                                               | 12.9 ms: 1.15x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.91 ms: 1.16x slower                                                   |
| docutils                 | 3.53 sec                                                              | 4.10 sec: 1.16x slower                                                  |
| genshi_xml               | 69.8 ms                                                               | 82.0 ms: 1.17x slower                                                   |
| coverage                 | 83.6 ms                                                               | 98.8 ms: 1.18x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 4.93 ms: 1.19x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.7 ms: 1.26x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.85 ms: 1.28x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                            |

Benchmark hidden because not significant (4): pylint, regex_dna, 2to3, pidigits
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240824-3.14.0a0-52caaef-JIT/bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.26x