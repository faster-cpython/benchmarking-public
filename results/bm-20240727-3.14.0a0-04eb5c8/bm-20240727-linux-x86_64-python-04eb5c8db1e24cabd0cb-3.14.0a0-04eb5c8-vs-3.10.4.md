# Results vs. 3.10.4

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.43x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 264 ms: 1.32x faster                                                  |
| docutils       | 3.30 sec                                               | 2.74 sec: 1.20x faster                                                |
| html5lib       | 88.9 ms                                                | 65.6 ms: 1.35x faster                                                 |
| tornado_http   | 136 ms                                                 | 90.9 ms: 1.50x faster                                                 |
| Geometric mean | (ref)                                                  | 1.34x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 323 ms: 2.26x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 409 ms: 2.13x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 893 ms: 1.98x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 562 ms: 1.81x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.04x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 89.0 ms: 1.73x faster                                                 |
| float          | 117 ms                                                 | 78.1 ms: 1.50x faster                                                 |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.38x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 131 ms: 1.44x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                 |
| regex_dna      | 227 ms                                                 | 226 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 306 us: 1.58x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 212 us: 1.56x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.03 sec: 1.54x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 60.2 ms: 1.31x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 87.0 ms: 1.14x faster                                                 |
| json_loads           | 31.2 us                                                | 27.6 us: 1.13x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 154 ms: 1.09x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.0 ms: 1.48x faster                                                 |
| django_template | 48.2 ms                                                | 34.5 ms: 1.40x faster                                                 |
| genshi_text     | 31.8 ms                                                | 23.7 ms: 1.34x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 52.4 ms: 1.26x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.37x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.27x faster                                                  |
| generators               | 80.1 ms                                                | 28.5 ms: 2.81x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.24 ms: 2.44x faster                                                 |
| async_tree_none          | 728 ms                                                 | 323 ms: 2.26x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 409 ms: 2.13x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.4 us: 1.99x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 893 ms: 1.98x faster                                                  |
| chaos                    | 115 ms                                                 | 59.3 ms: 1.95x faster                                                 |
| raytrace                 | 507 ms                                                 | 261 ms: 1.94x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 487 ms: 1.89x faster                                                  |
| richards_super           | 94.7 ms                                                | 51.8 ms: 1.83x faster                                                 |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 562 ms: 1.81x faster                                                  |
| deepcopy                 | 479 us                                                 | 267 us: 1.80x faster                                                  |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.75x faster                                                  |
| pylint                   | 551 ms                                                 | 318 ms: 1.74x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 73.6 ms: 1.74x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                 |
| richards                 | 79.3 ms                                                | 45.9 ms: 1.73x faster                                                 |
| nbody                    | 154 ms                                                 | 89.0 ms: 1.73x faster                                                 |
| go                       | 240 ms                                                 | 139 ms: 1.73x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 68.6 ms: 1.72x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.22 ms: 1.67x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 306 us: 1.58x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 212 us: 1.56x faster                                                  |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 2.03 sec: 1.54x faster                                                |
| pyflate                  | 716 ms                                                 | 470 ms: 1.53x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.76 us: 1.51x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.49 us: 1.51x faster                                                 |
| tornado_http             | 136 ms                                                 | 90.9 ms: 1.50x faster                                                 |
| float                    | 117 ms                                                 | 78.1 ms: 1.50x faster                                                 |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.50x faster                                                  |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.48x faster                                                 |
| logging_format           | 9.09 us                                                | 6.17 us: 1.47x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                |
| regex_compile            | 188 ms                                                 | 131 ms: 1.44x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.62 ms: 1.40x faster                                                 |
| django_template          | 48.2 ms                                                | 34.5 ms: 1.40x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                                |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                 |
| thrift                   | 1.07 ms                                                | 777 us: 1.38x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.37x faster                                                |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 748 ms: 1.36x faster                                                  |
| html5lib                 | 88.9 ms                                                | 65.6 ms: 1.35x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.34x faster                                                  |
| genshi_text              | 31.8 ms                                                | 23.7 ms: 1.34x faster                                                 |
| nqueens                  | 106 ms                                                 | 79.8 ms: 1.33x faster                                                 |
| scimark_fft              | 466 ms                                                 | 351 ms: 1.33x faster                                                  |
| 2to3                     | 348 ms                                                 | 264 ms: 1.32x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 60.2 ms: 1.31x faster                                                 |
| fannkuch                 | 532 ms                                                 | 405 ms: 1.31x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                                 |
| pathlib                  | 20.5 ms                                                | 15.7 ms: 1.30x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 53.2 ms: 1.30x faster                                                 |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.29x faster                                                  |
| sympy_str                | 346 ms                                                 | 274 ms: 1.26x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 52.4 ms: 1.26x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 789 us: 1.25x faster                                                  |
| dask                     | 441 ms                                                 | 355 ms: 1.24x faster                                                  |
| sympy_expand             | 566 ms                                                 | 464 ms: 1.22x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.74 sec: 1.20x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 87.0 ms: 1.14x faster                                                 |
| json_loads               | 31.2 us                                                | 27.6 us: 1.13x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                                |
| regex_v8                 | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                 |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                  |
| json                     | 5.69 ms                                                | 5.17 ms: 1.10x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 154 ms: 1.09x faster                                                  |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| async_generators         | 444 ms                                                 | 437 ms: 1.01x faster                                                  |
| regex_dna                | 227 ms                                                 | 226 ms: 1.00x faster                                                  |
| gc_traversal             | 3.62 ms                                                | 3.75 ms: 1.03x slower                                                 |
| coverage                 | 79.4 ms                                                | 85.4 ms: 1.07x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.08x slower                                                 |
| telco                    | 7.27 ms                                                | 8.10 ms: 1.12x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                          |

Benchmark hidden because not significant (3): bench_mp_pool, asyncio_websockets, regex_effbot
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.12x