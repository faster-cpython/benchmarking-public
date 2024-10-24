# Results vs. 3.10.4

- fork: colesbury
- ref: gh_125610_STORE_ATTR
- machine: linux-x86_64
- commit hash: 3a126a8
- commit date: 2024-10-16
- overall geometric mean: 1.39x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                      |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                    |
| html5lib       | 88.9 ms                                                | 63.0 ms: 1.41x faster                                                     |
| tornado_http   | 136 ms                                                 | 90.2 ms: 1.51x faster                                                     |
| Geometric mean | (ref)                                                  | 1.38x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 328 ms: 2.22x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 415 ms: 2.09x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 853 ms: 2.07x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 575 ms: 1.77x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.03x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 89.3 ms: 1.72x faster                                                     |
| float          | 117 ms                                                 | 78.7 ms: 1.49x faster                                                     |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.38x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                      |
| regex_v8       | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                     |
| regex_dna      | 227 ms                                                 | 210 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                  | 1.16x faster                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 309 us: 1.57x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                      |
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                     |
| json_loads           | 31.2 us                                                | 27.0 us: 1.16x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 86.1 ms: 1.15x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 160 ms: 1.05x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.8 ms: 1.24x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                     |
| django_template | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                     |
| genshi_text     | 31.8 ms                                                | 22.9 ms: 1.39x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 51.3 ms: 1.29x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.41x faster                                                      |
| generators               | 80.1 ms                                                | 27.7 ms: 2.89x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.25 ms: 2.43x faster                                                     |
| async_tree_none          | 728 ms                                                 | 328 ms: 2.22x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 415 ms: 2.09x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 853 ms: 2.07x faster                                                      |
| go                       | 240 ms                                                 | 120 ms: 2.01x faster                                                      |
| chaos                    | 115 ms                                                 | 59.9 ms: 1.93x faster                                                     |
| raytrace                 | 507 ms                                                 | 266 ms: 1.90x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 30.7 us: 1.90x faster                                                     |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                      |
| logging_silent           | 190 ns                                                 | 104 ns: 1.83x faster                                                      |
| richards_super           | 94.7 ms                                                | 52.2 ms: 1.82x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 575 ms: 1.77x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 72.4 ms: 1.76x faster                                                     |
| pylint                   | 551 ms                                                 | 316 ms: 1.74x faster                                                      |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 68.5 ms: 1.73x faster                                                     |
| nbody                    | 154 ms                                                 | 89.3 ms: 1.72x faster                                                     |
| richards                 | 79.3 ms                                                | 46.1 ms: 1.72x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.23 ms: 1.67x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 309 us: 1.57x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                     |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.47 us: 1.52x faster                                                     |
| tornado_http             | 136 ms                                                 | 90.2 ms: 1.51x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                    |
| logging_format           | 9.09 us                                                | 6.05 us: 1.50x faster                                                     |
| pyflate                  | 716 ms                                                 | 480 ms: 1.49x faster                                                      |
| float                    | 117 ms                                                 | 78.7 ms: 1.49x faster                                                     |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.48x faster                                                     |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.47x faster                                                      |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                      |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                                    |
| html5lib                 | 88.9 ms                                                | 63.0 ms: 1.41x faster                                                     |
| django_template          | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 730 ms: 1.39x faster                                                      |
| genshi_text              | 31.8 ms                                                | 22.9 ms: 1.39x faster                                                     |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                      |
| thrift                   | 1.07 ms                                                | 782 us: 1.37x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.35x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.80 ms: 1.35x faster                                                     |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 59.6 ms: 1.33x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 63.6 ms: 1.33x faster                                                     |
| fannkuch                 | 532 ms                                                 | 406 ms: 1.31x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 53.1 ms: 1.30x faster                                                     |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 51.3 ms: 1.29x faster                                                     |
| scimark_fft              | 466 ms                                                 | 363 ms: 1.28x faster                                                      |
| nqueens                  | 106 ms                                                 | 82.7 ms: 1.28x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                    |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                                      |
| python_startup           | 14.6 ms                                                | 11.8 ms: 1.24x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 838 us: 1.18x faster                                                      |
| json_loads               | 31.2 us                                                | 27.0 us: 1.16x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 86.1 ms: 1.15x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                     |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                      |
| json                     | 5.69 ms                                                | 5.10 ms: 1.12x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                                      |
| regex_dna                | 227 ms                                                 | 210 ms: 1.08x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 160 ms: 1.05x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.71 sec: 1.05x faster                                                    |
| async_generators         | 444 ms                                                 | 434 ms: 1.02x faster                                                      |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                      |
| coverage                 | 79.4 ms                                                | 83.8 ms: 1.05x slower                                                     |
| telco                    | 7.27 ms                                                | 7.86 ms: 1.08x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 4.37 ms: 1.21x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.66 ms: 1.64x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 78.5 ms: 3.27x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                              |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241016-3.14.0a1+-3a126a8/bm-20241016-linux-x86_64-colesbury-gh_125610_STORE_ATTR-3.14.0a1+-3a126a8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.25x