# Results vs. 3.10.4

- fork: faster-cpython
- ref: exponential_backoff_
- machine: linux-x86_64
- commit hash: bdf272d
- commit date: 2024-03-19
- overall geometric mean: 1.22x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 300 ms: 1.16x faster                                                             |
| chameleon      | 9.68 ms                                                | 7.14 ms: 1.36x faster                                                            |
| docutils       | 3.30 sec                                               | 2.86 sec: 1.15x faster                                                           |
| html5lib       | 88.9 ms                                                | 69.7 ms: 1.28x faster                                                            |
| tornado_http   | 136 ms                                                 | 103 ms: 1.32x faster                                                             |
| Geometric mean | (ref)                                                  | 1.25x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 465 ms: 1.57x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 596 ms: 1.46x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 1.23 sec: 1.44x faster                                                           |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 747 ms: 1.36x faster                                                             |
| Geometric mean          | (ref)                                                  | 1.45x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 121 ms: 1.27x faster                                                             |
| float          | 117 ms                                                 | 93.9 ms: 1.25x faster                                                            |
| pidigits       | 191 ms                                                 | 191 ms: 1.00x slower                                                             |
| Geometric mean | (ref)                                                  | 1.16x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 27.8 ms                                                | 24.5 ms: 1.14x faster                                                            |
| regex_compile  | 188 ms                                                 | 175 ms: 1.08x faster                                                             |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                                             |
| regex_effbot   | 3.63 ms                                                | 3.56 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 313 us: 1.55x faster                                                             |
| json_dumps           | 14.2 ms                                                | 10.7 ms: 1.33x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.46 sec: 1.28x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 63.6 ms: 1.24x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 277 us: 1.19x faster                                                             |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 92.5 ms: 1.07x faster                                                            |
| unpickle_list        | 5.20 us                                                | 4.94 us: 1.05x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 163 ms: 1.03x faster                                                             |
| xml_etree_iterparse  | 115 ms                                                 | 113 ms: 1.02x faster                                                             |
| pickle_list          | 5.08 us                                                | 5.02 us: 1.01x faster                                                            |
| pickle               | 10.7 us                                                | 11.7 us: 1.09x slower                                                            |
| unpickle             | 14.4 us                                                | 15.8 us: 1.10x slower                                                            |
| pickle_dict          | 29.6 us                                                | 33.6 us: 1.14x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                            |
| python_startup_no_site | 5.93 ms                                                | 9.07 ms: 1.53x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 35.0 ms: 1.38x faster                                                            |
| mako            | 16.3 ms                                                | 13.2 ms: 1.24x faster                                                            |
| genshi_text     | 31.8 ms                                                | 27.7 ms: 1.15x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 62.4 ms: 1.06x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.20x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 115 us: 4.73x faster                                                             |
| generators               | 80.1 ms                                                | 29.8 ms: 2.69x faster                                                            |
| deltablue                | 7.91 ms                                                | 3.83 ms: 2.07x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 508 ms: 1.82x faster                                                             |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                                             |
| pylint                   | 551 ms                                                 | 329 ms: 1.68x faster                                                             |
| async_tree_none          | 728 ms                                                 | 465 ms: 1.57x faster                                                             |
| pickle_pure_python       | 484 us                                                 | 313 us: 1.55x faster                                                             |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                            |
| richards_super           | 94.7 ms                                                | 62.3 ms: 1.52x faster                                                            |
| chaos                    | 115 ms                                                 | 76.1 ms: 1.52x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.44 ms: 1.51x faster                                                            |
| scimark_sor              | 220 ms                                                 | 149 ms: 1.47x faster                                                             |
| raytrace                 | 507 ms                                                 | 346 ms: 1.46x faster                                                             |
| async_tree_memoization   | 870 ms                                                 | 596 ms: 1.46x faster                                                             |
| sqlglot_transpile        | 2.57 ms                                                | 1.79 ms: 1.44x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 88.8 ms: 1.44x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 1.23 sec: 1.44x faster                                                           |
| richards                 | 79.3 ms                                                | 56.1 ms: 1.41x faster                                                            |
| go                       | 240 ms                                                 | 172 ms: 1.40x faster                                                             |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                           |
| django_template          | 48.2 ms                                                | 35.0 ms: 1.38x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 747 ms: 1.36x faster                                                             |
| chameleon                | 9.68 ms                                                | 7.14 ms: 1.36x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 43.2 us: 1.35x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 87.6 ms: 1.35x faster                                                            |
| comprehensions           | 28.8 us                                                | 21.3 us: 1.35x faster                                                            |
| json_dumps               | 14.2 ms                                                | 10.7 ms: 1.33x faster                                                            |
| tornado_http             | 136 ms                                                 | 103 ms: 1.32x faster                                                             |
| deepcopy_reduce          | 4.17 us                                                | 3.20 us: 1.30x faster                                                            |
| deepcopy                 | 479 us                                                 | 368 us: 1.30x faster                                                             |
| logging_simple           | 8.30 us                                                | 6.38 us: 1.30x faster                                                            |
| thrift                   | 1.07 ms                                                | 825 us: 1.30x faster                                                             |
| logging_format           | 9.09 us                                                | 7.08 us: 1.28x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 2.46 sec: 1.28x faster                                                           |
| html5lib                 | 88.9 ms                                                | 69.7 ms: 1.28x faster                                                            |
| nbody                    | 154 ms                                                 | 121 ms: 1.27x faster                                                             |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                             |
| float                    | 117 ms                                                 | 93.9 ms: 1.25x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 63.6 ms: 1.24x faster                                                            |
| mako                     | 16.3 ms                                                | 13.2 ms: 1.24x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.30 sec: 1.22x faster                                                           |
| pyflate                  | 716 ms                                                 | 590 ms: 1.21x faster                                                             |
| sympy_integrate          | 25.8 ms                                                | 21.5 ms: 1.20x faster                                                            |
| spectral_norm            | 170 ms                                                 | 142 ms: 1.20x faster                                                             |
| djangocms                | 38.4 us                                                | 32.2 us: 1.19x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 277 us: 1.19x faster                                                             |
| aiohttp                  | 1.44 ms                                                | 1.21 ms: 1.19x faster                                                            |
| gunicorn                 | 1.53 ms                                                | 1.30 ms: 1.17x faster                                                            |
| sympy_sum                | 196 ms                                                 | 168 ms: 1.17x faster                                                             |
| dask                     | 441 ms                                                 | 377 ms: 1.17x faster                                                             |
| hexiom                   | 10.4 ms                                                | 8.92 ms: 1.17x faster                                                            |
| 2to3                     | 348 ms                                                 | 300 ms: 1.16x faster                                                             |
| docutils                 | 3.30 sec                                               | 2.86 sec: 1.15x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 73.4 ms: 1.15x faster                                                            |
| genshi_text              | 31.8 ms                                                | 27.7 ms: 1.15x faster                                                            |
| pprint_safe_repr         | 1.02 sec                                               | 887 ms: 1.15x faster                                                             |
| pprint_pformat           | 2.10 sec                                               | 1.85 sec: 1.14x faster                                                           |
| bench_thread_pool        | 986 us                                                 | 867 us: 1.14x faster                                                             |
| sympy_str                | 346 ms                                                 | 304 ms: 1.14x faster                                                             |
| regex_v8                 | 27.8 ms                                                | 24.5 ms: 1.14x faster                                                            |
| sqlglot_optimize         | 69.2 ms                                                | 61.2 ms: 1.13x faster                                                            |
| fannkuch                 | 532 ms                                                 | 481 ms: 1.11x faster                                                             |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                                            |
| sympy_expand             | 566 ms                                                 | 516 ms: 1.10x faster                                                             |
| scimark_lu               | 176 ms                                                 | 162 ms: 1.09x faster                                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.99 ms: 1.08x faster                                                            |
| regex_compile            | 188 ms                                                 | 175 ms: 1.08x faster                                                             |
| json                     | 5.69 ms                                                | 5.29 ms: 1.08x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 92.5 ms: 1.07x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 62.4 ms: 1.06x faster                                                            |
| nqueens                  | 106 ms                                                 | 100 ms: 1.06x faster                                                             |
| mdp                      | 2.85 sec                                               | 2.70 sec: 1.06x faster                                                           |
| unpickle_list            | 5.20 us                                                | 4.94 us: 1.05x faster                                                            |
| create_gc_cycles         | 1.62 ms                                                | 1.54 ms: 1.05x faster                                                            |
| scimark_fft              | 466 ms                                                 | 444 ms: 1.05x faster                                                             |
| pathlib                  | 20.5 ms                                                | 19.7 ms: 1.04x faster                                                            |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                                             |
| xml_etree_parse          | 168 ms                                                 | 163 ms: 1.03x faster                                                             |
| sqlite_synth             | 3.02 us                                                | 2.95 us: 1.03x faster                                                            |
| regex_effbot             | 3.63 ms                                                | 3.56 ms: 1.02x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 113 ms: 1.02x faster                                                             |
| unpack_sequence          | 60.0 ns                                                | 58.9 ns: 1.02x faster                                                            |
| pickle_list              | 5.08 us                                                | 5.02 us: 1.01x faster                                                            |
| meteor_contest           | 120 ms                                                 | 119 ms: 1.01x faster                                                             |
| pidigits                 | 191 ms                                                 | 191 ms: 1.00x slower                                                             |
| asyncio_websockets       | 559 ms                                                 | 564 ms: 1.01x slower                                                             |
| async_generators         | 444 ms                                                 | 476 ms: 1.07x slower                                                             |
| gc_traversal             | 3.62 ms                                                | 3.91 ms: 1.08x slower                                                            |
| pickle                   | 10.7 us                                                | 11.7 us: 1.09x slower                                                            |
| unpickle                 | 14.4 us                                                | 15.8 us: 1.10x slower                                                            |
| pickle_dict              | 29.6 us                                                | 33.6 us: 1.14x slower                                                            |
| telco                    | 7.27 ms                                                | 9.02 ms: 1.24x slower                                                            |
| coverage                 | 79.4 ms                                                | 99.2 ms: 1.25x slower                                                            |
| python_startup_no_site   | 5.93 ms                                                | 9.07 ms: 1.53x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.22x faster                                                                     |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240319-3.13.0a5+-bdf272d-PYTHON_UOPS/bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.14x


# Memory

- memory change: 1.08x