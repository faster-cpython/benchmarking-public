# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_escape
- machine: linux-x86_64
- commit hash: 3bd6587
- commit date: 2024-07-24
- overall geometric mean: 1.42x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 271 ms: 1.29x faster                                             |
| docutils       | 3.30 sec                                               | 2.89 sec: 1.14x faster                                           |
| html5lib       | 88.9 ms                                                | 63.7 ms: 1.39x faster                                            |
| tornado_http   | 136 ms                                                 | 93.4 ms: 1.46x faster                                            |
| Geometric mean | (ref)                                                  | 1.31x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 327 ms: 2.23x faster                                             |
| async_tree_memoization  | 870 ms                                                 | 426 ms: 2.04x faster                                             |
| async_tree_io           | 1.77 sec                                               | 899 ms: 1.97x faster                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 564 ms: 1.80x faster                                             |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.3 ms: 1.89x faster                                            |
| float          | 117 ms                                                 | 70.7 ms: 1.66x faster                                            |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.47x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.40x faster                                             |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                            |
| regex_dna      | 227 ms                                                 | 231 ms: 1.02x slower                                             |
| regex_effbot   | 3.63 ms                                                | 3.76 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                  | 1.11x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.64x faster                                           |
| pickle_pure_python   | 484 us                                                 | 302 us: 1.61x faster                                             |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                             |
| xml_etree_process    | 79.1 ms                                                | 56.2 ms: 1.41x faster                                            |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.37x faster                                            |
| xml_etree_generate   | 99.4 ms                                                | 80.2 ms: 1.24x faster                                            |
| xml_etree_iterparse  | 115 ms                                                 | 98.4 ms: 1.17x faster                                            |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                             |
| json_loads           | 31.2 us                                                | 27.8 us: 1.12x faster                                            |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                            |
| python_startup_no_site | 5.93 ms                                                | 7.16 ms: 1.21x slower                                            |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.72 ms: 1.68x faster                                            |
| django_template | 48.2 ms                                                | 36.3 ms: 1.33x faster                                            |
| genshi_text     | 31.8 ms                                                | 24.5 ms: 1.30x faster                                            |
| genshi_xml      | 66.0 ms                                                | 58.3 ms: 1.13x faster                                            |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.21x faster                                             |
| generators               | 80.1 ms                                                | 28.8 ms: 2.78x faster                                            |
| deltablue                | 7.91 ms                                                | 3.53 ms: 2.24x faster                                            |
| async_tree_none          | 728 ms                                                 | 327 ms: 2.23x faster                                             |
| deepcopy_memo            | 58.5 us                                                | 28.1 us: 2.08x faster                                            |
| async_tree_memoization   | 870 ms                                                 | 426 ms: 2.04x faster                                             |
| richards_super           | 94.7 ms                                                | 47.6 ms: 1.99x faster                                            |
| chaos                    | 115 ms                                                 | 58.1 ms: 1.99x faster                                            |
| scimark_monte_carlo      | 118 ms                                                 | 59.9 ms: 1.97x faster                                            |
| async_tree_io            | 1.77 sec                                               | 899 ms: 1.97x faster                                             |
| crypto_pyaes             | 128 ms                                                 | 66.5 ms: 1.92x faster                                            |
| richards                 | 79.3 ms                                                | 41.5 ms: 1.91x faster                                            |
| nbody                    | 154 ms                                                 | 81.3 ms: 1.89x faster                                            |
| raytrace                 | 507 ms                                                 | 269 ms: 1.88x faster                                             |
| logging_silent           | 190 ns                                                 | 103 ns: 1.85x faster                                             |
| asyncio_tcp              | 922 ms                                                 | 504 ms: 1.83x faster                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 564 ms: 1.80x faster                                             |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.75x faster                                            |
| deepcopy                 | 479 us                                                 | 275 us: 1.74x faster                                             |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.72x faster                                             |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                            |
| mako                     | 16.3 ms                                                | 9.72 ms: 1.68x faster                                            |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.67x faster                                             |
| go                       | 240 ms                                                 | 145 ms: 1.66x faster                                             |
| float                    | 117 ms                                                 | 70.7 ms: 1.66x faster                                            |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.64x faster                                           |
| pyflate                  | 716 ms                                                 | 440 ms: 1.63x faster                                             |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                            |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.61x faster                                             |
| hexiom                   | 10.4 ms                                                | 6.51 ms: 1.60x faster                                            |
| pylint                   | 551 ms                                                 | 351 ms: 1.57x faster                                             |
| coroutines               | 35.1 ms                                                | 22.5 ms: 1.56x faster                                            |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.22 ms: 1.53x faster                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.74 us: 1.52x faster                                            |
| scimark_fft              | 466 ms                                                 | 308 ms: 1.51x faster                                             |
| logging_simple           | 8.30 us                                                | 5.55 us: 1.49x faster                                            |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                            |
| tornado_http             | 136 ms                                                 | 93.4 ms: 1.46x faster                                            |
| fannkuch                 | 532 ms                                                 | 366 ms: 1.45x faster                                             |
| pprint_safe_repr         | 1.02 sec                                               | 704 ms: 1.45x faster                                             |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                           |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.41x faster                                             |
| xml_etree_process        | 79.1 ms                                                | 56.2 ms: 1.41x faster                                            |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                           |
| regex_compile            | 188 ms                                                 | 135 ms: 1.40x faster                                             |
| html5lib                 | 88.9 ms                                                | 63.7 ms: 1.39x faster                                            |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                            |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.37x faster                                            |
| thrift                   | 1.07 ms                                                | 797 us: 1.34x faster                                             |
| django_template          | 48.2 ms                                                | 36.3 ms: 1.33x faster                                            |
| genshi_text              | 31.8 ms                                                | 24.5 ms: 1.30x faster                                            |
| 2to3                     | 348 ms                                                 | 271 ms: 1.29x faster                                             |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                            |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                             |
| nqueens                  | 106 ms                                                 | 84.8 ms: 1.25x faster                                            |
| xml_etree_generate       | 99.4 ms                                                | 80.2 ms: 1.24x faster                                            |
| sqlglot_optimize         | 69.2 ms                                                | 56.0 ms: 1.24x faster                                            |
| dulwich_log              | 84.3 ms                                                | 68.9 ms: 1.22x faster                                            |
| dask                     | 441 ms                                                 | 364 ms: 1.21x faster                                             |
| bench_thread_pool        | 986 us                                                 | 821 us: 1.20x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 98.4 ms: 1.17x faster                                            |
| sympy_str                | 346 ms                                                 | 296 ms: 1.17x faster                                             |
| sympy_integrate          | 25.8 ms                                                | 22.2 ms: 1.16x faster                                            |
| sympy_sum                | 196 ms                                                 | 169 ms: 1.16x faster                                             |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                            |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                             |
| docutils                 | 3.30 sec                                               | 2.89 sec: 1.14x faster                                           |
| genshi_xml               | 66.0 ms                                                | 58.3 ms: 1.13x faster                                            |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                             |
| sympy_expand             | 566 ms                                                 | 501 ms: 1.13x faster                                             |
| json_loads               | 31.2 us                                                | 27.8 us: 1.12x faster                                            |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                           |
| json                     | 5.69 ms                                                | 5.14 ms: 1.11x faster                                            |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                             |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                             |
| regex_dna                | 227 ms                                                 | 231 ms: 1.02x slower                                             |
| async_generators         | 444 ms                                                 | 459 ms: 1.03x slower                                             |
| regex_effbot             | 3.63 ms                                                | 3.76 ms: 1.04x slower                                            |
| gc_traversal             | 3.62 ms                                                | 3.79 ms: 1.05x slower                                            |
| telco                    | 7.27 ms                                                | 7.81 ms: 1.08x slower                                            |
| create_gc_cycles         | 1.62 ms                                                | 1.77 ms: 1.09x slower                                            |
| coverage                 | 79.4 ms                                                | 92.0 ms: 1.16x slower                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.16 ms: 1.21x slower                                            |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                     |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240724-3.14.0a0-3bd6587-JIT/bm-20240724-linux-x86_64-brandtbucher-no_escape-3.14.0a0-3bd6587.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.20x