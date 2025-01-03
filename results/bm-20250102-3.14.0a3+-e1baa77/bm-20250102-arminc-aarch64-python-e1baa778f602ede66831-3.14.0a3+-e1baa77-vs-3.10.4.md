# Results vs. 3.10.4

- fork: python
- ref: e1baa778f602ede66831
- machine: linux-aarch64
- commit hash: e1baa77
- commit date: 2025-01-02
- overall geometric mean: 1.313x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 307 ms: 1.24x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.02 sec: 1.17x faster                                                   |
| html5lib       | 86.5 ms                                                               | 65.5 ms: 1.32x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 904 ms: 2.53x faster                                                     |
| async_tree_none         | 950 ms                                                                | 393 ms: 2.42x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 502 ms: 2.26x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 677 ms: 1.88x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.26x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 92.1 ms: 1.46x faster                                                    |
| nbody          | 166 ms                                                                | 122 ms: 1.36x faster                                                     |
| pidigits       | 235 ms                                                                | 246 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 127 ms: 1.39x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 3.99 ms: 1.07x faster                                                    |
| regex_dna      | 257 ms                                                                | 250 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 382 us: 1.39x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 267 us: 1.37x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.59 sec: 1.30x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 83.1 ms: 1.20x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 182 ms: 1.16x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.5 ms: 1.15x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.11x faster                                                     |
| json_loads           | 30.9 us                                                               | 32.5 us: 1.05x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.97 ms: 1.30x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.37x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.4 ms: 1.31x faster                                                    |
| django_template | 53.3 ms                                                               | 41.2 ms: 1.30x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.4 ms: 1.28x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 64.3 ms: 1.09x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.24x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 198 us: 3.34x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 904 ms: 2.53x faster                                                     |
| async_tree_none          | 950 ms                                                                | 393 ms: 2.42x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 502 ms: 2.26x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.97 ms: 2.25x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 677 ms: 1.88x faster                                                     |
| go                       | 264 ms                                                                | 143 ms: 1.84x faster                                                     |
| generators               | 68.1 ms                                                               | 37.9 ms: 1.79x faster                                                    |
| raytrace                 | 573 ms                                                                | 323 ms: 1.77x faster                                                     |
| richards                 | 91.7 ms                                                               | 52.0 ms: 1.76x faster                                                    |
| richards_super           | 107 ms                                                                | 61.8 ms: 1.73x faster                                                    |
| chaos                    | 121 ms                                                                | 71.3 ms: 1.70x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.44 ms: 1.67x faster                                                    |
| scimark_lu               | 227 ms                                                                | 140 ms: 1.63x faster                                                     |
| pylint                   | 485 ms                                                                | 307 ms: 1.58x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 1.80 ms: 1.58x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 85.3 ms: 1.57x faster                                                    |
| logging_silent           | 222 ns                                                                | 142 ns: 1.57x faster                                                     |
| scimark_sor              | 246 ms                                                                | 159 ms: 1.54x faster                                                     |
| comprehensions           | 33.1 us                                                               | 21.5 us: 1.54x faster                                                    |
| deepcopy                 | 511 us                                                                | 337 us: 1.51x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 41.3 us: 1.50x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 86.8 ms: 1.47x faster                                                    |
| float                    | 135 ms                                                                | 92.1 ms: 1.46x faster                                                    |
| spectral_norm            | 186 ms                                                                | 129 ms: 1.45x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 7.53 ms: 1.45x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 382 us: 1.39x faster                                                     |
| pyflate                  | 795 ms                                                                | 573 ms: 1.39x faster                                                     |
| regex_compile            | 177 ms                                                                | 127 ms: 1.39x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 267 us: 1.37x faster                                                     |
| nbody                    | 166 ms                                                                | 122 ms: 1.36x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 145 ms: 1.36x faster                                                     |
| logging_simple           | 9.78 us                                                               | 7.26 us: 1.35x faster                                                    |
| thrift                   | 1.26 ms                                                               | 936 us: 1.35x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.90 us: 1.34x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.28 sec: 1.32x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 65.5 ms: 1.32x faster                                                    |
| mako                     | 18.9 ms                                                               | 14.4 ms: 1.31x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.8 ms: 1.30x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.59 sec: 1.30x faster                                                   |
| django_template          | 53.3 ms                                                               | 41.2 ms: 1.30x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.4 ms: 1.28x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.59 us: 1.28x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.4 ms: 1.27x faster                                                    |
| sympy_sum                | 184 ms                                                                | 147 ms: 1.25x faster                                                     |
| 2to3                     | 381 ms                                                                | 307 ms: 1.24x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.20 ms: 1.23x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 21.8 ms: 1.22x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.7 ms: 1.21x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 61.2 ms: 1.20x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 83.1 ms: 1.20x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.97 sec: 1.20x faster                                                   |
| sympy_str                | 329 ms                                                                | 275 ms: 1.20x faster                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 962 ms: 1.19x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 63.3 ms: 1.19x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.34 ms: 1.18x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 132 ms: 1.18x faster                                                     |
| docutils                 | 3.53 sec                                                              | 3.02 sec: 1.17x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 182 ms: 1.16x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.5 ms: 1.15x faster                                                    |
| scimark_fft              | 500 ms                                                                | 437 ms: 1.14x faster                                                     |
| fannkuch                 | 546 ms                                                                | 480 ms: 1.14x faster                                                     |
| sympy_expand             | 543 ms                                                                | 478 ms: 1.14x faster                                                     |
| nqueens                  | 117 ms                                                                | 105 ms: 1.12x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.11x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 64.3 ms: 1.09x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.42 sec: 1.08x faster                                                   |
| meteor_contest           | 126 ms                                                                | 117 ms: 1.08x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 3.99 ms: 1.07x faster                                                    |
| json                     | 5.88 ms                                                               | 5.70 ms: 1.03x faster                                                    |
| regex_dna                | 257 ms                                                                | 250 ms: 1.03x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 4.06 us: 1.01x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 671 ms: 1.02x slower                                                     |
| pidigits                 | 235 ms                                                                | 246 ms: 1.05x slower                                                     |
| json_loads               | 30.9 us                                                               | 32.5 us: 1.05x slower                                                    |
| async_generators         | 452 ms                                                                | 500 ms: 1.11x slower                                                     |
| mypy2                    | 936 ms                                                                | 1.03 sec: 1.11x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.56 ms: 1.13x slower                                                    |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 8.97 ms: 1.30x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.59 ms: 1.59x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 7.00 ms: 1.68x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 4.93 sec: 338.98x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                             |

Benchmark hidden because not significant (2): xml_etree_generate, regex_v8
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250102-3.14.0a3+-e1baa77/bm-20250102-arminc-aarch64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.313x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.31x