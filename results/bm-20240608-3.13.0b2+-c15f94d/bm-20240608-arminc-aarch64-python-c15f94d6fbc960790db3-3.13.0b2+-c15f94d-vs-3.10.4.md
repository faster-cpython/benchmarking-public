# Results vs. 3.10.4

- fork: python
- ref: c15f94d6fbc960790db3
- machine: linux-aarch64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 306 ms: 1.24x faster                                                     |
| chameleon      | 10.8 ms                                                               | 8.94 ms: 1.21x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                   |
| html5lib       | 86.5 ms                                                               | 66.1 ms: 1.31x faster                                                    |
| tornado_http   | 178 ms                                                                | 126 ms: 1.42x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 490 ms: 1.94x faster                                                     |
| async_tree_io           | 2.28 sec                                                              | 1.21 sec: 1.89x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 645 ms: 1.76x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 792 ms: 1.61x faster                                                     |
| Geometric mean          | (ref)                                                                 | 1.79x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 113 ms: 1.47x faster                                                     |
| float          | 135 ms                                                                | 91.9 ms: 1.47x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 129 ms: 1.37x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 30.5 ms: 1.05x faster                                                    |
| regex_dna      | 257 ms                                                                | 249 ms: 1.03x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 253 us: 1.44x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 368 us: 1.44x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.23x faster                                                    |
| xml_etree_process    | 99.5 ms                                                               | 81.7 ms: 1.22x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 194 ms: 1.09x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 6.47 us: 1.08x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 117 ms: 1.05x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.05x faster                                                     |
| pickle_list          | 5.24 us                                                               | 5.35 us: 1.02x slower                                                    |
| json_loads           | 30.9 us                                                               | 32.0 us: 1.03x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 38.0 us: 1.08x slower                                                    |
| pickle               | 12.5 us                                                               | 13.6 us: 1.09x slower                                                    |
| unpickle             | 17.5 us                                                               | 19.6 us: 1.12x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 8.71 ms: 1.27x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.5 ms: 1.41x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.6 ms: 1.27x faster                                                    |
| django_template | 53.3 ms                                                               | 42.7 ms: 1.25x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 62.1 ms: 1.13x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.26x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 192 us: 3.44x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.85 ms: 2.32x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.22 ms: 2.01x faster                                                    |
| async_tree_none          | 950 ms                                                                | 490 ms: 1.94x faster                                                     |
| raytrace                 | 573 ms                                                                | 299 ms: 1.92x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 1.21 sec: 1.89x faster                                                   |
| generators               | 68.1 ms                                                               | 37.4 ms: 1.82x faster                                                    |
| chaos                    | 121 ms                                                                | 67.8 ms: 1.79x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 645 ms: 1.76x faster                                                     |
| richards_super           | 107 ms                                                                | 62.2 ms: 1.72x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.40 ms: 1.71x faster                                                    |
| logging_silent           | 222 ns                                                                | 132 ns: 1.68x faster                                                     |
| richards                 | 91.7 ms                                                               | 55.4 ms: 1.65x faster                                                    |
| comprehensions           | 33.1 us                                                               | 20.1 us: 1.65x faster                                                    |
| go                       | 264 ms                                                                | 161 ms: 1.64x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 81.6 ms: 1.64x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.75 ms: 1.62x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 586 ms: 1.61x faster                                                     |
| scimark_lu               | 227 ms                                                                | 141 ms: 1.61x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 792 ms: 1.61x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 81.6 ms: 1.57x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.06 ms: 1.55x faster                                                    |
| scimark_sor              | 246 ms                                                                | 161 ms: 1.53x faster                                                     |
| nbody                    | 166 ms                                                                | 113 ms: 1.47x faster                                                     |
| float                    | 135 ms                                                                | 91.9 ms: 1.47x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.24 sec: 1.47x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 253 us: 1.44x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 368 us: 1.44x faster                                                     |
| pyflate                  | 795 ms                                                                | 554 ms: 1.44x faster                                                     |
| pylint                   | 485 ms                                                                | 338 ms: 1.44x faster                                                     |
| tornado_http             | 178 ms                                                                | 126 ms: 1.42x faster                                                     |
| mako                     | 18.9 ms                                                               | 13.5 ms: 1.41x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.21 sec: 1.39x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.06 us: 1.39x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.75 us: 1.37x faster                                                    |
| regex_compile            | 177 ms                                                                | 129 ms: 1.37x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                                   |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.32x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 66.1 ms: 1.31x faster                                                    |
| thrift                   | 1.26 ms                                                               | 967 us: 1.30x faster                                                     |
| sympy_sum                | 184 ms                                                                | 143 ms: 1.28x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 27.6 ms: 1.27x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.2 ms: 1.27x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 21.0 ms: 1.26x faster                                                    |
| django_template          | 53.3 ms                                                               | 42.7 ms: 1.25x faster                                                    |
| 2to3                     | 381 ms                                                                | 306 ms: 1.24x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.28 ms: 1.24x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.23x faster                                                    |
| mypy2                    | 936 ms                                                                | 759 ms: 1.23x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 50.1 us: 1.23x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 127 ms: 1.23x faster                                                     |
| sympy_str                | 329 ms                                                                | 268 ms: 1.23x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 1.93 sec: 1.23x faster                                                   |
| fannkuch                 | 546 ms                                                                | 447 ms: 1.22x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 81.7 ms: 1.22x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 943 ms: 1.22x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 62.0 ms: 1.22x faster                                                    |
| chameleon                | 10.8 ms                                                               | 8.94 ms: 1.21x faster                                                    |
| dask                     | 450 ms                                                                | 373 ms: 1.21x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 61.0 ms: 1.20x faster                                                    |
| nqueens                  | 117 ms                                                                | 99.7 ms: 1.18x faster                                                    |
| sympy_expand             | 543 ms                                                                | 462 ms: 1.18x faster                                                     |
| gunicorn                 | 1.45 ms                                                               | 1.24 ms: 1.17x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.6 ms: 1.16x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.00 us: 1.15x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.66 ms: 1.14x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                   |
| deepcopy                 | 511 us                                                                | 448 us: 1.14x faster                                                     |
| aiohttp                  | 1.39 ms                                                               | 1.22 ms: 1.14x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 62.1 ms: 1.13x faster                                                    |
| scimark_fft              | 500 ms                                                                | 446 ms: 1.12x faster                                                     |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.31 sec: 1.12x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 194 ms: 1.09x faster                                                     |
| unpickle_list            | 6.99 us                                                               | 6.47 us: 1.08x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 117 ms: 1.05x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.91 us: 1.05x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.5 ms: 1.05x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.05x faster                                                     |
| json                     | 5.88 ms                                                               | 5.64 ms: 1.04x faster                                                    |
| regex_dna                | 257 ms                                                                | 249 ms: 1.03x faster                                                     |
| pickle_list              | 5.24 us                                                               | 5.35 us: 1.02x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.0 us: 1.03x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.34 ms: 1.03x slower                                                    |
| async_generators         | 452 ms                                                                | 486 ms: 1.07x slower                                                     |
| pickle_dict              | 35.1 us                                                               | 38.0 us: 1.08x slower                                                    |
| pickle                   | 12.5 us                                                               | 13.6 us: 1.09x slower                                                    |
| unpickle                 | 17.5 us                                                               | 19.6 us: 1.12x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.86 ms: 1.16x slower                                                    |
| coverage                 | 83.6 ms                                                               | 98.0 ms: 1.17x slower                                                    |
| python_startup           | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.04 ms: 1.21x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.71 ms: 1.27x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.28x faster                                                             |

Benchmark hidden because not significant (3): pidigits, asyncio_websockets, flaskblogging
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-arminc-aarch64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.14x