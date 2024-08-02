# Results vs. 3.10.4

- fork: python
- ref: edb6883ef3f7a8ef0c83
- machine: linux-x86_64
- commit hash: edb6883
- commit date: 2024-06-01
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 271 ms: 1.28x faster                                                   |
| chameleon      | 9.68 ms                                                | 6.89 ms: 1.41x faster                                                  |
| docutils       | 3.30 sec                                               | 2.84 sec: 1.16x faster                                                 |
| html5lib       | 88.9 ms                                                | 68.3 ms: 1.30x faster                                                  |
| tornado_http   | 136 ms                                                 | 93.8 ms: 1.45x faster                                                  |
| Geometric mean | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 371 ms: 1.96x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 456 ms: 1.91x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 939 ms: 1.88x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 608 ms: 1.67x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.85x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 90.1 ms: 1.70x faster                                                  |
| float          | 117 ms                                                 | 78.7 ms: 1.49x faster                                                  |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.40x faster                                                   |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                  |
| regex_dna      | 227 ms                                                 | 226 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 301 us: 1.61x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 2.17 sec: 1.44x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 60.4 ms: 1.31x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 86.4 ms: 1.15x faster                                                  |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 108 ms: 1.07x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 161 ms: 1.04x faster                                                   |
| unpickle             | 14.4 us                                                | 14.6 us: 1.02x slower                                                  |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                                  |
| pickle_dict          | 29.6 us                                                | 33.5 us: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                           |

Benchmark hidden because not significant (2): pickle_list, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.7 ms: 1.36x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.8 ms: 1.52x faster                                                  |
| django_template | 48.2 ms                                                | 34.5 ms: 1.40x faster                                                  |
| genshi_text     | 31.8 ms                                                | 23.0 ms: 1.38x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 50.5 ms: 1.31x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.31x faster                                                   |
| generators               | 80.1 ms                                                | 29.3 ms: 2.74x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.28 ms: 2.41x faster                                                  |
| async_tree_none          | 728 ms                                                 | 371 ms: 1.96x faster                                                   |
| chaos                    | 115 ms                                                 | 60.2 ms: 1.92x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 456 ms: 1.91x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 939 ms: 1.88x faster                                                   |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                   |
| logging_silent           | 190 ns                                                 | 102 ns: 1.85x faster                                                   |
| asyncio_tcp              | 922 ms                                                 | 508 ms: 1.81x faster                                                   |
| pylint                   | 551 ms                                                 | 315 ms: 1.75x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 67.8 ms: 1.74x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 74.4 ms: 1.72x faster                                                  |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.72x faster                                                   |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                  |
| nbody                    | 154 ms                                                 | 90.1 ms: 1.70x faster                                                  |
| go                       | 240 ms                                                 | 143 ms: 1.68x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 608 ms: 1.67x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.25 ms: 1.66x faster                                                  |
| richards_super           | 94.7 ms                                                | 57.2 ms: 1.66x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.65x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 301 us: 1.61x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                  |
| richards                 | 79.3 ms                                                | 50.7 ms: 1.56x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                  |
| pyflate                  | 716 ms                                                 | 468 ms: 1.53x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 38.3 us: 1.53x faster                                                  |
| mako                     | 16.3 ms                                                | 10.8 ms: 1.52x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                   |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                   |
| float                    | 117 ms                                                 | 78.7 ms: 1.49x faster                                                  |
| tornado_http             | 136 ms                                                 | 93.8 ms: 1.45x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.17 sec: 1.44x faster                                                 |
| spectral_norm            | 170 ms                                                 | 118 ms: 1.44x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.77 us: 1.44x faster                                                  |
| logging_format           | 9.09 us                                                | 6.38 us: 1.43x faster                                                  |
| chameleon                | 9.68 ms                                                | 6.89 ms: 1.41x faster                                                  |
| regex_compile            | 188 ms                                                 | 135 ms: 1.40x faster                                                   |
| django_template          | 48.2 ms                                                | 34.5 ms: 1.40x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.40x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.84 sec: 1.39x faster                                                 |
| genshi_text              | 31.8 ms                                                | 23.0 ms: 1.38x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 741 ms: 1.37x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                 |
| python_startup           | 14.6 ms                                                | 10.7 ms: 1.36x faster                                                  |
| fannkuch                 | 532 ms                                                 | 395 ms: 1.35x faster                                                   |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                  |
| deepcopy                 | 479 us                                                 | 358 us: 1.34x faster                                                   |
| nqueens                  | 106 ms                                                 | 79.5 ms: 1.33x faster                                                  |
| thrift                   | 1.07 ms                                                | 816 us: 1.31x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 50.5 ms: 1.31x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 60.4 ms: 1.31x faster                                                  |
| html5lib                 | 88.9 ms                                                | 68.3 ms: 1.30x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.29x faster                                                   |
| 2to3                     | 348 ms                                                 | 271 ms: 1.28x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 3.27 us: 1.27x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 66.4 ms: 1.27x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 20.4 ms: 1.27x faster                                                  |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.26x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 55.1 ms: 1.26x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.19 ms: 1.25x faster                                                  |
| scimark_fft              | 466 ms                                                 | 375 ms: 1.24x faster                                                   |
| sympy_str                | 346 ms                                                 | 281 ms: 1.23x faster                                                   |
| djangocms                | 38.4 us                                                | 31.4 us: 1.23x faster                                                  |
| aiohttp                  | 1.44 ms                                                | 1.18 ms: 1.22x faster                                                  |
| mypy2                    | 894 ms                                                 | 734 ms: 1.22x faster                                                   |
| sympy_expand             | 566 ms                                                 | 470 ms: 1.20x faster                                                   |
| gunicorn                 | 1.53 ms                                                | 1.28 ms: 1.20x faster                                                  |
| dask                     | 441 ms                                                 | 368 ms: 1.20x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 834 us: 1.18x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.84 sec: 1.16x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 86.4 ms: 1.15x faster                                                  |
| pathlib                  | 20.5 ms                                                | 17.8 ms: 1.15x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                                 |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                  |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                                  |
| json                     | 5.69 ms                                                | 5.29 ms: 1.08x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 108 ms: 1.07x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 161 ms: 1.04x faster                                                   |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                   |
| async_generators         | 444 ms                                                 | 440 ms: 1.01x faster                                                   |
| bench_mp_pool            | 24.0 ms                                                | 23.9 ms: 1.00x faster                                                  |
| regex_dna                | 227 ms                                                 | 226 ms: 1.00x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 566 ms: 1.01x slower                                                   |
| unpickle                 | 14.4 us                                                | 14.6 us: 1.02x slower                                                  |
| flaskblogging            | 8.58 ms                                                | 8.93 ms: 1.04x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 3.85 ms: 1.06x slower                                                  |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.80 ms: 1.11x slower                                                  |
| pickle_dict              | 29.6 us                                                | 33.5 us: 1.13x slower                                                  |
| coverage                 | 79.4 ms                                                | 92.6 ms: 1.17x slower                                                  |
| telco                    | 7.27 ms                                                | 8.62 ms: 1.19x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.19x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                           |

Benchmark hidden because not significant (4): sqlite_synth, pickle_list, unpickle_list, regex_effbot
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240601-3.13.0b1+-edb6883/bm-20240601-linux-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.12x