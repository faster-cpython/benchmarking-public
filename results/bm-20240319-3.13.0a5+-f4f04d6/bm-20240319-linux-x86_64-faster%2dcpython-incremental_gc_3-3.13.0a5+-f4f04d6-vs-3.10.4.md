# Results vs. 3.10.4

- fork: faster-cpython
- ref: incremental_gc_3
- machine: linux-x86_64
- commit hash: f4f04d6
- commit date: 2024-03-19
- overall geometric mean: 1.16x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 294 ms: 1.18x faster                                                         |
| chameleon      | 9.68 ms                                                | 6.94 ms: 1.40x faster                                                        |
| docutils       | 3.30 sec                                               | 4.66 sec: 1.41x slower                                                       |
| html5lib       | 88.9 ms                                                | 75.0 ms: 1.18x faster                                                        |
| tornado_http   | 136 ms                                                 | 99.0 ms: 1.38x faster                                                        |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 1.02 sec                                               | 4.17 sec: 4.11x slower                                                       |
| async_tree_none         | 728 ms                                                 | 3.42 sec: 4.70x slower                                                       |
| async_tree_memoization  | 870 ms                                                 | 4.43 sec: 5.09x slower                                                       |
| async_tree_io           | 1.77 sec                                               | 13.3 sec: 7.51x slower                                                       |
| Geometric mean          | (ref)                                                  | 5.21x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 91.7 ms: 1.67x faster                                                        |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                                         |
| float          | 117 ms                                                 | 144 ms: 1.23x slower                                                         |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.41x faster                                                         |
| regex_v8       | 27.8 ms                                                | 26.6 ms: 1.04x faster                                                        |
| regex_dna      | 227 ms                                                 | 228 ms: 1.01x slower                                                         |
| regex_effbot   | 3.63 ms                                                | 3.69 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 297 us: 1.63x faster                                                         |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                         |
| tomli_loads          | 3.14 sec                                               | 2.20 sec: 1.42x faster                                                       |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 67.9 ms: 1.16x faster                                                        |
| json_loads           | 31.2 us                                                | 28.1 us: 1.11x faster                                                        |
| unpickle_list        | 5.20 us                                                | 5.11 us: 1.02x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 98.4 ms: 1.01x faster                                                        |
| pickle_list          | 5.08 us                                                | 5.33 us: 1.05x slower                                                        |
| unpickle             | 14.4 us                                                | 15.4 us: 1.07x slower                                                        |
| pickle               | 10.7 us                                                | 11.9 us: 1.12x slower                                                        |
| pickle_dict          | 29.6 us                                                | 35.0 us: 1.18x slower                                                        |
| xml_etree_parse      | 168 ms                                                 | 217 ms: 1.29x slower                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 165 ms: 1.43x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 8.85 ms: 1.49x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                        |
| django_template | 48.2 ms                                                | 34.5 ms: 1.39x faster                                                        |
| genshi_text     | 31.8 ms                                                | 23.2 ms: 1.37x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 59.8 ms: 1.10x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 114 us: 4.78x faster                                                         |
| generators               | 80.1 ms                                                | 29.2 ms: 2.74x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.57 ms: 2.21x faster                                                        |
| logging_silent           | 190 ns                                                 | 97.5 ns: 1.95x faster                                                        |
| raytrace                 | 507 ms                                                 | 263 ms: 1.93x faster                                                         |
| chaos                    | 115 ms                                                 | 60.8 ms: 1.90x faster                                                        |
| asyncio_tcp              | 922 ms                                                 | 502 ms: 1.83x faster                                                         |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                         |
| richards_super           | 94.7 ms                                                | 52.3 ms: 1.81x faster                                                        |
| comprehensions           | 28.8 us                                                | 16.1 us: 1.78x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 71.9 ms: 1.78x faster                                                        |
| scimark_monte_carlo      | 118 ms                                                 | 66.9 ms: 1.77x faster                                                        |
| richards                 | 79.3 ms                                                | 45.1 ms: 1.76x faster                                                        |
| go                       | 240 ms                                                 | 140 ms: 1.71x faster                                                         |
| hexiom                   | 10.4 ms                                                | 6.10 ms: 1.70x faster                                                        |
| nbody                    | 154 ms                                                 | 91.7 ms: 1.67x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 297 us: 1.63x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 36.8 us: 1.59x faster                                                        |
| spectral_norm            | 170 ms                                                 | 109 ms: 1.56x faster                                                         |
| pyflate                  | 716 ms                                                 | 461 ms: 1.56x faster                                                         |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.55x faster                                                         |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                         |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.49 ms: 1.46x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 2.20 sec: 1.42x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.85 us: 1.42x faster                                                        |
| regex_compile            | 188 ms                                                 | 134 ms: 1.41x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                       |
| logging_format           | 9.09 us                                                | 6.51 us: 1.40x faster                                                        |
| chameleon                | 9.68 ms                                                | 6.94 ms: 1.40x faster                                                        |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.84 sec: 1.39x faster                                                       |
| django_template          | 48.2 ms                                                | 34.5 ms: 1.39x faster                                                        |
| deepcopy                 | 479 us                                                 | 345 us: 1.39x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 734 ms: 1.39x faster                                                         |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.86 ms: 1.38x faster                                                        |
| tornado_http             | 136 ms                                                 | 99.0 ms: 1.38x faster                                                        |
| genshi_text              | 31.8 ms                                                | 23.2 ms: 1.37x faster                                                        |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 3.11 us: 1.34x faster                                                        |
| thrift                   | 1.07 ms                                                | 800 us: 1.34x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.32x faster                                                         |
| nqueens                  | 106 ms                                                 | 80.8 ms: 1.31x faster                                                        |
| fannkuch                 | 532 ms                                                 | 406 ms: 1.31x faster                                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.95 ms: 1.31x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                        |
| sympy_sum                | 196 ms                                                 | 153 ms: 1.28x faster                                                         |
| scimark_fft              | 466 ms                                                 | 366 ms: 1.27x faster                                                         |
| sympy_str                | 346 ms                                                 | 274 ms: 1.26x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 68.1 ms: 1.24x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 56.1 ms: 1.23x faster                                                        |
| sympy_expand             | 566 ms                                                 | 463 ms: 1.22x faster                                                         |
| bench_thread_pool        | 986 us                                                 | 824 us: 1.20x faster                                                         |
| html5lib                 | 88.9 ms                                                | 75.0 ms: 1.18x faster                                                        |
| 2to3                     | 348 ms                                                 | 294 ms: 1.18x faster                                                         |
| aiohttp                  | 1.44 ms                                                | 1.23 ms: 1.17x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 67.9 ms: 1.16x faster                                                        |
| djangocms                | 38.4 us                                                | 33.3 us: 1.15x faster                                                        |
| gunicorn                 | 1.53 ms                                                | 1.33 ms: 1.15x faster                                                        |
| json_loads               | 31.2 us                                                | 28.1 us: 1.11x faster                                                        |
| mypy2                    | 894 ms                                                 | 806 ms: 1.11x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 59.8 ms: 1.10x faster                                                        |
| pathlib                  | 20.5 ms                                                | 18.6 ms: 1.10x faster                                                        |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                                         |
| create_gc_cycles         | 1.62 ms                                                | 1.49 ms: 1.09x faster                                                        |
| json                     | 5.69 ms                                                | 5.23 ms: 1.09x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.62 sec: 1.09x faster                                                       |
| unpack_sequence          | 60.0 ns                                                | 56.9 ns: 1.06x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 26.6 ms: 1.04x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.52 sec: 1.04x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.93 us: 1.03x faster                                                        |
| gc_traversal             | 3.62 ms                                                | 3.56 ms: 1.02x faster                                                        |
| unpickle_list            | 5.20 us                                                | 5.11 us: 1.02x faster                                                        |
| bench_mp_pool            | 24.0 ms                                                | 23.7 ms: 1.01x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 98.4 ms: 1.01x faster                                                        |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                                         |
| regex_dna                | 227 ms                                                 | 228 ms: 1.01x slower                                                         |
| asyncio_websockets       | 559 ms                                                 | 568 ms: 1.02x slower                                                         |
| regex_effbot             | 3.63 ms                                                | 3.69 ms: 1.02x slower                                                        |
| pickle_list              | 5.08 us                                                | 5.33 us: 1.05x slower                                                        |
| unpickle                 | 14.4 us                                                | 15.4 us: 1.07x slower                                                        |
| pickle                   | 10.7 us                                                | 11.9 us: 1.12x slower                                                        |
| pickle_dict              | 29.6 us                                                | 35.0 us: 1.18x slower                                                        |
| telco                    | 7.27 ms                                                | 8.63 ms: 1.19x slower                                                        |
| async_generators         | 444 ms                                                 | 536 ms: 1.21x slower                                                         |
| coverage                 | 79.4 ms                                                | 96.1 ms: 1.21x slower                                                        |
| float                    | 117 ms                                                 | 144 ms: 1.23x slower                                                         |
| xml_etree_parse          | 168 ms                                                 | 217 ms: 1.29x slower                                                         |
| docutils                 | 3.30 sec                                               | 4.66 sec: 1.41x slower                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 165 ms: 1.43x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 8.85 ms: 1.49x slower                                                        |
| dask                     | 441 ms                                                 | 756 ms: 1.72x slower                                                         |
| pylint                   | 551 ms                                                 | 1.00 sec: 1.82x slower                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 4.17 sec: 4.11x slower                                                       |
| async_tree_none          | 728 ms                                                 | 3.42 sec: 4.70x slower                                                       |
| async_tree_memoization   | 870 ms                                                 | 4.43 sec: 5.09x slower                                                       |
| async_tree_io            | 1.77 sec                                               | 13.3 sec: 7.51x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.16x faster                                                                 |
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240319-3.13.0a5+-f4f04d6/bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.10x


# Memory

- memory change: 1.06x