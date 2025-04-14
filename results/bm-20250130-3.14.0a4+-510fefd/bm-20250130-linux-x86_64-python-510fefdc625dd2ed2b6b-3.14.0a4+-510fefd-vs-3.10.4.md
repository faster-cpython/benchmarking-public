# Results vs. 3.10.4

- fork: python
- ref: 510fefdc625dd2ed2b6b
- machine: linux-x86_64
- commit hash: 510fefd
- commit date: 2025-01-30
- overall geometric mean: 1.458x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 251 ms: 1.39x faster                                                   |
| docutils       | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                 |
| html5lib       | 88.9 ms                                                | 61.1 ms: 1.45x faster                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 619 ms: 2.86x faster                                                   |
| async_tree_none         | 728 ms                                                 | 264 ms: 2.76x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 322 ms: 2.70x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 494 ms: 2.05x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.57x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 91.6 ms: 1.68x faster                                                  |
| float          | 117 ms                                                 | 70.1 ms: 1.67x faster                                                  |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.42x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.50x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.21 ms: 1.13x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                  |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.51x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 59.2 ms: 1.34x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 83.6 ms: 1.19x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 98.3 ms: 1.17x faster                                                  |
| json_loads           | 31.2 us                                                | 28.5 us: 1.09x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.14x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.00 ms: 1.18x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                  |
| genshi_text     | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                  |
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 47.9 ms: 1.38x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 158 us: 3.45x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 619 ms: 2.86x faster                                                   |
| generators               | 80.1 ms                                                | 28.3 ms: 2.83x faster                                                  |
| async_tree_none          | 728 ms                                                 | 264 ms: 2.76x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 322 ms: 2.70x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.23 ms: 2.45x faster                                                  |
| go                       | 240 ms                                                 | 117 ms: 2.06x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 494 ms: 2.05x faster                                                   |
| pylint                   | 551 ms                                                 | 272 ms: 2.03x faster                                                   |
| chaos                    | 115 ms                                                 | 58.0 ms: 1.99x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 30.2 us: 1.94x faster                                                  |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                                   |
| deepcopy                 | 479 us                                                 | 257 us: 1.87x faster                                                   |
| richards_super           | 94.7 ms                                                | 51.5 ms: 1.84x faster                                                  |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 70.8 ms: 1.81x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.3 us: 1.77x faster                                                  |
| richards                 | 79.3 ms                                                | 45.1 ms: 1.76x faster                                                  |
| logging_silent           | 190 ns                                                 | 108 ns: 1.76x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 67.4 ms: 1.75x faster                                                  |
| spectral_norm            | 170 ms                                                 | 98.0 ms: 1.73x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.26 ms: 1.72x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.13 ms: 1.70x faster                                                  |
| nbody                    | 154 ms                                                 | 91.6 ms: 1.68x faster                                                  |
| float                    | 117 ms                                                 | 70.1 ms: 1.67x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.56 ms: 1.65x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                  |
| pyflate                  | 716 ms                                                 | 464 ms: 1.54x faster                                                   |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.51x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.50 us: 1.51x faster                                                  |
| django_template          | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                  |
| regex_compile            | 188 ms                                                 | 125 ms: 1.50x faster                                                   |
| genshi_text              | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                  |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                   |
| logging_format           | 9.09 us                                                | 6.07 us: 1.50x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.41 ms: 1.47x faster                                                  |
| html5lib                 | 88.9 ms                                                | 61.1 ms: 1.45x faster                                                  |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.4 ms: 1.42x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 721 ms: 1.41x faster                                                   |
| thrift                   | 1.07 ms                                                | 760 us: 1.41x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.40x faster                                                 |
| 2to3                     | 348 ms                                                 | 251 ms: 1.39x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 103 ms: 1.38x faster                                                   |
| scimark_fft              | 466 ms                                                 | 337 ms: 1.38x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 47.9 ms: 1.38x faster                                                  |
| sympy_sum                | 196 ms                                                 | 145 ms: 1.36x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.35x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 59.2 ms: 1.34x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 51.9 ms: 1.33x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.32x faster                                                  |
| fannkuch                 | 532 ms                                                 | 405 ms: 1.31x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 64.5 ms: 1.31x faster                                                  |
| sympy_str                | 346 ms                                                 | 265 ms: 1.31x faster                                                   |
| pathlib                  | 20.5 ms                                                | 15.7 ms: 1.30x faster                                                  |
| nqueens                  | 106 ms                                                 | 82.0 ms: 1.29x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                 |
| sympy_expand             | 566 ms                                                 | 450 ms: 1.26x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 83.6 ms: 1.19x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 98.3 ms: 1.17x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.47 sec: 1.15x faster                                                 |
| async_generators         | 444 ms                                                 | 385 ms: 1.15x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 857 us: 1.15x faster                                                   |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.14x faster                                                  |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.21 ms: 1.13x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                  |
| json                     | 5.69 ms                                                | 5.09 ms: 1.12x faster                                                  |
| json_loads               | 31.2 us                                                | 28.5 us: 1.09x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                                  |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                   |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                   |
| telco                    | 7.27 ms                                                | 7.89 ms: 1.09x slower                                                  |
| coverage                 | 79.4 ms                                                | 90.2 ms: 1.14x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.00 ms: 1.18x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.61 ms: 1.27x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.44 ms: 1.51x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 80.5 ms: 3.35x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                           |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250130-3.14.0a4+-510fefd/bm-20250130-linux-x86_64-python-510fefdc625dd2ed2b6b-3.14.0a4+-510fefd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.458x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.26x