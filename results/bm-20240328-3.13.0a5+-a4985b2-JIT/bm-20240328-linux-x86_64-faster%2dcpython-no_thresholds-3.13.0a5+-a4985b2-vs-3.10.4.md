# Results vs. 3.10.4

- fork: faster-cpython
- ref: no_thresholds
- machine: linux-x86_64
- commit hash: a4985b2
- commit date: 2024-03-28
- overall geometric mean: 1.28x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 281 ms: 1.24x faster                                                      |
| chameleon      | 9.68 ms                                                | 7.06 ms: 1.37x faster                                                     |
| docutils       | 3.30 sec                                               | 2.94 sec: 1.12x faster                                                    |
| html5lib       | 88.9 ms                                                | 66.2 ms: 1.34x faster                                                     |
| tornado_http   | 136 ms                                                 | 97.6 ms: 1.40x faster                                                     |
| Geometric mean | (ref)                                                  | 1.29x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 355 ms: 2.05x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 455 ms: 1.91x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 938 ms: 1.89x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 612 ms: 1.66x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.87x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 90.6 ms: 1.69x faster                                                     |
| float          | 117 ms                                                 | 79.5 ms: 1.47x faster                                                     |
| pidigits       | 191 ms                                                 | 190 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.36x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 151 ms: 1.25x faster                                                      |
| regex_v8       | 27.8 ms                                                | 26.2 ms: 1.06x faster                                                     |
| regex_dna      | 227 ms                                                 | 231 ms: 1.02x slower                                                      |
| regex_effbot   | 3.63 ms                                                | 3.81 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 306 us: 1.58x faster                                                      |
| tomli_loads          | 3.14 sec                                               | 2.15 sec: 1.46x faster                                                    |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 62.8 ms: 1.26x faster                                                     |
| unpickle_pure_python | 331 us                                                 | 267 us: 1.24x faster                                                      |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 91.9 ms: 1.08x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 162 ms: 1.04x faster                                                      |
| unpickle_list        | 5.20 us                                                | 5.04 us: 1.03x faster                                                     |
| pickle_list          | 5.08 us                                                | 4.94 us: 1.03x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 113 ms: 1.02x faster                                                      |
| pickle               | 10.7 us                                                | 11.9 us: 1.12x slower                                                     |
| pickle_dict          | 29.6 us                                                | 34.0 us: 1.15x slower                                                     |
| unpickle             | 14.4 us                                                | 16.7 us: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.2 ms: 1.31x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 9.62 ms: 1.62x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.7 ms: 1.53x faster                                                     |
| django_template | 48.2 ms                                                | 37.0 ms: 1.30x faster                                                     |
| genshi_text     | 31.8 ms                                                | 25.9 ms: 1.23x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 57.0 ms: 1.16x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.30x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 116 us: 4.71x faster                                                      |
| generators               | 80.1 ms                                                | 29.8 ms: 2.69x faster                                                     |
| async_tree_none          | 728 ms                                                 | 355 ms: 2.05x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 455 ms: 1.91x faster                                                      |
| deltablue                | 7.91 ms                                                | 4.14 ms: 1.91x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 938 ms: 1.89x faster                                                      |
| logging_silent           | 190 ns                                                 | 104 ns: 1.83x faster                                                      |
| asyncio_tcp              | 922 ms                                                 | 512 ms: 1.80x faster                                                      |
| chaos                    | 115 ms                                                 | 65.3 ms: 1.77x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 74.9 ms: 1.71x faster                                                     |
| nbody                    | 154 ms                                                 | 90.6 ms: 1.69x faster                                                     |
| raytrace                 | 507 ms                                                 | 302 ms: 1.68x faster                                                      |
| scimark_sor              | 220 ms                                                 | 132 ms: 1.66x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 612 ms: 1.66x faster                                                      |
| pylint                   | 551 ms                                                 | 341 ms: 1.62x faster                                                      |
| richards_super           | 94.7 ms                                                | 58.6 ms: 1.62x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.36 ms: 1.59x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 306 us: 1.58x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 74.8 ms: 1.58x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.53x faster                                                     |
| mako                     | 16.3 ms                                                | 10.7 ms: 1.53x faster                                                     |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                     |
| richards                 | 79.3 ms                                                | 52.9 ms: 1.50x faster                                                     |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.49x faster                                                      |
| comprehensions           | 28.8 us                                                | 19.5 us: 1.48x faster                                                     |
| float                    | 117 ms                                                 | 79.5 ms: 1.47x faster                                                     |
| pyflate                  | 716 ms                                                 | 488 ms: 1.47x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 2.15 sec: 1.46x faster                                                    |
| tornado_http             | 136 ms                                                 | 97.6 ms: 1.40x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                    |
| go                       | 240 ms                                                 | 173 ms: 1.39x faster                                                      |
| logging_simple           | 8.30 us                                                | 6.01 us: 1.38x faster                                                     |
| chameleon                | 9.68 ms                                                | 7.06 ms: 1.37x faster                                                     |
| scimark_fft              | 466 ms                                                 | 343 ms: 1.36x faster                                                      |
| logging_format           | 9.09 us                                                | 6.73 us: 1.35x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.79 ms: 1.35x faster                                                     |
| html5lib                 | 88.9 ms                                                | 66.2 ms: 1.34x faster                                                     |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                     |
| scimark_lu               | 176 ms                                                 | 132 ms: 1.33x faster                                                      |
| fannkuch                 | 532 ms                                                 | 400 ms: 1.33x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.58 sec: 1.33x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 772 ms: 1.32x faster                                                      |
| thrift                   | 1.07 ms                                                | 819 us: 1.31x faster                                                      |
| python_startup           | 14.6 ms                                                | 11.2 ms: 1.31x faster                                                     |
| django_template          | 48.2 ms                                                | 37.0 ms: 1.30x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 44.9 us: 1.30x faster                                                     |
| hexiom                   | 10.4 ms                                                | 8.09 ms: 1.28x faster                                                     |
| deepcopy                 | 479 us                                                 | 375 us: 1.28x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 3.28 us: 1.27x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 62.8 ms: 1.26x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.26 sec: 1.25x faster                                                    |
| regex_compile            | 188 ms                                                 | 151 ms: 1.25x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 115 ms: 1.25x faster                                                      |
| 2to3                     | 348 ms                                                 | 281 ms: 1.24x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 267 us: 1.24x faster                                                      |
| genshi_text              | 31.8 ms                                                | 25.9 ms: 1.23x faster                                                     |
| aiohttp                  | 1.44 ms                                                | 1.21 ms: 1.19x faster                                                     |
| djangocms                | 38.4 us                                                | 32.4 us: 1.19x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 71.5 ms: 1.18x faster                                                     |
| gunicorn                 | 1.53 ms                                                | 1.30 ms: 1.17x faster                                                     |
| sympy_str                | 346 ms                                                 | 295 ms: 1.17x faster                                                      |
| dask                     | 441 ms                                                 | 376 ms: 1.17x faster                                                      |
| sympy_sum                | 196 ms                                                 | 168 ms: 1.17x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 59.4 ms: 1.16x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 57.0 ms: 1.16x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 22.4 ms: 1.15x faster                                                     |
| sympy_expand             | 566 ms                                                 | 498 ms: 1.14x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.94 sec: 1.12x faster                                                    |
| mypy2                    | 894 ms                                                 | 798 ms: 1.12x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 890 us: 1.11x faster                                                      |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 91.9 ms: 1.08x faster                                                     |
| meteor_contest           | 120 ms                                                 | 112 ms: 1.07x faster                                                      |
| pathlib                  | 20.5 ms                                                | 19.2 ms: 1.06x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 26.2 ms: 1.06x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.06x faster                                                     |
| json                     | 5.69 ms                                                | 5.43 ms: 1.05x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 162 ms: 1.04x faster                                                      |
| unpickle_list            | 5.20 us                                                | 5.04 us: 1.03x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.77 sec: 1.03x faster                                                    |
| pickle_list              | 5.08 us                                                | 4.94 us: 1.03x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 113 ms: 1.02x faster                                                      |
| nqueens                  | 106 ms                                                 | 104 ms: 1.02x faster                                                      |
| pidigits                 | 191 ms                                                 | 190 ms: 1.00x faster                                                      |
| regex_dna                | 227 ms                                                 | 231 ms: 1.02x slower                                                      |
| asyncio_websockets       | 559 ms                                                 | 570 ms: 1.02x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 3.77 ms: 1.04x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 1.70 ms: 1.05x slower                                                     |
| regex_effbot             | 3.63 ms                                                | 3.81 ms: 1.05x slower                                                     |
| async_generators         | 444 ms                                                 | 493 ms: 1.11x slower                                                      |
| pickle                   | 10.7 us                                                | 11.9 us: 1.12x slower                                                     |
| pickle_dict              | 29.6 us                                                | 34.0 us: 1.15x slower                                                     |
| unpickle                 | 14.4 us                                                | 16.7 us: 1.16x slower                                                     |
| telco                    | 7.27 ms                                                | 8.68 ms: 1.19x slower                                                     |
| coverage                 | 79.4 ms                                                | 97.5 ms: 1.23x slower                                                     |
| unpack_sequence          | 60.0 ns                                                | 86.9 ns: 1.45x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 9.62 ms: 1.62x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.28x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240328-3.13.0a5+-a4985b2-JIT/bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x


# Memory

- memory change: 1.19x