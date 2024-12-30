# Results vs. 3.10.4

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: linux-aarch64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.217x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 324 ms: 1.18x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.23 sec: 1.09x faster                                                   |
| html5lib       | 86.5 ms                                                               | 70.2 ms: 1.23x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.17x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 956 ms: 2.39x faster                                                     |
| async_tree_none         | 950 ms                                                                | 421 ms: 2.26x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 534 ms: 2.12x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 714 ms: 1.78x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.12x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 94.0 ms: 1.43x faster                                                    |
| nbody          | 166 ms                                                                | 120 ms: 1.38x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 145 ms: 1.22x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.06 ms: 1.05x faster                                                    |
| regex_dna      | 257 ms                                                                | 252 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 263 us: 1.39x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 395 us: 1.34x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 84.2 ms: 1.18x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 180 ms: 1.18x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.6 ms: 1.15x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.08x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 144 ms: 1.08x faster                                                     |
| json_loads           | 30.9 us                                                               | 33.3 us: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.03 ms: 1.31x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.38x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                    |
| django_template | 53.3 ms                                                               | 48.3 ms: 1.10x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 87.0 ms: 1.25x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.05x faster                                                             |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 230 us: 2.87x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 956 ms: 2.39x faster                                                     |
| async_tree_none          | 950 ms                                                                | 421 ms: 2.26x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 534 ms: 2.12x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.33 ms: 2.07x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 714 ms: 1.78x faster                                                     |
| richards                 | 91.7 ms                                                               | 56.0 ms: 1.64x faster                                                    |
| richards_super           | 107 ms                                                                | 65.7 ms: 1.63x faster                                                    |
| go                       | 264 ms                                                                | 168 ms: 1.57x faster                                                     |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.57x faster                                                     |
| raytrace                 | 573 ms                                                                | 367 ms: 1.56x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.57 ms: 1.53x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 41.4 us: 1.49x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 86.6 ms: 1.48x faster                                                    |
| logging_silent           | 222 ns                                                                | 151 ns: 1.47x faster                                                     |
| scimark_lu               | 227 ms                                                                | 154 ms: 1.47x faster                                                     |
| float                    | 135 ms                                                                | 94.0 ms: 1.43x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 94.0 ms: 1.43x faster                                                    |
| pylint                   | 485 ms                                                                | 342 ms: 1.42x faster                                                     |
| sqlglot_transpile        | 2.84 ms                                                               | 2.01 ms: 1.41x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.4 ms: 1.41x faster                                                    |
| chaos                    | 121 ms                                                                | 86.2 ms: 1.40x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 263 us: 1.39x faster                                                     |
| nbody                    | 166 ms                                                                | 120 ms: 1.38x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 395 us: 1.34x faster                                                     |
| comprehensions           | 33.1 us                                                               | 25.0 us: 1.33x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                                   |
| sqlalchemy_declarative   | 197 ms                                                                | 151 ms: 1.30x faster                                                     |
| generators               | 68.1 ms                                                               | 52.2 ms: 1.30x faster                                                    |
| pyflate                  | 795 ms                                                                | 616 ms: 1.29x faster                                                     |
| deepcopy                 | 511 us                                                                | 397 us: 1.29x faster                                                     |
| spectral_norm            | 186 ms                                                                | 147 ms: 1.27x faster                                                     |
| coroutines               | 37.2 ms                                                               | 29.5 ms: 1.26x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 70.2 ms: 1.23x faster                                                    |
| thrift                   | 1.26 ms                                                               | 1.03 ms: 1.23x faster                                                    |
| regex_compile            | 177 ms                                                                | 145 ms: 1.22x faster                                                     |
| logging_format           | 10.6 us                                                               | 8.75 us: 1.21x faster                                                    |
| logging_simple           | 9.78 us                                                               | 8.13 us: 1.20x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.0 ms: 1.20x faster                                                    |
| scimark_fft              | 500 ms                                                                | 420 ms: 1.19x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 84.2 ms: 1.18x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 180 ms: 1.18x faster                                                     |
| 2to3                     | 381 ms                                                                | 324 ms: 1.18x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 17.6 ms: 1.16x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 9.50 ms: 1.15x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.38 ms: 1.15x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.6 ms: 1.15x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.02 us: 1.14x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.48 sec: 1.14x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 23.6 ms: 1.12x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.83 ms: 1.12x faster                                                    |
| django_template          | 53.3 ms                                                               | 48.3 ms: 1.10x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.23 sec: 1.09x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 144 ms: 1.08x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.08x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 144 ms: 1.08x faster                                                     |
| fannkuch                 | 546 ms                                                                | 506 ms: 1.08x faster                                                     |
| sympy_sum                | 184 ms                                                                | 171 ms: 1.07x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 71.1 ms: 1.06x faster                                                    |
| sympy_str                | 329 ms                                                                | 310 ms: 1.06x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 4.06 ms: 1.05x faster                                                    |
| sympy_expand             | 543 ms                                                                | 525 ms: 1.03x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.59 sec: 1.03x faster                                                   |
| regex_dna                | 257 ms                                                                | 252 ms: 1.02x faster                                                     |
| asyncio_websockets       | 657 ms                                                                | 673 ms: 1.02x slower                                                     |
| json_loads               | 30.9 us                                                               | 33.3 us: 1.08x slower                                                    |
| nqueens                  | 117 ms                                                                | 131 ms: 1.12x slower                                                     |
| pprint_pformat           | 2.36 sec                                                              | 2.67 sec: 1.13x slower                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.32 sec: 1.15x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.92 ms: 1.17x slower                                                    |
| mypy2                    | 936 ms                                                                | 1.10 sec: 1.18x slower                                                   |
| async_generators         | 452 ms                                                                | 542 ms: 1.20x slower                                                     |
| genshi_xml               | 69.8 ms                                                               | 87.0 ms: 1.25x slower                                                    |
| coverage                 | 83.6 ms                                                               | 105 ms: 1.25x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 9.03 ms: 1.31x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.63 ms: 1.61x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.86 ms: 1.65x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 1.56 sec: 107.40x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.13x faster                                                             |

Benchmark hidden because not significant (7): json, dulwich_log, regex_v8, meteor_contest, genshi_text, sqlite_synth, pidigits
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241228-3.14.0a3+-f9a5a3a-JIT/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.217x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.33x