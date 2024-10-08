# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 276 ms: 1.26x faster                                       |
| chameleon      | 9.68 ms                                                | 6.75 ms: 1.43x faster                                      |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                     |
| tornado_http   | 136 ms                                                 | 96.9 ms: 1.41x faster                                      |
| Geometric mean | (ref)                                                  | 1.34x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 439 ms: 1.66x faster                                       |
| async_tree_memoization  | 870 ms                                                 | 568 ms: 1.53x faster                                       |
| async_tree_io           | 1.77 sec                                               | 1.18 sec: 1.50x faster                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 716 ms: 1.42x faster                                       |
| Geometric mean          | (ref)                                                  | 1.53x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 154 ms                                                 | 102 ms: 1.50x faster                                       |
| float          | 117 ms                                                 | 86.1 ms: 1.36x faster                                      |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                  | 1.27x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 141 ms: 1.34x faster                                       |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                      |
| regex_effbot   | 3.63 ms                                                | 3.57 ms: 1.02x faster                                      |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 296 us: 1.64x faster                                       |
| unpickle_pure_python | 331 us                                                 | 228 us: 1.45x faster                                       |
| tomli_loads          | 3.14 sec                                               | 2.19 sec: 1.43x faster                                     |
| xml_etree_process    | 79.1 ms                                                | 57.9 ms: 1.37x faster                                      |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.34x faster                                      |
| xml_etree_generate   | 99.4 ms                                                | 85.7 ms: 1.16x faster                                      |
| json_loads           | 31.2 us                                                | 27.3 us: 1.14x faster                                      |
| xml_etree_iterparse  | 115 ms                                                 | 108 ms: 1.07x faster                                       |
| xml_etree_parse      | 168 ms                                                 | 157 ms: 1.07x faster                                       |
| unpickle_list        | 5.20 us                                                | 5.11 us: 1.02x faster                                      |
| unpickle             | 14.4 us                                                | 15.1 us: 1.05x slower                                      |
| pickle               | 10.7 us                                                | 11.4 us: 1.07x slower                                      |
| pickle_dict          | 29.6 us                                                | 33.6 us: 1.13x slower                                      |
| Geometric mean       | (ref)                                                  | 1.16x faster                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.3 ms: 1.42x faster                                      |
| python_startup_no_site | 5.93 ms                                                | 8.95 ms: 1.51x slower                                      |
| Geometric mean         | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 16.3 ms                                                | 12.4 ms: 1.32x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 110 us: 4.96x faster                                       |
| generators               | 80.1 ms                                                | 29.1 ms: 2.75x faster                                      |
| deltablue                | 7.91 ms                                                | 3.32 ms: 2.38x faster                                      |
| logging_silent           | 190 ns                                                 | 101 ns: 1.87x faster                                       |
| richards_super           | 94.7 ms                                                | 50.8 ms: 1.86x faster                                      |
| asyncio_tcp              | 922 ms                                                 | 497 ms: 1.86x faster                                       |
| raytrace                 | 507 ms                                                 | 280 ms: 1.81x faster                                       |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.81x faster                                       |
| richards                 | 79.3 ms                                                | 44.8 ms: 1.77x faster                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                      |
| chaos                    | 115 ms                                                 | 69.1 ms: 1.67x faster                                      |
| async_tree_none          | 728 ms                                                 | 439 ms: 1.66x faster                                       |
| go                       | 240 ms                                                 | 146 ms: 1.64x faster                                       |
| pickle_pure_python       | 484 us                                                 | 296 us: 1.64x faster                                       |
| crypto_pyaes             | 128 ms                                                 | 79.1 ms: 1.62x faster                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                      |
| scimark_monte_carlo      | 118 ms                                                 | 74.0 ms: 1.60x faster                                      |
| comprehensions           | 28.8 us                                                | 18.2 us: 1.58x faster                                      |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.57x faster                                       |
| deepcopy_memo            | 58.5 us                                                | 38.1 us: 1.53x faster                                      |
| async_tree_memoization   | 870 ms                                                 | 568 ms: 1.53x faster                                       |
| async_tree_io            | 1.77 sec                                               | 1.18 sec: 1.50x faster                                     |
| nbody                    | 154 ms                                                 | 102 ms: 1.50x faster                                       |
| coroutines               | 35.1 ms                                                | 23.7 ms: 1.48x faster                                      |
| unpickle_pure_python     | 331 us                                                 | 228 us: 1.45x faster                                       |
| logging_simple           | 8.30 us                                                | 5.74 us: 1.45x faster                                      |
| logging_format           | 9.09 us                                                | 6.30 us: 1.44x faster                                      |
| tomli_loads              | 3.14 sec                                               | 2.19 sec: 1.43x faster                                     |
| chameleon                | 9.68 ms                                                | 6.75 ms: 1.43x faster                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 716 ms: 1.42x faster                                       |
| python_startup           | 14.6 ms                                                | 10.3 ms: 1.42x faster                                      |
| tornado_http             | 136 ms                                                 | 96.9 ms: 1.41x faster                                      |
| pyflate                  | 716 ms                                                 | 514 ms: 1.39x faster                                       |
| deepcopy                 | 479 us                                                 | 345 us: 1.39x faster                                       |
| deepcopy_reduce          | 4.17 us                                                | 3.04 us: 1.37x faster                                      |
| xml_etree_process        | 79.1 ms                                                | 57.9 ms: 1.37x faster                                      |
| float                    | 117 ms                                                 | 86.1 ms: 1.36x faster                                      |
| hexiom                   | 10.4 ms                                                | 7.72 ms: 1.35x faster                                      |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.34x faster                                      |
| regex_compile            | 188 ms                                                 | 141 ms: 1.34x faster                                       |
| unpack_sequence          | 60.0 ns                                                | 44.9 ns: 1.34x faster                                      |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                       |
| mako                     | 16.3 ms                                                | 12.4 ms: 1.32x faster                                      |
| pprint_safe_repr         | 1.02 sec                                               | 775 ms: 1.31x faster                                       |
| pprint_pformat           | 2.10 sec                                               | 1.61 sec: 1.30x faster                                     |
| pycparser                | 1.58 sec                                               | 1.22 sec: 1.29x faster                                     |
| spectral_norm            | 170 ms                                                 | 132 ms: 1.29x faster                                       |
| scimark_fft              | 466 ms                                                 | 366 ms: 1.27x faster                                       |
| sympy_integrate          | 25.8 ms                                                | 20.3 ms: 1.27x faster                                      |
| 2to3                     | 348 ms                                                 | 276 ms: 1.26x faster                                       |
| fannkuch                 | 532 ms                                                 | 422 ms: 1.26x faster                                       |
| sqlglot_optimize         | 69.2 ms                                                | 55.1 ms: 1.26x faster                                      |
| sympy_sum                | 196 ms                                                 | 157 ms: 1.25x faster                                       |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                     |
| dulwich_log              | 84.3 ms                                                | 68.2 ms: 1.24x faster                                      |
| sympy_str                | 346 ms                                                 | 281 ms: 1.23x faster                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.35 ms: 1.21x faster                                      |
| bench_thread_pool        | 986 us                                                 | 836 us: 1.18x faster                                       |
| sympy_expand             | 566 ms                                                 | 480 ms: 1.18x faster                                       |
| nqueens                  | 106 ms                                                 | 89.8 ms: 1.18x faster                                      |
| xml_etree_generate       | 99.4 ms                                                | 85.7 ms: 1.16x faster                                      |
| json_loads               | 31.2 us                                                | 27.3 us: 1.14x faster                                      |
| pathlib                  | 20.5 ms                                                | 18.1 ms: 1.13x faster                                      |
| json                     | 5.69 ms                                                | 5.12 ms: 1.11x faster                                      |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                      |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.49 ms: 1.08x faster                                      |
| sqlite_synth             | 3.02 us                                                | 2.82 us: 1.07x faster                                      |
| xml_etree_iterparse      | 115 ms                                                 | 108 ms: 1.07x faster                                       |
| xml_etree_parse          | 168 ms                                                 | 157 ms: 1.07x faster                                       |
| mdp                      | 2.85 sec                                               | 2.78 sec: 1.02x faster                                     |
| regex_effbot             | 3.63 ms                                                | 3.57 ms: 1.02x faster                                      |
| unpickle_list            | 5.20 us                                                | 5.11 us: 1.02x faster                                      |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                       |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                       |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                       |
| gc_traversal             | 3.62 ms                                                | 3.76 ms: 1.04x slower                                      |
| async_generators         | 444 ms                                                 | 463 ms: 1.04x slower                                       |
| unpickle                 | 14.4 us                                                | 15.1 us: 1.05x slower                                      |
| pickle                   | 10.7 us                                                | 11.4 us: 1.07x slower                                      |
| pickle_dict              | 29.6 us                                                | 33.6 us: 1.13x slower                                      |
| telco                    | 7.27 ms                                                | 8.40 ms: 1.16x slower                                      |
| dask                     | 441 ms                                                 | 527 ms: 1.20x slower                                       |
| coverage                 | 79.4 ms                                                | 95.8 ms: 1.21x slower                                      |
| python_startup_no_site   | 5.93 ms                                                | 8.95 ms: 1.51x slower                                      |
| Geometric mean           | (ref)                                                  | 1.31x faster                                               |

Benchmark hidden because not significant (3): mypy2, pickle_list, bench_mp_pool
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift
Ignored benchmarks (4) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.24x


# Memory

- memory change: 1.10x