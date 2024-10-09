# Results vs. 3.10.4

- fork: python
- ref: v3.13.0
- machine: linux-x86_64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.36x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 265 ms: 1.32x faster                                   |
| chameleon      | 9.68 ms                                                | 6.85 ms: 1.41x faster                                  |
| docutils       | 3.30 sec                                               | 2.58 sec: 1.28x faster                                 |
| html5lib       | 88.9 ms                                                | 64.5 ms: 1.38x faster                                  |
| tornado_http   | 136 ms                                                 | 91.5 ms: 1.49x faster                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 843 ms: 2.10x faster                                   |
| async_tree_none         | 728 ms                                                 | 354 ms: 2.06x faster                                   |
| async_tree_memoization  | 870 ms                                                 | 442 ms: 1.97x faster                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 574 ms: 1.77x faster                                   |
| Geometric mean          | (ref)                                                  | 1.97x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 154 ms                                                 | 85.7 ms: 1.79x faster                                  |
| float          | 117 ms                                                 | 78.5 ms: 1.49x faster                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                   |
| Geometric mean | (ref)                                                  | 1.40x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 131 ms: 1.44x faster                                   |
| regex_v8       | 27.8 ms                                                | 25.3 ms: 1.10x faster                                  |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                   |
| regex_effbot   | 3.63 ms                                                | 3.88 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 300 us: 1.61x faster                                   |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                   |
| tomli_loads          | 3.14 sec                                               | 2.11 sec: 1.49x faster                                 |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                  |
| xml_etree_process    | 79.1 ms                                                | 60.4 ms: 1.31x faster                                  |
| json_loads           | 31.2 us                                                | 27.0 us: 1.16x faster                                  |
| xml_etree_generate   | 99.4 ms                                                | 87.0 ms: 1.14x faster                                  |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.13x faster                                   |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                   |
| unpickle_list        | 5.20 us                                                | 4.96 us: 1.05x faster                                  |
| pickle_list          | 5.08 us                                                | 5.01 us: 1.01x faster                                  |
| unpickle             | 14.4 us                                                | 14.9 us: 1.03x slower                                  |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                  |
| pickle_dict          | 29.6 us                                                | 33.2 us: 1.12x slower                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                  |
| python_startup_no_site | 5.93 ms                                                | 6.99 ms: 1.18x slower                                  |
| Geometric mean         | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                  |
| django_template | 48.2 ms                                                | 34.4 ms: 1.40x faster                                  |
| genshi_text     | 31.8 ms                                                | 22.9 ms: 1.39x faster                                  |
| genshi_xml      | 66.0 ms                                                | 50.3 ms: 1.31x faster                                  |
| Geometric mean  | (ref)                                                  | 1.39x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.42x faster                                   |
| generators               | 80.1 ms                                                | 28.8 ms: 2.78x faster                                  |
| deltablue                | 7.91 ms                                                | 3.15 ms: 2.51x faster                                  |
| async_tree_io            | 1.77 sec                                               | 843 ms: 2.10x faster                                   |
| async_tree_none          | 728 ms                                                 | 354 ms: 2.06x faster                                   |
| chaos                    | 115 ms                                                 | 58.4 ms: 1.98x faster                                  |
| async_tree_memoization   | 870 ms                                                 | 442 ms: 1.97x faster                                   |
| raytrace                 | 507 ms                                                 | 262 ms: 1.94x faster                                   |
| asyncio_tcp              | 922 ms                                                 | 488 ms: 1.89x faster                                   |
| logging_silent           | 190 ns                                                 | 102 ns: 1.86x faster                                   |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.79x faster                                   |
| nbody                    | 154 ms                                                 | 85.7 ms: 1.79x faster                                  |
| scimark_monte_carlo      | 118 ms                                                 | 66.3 ms: 1.78x faster                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 574 ms: 1.77x faster                                   |
| pylint                   | 551 ms                                                 | 313 ms: 1.76x faster                                   |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                  |
| crypto_pyaes             | 128 ms                                                 | 73.0 ms: 1.75x faster                                  |
| richards_super           | 94.7 ms                                                | 54.4 ms: 1.74x faster                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                  |
| hexiom                   | 10.4 ms                                                | 6.13 ms: 1.70x faster                                  |
| go                       | 240 ms                                                 | 142 ms: 1.70x faster                                   |
| richards                 | 79.3 ms                                                | 48.1 ms: 1.65x faster                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                  |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.61x faster                                   |
| pyflate                  | 716 ms                                                 | 460 ms: 1.56x faster                                   |
| coroutines               | 35.1 ms                                                | 22.5 ms: 1.56x faster                                  |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                   |
| deepcopy_memo            | 58.5 us                                                | 38.0 us: 1.54x faster                                  |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                   |
| float                    | 117 ms                                                 | 78.5 ms: 1.49x faster                                  |
| tornado_http             | 136 ms                                                 | 91.5 ms: 1.49x faster                                  |
| tomli_loads              | 3.14 sec                                               | 2.11 sec: 1.49x faster                                 |
| spectral_norm            | 170 ms                                                 | 115 ms: 1.48x faster                                   |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                  |
| logging_simple           | 8.30 us                                                | 5.66 us: 1.47x faster                                  |
| logging_format           | 9.09 us                                                | 6.25 us: 1.45x faster                                  |
| regex_compile            | 188 ms                                                 | 131 ms: 1.44x faster                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                 |
| unpack_sequence          | 60.0 ns                                                | 42.4 ns: 1.42x faster                                  |
| chameleon                | 9.68 ms                                                | 6.85 ms: 1.41x faster                                  |
| django_template          | 48.2 ms                                                | 34.4 ms: 1.40x faster                                  |
| fannkuch                 | 532 ms                                                 | 381 ms: 1.40x faster                                   |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                 |
| genshi_text              | 31.8 ms                                                | 22.9 ms: 1.39x faster                                  |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                  |
| html5lib                 | 88.9 ms                                                | 64.5 ms: 1.38x faster                                  |
| pprint_safe_repr         | 1.02 sec                                               | 744 ms: 1.37x faster                                   |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                  |
| deepcopy                 | 479 us                                                 | 352 us: 1.36x faster                                   |
| thrift                   | 1.07 ms                                                | 796 us: 1.35x faster                                   |
| dulwich_log              | 84.3 ms                                                | 63.0 ms: 1.34x faster                                  |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.33x faster                                   |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                 |
| deepcopy_reduce          | 4.17 us                                                | 3.17 us: 1.32x faster                                  |
| 2to3                     | 348 ms                                                 | 265 ms: 1.32x faster                                   |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                   |
| nqueens                  | 106 ms                                                 | 80.6 ms: 1.31x faster                                  |
| genshi_xml               | 66.0 ms                                                | 50.3 ms: 1.31x faster                                  |
| xml_etree_process        | 79.1 ms                                                | 60.4 ms: 1.31x faster                                  |
| dask                     | 441 ms                                                 | 338 ms: 1.31x faster                                   |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.03 ms: 1.29x faster                                  |
| sqlglot_optimize         | 69.2 ms                                                | 53.9 ms: 1.28x faster                                  |
| docutils                 | 3.30 sec                                               | 2.58 sec: 1.28x faster                                 |
| sympy_str                | 346 ms                                                 | 274 ms: 1.26x faster                                   |
| scimark_fft              | 466 ms                                                 | 369 ms: 1.26x faster                                   |
| aiohttp                  | 1.44 ms                                                | 1.14 ms: 1.26x faster                                  |
| gunicorn                 | 1.53 ms                                                | 1.23 ms: 1.25x faster                                  |
| sympy_expand             | 566 ms                                                 | 462 ms: 1.23x faster                                   |
| bench_thread_pool        | 986 us                                                 | 815 us: 1.21x faster                                   |
| djangocms                | 38.4 us                                                | 31.9 us: 1.21x faster                                  |
| pathlib                  | 20.5 ms                                                | 17.1 ms: 1.20x faster                                  |
| json_loads               | 31.2 us                                                | 27.0 us: 1.16x faster                                  |
| xml_etree_generate       | 99.4 ms                                                | 87.0 ms: 1.14x faster                                  |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.13x faster                                   |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                   |
| regex_v8                 | 27.8 ms                                                | 25.3 ms: 1.10x faster                                  |
| json                     | 5.69 ms                                                | 5.20 ms: 1.09x faster                                  |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                   |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                  |
| unpickle_list            | 5.20 us                                                | 4.96 us: 1.05x faster                                  |
| mdp                      | 2.85 sec                                               | 2.74 sec: 1.04x faster                                 |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                   |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                   |
| async_generators         | 444 ms                                                 | 433 ms: 1.03x faster                                   |
| pickle_list              | 5.08 us                                                | 5.01 us: 1.01x faster                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.61 ms: 1.01x faster                                  |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                   |
| unpickle                 | 14.4 us                                                | 14.9 us: 1.03x slower                                  |
| gc_traversal             | 3.62 ms                                                | 3.81 ms: 1.05x slower                                  |
| coverage                 | 79.4 ms                                                | 83.7 ms: 1.05x slower                                  |
| flaskblogging            | 8.58 ms                                                | 9.11 ms: 1.06x slower                                  |
| regex_effbot             | 3.63 ms                                                | 3.88 ms: 1.07x slower                                  |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                  |
| pickle_dict              | 29.6 us                                                | 33.2 us: 1.12x slower                                  |
| telco                    | 7.27 ms                                                | 8.45 ms: 1.16x slower                                  |
| python_startup_no_site   | 5.93 ms                                                | 6.99 ms: 1.18x slower                                  |
| mypy2                    | 894 ms                                                 | 1.07 sec: 1.19x slower                                 |
| Geometric mean           | (ref)                                                  | 1.36x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.12x