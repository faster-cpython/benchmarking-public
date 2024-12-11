# Results vs. 3.10.4

- fork: eendebakpt
- ref: small_int_immortal_v
- machine: linux-x86_64
- commit hash: e232ca4
- commit date: 2024-12-11
- overall geometric mean: 1.421x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.36x faster                                                       |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                     |
| html5lib       | 88.9 ms                                                | 63.5 ms: 1.40x faster                                                      |
| Geometric mean | (ref)                                                  | 1.34x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 626 ms: 2.82x faster                                                       |
| async_tree_none         | 728 ms                                                 | 269 ms: 2.71x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 339 ms: 2.56x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 507 ms: 2.01x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.50x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 94.0 ms: 1.63x faster                                                      |
| float          | 117 ms                                                 | 76.3 ms: 1.53x faster                                                      |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.37x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                       |
| regex_v8       | 27.8 ms                                                | 25.9 ms: 1.07x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.52 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                     |
| unpickle_pure_python | 331 us                                                 | 221 us: 1.49x faster                                                       |
| pickle_pure_python   | 484 us                                                 | 327 us: 1.48x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 60.6 ms: 1.31x faster                                                      |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 97.3 ms: 1.19x faster                                                      |
| json_loads           | 31.2 us                                                | 26.8 us: 1.17x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 86.8 ms: 1.15x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 7.01 ms: 1.18x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                      |
| genshi_text     | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                      |
| mako            | 16.3 ms                                                | 11.7 ms: 1.40x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 50.2 ms: 1.32x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.22x faster                                                       |
| generators               | 80.1 ms                                                | 27.3 ms: 2.93x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 626 ms: 2.82x faster                                                       |
| async_tree_none          | 728 ms                                                 | 269 ms: 2.71x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 339 ms: 2.56x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                                      |
| go                       | 240 ms                                                 | 119 ms: 2.02x faster                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 507 ms: 2.01x faster                                                       |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 30.9 us: 1.89x faster                                                      |
| chaos                    | 115 ms                                                 | 61.1 ms: 1.89x faster                                                      |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                                       |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 70.4 ms: 1.81x faster                                                      |
| richards_super           | 94.7 ms                                                | 52.3 ms: 1.81x faster                                                      |
| djangocms                | 38.4 us                                                | 21.8 us: 1.76x faster                                                      |
| logging_silent           | 190 ns                                                 | 109 ns: 1.75x faster                                                       |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 68.9 ms: 1.71x faster                                                      |
| richards                 | 79.3 ms                                                | 46.2 ms: 1.71x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.27 ms: 1.66x faster                                                      |
| nbody                    | 154 ms                                                 | 94.0 ms: 1.63x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                      |
| float                    | 117 ms                                                 | 76.3 ms: 1.53x faster                                                      |
| spectral_norm            | 170 ms                                                 | 112 ms: 1.52x faster                                                       |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                      |
| django_template          | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 221 us: 1.49x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.58 us: 1.49x faster                                                      |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 327 us: 1.48x faster                                                       |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                       |
| logging_format           | 9.09 us                                                | 6.25 us: 1.45x faster                                                      |
| pyflate                  | 716 ms                                                 | 496 ms: 1.44x faster                                                       |
| genshi_text              | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                      |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.3 ms: 1.44x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                     |
| html5lib                 | 88.9 ms                                                | 63.5 ms: 1.40x faster                                                      |
| mako                     | 16.3 ms                                                | 11.7 ms: 1.40x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 731 ms: 1.39x faster                                                       |
| thrift                   | 1.07 ms                                                | 776 us: 1.38x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 104 ms: 1.37x faster                                                       |
| 2to3                     | 348 ms                                                 | 255 ms: 1.36x faster                                                       |
| sqlalchemy_declarative   | 172 ms                                                 | 127 ms: 1.36x faster                                                       |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.90 ms: 1.32x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 50.2 ms: 1.32x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 52.6 ms: 1.32x faster                                                      |
| fannkuch                 | 532 ms                                                 | 405 ms: 1.31x faster                                                       |
| nqueens                  | 106 ms                                                 | 80.7 ms: 1.31x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 60.6 ms: 1.31x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 65.2 ms: 1.29x faster                                                      |
| sympy_str                | 346 ms                                                 | 269 ms: 1.28x faster                                                       |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                      |
| scimark_fft              | 466 ms                                                 | 376 ms: 1.24x faster                                                       |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                      |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 97.3 ms: 1.19x faster                                                      |
| json_loads               | 31.2 us                                                | 26.8 us: 1.17x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 857 us: 1.15x faster                                                       |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.15x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 86.8 ms: 1.15x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                                     |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                       |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 25.9 ms: 1.07x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.06x faster                                                      |
| async_generators         | 444 ms                                                 | 421 ms: 1.05x faster                                                       |
| regex_effbot             | 3.63 ms                                                | 3.52 ms: 1.03x faster                                                      |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                       |
| coverage                 | 79.4 ms                                                | 83.1 ms: 1.05x slower                                                      |
| mypy2                    | 894 ms                                                 | 948 ms: 1.06x slower                                                       |
| telco                    | 7.27 ms                                                | 7.78 ms: 1.07x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.01 ms: 1.18x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 4.76 ms: 1.31x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                | 81.0 ms: 3.37x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                               |

Benchmark hidden because not significant (1): regex_dna
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241211-3.14.0a2+-e232ca4/bm-20241211-linux-x86_64-eendebakpt-small_int_immortal_v-3.14.0a2+-e232ca4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.421x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.27x