# Results vs. 3.10.4

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.05x slower
- HPT reliability: 99.72%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 394 ms: 1.13x slower                                                  |
| docutils       | 3.30 sec                                               | 3.35 sec: 1.02x slower                                                |
| html5lib       | 88.9 ms                                                | 97.3 ms: 1.10x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 908 ms: 1.95x faster                                                  |
| async_tree_none         | 728 ms                                                 | 406 ms: 1.79x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 510 ms: 1.71x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 662 ms: 1.54x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.74x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 191 ms                                                 | 184 ms: 1.04x faster                                                  |
| float          | 117 ms                                                 | 142 ms: 1.21x slower                                                  |
| nbody          | 154 ms                                                 | 217 ms: 1.42x slower                                                  |
| Geometric mean | (ref)                                                  | 1.18x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 27.8 ms                                                | 26.8 ms: 1.04x faster                                                 |
| regex_dna      | 227 ms                                                 | 221 ms: 1.02x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.56 ms: 1.02x faster                                                 |
| regex_compile  | 188 ms                                                 | 217 ms: 1.15x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.18x faster                                                  |
| json_dumps           | 14.2 ms                                                | 13.4 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 111 ms: 1.04x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 3.22 sec: 1.03x slower                                                |
| json_loads           | 31.2 us                                                | 32.2 us: 1.03x slower                                                 |
| xml_etree_generate   | 99.4 ms                                                | 111 ms: 1.11x slower                                                  |
| xml_etree_process    | 79.1 ms                                                | 89.5 ms: 1.13x slower                                                 |
| pickle_pure_python   | 484 us                                                 | 571 us: 1.18x slower                                                  |
| unpickle_pure_python | 331 us                                                 | 399 us: 1.21x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.4 ms: 1.09x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 9.08 ms: 1.53x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.19x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 40.2 ms: 1.26x slower                                                 |
| django_template | 48.2 ms                                                | 60.9 ms: 1.27x slower                                                 |
| genshi_xml      | 66.0 ms                                                | 83.9 ms: 1.27x slower                                                 |
| mako            | 16.3 ms                                                | 21.1 ms: 1.29x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.27x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 254 us: 2.14x faster                                                  |
| generators               | 80.1 ms                                                | 38.0 ms: 2.11x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 908 ms: 1.95x faster                                                  |
| async_tree_none          | 728 ms                                                 | 406 ms: 1.79x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 510 ms: 1.71x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 567 ms: 1.63x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 662 ms: 1.54x faster                                                  |
| pylint                   | 551 ms                                                 | 394 ms: 1.40x faster                                                  |
| gc_traversal             | 3.62 ms                                                | 2.89 ms: 1.25x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 2.08 sec: 1.24x faster                                                |
| create_gc_cycles         | 1.62 ms                                                | 1.37 ms: 1.18x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.18x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 112 ms: 1.14x faster                                                  |
| deepcopy                 | 479 us                                                 | 423 us: 1.13x faster                                                  |
| coroutines               | 35.1 ms                                                | 31.2 ms: 1.12x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 52.3 us: 1.12x faster                                                 |
| python_startup           | 14.6 ms                                                | 13.4 ms: 1.09x faster                                                 |
| pathlib                  | 20.5 ms                                                | 19.2 ms: 1.06x faster                                                 |
| json_dumps               | 14.2 ms                                                | 13.4 ms: 1.06x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 111 ms: 1.04x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 26.8 ms: 1.04x faster                                                 |
| pidigits                 | 191 ms                                                 | 184 ms: 1.04x faster                                                  |
| regex_dna                | 227 ms                                                 | 221 ms: 1.02x faster                                                  |
| logging_silent           | 190 ns                                                 | 185 ns: 1.02x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.56 ms: 1.02x faster                                                 |
| richards                 | 79.3 ms                                                | 78.0 ms: 1.02x faster                                                 |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                  |
| bench_mp_pool            | 24.0 ms                                                | 23.9 ms: 1.00x faster                                                 |
| docutils                 | 3.30 sec                                               | 3.35 sec: 1.02x slower                                                |
| scimark_fft              | 466 ms                                                 | 475 ms: 1.02x slower                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.63 ms: 1.02x slower                                                 |
| tomli_loads              | 3.14 sec                                               | 3.22 sec: 1.03x slower                                                |
| json_loads               | 31.2 us                                                | 32.2 us: 1.03x slower                                                 |
| pycparser                | 1.58 sec                                               | 1.64 sec: 1.04x slower                                                |
| deltablue                | 7.91 ms                                                | 8.28 ms: 1.05x slower                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 124 ms: 1.05x slower                                                  |
| json                     | 5.69 ms                                                | 5.99 ms: 1.05x slower                                                 |
| deepcopy_reduce          | 4.17 us                                                | 4.42 us: 1.06x slower                                                 |
| chaos                    | 115 ms                                                 | 124 ms: 1.08x slower                                                  |
| pyflate                  | 716 ms                                                 | 777 ms: 1.08x slower                                                  |
| spectral_norm            | 170 ms                                                 | 186 ms: 1.09x slower                                                  |
| html5lib                 | 88.9 ms                                                | 97.3 ms: 1.10x slower                                                 |
| sympy_integrate          | 25.8 ms                                                | 28.7 ms: 1.11x slower                                                 |
| xml_etree_generate       | 99.4 ms                                                | 111 ms: 1.11x slower                                                  |
| nqueens                  | 106 ms                                                 | 119 ms: 1.13x slower                                                  |
| xml_etree_process        | 79.1 ms                                                | 89.5 ms: 1.13x slower                                                 |
| 2to3                     | 348 ms                                                 | 394 ms: 1.13x slower                                                  |
| fannkuch                 | 532 ms                                                 | 608 ms: 1.14x slower                                                  |
| regex_compile            | 188 ms                                                 | 217 ms: 1.15x slower                                                  |
| hexiom                   | 10.4 ms                                                | 12.0 ms: 1.16x slower                                                 |
| thrift                   | 1.07 ms                                                | 1.25 ms: 1.17x slower                                                 |
| raytrace                 | 507 ms                                                 | 593 ms: 1.17x slower                                                  |
| pickle_pure_python       | 484 us                                                 | 571 us: 1.18x slower                                                  |
| mdp                      | 2.85 sec                                               | 3.37 sec: 1.18x slower                                                |
| scimark_sor              | 220 ms                                                 | 264 ms: 1.20x slower                                                  |
| unpickle_pure_python     | 331 us                                                 | 399 us: 1.21x slower                                                  |
| float                    | 117 ms                                                 | 142 ms: 1.21x slower                                                  |
| sympy_str                | 346 ms                                                 | 424 ms: 1.23x slower                                                  |
| sqlglot_normalize        | 143 ms                                                 | 177 ms: 1.24x slower                                                  |
| meteor_contest           | 120 ms                                                 | 148 ms: 1.24x slower                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 3.20 ms: 1.24x slower                                                 |
| sqlglot_parse            | 2.17 ms                                                | 2.71 ms: 1.25x slower                                                 |
| genshi_text              | 31.8 ms                                                | 40.2 ms: 1.26x slower                                                 |
| django_template          | 48.2 ms                                                | 60.9 ms: 1.27x slower                                                 |
| genshi_xml               | 66.0 ms                                                | 83.9 ms: 1.27x slower                                                 |
| async_generators         | 444 ms                                                 | 565 ms: 1.27x slower                                                  |
| go                       | 240 ms                                                 | 307 ms: 1.28x slower                                                  |
| logging_simple           | 8.30 us                                                | 10.7 us: 1.28x slower                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 88.8 ms: 1.28x slower                                                 |
| sympy_sum                | 196 ms                                                 | 254 ms: 1.29x slower                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 1.32 sec: 1.29x slower                                                |
| pprint_pformat           | 2.10 sec                                               | 2.72 sec: 1.29x slower                                                |
| mako                     | 16.3 ms                                                | 21.1 ms: 1.29x slower                                                 |
| logging_format           | 9.09 us                                                | 12.0 us: 1.32x slower                                                 |
| sympy_expand             | 566 ms                                                 | 753 ms: 1.33x slower                                                  |
| telco                    | 7.27 ms                                                | 10.0 ms: 1.38x slower                                                 |
| coverage                 | 79.4 ms                                                | 110 ms: 1.39x slower                                                  |
| scimark_lu               | 176 ms                                                 | 245 ms: 1.39x slower                                                  |
| nbody                    | 154 ms                                                 | 217 ms: 1.42x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 9.08 ms: 1.53x slower                                                 |
| bench_thread_pool        | 986 us                                                 | 3.03 ms: 3.07x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (3): tornado_http, richards_super, comprehensions
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 99.72% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.28x