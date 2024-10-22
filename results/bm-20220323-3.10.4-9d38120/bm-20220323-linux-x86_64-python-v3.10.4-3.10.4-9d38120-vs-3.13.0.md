# Results vs. 3.13.0

- fork: python
- ref: v3.10.4
- machine: linux-x86_64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.36x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x slower
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 348 ms: 1.32x slower                                   |
| chameleon      | 6.85 ms                                                | 9.68 ms: 1.41x slower                                  |
| docutils       | 2.58 sec                                               | 3.30 sec: 1.28x slower                                 |
| html5lib       | 64.5 ms                                                | 88.9 ms: 1.38x slower                                  |
| tornado_http   | 91.5 ms                                                | 136 ms: 1.49x slower                                   |
| Geometric mean | (ref)                                                  | 1.37x slower                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_websockets      | 555 ms                                                 | 559 ms: 1.01x slower                                   |
| async_generators        | 433 ms                                                 | 444 ms: 1.03x slower                                   |
| asyncio_tcp_ssl         | 1.79 sec                                               | 2.57 sec: 1.44x slower                                 |
| coroutines              | 22.5 ms                                                | 35.1 ms: 1.56x slower                                  |
| async_tree_cpu_io_mixed | 574 ms                                                 | 1.02 sec: 1.77x slower                                 |
| asyncio_tcp             | 488 ms                                                 | 922 ms: 1.89x slower                                   |
| async_tree_memoization  | 442 ms                                                 | 870 ms: 1.97x slower                                   |
| async_tree_none         | 354 ms                                                 | 728 ms: 2.06x slower                                   |
| async_tree_io           | 843 ms                                                 | 1.77 sec: 2.10x slower                                 |
| Geometric mean          | (ref)                                                  | 1.59x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 191 ms: 1.03x slower                                   |
| float          | 78.5 ms                                                | 117 ms: 1.49x slower                                   |
| nbody          | 85.7 ms                                                | 154 ms: 1.79x slower                                   |
| Geometric mean | (ref)                                                  | 1.40x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.63 ms: 1.07x faster                                  |
| regex_dna      | 220 ms                                                 | 227 ms: 1.03x slower                                   |
| regex_v8       | 25.3 ms                                                | 27.8 ms: 1.10x slower                                  |
| regex_compile  | 131 ms                                                 | 188 ms: 1.44x slower                                   |
| Geometric mean | (ref)                                                  | 1.11x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_dict          | 33.2 us                                                | 29.6 us: 1.12x faster                                  |
| pickle               | 11.6 us                                                | 10.7 us: 1.09x faster                                  |
| unpickle             | 14.9 us                                                | 14.4 us: 1.03x faster                                  |
| pickle_list          | 5.01 us                                                | 5.08 us: 1.01x slower                                  |
| unpickle_list        | 4.96 us                                                | 5.20 us: 1.05x slower                                  |
| xml_etree_parse      | 156 ms                                                 | 168 ms: 1.08x slower                                   |
| xml_etree_iterparse  | 102 ms                                                 | 115 ms: 1.13x slower                                   |
| xml_etree_generate   | 87.0 ms                                                | 99.4 ms: 1.14x slower                                  |
| json_loads           | 27.0 us                                                | 31.2 us: 1.16x slower                                  |
| xml_etree_process    | 60.4 ms                                                | 79.1 ms: 1.31x slower                                  |
| json_dumps           | 10.4 ms                                                | 14.2 ms: 1.36x slower                                  |
| tomli_loads          | 2.11 sec                                               | 3.14 sec: 1.49x slower                                 |
| unpickle_pure_python | 213 us                                                 | 331 us: 1.55x slower                                   |
| pickle_pure_python   | 300 us                                                 | 484 us: 1.61x slower                                   |
| Geometric mean       | (ref)                                                  | 1.17x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 5.93 ms: 1.18x faster                                  |
| python_startup         | 10.6 ms                                                | 14.6 ms: 1.38x slower                                  |
| Geometric mean         | (ref)                                                  | 1.08x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 50.3 ms                                                | 66.0 ms: 1.31x slower                                  |
| genshi_text     | 22.9 ms                                                | 31.8 ms: 1.39x slower                                  |
| django_template | 34.4 ms                                                | 48.2 ms: 1.40x slower                                  |
| mako            | 11.1 ms                                                | 16.3 ms: 1.47x slower                                  |
| Geometric mean  | (ref)                                                  | 1.39x slower                                           |

All benchmarks:
===============

