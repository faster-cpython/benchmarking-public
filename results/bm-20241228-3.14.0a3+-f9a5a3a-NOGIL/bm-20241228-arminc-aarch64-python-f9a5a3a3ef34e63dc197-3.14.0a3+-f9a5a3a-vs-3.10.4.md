# Results vs. 3.10.4

- fork: python
- ref: f9a5a3a3ef34e63dc197
- machine: linux-aarch64
- commit hash: f9a5a3a
- commit date: 2024-12-28
- overall geometric mean: 1.068x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.54x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 471 ms: 1.24x slower                                                     |
| docutils       | 3.53 sec                                                              | 3.71 sec: 1.05x slower                                                   |
| html5lib       | 86.5 ms                                                               | 110 ms: 1.27x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.18x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.21 sec: 1.89x faster                                                   |
| async_tree_none         | 950 ms                                                                | 543 ms: 1.75x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 667 ms: 1.70x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 850 ms: 1.50x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.70x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 191 ms: 1.15x slower                                                     |
| float          | 135 ms                                                                | 162 ms: 1.20x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.12x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 195 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                             |

Benchmark hidden because not significant (3): regex_effbot, regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 212 ms                                                                | 180 ms: 1.18x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 142 ms: 1.10x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 3.58 sec: 1.07x slower                                                   |
| json_dumps           | 16.7 ms                                                               | 18.6 ms: 1.11x slower                                                    |
| xml_etree_process    | 99.5 ms                                                               | 111 ms: 1.12x slower                                                     |
| xml_etree_generate   | 123 ms                                                                | 143 ms: 1.17x slower                                                     |
| json_loads           | 30.9 us                                                               | 37.3 us: 1.21x slower                                                    |
| unpickle_pure_python | 366 us                                                                | 467 us: 1.28x slower                                                     |
| pickle_pure_python   | 529 us                                                                | 701 us: 1.33x slower                                                     |
| Geometric mean       | (ref)                                                                 | 1.10x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 12.4 ms: 1.80x slower                                                    |
| python_startup         | 11.2 ms                                                               | 20.6 ms: 1.84x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.82x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 35.2 ms                                                               | 40.4 ms: 1.15x slower                                                    |
| genshi_xml      | 69.8 ms                                                               | 85.3 ms: 1.22x slower                                                    |
| django_template | 53.3 ms                                                               | 65.9 ms: 1.24x slower                                                    |
| mako            | 18.9 ms                                                               | 25.2 ms: 1.33x slower                                                    |
| Geometric mean  | (ref)                                                                 | 1.23x slower                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 290 us: 2.28x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.21 sec: 1.89x faster                                                   |
| async_tree_none          | 950 ms                                                                | 543 ms: 1.75x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 667 ms: 1.70x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 850 ms: 1.50x faster                                                     |
| generators               | 68.1 ms                                                               | 57.3 ms: 1.19x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 180 ms: 1.18x faster                                                     |
| deepcopy                 | 511 us                                                                | 437 us: 1.17x faster                                                     |
| spectral_norm            | 186 ms                                                                | 165 ms: 1.13x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 142 ms: 1.10x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 122 ms: 1.09x faster                                                     |
| pylint                   | 485 ms                                                                | 446 ms: 1.09x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.80 us: 1.08x faster                                                    |
| coroutines               | 37.2 ms                                                               | 34.4 ms: 1.08x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 57.4 us: 1.08x faster                                                    |
| scimark_lu               | 227 ms                                                                | 220 ms: 1.03x faster                                                     |
| asyncio_websockets       | 657 ms                                                                | 681 ms: 1.04x slower                                                     |
| docutils                 | 3.53 sec                                                              | 3.71 sec: 1.05x slower                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 4.87 us: 1.06x slower                                                    |
| tomli_loads              | 3.36 sec                                                              | 3.58 sec: 1.07x slower                                                   |
| chaos                    | 121 ms                                                                | 129 ms: 1.07x slower                                                     |
| richards                 | 91.7 ms                                                               | 98.2 ms: 1.07x slower                                                    |
| json                     | 5.88 ms                                                               | 6.37 ms: 1.08x slower                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.32 ms: 1.09x slower                                                    |
| mdp                      | 3.70 sec                                                              | 4.05 sec: 1.10x slower                                                   |
| regex_compile            | 177 ms                                                                | 195 ms: 1.10x slower                                                     |
| json_dumps               | 16.7 ms                                                               | 18.6 ms: 1.11x slower                                                    |
| thrift                   | 1.26 ms                                                               | 1.41 ms: 1.12x slower                                                    |
| xml_etree_process        | 99.5 ms                                                               | 111 ms: 1.12x slower                                                     |
| sympy_sum                | 184 ms                                                                | 206 ms: 1.12x slower                                                     |
| sqlglot_normalize        | 156 ms                                                                | 176 ms: 1.12x slower                                                     |
| dulwich_log              | 73.5 ms                                                               | 82.8 ms: 1.13x slower                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 86.3 ms: 1.14x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 40.4 ms: 1.15x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 30.5 ms: 1.15x slower                                                    |
| nbody                    | 166 ms                                                                | 191 ms: 1.15x slower                                                     |
| logging_simple           | 9.78 us                                                               | 11.3 us: 1.15x slower                                                    |
| pyflate                  | 795 ms                                                                | 921 ms: 1.16x slower                                                     |
| raytrace                 | 573 ms                                                                | 664 ms: 1.16x slower                                                     |
| logging_format           | 10.6 us                                                               | 12.3 us: 1.16x slower                                                    |
| xml_etree_generate       | 123 ms                                                                | 143 ms: 1.17x slower                                                     |
| scimark_sor              | 246 ms                                                                | 288 ms: 1.17x slower                                                     |
| nqueens                  | 117 ms                                                                | 138 ms: 1.18x slower                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 235 ms: 1.19x slower                                                     |
| logging_silent           | 222 ns                                                                | 265 ns: 1.19x slower                                                     |
| float                    | 135 ms                                                                | 162 ms: 1.20x slower                                                     |
| json_loads               | 30.9 us                                                               | 37.3 us: 1.21x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.02 ms: 1.21x slower                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 155 ms: 1.21x slower                                                     |
| comprehensions           | 33.1 us                                                               | 40.3 us: 1.22x slower                                                    |
| sympy_str                | 329 ms                                                                | 400 ms: 1.22x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.40 sec: 1.22x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 85.3 ms: 1.22x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.89 sec: 1.22x slower                                                   |
| hexiom                   | 10.9 ms                                                               | 13.4 ms: 1.23x slower                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 3.49 ms: 1.23x slower                                                    |
| 2to3                     | 381 ms                                                                | 471 ms: 1.24x slower                                                     |
| django_template          | 53.3 ms                                                               | 65.9 ms: 1.24x slower                                                    |
| deltablue                | 8.94 ms                                                               | 11.1 ms: 1.24x slower                                                    |
| sympy_expand             | 543 ms                                                                | 687 ms: 1.27x slower                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 2.02 ms: 1.27x slower                                                    |
| html5lib                 | 86.5 ms                                                               | 110 ms: 1.27x slower                                                     |
| unpickle_pure_python     | 366 us                                                                | 467 us: 1.28x slower                                                     |
| fannkuch                 | 546 ms                                                                | 703 ms: 1.29x slower                                                     |
| go                       | 264 ms                                                                | 341 ms: 1.29x slower                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 3.11 ms: 1.29x slower                                                    |
| meteor_contest           | 126 ms                                                                | 163 ms: 1.29x slower                                                     |
| create_gc_cycles         | 2.26 ms                                                               | 2.92 ms: 1.29x slower                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 26.7 ms: 1.30x slower                                                    |
| pickle_pure_python       | 529 us                                                                | 701 us: 1.33x slower                                                     |
| mako                     | 18.9 ms                                                               | 25.2 ms: 1.33x slower                                                    |
| async_generators         | 452 ms                                                                | 621 ms: 1.37x slower                                                     |
| telco                    | 8.49 ms                                                               | 12.4 ms: 1.46x slower                                                    |
| mypy2                    | 936 ms                                                                | 1.53 sec: 1.64x slower                                                   |
| coverage                 | 83.6 ms                                                               | 143 ms: 1.71x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 12.4 ms: 1.80x slower                                                    |
| python_startup           | 11.2 ms                                                               | 20.6 ms: 1.84x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 63.2 ms: 4.35x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.12x slower                                                             |

Benchmark hidden because not significant (8): pathlib, regex_effbot, pidigits, pycparser, richards_super, scimark_fft, regex_v8, regex_dna
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241228-3.14.0a3+-f9a5a3a-NOGIL/bm-20241228-arminc-aarch64-python-f9a5a3a3ef34e63dc197-3.14.0a3+-f9a5a3a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.068x slower

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.54x