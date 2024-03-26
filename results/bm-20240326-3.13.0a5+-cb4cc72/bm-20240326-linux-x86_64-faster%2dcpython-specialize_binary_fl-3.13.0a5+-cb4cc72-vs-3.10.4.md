# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_binary_fl
- machine: linux-x86_64
- commit hash: cb4cc72
- commit date: 2024-03-26
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 269 ms: 1.30x faster                                                             |
| chameleon      | 9.68 ms                                                | 6.94 ms: 1.40x faster                                                            |
| docutils       | 3.30 sec                                               | 2.77 sec: 1.19x faster                                                           |
| html5lib       | 88.9 ms                                                | 66.0 ms: 1.35x faster                                                            |
| tornado_http   | 136 ms                                                 | 95.3 ms: 1.43x faster                                                            |
| Geometric mean | (ref)                                                  | 1.33x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 376 ms: 1.94x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 920 ms: 1.92x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 464 ms: 1.87x faster                                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 599 ms: 1.70x faster                                                             |
| Geometric mean          | (ref)                                                  | 1.85x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 91.2 ms: 1.68x faster                                                            |
| float          | 117 ms                                                 | 77.2 ms: 1.52x faster                                                            |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.40x faster                                                             |
| regex_v8       | 27.8 ms                                                | 25.6 ms: 1.09x faster                                                            |
| regex_dna      | 227 ms                                                 | 226 ms: 1.00x faster                                                             |
| regex_effbot   | 3.63 ms                                                | 3.69 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.61x faster                                                             |
| unpickle_pure_python | 331 us                                                 | 221 us: 1.49x faster                                                             |
| tomli_loads          | 3.14 sec                                               | 2.21 sec: 1.42x faster                                                           |
| json_dumps           | 14.2 ms                                                | 10.7 ms: 1.33x faster                                                            |
| xml_etree_process    | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 85.7 ms: 1.16x faster                                                            |
| json_loads           | 31.2 us                                                | 28.5 us: 1.09x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 108 ms: 1.07x faster                                                             |
| xml_etree_parse      | 168 ms                                                 | 160 ms: 1.05x faster                                                             |
| pickle_list          | 5.08 us                                                | 5.16 us: 1.02x slower                                                            |
| unpickle_list        | 5.20 us                                                | 5.50 us: 1.06x slower                                                            |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                                            |
| unpickle             | 14.4 us                                                | 16.0 us: 1.11x slower                                                            |
| pickle_dict          | 29.6 us                                                | 35.2 us: 1.19x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                            |
| python_startup_no_site | 5.93 ms                                                | 8.95 ms: 1.51x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                            |
| django_template | 48.2 ms                                                | 34.6 ms: 1.39x faster                                                            |
| genshi_text     | 31.8 ms                                                | 24.2 ms: 1.32x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 50.8 ms: 1.30x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 109 us: 5.01x faster                                                             |
| generators               | 80.1 ms                                                | 29.9 ms: 2.68x faster                                                            |
| deltablue                | 7.91 ms                                                | 3.25 ms: 2.43x faster                                                            |
| async_tree_none          | 728 ms                                                 | 376 ms: 1.94x faster                                                             |
| async_tree_io            | 1.77 sec                                               | 920 ms: 1.92x faster                                                             |
| chaos                    | 115 ms                                                 | 60.4 ms: 1.91x faster                                                            |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                                             |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                             |
| async_tree_memoization   | 870 ms                                                 | 464 ms: 1.87x faster                                                             |
| richards_super           | 94.7 ms                                                | 51.8 ms: 1.83x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 505 ms: 1.82x faster                                                             |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.79x faster                                                             |
| crypto_pyaes             | 128 ms                                                 | 72.8 ms: 1.76x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 67.4 ms: 1.75x faster                                                            |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.75x faster                                                            |
| richards                 | 79.3 ms                                                | 46.0 ms: 1.72x faster                                                            |
| pylint                   | 551 ms                                                 | 320 ms: 1.72x faster                                                             |
| go                       | 240 ms                                                 | 140 ms: 1.71x faster                                                             |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.70x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 599 ms: 1.70x faster                                                             |
| nbody                    | 154 ms                                                 | 91.2 ms: 1.68x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.33 ms: 1.64x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.61x faster                                                             |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                             |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                                            |
| float                    | 117 ms                                                 | 77.2 ms: 1.52x faster                                                            |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.50x faster                                                             |
| pyflate                  | 716 ms                                                 | 478 ms: 1.50x faster                                                             |
| unpickle_pure_python     | 331 us                                                 | 221 us: 1.49x faster                                                             |
| deepcopy_memo            | 58.5 us                                                | 39.2 us: 1.49x faster                                                            |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                            |
| tornado_http             | 136 ms                                                 | 95.3 ms: 1.43x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 2.21 sec: 1.42x faster                                                           |
| unpack_sequence          | 60.0 ns                                                | 42.3 ns: 1.42x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.91 us: 1.40x faster                                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.83 sec: 1.40x faster                                                           |
| regex_compile            | 188 ms                                                 | 134 ms: 1.40x faster                                                             |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.40x faster                                                           |
| chameleon                | 9.68 ms                                                | 6.94 ms: 1.40x faster                                                            |
| django_template          | 48.2 ms                                                | 34.6 ms: 1.39x faster                                                            |
| pprint_safe_repr         | 1.02 sec                                               | 731 ms: 1.39x faster                                                             |
| logging_format           | 9.09 us                                                | 6.56 us: 1.39x faster                                                            |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                            |
| html5lib                 | 88.9 ms                                                | 66.0 ms: 1.35x faster                                                            |
| deepcopy                 | 479 us                                                 | 356 us: 1.35x faster                                                             |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.7 ms: 1.33x faster                                                            |
| thrift                   | 1.07 ms                                                | 808 us: 1.33x faster                                                             |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                                             |
| xml_etree_process        | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                            |
| genshi_text              | 31.8 ms                                                | 24.2 ms: 1.32x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.93 ms: 1.31x faster                                                            |
| nqueens                  | 106 ms                                                 | 80.7 ms: 1.31x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 3.19 us: 1.31x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 50.8 ms: 1.30x faster                                                            |
| 2to3                     | 348 ms                                                 | 269 ms: 1.30x faster                                                             |
| sympy_integrate          | 25.8 ms                                                | 20.1 ms: 1.28x faster                                                            |
| sympy_sum                | 196 ms                                                 | 153 ms: 1.28x faster                                                             |
| scimark_fft              | 466 ms                                                 | 367 ms: 1.27x faster                                                             |
| sqlglot_optimize         | 69.2 ms                                                | 55.0 ms: 1.26x faster                                                            |
| sympy_str                | 346 ms                                                 | 276 ms: 1.25x faster                                                             |
| dulwich_log              | 84.3 ms                                                | 68.0 ms: 1.24x faster                                                            |
| djangocms                | 38.4 us                                                | 31.2 us: 1.23x faster                                                            |
| sympy_expand             | 566 ms                                                 | 463 ms: 1.22x faster                                                             |
| aiohttp                  | 1.44 ms                                                | 1.19 ms: 1.21x faster                                                            |
| mypy2                    | 894 ms                                                 | 741 ms: 1.21x faster                                                             |
| dask                     | 441 ms                                                 | 368 ms: 1.20x faster                                                             |
| gunicorn                 | 1.53 ms                                                | 1.28 ms: 1.20x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.77 sec: 1.19x faster                                                           |
| bench_thread_pool        | 986 us                                                 | 833 us: 1.18x faster                                                             |
| xml_etree_generate       | 99.4 ms                                                | 85.7 ms: 1.16x faster                                                            |
| create_gc_cycles         | 1.62 ms                                                | 1.46 ms: 1.11x faster                                                            |
| pathlib                  | 20.5 ms                                                | 18.7 ms: 1.10x faster                                                            |
| json_loads               | 31.2 us                                                | 28.5 us: 1.09x faster                                                            |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.09x faster                                                             |
| regex_v8                 | 27.8 ms                                                | 25.6 ms: 1.09x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 108 ms: 1.07x faster                                                             |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 160 ms: 1.05x faster                                                             |
| sqlite_synth             | 3.02 us                                                | 2.92 us: 1.04x faster                                                            |
| mdp                      | 2.85 sec                                               | 2.78 sec: 1.02x faster                                                           |
| gc_traversal             | 3.62 ms                                                | 3.58 ms: 1.01x faster                                                            |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                             |
| regex_dna                | 227 ms                                                 | 226 ms: 1.00x faster                                                             |
| asyncio_websockets       | 559 ms                                                 | 565 ms: 1.01x slower                                                             |
| pickle_list              | 5.08 us                                                | 5.16 us: 1.02x slower                                                            |
| regex_effbot             | 3.63 ms                                                | 3.69 ms: 1.02x slower                                                            |
| unpickle_list            | 5.20 us                                                | 5.50 us: 1.06x slower                                                            |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                                            |
| unpickle                 | 14.4 us                                                | 16.0 us: 1.11x slower                                                            |
| telco                    | 7.27 ms                                                | 8.55 ms: 1.18x slower                                                            |
| pickle_dict              | 29.6 us                                                | 35.2 us: 1.19x slower                                                            |
| coverage                 | 79.4 ms                                                | 96.4 ms: 1.21x slower                                                            |
| python_startup_no_site   | 5.93 ms                                                | 8.95 ms: 1.51x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                                     |

Benchmark hidden because not significant (2): bench_mp_pool, async_generators
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240326-3.13.0a5+-cb4cc72/bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x


# Memory

- memory change: 1.08x