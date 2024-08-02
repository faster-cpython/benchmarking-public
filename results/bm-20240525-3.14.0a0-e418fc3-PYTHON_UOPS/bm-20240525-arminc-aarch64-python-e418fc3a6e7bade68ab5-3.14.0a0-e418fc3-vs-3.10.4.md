# Results vs. 3.10.4

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-aarch64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.10x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 359 ms: 1.06x faster                                                    |
| chameleon      | 10.8 ms                                                               | 10.2 ms: 1.06x faster                                                   |
| html5lib       | 86.5 ms                                                               | 74.4 ms: 1.16x faster                                                   |
| tornado_http   | 178 ms                                                                | 138 ms: 1.29x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 529 ms: 1.80x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.30 sec: 1.76x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 697 ms: 1.63x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 850 ms: 1.50x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.67x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 117 ms: 1.16x faster                                                    |
| nbody          | 166 ms                                                                | 151 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.08x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.9 ms: 1.04x faster                                                   |
| regex_compile  | 177 ms                                                                | 171 ms: 1.03x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.93 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps          | 16.7 ms                                                               | 13.7 ms: 1.22x faster                                                   |
| pickle_pure_python  | 529 us                                                                | 467 us: 1.13x faster                                                    |
| xml_etree_process   | 99.5 ms                                                               | 88.2 ms: 1.13x faster                                                   |
| xml_etree_parse     | 212 ms                                                                | 191 ms: 1.11x faster                                                    |
| unpickle_list       | 6.99 us                                                               | 6.51 us: 1.07x faster                                                   |
| tomli_loads         | 3.36 sec                                                              | 3.25 sec: 1.03x faster                                                  |
| pickle_list         | 5.24 us                                                               | 5.32 us: 1.01x slower                                                   |
| xml_etree_iterparse | 156 ms                                                                | 162 ms: 1.04x slower                                                    |
| xml_etree_generate  | 123 ms                                                                | 128 ms: 1.04x slower                                                    |
| json_loads          | 30.9 us                                                               | 32.4 us: 1.05x slower                                                   |
| pickle_dict         | 35.1 us                                                               | 37.8 us: 1.08x slower                                                   |
| pickle              | 12.5 us                                                               | 13.8 us: 1.10x slower                                                   |
| unpickle            | 17.5 us                                                               | 19.7 us: 1.13x slower                                                   |
| Geometric mean      | (ref)                                                                 | 1.02x faster                                                            |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 12.8 ms: 1.14x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.57 ms: 1.24x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.19x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 17.3 ms: 1.10x faster                                                   |
| django_template | 53.3 ms                                                               | 50.1 ms: 1.07x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 37.6 ms: 1.07x slower                                                   |
| genshi_xml      | 69.8 ms                                                               | 78.5 ms: 1.12x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 226 us: 2.92x faster                                                    |
| async_tree_none          | 950 ms                                                                | 529 ms: 1.80x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.30 sec: 1.76x faster                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 8.62 ms: 1.69x faster                                                   |
| deltablue                | 8.94 ms                                                               | 5.31 ms: 1.68x faster                                                   |
| generators               | 68.1 ms                                                               | 40.7 ms: 1.67x faster                                                   |
| raytrace                 | 573 ms                                                                | 348 ms: 1.65x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 697 ms: 1.63x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 588 ms: 1.60x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 850 ms: 1.50x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.23 sec: 1.47x faster                                                  |
| richards_super           | 107 ms                                                                | 74.7 ms: 1.44x faster                                                   |
| chaos                    | 121 ms                                                                | 89.4 ms: 1.35x faster                                                   |
| richards                 | 91.7 ms                                                               | 68.2 ms: 1.34x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.36 us: 1.33x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.81 ms: 1.33x faster                                                   |
| logging_format           | 10.6 us                                                               | 8.01 us: 1.32x faster                                                   |
| go                       | 264 ms                                                                | 202 ms: 1.31x faster                                                    |
| tornado_http             | 178 ms                                                                | 138 ms: 1.29x faster                                                    |
| thrift                   | 1.26 ms                                                               | 987 us: 1.28x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 106 ms: 1.27x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 2.26 ms: 1.26x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.7 ms: 1.22x faster                                                   |
| scimark_sor              | 246 ms                                                                | 202 ms: 1.22x faster                                                    |
| pylint                   | 485 ms                                                                | 401 ms: 1.21x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.40 sec: 1.21x faster                                                  |
| coroutines               | 37.2 ms                                                               | 30.8 ms: 1.21x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 22.3 ms: 1.18x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 74.4 ms: 1.16x faster                                                   |
| dask                     | 450 ms                                                                | 389 ms: 1.16x faster                                                    |
| float                    | 135 ms                                                                | 117 ms: 1.16x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.39 ms: 1.14x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 467 us: 1.13x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 88.2 ms: 1.13x faster                                                   |
| logging_silent           | 222 ns                                                                | 197 ns: 1.12x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 66.1 ms: 1.11x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 191 ms: 1.11x faster                                                    |
| nbody                    | 166 ms                                                                | 151 ms: 1.10x faster                                                    |
| mako                     | 18.9 ms                                                               | 17.3 ms: 1.10x faster                                                   |
| scimark_lu               | 227 ms                                                                | 211 ms: 1.08x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 119 ms: 1.08x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.51 us: 1.07x faster                                                   |
| django_template          | 53.3 ms                                                               | 50.1 ms: 1.07x faster                                                   |
| 2to3                     | 381 ms                                                                | 359 ms: 1.06x faster                                                    |
| chameleon                | 10.8 ms                                                               | 10.2 ms: 1.06x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.93 us: 1.05x faster                                                   |
| sympy_sum                | 184 ms                                                                | 176 ms: 1.05x faster                                                    |
| pyflate                  | 795 ms                                                                | 760 ms: 1.05x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 149 ms: 1.04x faster                                                    |
| comprehensions           | 33.1 us                                                               | 31.8 us: 1.04x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 30.9 ms: 1.04x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 72.9 ms: 1.03x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 3.25 sec: 1.03x faster                                                  |
| regex_compile            | 177 ms                                                                | 171 ms: 1.03x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.60 sec: 1.03x faster                                                  |
| sympy_str                | 329 ms                                                                | 321 ms: 1.02x faster                                                    |
| sympy_expand             | 543 ms                                                                | 533 ms: 1.02x faster                                                    |
| json                     | 5.88 ms                                                               | 5.83 ms: 1.01x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 662 ms: 1.01x slower                                                    |
| pickle_list              | 5.24 us                                                               | 5.32 us: 1.01x slower                                                   |
| hexiom                   | 10.9 ms                                                               | 11.3 ms: 1.04x slower                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 162 ms: 1.04x slower                                                    |
| xml_etree_generate       | 123 ms                                                                | 128 ms: 1.04x slower                                                    |
| spectral_norm            | 186 ms                                                                | 194 ms: 1.04x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.4 us: 1.05x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.47 sec: 1.05x slower                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 1.21 sec: 1.05x slower                                                  |
| create_gc_cycles         | 2.26 ms                                                               | 2.39 ms: 1.06x slower                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 4.88 us: 1.06x slower                                                   |
| meteor_contest           | 126 ms                                                                | 135 ms: 1.07x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 37.6 ms: 1.07x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 37.8 us: 1.08x slower                                                   |
| flaskblogging            | 4.83 ms                                                               | 5.22 ms: 1.08x slower                                                   |
| deepcopy                 | 511 us                                                                | 553 us: 1.08x slower                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.35 ms: 1.10x slower                                                   |
| fannkuch                 | 546 ms                                                                | 598 ms: 1.10x slower                                                    |
| pickle                   | 12.5 us                                                               | 13.8 us: 1.10x slower                                                   |
| scimark_fft              | 500 ms                                                                | 558 ms: 1.12x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 78.5 ms: 1.12x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.7 us: 1.13x slower                                                   |
| async_generators         | 452 ms                                                                | 515 ms: 1.14x slower                                                    |
| python_startup           | 11.2 ms                                                               | 12.8 ms: 1.14x slower                                                   |
| nqueens                  | 117 ms                                                                | 136 ms: 1.16x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.93 ms: 1.16x slower                                                   |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                                    |
| deepcopy_memo            | 61.7 us                                                               | 75.9 us: 1.23x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.57 ms: 1.24x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.28 ms: 1.27x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.8 ms: 1.27x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.10x faster                                                            |

Benchmark hidden because not significant (5): regex_dna, sympy_integrate, unpickle_pure_python, docutils, pidigits
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240525-3.14.0a0-e418fc3-PYTHON_UOPS/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.15x