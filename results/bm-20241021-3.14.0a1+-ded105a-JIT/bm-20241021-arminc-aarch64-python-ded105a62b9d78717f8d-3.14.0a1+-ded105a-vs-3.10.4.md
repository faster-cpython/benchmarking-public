# Results vs. 3.10.4

- fork: python
- ref: ded105a62b9d78717f8d
- machine: linux-aarch64
- commit hash: ded105a
- commit date: 2024-10-21
- overall geometric mean: 1.10x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 3.53 sec                                                              | 3.61 sec: 1.02x slower                                                   |
| html5lib       | 86.5 ms                                                               | 72.5 ms: 1.19x faster                                                    |
| tornado_http   | 178 ms                                                                | 148 ms: 1.21x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                             |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 471 ms: 2.02x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.18 sec: 1.94x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 597 ms: 1.90x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 758 ms: 1.68x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.88x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 114 ms: 1.45x faster                                                     |
| float          | 135 ms                                                                | 97.0 ms: 1.39x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 31.8 ms: 1.01x faster                                                    |
| regex_compile  | 177 ms                                                                | 175 ms: 1.01x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 5.00 ms: 1.18x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 390 us: 1.36x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 270 us: 1.35x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 81.4 ms: 1.22x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.3 ms: 1.16x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 187 ms: 1.13x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.08x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                     |
| json_loads           | 30.9 us                                                               | 31.5 us: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.17x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.77 ms: 1.27x slower                                                    |
| python_startup         | 11.2 ms                                                               | 14.5 ms: 1.30x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.29x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                    |
| genshi_text    | 35.2 ms                                                               | 34.2 ms: 1.03x faster                                                    |
| genshi_xml     | 69.8 ms                                                               | 84.1 ms: 1.20x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 217 us: 3.05x faster                                                     |
| async_tree_none          | 950 ms                                                                | 471 ms: 2.02x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.57 ms: 1.96x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.18 sec: 1.94x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 597 ms: 1.90x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 758 ms: 1.68x faster                                                     |
| logging_silent           | 222 ns                                                                | 133 ns: 1.67x faster                                                     |
| raytrace                 | 573 ms                                                                | 352 ms: 1.63x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 38.7 us: 1.59x faster                                                    |
| scimark_sor              | 246 ms                                                                | 155 ms: 1.59x faster                                                     |
| richards_super           | 107 ms                                                                | 69.3 ms: 1.55x faster                                                    |
| scimark_lu               | 227 ms                                                                | 150 ms: 1.51x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 90.2 ms: 1.49x faster                                                    |
| nbody                    | 166 ms                                                                | 114 ms: 1.45x faster                                                     |
| richards                 | 91.7 ms                                                               | 63.1 ms: 1.45x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 89.6 ms: 1.43x faster                                                    |
| go                       | 264 ms                                                                | 187 ms: 1.41x faster                                                     |
| chaos                    | 121 ms                                                                | 85.8 ms: 1.41x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.71 ms: 1.41x faster                                                    |
| float                    | 135 ms                                                                | 97.0 ms: 1.39x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 390 us: 1.36x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 270 us: 1.35x faster                                                     |
| deepcopy                 | 511 us                                                                | 377 us: 1.35x faster                                                     |
| comprehensions           | 33.1 us                                                               | 24.7 us: 1.34x faster                                                    |
| logging_format           | 10.6 us                                                               | 8.13 us: 1.30x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.54 us: 1.30x faster                                                    |
| thrift                   | 1.26 ms                                                               | 973 us: 1.30x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 2.21 ms: 1.28x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.0 ms: 1.28x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                   |
| pyflate                  | 795 ms                                                                | 623 ms: 1.28x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 81.4 ms: 1.22x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.8 ms: 1.21x faster                                                    |
| tornado_http             | 178 ms                                                                | 148 ms: 1.21x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 72.5 ms: 1.19x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.92 us: 1.17x faster                                                    |
| spectral_norm            | 186 ms                                                                | 160 ms: 1.17x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.3 ms: 1.16x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.37 ms: 1.16x faster                                                    |
| generators               | 68.1 ms                                                               | 59.0 ms: 1.15x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 187 ms: 1.13x faster                                                     |
| scimark_fft              | 500 ms                                                                | 456 ms: 1.10x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.54 sec: 1.10x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.08x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.11 ms: 1.07x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 10.3 ms: 1.06x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.51 sec: 1.05x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                     |
| json                     | 5.88 ms                                                               | 5.65 ms: 1.04x faster                                                    |
| fannkuch                 | 546 ms                                                                | 526 ms: 1.04x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 34.2 ms: 1.03x faster                                                    |
| meteor_contest           | 126 ms                                                                | 123 ms: 1.03x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 31.8 ms: 1.01x faster                                                    |
| regex_compile            | 177 ms                                                                | 175 ms: 1.01x faster                                                     |
| sqlglot_normalize        | 156 ms                                                                | 157 ms: 1.01x slower                                                     |
| json_loads               | 30.9 us                                                               | 31.5 us: 1.02x slower                                                    |
| docutils                 | 3.53 sec                                                              | 3.61 sec: 1.02x slower                                                   |
| dulwich_log              | 73.5 ms                                                               | 76.2 ms: 1.04x slower                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.20 sec: 1.05x slower                                                   |
| nqueens                  | 117 ms                                                                | 123 ms: 1.05x slower                                                     |
| pprint_pformat           | 2.36 sec                                                              | 2.53 sec: 1.07x slower                                                   |
| sympy_str                | 329 ms                                                                | 357 ms: 1.09x slower                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 82.4 ms: 1.09x slower                                                    |
| sympy_expand             | 543 ms                                                                | 596 ms: 1.10x slower                                                     |
| telco                    | 8.49 ms                                                               | 9.41 ms: 1.11x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 29.9 ms: 1.13x slower                                                    |
| async_generators         | 452 ms                                                                | 513 ms: 1.13x slower                                                     |
| sympy_sum                | 184 ms                                                                | 216 ms: 1.17x slower                                                     |
| coverage                 | 83.6 ms                                                               | 98.3 ms: 1.18x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 5.00 ms: 1.18x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 84.1 ms: 1.20x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.77 ms: 1.27x slower                                                    |
| python_startup           | 11.2 ms                                                               | 14.5 ms: 1.30x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.38 ms: 1.54x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.65 ms: 1.62x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 2.31 sec: 159.05x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.10x faster                                                             |

Benchmark hidden because not significant (6): pylint, regex_dna, pidigits, asyncio_websockets, django_template, 2to3
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241021-3.14.0a1+-ded105a-JIT/bm-20241021-arminc-aarch64-python-ded105a62b9d78717f8d-3.14.0a1+-ded105a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.37x