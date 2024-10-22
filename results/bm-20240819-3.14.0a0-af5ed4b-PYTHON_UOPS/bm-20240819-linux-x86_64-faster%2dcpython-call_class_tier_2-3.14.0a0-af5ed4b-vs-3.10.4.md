# Results vs. 3.10.4

- fork: faster-cpython
- ref: call_class_tier_2
- machine: linux-x86_64
- commit hash: af5ed4b
- commit date: 2024-08-19
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 322 ms: 1.08x faster                                                         |
| docutils       | 3.30 sec                                               | 3.26 sec: 1.01x faster                                                       |
| html5lib       | 88.9 ms                                                | 75.5 ms: 1.18x faster                                                        |
| tornado_http   | 136 ms                                                 | 99.3 ms: 1.37x faster                                                        |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 349 ms: 2.09x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 454 ms: 1.92x faster                                                         |
| async_tree_io           | 1.77 sec                                               | 935 ms: 1.89x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 594 ms: 1.71x faster                                                         |
| Geometric mean          | (ref)                                                  | 1.90x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 84.9 ms: 1.38x faster                                                        |
| nbody          | 154 ms                                                 | 118 ms: 1.30x faster                                                         |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.22x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 27.8 ms                                                | 25.8 ms: 1.07x faster                                                        |
| regex_compile  | 188 ms                                                 | 180 ms: 1.05x faster                                                         |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 249 us: 1.33x faster                                                         |
| json_dumps           | 14.2 ms                                                | 10.8 ms: 1.31x faster                                                        |
| pickle_pure_python   | 484 us                                                 | 374 us: 1.30x faster                                                         |
| tomli_loads          | 3.14 sec                                               | 2.44 sec: 1.28x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 66.1 ms: 1.20x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                                         |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 107 ms: 1.08x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 93.7 ms: 1.06x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 13.5 ms: 1.21x faster                                                        |
| django_template | 48.2 ms                                                | 40.6 ms: 1.19x faster                                                        |
| genshi_text     | 31.8 ms                                                | 28.7 ms: 1.11x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 66.9 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 187 us: 2.91x faster                                                         |
| async_tree_none          | 728 ms                                                 | 349 ms: 2.09x faster                                                         |
| generators               | 80.1 ms                                                | 40.8 ms: 1.96x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 454 ms: 1.92x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 935 ms: 1.89x faster                                                         |
| asyncio_tcp              | 922 ms                                                 | 501 ms: 1.84x faster                                                         |
| deltablue                | 7.91 ms                                                | 4.48 ms: 1.77x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 594 ms: 1.71x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 36.6 us: 1.60x faster                                                        |
| logging_silent           | 190 ns                                                 | 124 ns: 1.53x faster                                                         |
| deepcopy                 | 479 us                                                 | 321 us: 1.49x faster                                                         |
| pylint                   | 551 ms                                                 | 372 ms: 1.48x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 86.7 ms: 1.47x faster                                                        |
| scimark_sor              | 220 ms                                                 | 149 ms: 1.47x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 80.2 ms: 1.47x faster                                                        |
| raytrace                 | 507 ms                                                 | 344 ms: 1.47x faster                                                         |
| coroutines               | 35.1 ms                                                | 23.9 ms: 1.47x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.94 us: 1.42x faster                                                        |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.82 sec: 1.41x faster                                                       |
| chaos                    | 115 ms                                                 | 82.2 ms: 1.41x faster                                                        |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                        |
| float                    | 117 ms                                                 | 84.9 ms: 1.38x faster                                                        |
| tornado_http             | 136 ms                                                 | 99.3 ms: 1.37x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.58 ms: 1.37x faster                                                        |
| go                       | 240 ms                                                 | 177 ms: 1.36x faster                                                         |
| thrift                   | 1.07 ms                                                | 803 us: 1.33x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 249 us: 1.33x faster                                                         |
| scimark_lu               | 176 ms                                                 | 134 ms: 1.31x faster                                                         |
| json_dumps               | 14.2 ms                                                | 10.8 ms: 1.31x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.97 ms: 1.30x faster                                                        |
| nbody                    | 154 ms                                                 | 118 ms: 1.30x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 374 us: 1.30x faster                                                         |
| logging_simple           | 8.30 us                                                | 6.42 us: 1.29x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 2.44 sec: 1.28x faster                                                       |
| pyflate                  | 716 ms                                                 | 560 ms: 1.28x faster                                                         |
| comprehensions           | 28.8 us                                                | 22.8 us: 1.26x faster                                                        |
| spectral_norm            | 170 ms                                                 | 135 ms: 1.26x faster                                                         |
| logging_format           | 9.09 us                                                | 7.28 us: 1.25x faster                                                        |
| richards_super           | 94.7 ms                                                | 76.0 ms: 1.25x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                        |
| mako                     | 16.3 ms                                                | 13.5 ms: 1.21x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 66.1 ms: 1.20x faster                                                        |
| django_template          | 48.2 ms                                                | 40.6 ms: 1.19x faster                                                        |
| html5lib                 | 88.9 ms                                                | 75.5 ms: 1.18x faster                                                        |
| richards                 | 79.3 ms                                                | 67.7 ms: 1.17x faster                                                        |
| hexiom                   | 10.4 ms                                                | 9.07 ms: 1.15x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 890 ms: 1.14x faster                                                         |
| bench_thread_pool        | 986 us                                                 | 863 us: 1.14x faster                                                         |
| fannkuch                 | 532 ms                                                 | 472 ms: 1.13x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.88 sec: 1.12x faster                                                       |
| genshi_text              | 31.8 ms                                                | 28.7 ms: 1.11x faster                                                        |
| scimark_fft              | 466 ms                                                 | 423 ms: 1.10x faster                                                         |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.45 sec: 1.09x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 107 ms: 1.08x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.98 ms: 1.08x faster                                                        |
| 2to3                     | 348 ms                                                 | 322 ms: 1.08x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 25.8 ms: 1.07x faster                                                        |
| sympy_sum                | 196 ms                                                 | 183 ms: 1.07x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 134 ms: 1.07x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 93.7 ms: 1.06x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 24.5 ms: 1.05x faster                                                        |
| regex_compile            | 188 ms                                                 | 180 ms: 1.05x faster                                                         |
| sqlglot_optimize         | 69.2 ms                                                | 66.5 ms: 1.04x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.75 sec: 1.04x faster                                                       |
| sympy_str                | 346 ms                                                 | 335 ms: 1.03x faster                                                         |
| json                     | 5.69 ms                                                | 5.53 ms: 1.03x faster                                                        |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                         |
| nqueens                  | 106 ms                                                 | 104 ms: 1.02x faster                                                         |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                         |
| docutils                 | 3.30 sec                                               | 3.26 sec: 1.01x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                         |
| meteor_contest           | 120 ms                                                 | 121 ms: 1.01x slower                                                         |
| genshi_xml               | 66.0 ms                                                | 66.9 ms: 1.01x slower                                                        |
| regex_effbot             | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 3.81 ms: 1.05x slower                                                        |
| async_generators         | 444 ms                                                 | 467 ms: 1.05x slower                                                         |
| coverage                 | 79.4 ms                                                | 84.6 ms: 1.06x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                        |
| telco                    | 7.27 ms                                                | 8.80 ms: 1.21x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.23x faster                                                                 |

Benchmark hidden because not significant (2): bench_mp_pool, sympy_expand
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240819-3.14.0a0-af5ed4b-PYTHON_UOPS/bm-20240819-linux-x86_64-faster%2dcpython-call_class_tier_2-3.14.0a0-af5ed4b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.14x