| Benchmark                | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mypy2                    | 1.07 sec                                               | 894 ms: 1.19x faster                                   |
| python_startup_no_site   | 6.99 ms                                                | 5.93 ms: 1.18x faster                                  |
| telco                    | 8.45 ms                                                | 7.27 ms: 1.16x faster                                  |
| pickle_dict              | 33.2 us                                                | 29.6 us: 1.12x faster                                  |
| pickle                   | 11.6 us                                                | 10.7 us: 1.09x faster                                  |
| regex_effbot             | 3.88 ms                                                | 3.63 ms: 1.07x faster                                  |
| flaskblogging            | 9.11 ms                                                | 8.58 ms: 1.06x faster                                  |
| coverage                 | 83.7 ms                                                | 79.4 ms: 1.05x faster                                  |
| gc_traversal             | 3.81 ms                                                | 3.62 ms: 1.05x faster                                  |
| unpickle                 | 14.9 us                                                | 14.4 us: 1.03x faster                                  |
| asyncio_websockets       | 555 ms                                                 | 559 ms: 1.01x slower                                   |
| create_gc_cycles         | 1.61 ms                                                | 1.62 ms: 1.01x slower                                  |
| pickle_list              | 5.01 us                                                | 5.08 us: 1.01x slower                                  |
| async_generators         | 433 ms                                                 | 444 ms: 1.03x slower                                   |
| pidigits                 | 186 ms                                                 | 191 ms: 1.03x slower                                   |
| regex_dna                | 220 ms                                                 | 227 ms: 1.03x slower                                   |
| mdp                      | 2.74 sec                                               | 2.85 sec: 1.04x slower                                 |
| unpickle_list            | 4.96 us                                                | 5.20 us: 1.05x slower                                  |
| sqlite_synth             | 2.85 us                                                | 3.02 us: 1.06x slower                                  |
| xml_etree_parse          | 156 ms                                                 | 168 ms: 1.08x slower                                   |
| json                     | 5.20 ms                                                | 5.69 ms: 1.09x slower                                  |
| regex_v8                 | 25.3 ms                                                | 27.8 ms: 1.10x slower                                  |
| meteor_contest           | 108 ms                                                 | 120 ms: 1.11x slower                                   |
| xml_etree_iterparse      | 102 ms                                                 | 115 ms: 1.13x slower                                   |
| xml_etree_generate       | 87.0 ms                                                | 99.4 ms: 1.14x slower                                  |
| json_loads               | 27.0 us                                                | 31.2 us: 1.16x slower                                  |
| pathlib                  | 17.1 ms                                                | 20.5 ms: 1.20x slower                                  |
| djangocms                | 31.9 us                                                | 38.4 us: 1.21x slower                                  |
| bench_thread_pool        | 815 us                                                 | 986 us: 1.21x slower                                   |
| sympy_expand             | 462 ms                                                 | 566 ms: 1.23x slower                                   |
| gunicorn                 | 1.23 ms                                                | 1.53 ms: 1.25x slower                                  |
| aiohttp                  | 1.14 ms                                                | 1.44 ms: 1.26x slower                                  |
| scimark_fft              | 369 ms                                                 | 466 ms: 1.26x slower                                   |
| sympy_str                | 274 ms                                                 | 346 ms: 1.26x slower                                   |
| docutils                 | 2.58 sec                                               | 3.30 sec: 1.28x slower                                 |
| sqlglot_optimize         | 53.9 ms                                                | 69.2 ms: 1.28x slower                                  |
| scimark_sparse_mat_mult  | 5.03 ms                                                | 6.47 ms: 1.29x slower                                  |
| sympy_integrate          | 19.9 ms                                                | 25.8 ms: 1.30x slower                                  |
| dask                     | 338 ms                                                 | 441 ms: 1.31x slower                                   |
| xml_etree_process        | 60.4 ms                                                | 79.1 ms: 1.31x slower                                  |
| genshi_xml               | 50.3 ms                                                | 66.0 ms: 1.31x slower                                  |
| nqueens                  | 80.6 ms                                                | 106 ms: 1.31x slower                                   |
| sympy_sum                | 150 ms                                                 | 196 ms: 1.31x slower                                   |
| 2to3                     | 265 ms                                                 | 348 ms: 1.32x slower                                   |
| deepcopy_reduce          | 3.17 us                                                | 4.17 us: 1.32x slower                                  |
| pycparser                | 1.19 sec                                               | 1.58 sec: 1.32x slower                                 |
| sqlglot_normalize        | 107 ms                                                 | 143 ms: 1.33x slower                                   |
| dulwich_log              | 63.0 ms                                                | 84.3 ms: 1.34x slower                                  |
| thrift                   | 796 us                                                 | 1.07 ms: 1.35x slower                                  |
| deepcopy                 | 352 us                                                 | 479 us: 1.36x slower                                   |
| json_dumps               | 10.4 ms                                                | 14.2 ms: 1.36x slower                                  |
| pprint_safe_repr         | 744 ms                                                 | 1.02 sec: 1.37x slower                                 |
| html5lib                 | 64.5 ms                                                | 88.9 ms: 1.38x slower                                  |
| python_startup           | 10.6 ms                                                | 14.6 ms: 1.38x slower                                  |
| genshi_text              | 22.9 ms                                                | 31.8 ms: 1.39x slower                                  |
| pprint_pformat           | 1.51 sec                                               | 2.10 sec: 1.39x slower                                 |
| fannkuch                 | 381 ms                                                 | 532 ms: 1.40x slower                                   |
| django_template          | 34.4 ms                                                | 48.2 ms: 1.40x slower                                  |
| chameleon                | 6.85 ms                                                | 9.68 ms: 1.41x slower                                  |
| unpack_sequence          | 42.4 ns                                                | 60.0 ns: 1.42x slower                                  |
| asyncio_tcp_ssl          | 1.79 sec                                               | 2.57 sec: 1.44x slower                                 |
| regex_compile            | 131 ms                                                 | 188 ms: 1.44x slower                                   |
| logging_format           | 6.25 us                                                | 9.09 us: 1.45x slower                                  |
| logging_simple           | 5.66 us                                                | 8.30 us: 1.47x slower                                  |
| mako                     | 11.1 ms                                                | 16.3 ms: 1.47x slower                                  |
| spectral_norm            | 115 ms                                                 | 170 ms: 1.48x slower                                   |
| tomli_loads              | 2.11 sec                                               | 3.14 sec: 1.49x slower                                 |
| tornado_http             | 91.5 ms                                                | 136 ms: 1.49x slower                                   |
| float                    | 78.5 ms                                                | 117 ms: 1.49x slower                                   |
| scimark_lu               | 115 ms                                                 | 176 ms: 1.53x slower                                   |
| deepcopy_memo            | 38.0 us                                                | 58.5 us: 1.54x slower                                  |
| unpickle_pure_python     | 213 us                                                 | 331 us: 1.55x slower                                   |
| coroutines               | 22.5 ms                                                | 35.1 ms: 1.56x slower                                  |
| pyflate                  | 460 ms                                                 | 716 ms: 1.56x slower                                   |
| pickle_pure_python       | 300 us                                                 | 484 us: 1.61x slower                                   |
| sqlglot_transpile        | 1.57 ms                                                | 2.57 ms: 1.64x slower                                  |
| richards                 | 48.1 ms                                                | 79.3 ms: 1.65x slower                                  |
| go                       | 142 ms                                                 | 240 ms: 1.70x slower                                   |
| hexiom                   | 6.13 ms                                                | 10.4 ms: 1.70x slower                                  |
| sqlglot_parse            | 1.27 ms                                                | 2.17 ms: 1.71x slower                                  |
| richards_super           | 54.4 ms                                                | 94.7 ms: 1.74x slower                                  |
| crypto_pyaes             | 73.0 ms                                                | 128 ms: 1.75x slower                                   |
| comprehensions           | 16.4 us                                                | 28.8 us: 1.75x slower                                  |
| pylint                   | 313 ms                                                 | 551 ms: 1.76x slower                                   |
| async_tree_cpu_io_mixed  | 574 ms                                                 | 1.02 sec: 1.77x slower                                 |
| scimark_monte_carlo      | 66.3 ms                                                | 118 ms: 1.78x slower                                   |
| nbody                    | 85.7 ms                                                | 154 ms: 1.79x slower                                   |
| scimark_sor              | 122 ms                                                 | 220 ms: 1.79x slower                                   |
| logging_silent           | 102 ns                                                 | 190 ns: 1.86x slower                                   |
| asyncio_tcp              | 488 ms                                                 | 922 ms: 1.89x slower                                   |
| raytrace                 | 262 ms                                                 | 507 ms: 1.94x slower                                   |
| async_tree_memoization   | 442 ms                                                 | 870 ms: 1.97x slower                                   |
| chaos                    | 58.4 ms                                                | 115 ms: 1.98x slower                                   |
| async_tree_none          | 354 ms                                                 | 728 ms: 2.06x slower                                   |
| async_tree_io            | 843 ms                                                 | 1.77 sec: 2.10x slower                                 |
| deltablue                | 3.15 ms                                                | 7.91 ms: 2.51x slower                                  |
| generators               | 28.8 ms                                                | 80.1 ms: 2.78x slower                                  |
| typing_runtime_protocols | 159 us                                                 | 544 us: 3.42x slower                                   |
| Geometric mean           | (ref)                                                  | 1.36x slower                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.33x
- 95% likely to have a slowdown of 1.31x
- 99% likely to have a slowdown of 1.30x

# Memory
- memory change: 0.91x