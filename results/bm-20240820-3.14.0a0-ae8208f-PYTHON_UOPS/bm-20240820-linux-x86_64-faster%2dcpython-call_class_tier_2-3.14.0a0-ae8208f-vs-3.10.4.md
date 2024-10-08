# Results vs. 3.10.4

- fork: faster-cpython
- ref: call_class_tier_2
- machine: linux-x86_64
- commit hash: ae8208f
- commit date: 2024-08-20
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 327 ms: 1.07x faster                                                         |
| docutils       | 3.30 sec                                               | 3.26 sec: 1.01x faster                                                       |
| html5lib       | 88.9 ms                                                | 75.9 ms: 1.17x faster                                                        |
| tornado_http   | 136 ms                                                 | 98.6 ms: 1.38x faster                                                        |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 351 ms: 2.07x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 456 ms: 1.91x faster                                                         |
| async_tree_io           | 1.77 sec                                               | 931 ms: 1.90x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 595 ms: 1.71x faster                                                         |
| Geometric mean          | (ref)                                                  | 1.89x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 84.3 ms: 1.39x faster                                                        |
| nbody          | 154 ms                                                 | 120 ms: 1.28x faster                                                         |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.22x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 27.8 ms                                                | 26.6 ms: 1.04x faster                                                        |
| regex_compile  | 188 ms                                                 | 183 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 253 us: 1.31x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 384 us: 1.26x faster                                                         |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                        |
| tomli_loads          | 3.14 sec                                               | 2.54 sec: 1.24x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 66.5 ms: 1.19x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                                         |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 108 ms: 1.07x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 94.2 ms: 1.06x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 13.6 ms: 1.20x faster                                                        |
| django_template | 48.2 ms                                                | 40.9 ms: 1.18x faster                                                        |
| genshi_text     | 31.8 ms                                                | 28.6 ms: 1.11x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 67.6 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 187 us: 2.91x faster                                                         |
| async_tree_none          | 728 ms                                                 | 351 ms: 2.07x faster                                                         |
| generators               | 80.1 ms                                                | 40.2 ms: 1.99x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 456 ms: 1.91x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 931 ms: 1.90x faster                                                         |
| asyncio_tcp              | 922 ms                                                 | 500 ms: 1.84x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 595 ms: 1.71x faster                                                         |
| deltablue                | 7.91 ms                                                | 4.70 ms: 1.68x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 38.8 us: 1.51x faster                                                        |
| deepcopy                 | 479 us                                                 | 323 us: 1.48x faster                                                         |
| pylint                   | 551 ms                                                 | 374 ms: 1.48x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 87.0 ms: 1.47x faster                                                        |
| coroutines               | 35.1 ms                                                | 23.9 ms: 1.47x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 80.8 ms: 1.46x faster                                                        |
| raytrace                 | 507 ms                                                 | 349 ms: 1.45x faster                                                         |
| logging_silent           | 190 ns                                                 | 132 ns: 1.43x faster                                                         |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                       |
| scimark_sor              | 220 ms                                                 | 157 ms: 1.40x faster                                                         |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                        |
| float                    | 117 ms                                                 | 84.3 ms: 1.39x faster                                                        |
| chaos                    | 115 ms                                                 | 83.4 ms: 1.38x faster                                                        |
| tornado_http             | 136 ms                                                 | 98.6 ms: 1.38x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 3.02 us: 1.38x faster                                                        |
| go                       | 240 ms                                                 | 175 ms: 1.37x faster                                                         |
| sqlglot_parse            | 2.17 ms                                                | 1.60 ms: 1.36x faster                                                        |
| thrift                   | 1.07 ms                                                | 807 us: 1.33x faster                                                         |
| scimark_lu               | 176 ms                                                 | 134 ms: 1.32x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 253 us: 1.31x faster                                                         |
| sqlglot_transpile        | 2.57 ms                                                | 2.00 ms: 1.29x faster                                                        |
| pyflate                  | 716 ms                                                 | 558 ms: 1.28x faster                                                         |
| nbody                    | 154 ms                                                 | 120 ms: 1.28x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 384 us: 1.26x faster                                                         |
| logging_simple           | 8.30 us                                                | 6.63 us: 1.25x faster                                                        |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 2.54 sec: 1.24x faster                                                       |
| spectral_norm            | 170 ms                                                 | 139 ms: 1.22x faster                                                         |
| logging_format           | 9.09 us                                                | 7.48 us: 1.21x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.21x faster                                                        |
| mako                     | 16.3 ms                                                | 13.6 ms: 1.20x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 66.5 ms: 1.19x faster                                                        |
| comprehensions           | 28.8 us                                                | 24.2 us: 1.19x faster                                                        |
| django_template          | 48.2 ms                                                | 40.9 ms: 1.18x faster                                                        |
| richards_super           | 94.7 ms                                                | 80.7 ms: 1.17x faster                                                        |
| html5lib                 | 88.9 ms                                                | 75.9 ms: 1.17x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 866 us: 1.14x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 911 ms: 1.12x faster                                                         |
| fannkuch                 | 532 ms                                                 | 478 ms: 1.11x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.82 ms: 1.11x faster                                                        |
| genshi_text              | 31.8 ms                                                | 28.6 ms: 1.11x faster                                                        |
| richards                 | 79.3 ms                                                | 72.0 ms: 1.10x faster                                                        |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.93 sec: 1.09x faster                                                       |
| hexiom                   | 10.4 ms                                                | 9.54 ms: 1.09x faster                                                        |
| scimark_fft              | 466 ms                                                 | 433 ms: 1.08x faster                                                         |
| sympy_sum                | 196 ms                                                 | 183 ms: 1.08x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.47 sec: 1.07x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 108 ms: 1.07x faster                                                         |
| 2to3                     | 348 ms                                                 | 327 ms: 1.07x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 94.2 ms: 1.06x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 136 ms: 1.05x faster                                                         |
| sympy_integrate          | 25.8 ms                                                | 24.5 ms: 1.05x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 26.6 ms: 1.04x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 67.0 ms: 1.03x faster                                                        |
| regex_compile            | 188 ms                                                 | 183 ms: 1.03x faster                                                         |
| sympy_str                | 346 ms                                                 | 338 ms: 1.02x faster                                                         |
| nqueens                  | 106 ms                                                 | 104 ms: 1.02x faster                                                         |
| json                     | 5.69 ms                                                | 5.59 ms: 1.02x faster                                                        |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                         |
| docutils                 | 3.30 sec                                               | 3.26 sec: 1.01x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.89 sec: 1.01x slower                                                       |
| meteor_contest           | 120 ms                                                 | 122 ms: 1.02x slower                                                         |
| genshi_xml               | 66.0 ms                                                | 67.6 ms: 1.02x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 3.73 ms: 1.03x slower                                                        |
| async_generators         | 444 ms                                                 | 467 ms: 1.05x slower                                                         |
| coverage                 | 79.4 ms                                                | 84.9 ms: 1.07x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 1.78 ms: 1.10x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                        |
| telco                    | 7.27 ms                                                | 8.76 ms: 1.21x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.22x faster                                                                 |

Benchmark hidden because not significant (4): sympy_expand, regex_dna, bench_mp_pool, regex_effbot
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240820-3.14.0a0-ae8208f-PYTHON_UOPS/bm-20240820-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-ae8208f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.13x