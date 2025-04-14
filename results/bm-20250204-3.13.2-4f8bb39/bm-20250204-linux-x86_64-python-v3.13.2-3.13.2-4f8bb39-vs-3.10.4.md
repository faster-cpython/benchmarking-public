# Results vs. 3.10.4

- fork: python
- ref: v3.13.2
- machine: linux-x86_64
- commit hash: 4f8bb39
- commit date: 2025-02-04
- overall geometric mean: 1.393x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 266 ms: 1.31x faster                                   |
| chameleon      | 9.68 ms                                                | 6.89 ms: 1.41x faster                                  |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                 |
| html5lib       | 88.9 ms                                                | 64.7 ms: 1.37x faster                                  |
| tornado_http   | 136 ms                                                 | 91.7 ms: 1.49x faster                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 843 ms: 2.10x faster                                   |
| async_tree_none         | 728 ms                                                 | 352 ms: 2.07x faster                                   |
| async_tree_memoization  | 870 ms                                                 | 457 ms: 1.90x faster                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 581 ms: 1.75x faster                                   |
| Geometric mean          | (ref)                                                  | 1.95x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 154 ms                                                 | 87.8 ms: 1.75x faster                                  |
| float          | 117 ms                                                 | 78.9 ms: 1.49x faster                                  |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                   |
| Geometric mean | (ref)                                                  | 1.38x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 131 ms: 1.44x faster                                   |
| regex_effbot   | 3.63 ms                                                | 3.38 ms: 1.07x faster                                  |
| regex_v8       | 27.8 ms                                                | 26.4 ms: 1.05x faster                                  |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                   |
| Geometric mean | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 304 us: 1.59x faster                                   |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.53x faster                                   |
| tomli_loads          | 3.14 sec                                               | 2.11 sec: 1.49x faster                                 |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                  |
| xml_etree_process    | 79.1 ms                                                | 60.5 ms: 1.31x faster                                  |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                  |
| xml_etree_generate   | 99.4 ms                                                | 86.2 ms: 1.15x faster                                  |
| xml_etree_iterparse  | 115 ms                                                 | 103 ms: 1.12x faster                                   |
| xml_etree_parse      | 168 ms                                                 | 155 ms: 1.08x faster                                   |
| Geometric mean       | (ref)                                                  | 1.30x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.15x faster                                  |
| python_startup_no_site | 5.93 ms                                                | 6.99 ms: 1.18x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.1 ms: 1.50x faster                                  |
| mako            | 16.3 ms                                                | 11.0 ms: 1.48x faster                                  |
| genshi_text     | 31.8 ms                                                | 22.7 ms: 1.40x faster                                  |
| genshi_xml      | 66.0 ms                                                | 51.0 ms: 1.29x faster                                  |
| Geometric mean  | (ref)                                                  | 1.42x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.37x faster                                   |
| generators               | 80.1 ms                                                | 29.2 ms: 2.75x faster                                  |
| deltablue                | 7.91 ms                                                | 3.18 ms: 2.49x faster                                  |
| async_tree_io            | 1.77 sec                                               | 843 ms: 2.10x faster                                   |
| async_tree_none          | 728 ms                                                 | 352 ms: 2.07x faster                                   |
| chaos                    | 115 ms                                                 | 59.0 ms: 1.96x faster                                  |
| async_tree_memoization   | 870 ms                                                 | 457 ms: 1.90x faster                                   |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                   |
| logging_silent           | 190 ns                                                 | 100 ns: 1.90x faster                                   |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.79x faster                                   |
| pylint                   | 551 ms                                                 | 313 ms: 1.76x faster                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 581 ms: 1.75x faster                                   |
| nbody                    | 154 ms                                                 | 87.8 ms: 1.75x faster                                  |
| scimark_monte_carlo      | 118 ms                                                 | 68.2 ms: 1.73x faster                                  |
| djangocms                | 38.4 us                                                | 22.2 us: 1.73x faster                                  |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                  |
| richards_super           | 94.7 ms                                                | 55.1 ms: 1.72x faster                                  |
| crypto_pyaes             | 128 ms                                                 | 74.6 ms: 1.71x faster                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                  |
| go                       | 240 ms                                                 | 141 ms: 1.71x faster                                   |
| hexiom                   | 10.4 ms                                                | 6.21 ms: 1.67x faster                                  |
| richards                 | 79.3 ms                                                | 47.8 ms: 1.66x faster                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                  |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.59x faster                                   |
| coroutines               | 35.1 ms                                                | 22.4 ms: 1.56x faster                                  |
| spectral_norm            | 170 ms                                                 | 111 ms: 1.53x faster                                   |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.53x faster                                   |
| pyflate                  | 716 ms                                                 | 474 ms: 1.51x faster                                   |
| deepcopy_memo            | 58.5 us                                                | 38.8 us: 1.51x faster                                  |
| django_template          | 48.2 ms                                                | 32.1 ms: 1.50x faster                                  |
| tomli_loads              | 3.14 sec                                               | 2.11 sec: 1.49x faster                                 |
| tornado_http             | 136 ms                                                 | 91.7 ms: 1.49x faster                                  |
| float                    | 117 ms                                                 | 78.9 ms: 1.49x faster                                  |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.49x faster                                   |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.48x faster                                  |
| logging_simple           | 8.30 us                                                | 5.72 us: 1.45x faster                                  |
| regex_compile            | 188 ms                                                 | 131 ms: 1.44x faster                                   |
| logging_format           | 9.09 us                                                | 6.43 us: 1.41x faster                                  |
| chameleon                | 9.68 ms                                                | 6.89 ms: 1.41x faster                                  |
| genshi_text              | 31.8 ms                                                | 22.7 ms: 1.40x faster                                  |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                 |
| pprint_safe_repr         | 1.02 sec                                               | 737 ms: 1.38x faster                                   |
| html5lib                 | 88.9 ms                                                | 64.7 ms: 1.37x faster                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.37x faster                                  |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                  |
| thrift                   | 1.07 ms                                                | 789 us: 1.36x faster                                   |
| nqueens                  | 106 ms                                                 | 78.1 ms: 1.35x faster                                  |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.35x faster                                 |
| deepcopy                 | 479 us                                                 | 360 us: 1.33x faster                                   |
| fannkuch                 | 532 ms                                                 | 400 ms: 1.33x faster                                   |
| xml_etree_process        | 79.1 ms                                                | 60.5 ms: 1.31x faster                                  |
| 2to3                     | 348 ms                                                 | 266 ms: 1.31x faster                                   |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                   |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                  |
| dulwich_log              | 84.3 ms                                                | 64.9 ms: 1.30x faster                                  |
| deepcopy_reduce          | 4.17 us                                                | 3.21 us: 1.30x faster                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.30x faster                                   |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.29x faster                                   |
| genshi_xml               | 66.0 ms                                                | 51.0 ms: 1.29x faster                                  |
| scimark_fft              | 466 ms                                                 | 361 ms: 1.29x faster                                   |
| sqlglot_optimize         | 69.2 ms                                                | 53.9 ms: 1.28x faster                                  |
| gunicorn                 | 1.53 ms                                                | 1.20 ms: 1.28x faster                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.07 ms: 1.28x faster                                  |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                 |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                   |
| sympy_expand             | 566 ms                                                 | 463 ms: 1.22x faster                                   |
| bench_thread_pool        | 986 us                                                 | 815 us: 1.21x faster                                   |
| pathlib                  | 20.5 ms                                                | 17.4 ms: 1.18x faster                                  |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                  |
| xml_etree_generate       | 99.4 ms                                                | 86.2 ms: 1.15x faster                                  |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.15x faster                                  |
| async_generators         | 444 ms                                                 | 392 ms: 1.13x faster                                   |
| xml_etree_iterparse      | 115 ms                                                 | 103 ms: 1.12x faster                                   |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                 |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                  |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                   |
| xml_etree_parse          | 168 ms                                                 | 155 ms: 1.08x faster                                   |
| regex_effbot             | 3.63 ms                                                | 3.38 ms: 1.07x faster                                  |
| regex_v8                 | 27.8 ms                                                | 26.4 ms: 1.05x faster                                  |
| sqlite_synth             | 3.02 us                                                | 2.90 us: 1.04x faster                                  |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                   |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                   |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                   |
| coverage                 | 79.4 ms                                                | 84.8 ms: 1.07x slower                                  |
| python_startup_no_site   | 5.93 ms                                                | 6.99 ms: 1.18x slower                                  |
| telco                    | 7.27 ms                                                | 8.62 ms: 1.19x slower                                  |
| gc_traversal             | 3.62 ms                                                | 4.65 ms: 1.28x slower                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.44 ms: 1.51x slower                                  |
| Geometric mean           | (ref)                                                  | 1.39x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250204-3.13.2-4f8bb39/bm-20250204-linux-x86_64-python-v3.13.2-3.13.2-4f8bb39.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.393x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.23x