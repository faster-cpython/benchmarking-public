# Results vs. 3.10.4

- fork: faster-cpython
- ref: inline_values
- machine: linux-x86_64
- commit hash: c05d01d
- commit date: 2024-03-26
- overall geometric mean: 1.36x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 268 ms: 1.30x faster                                                      |
| chameleon      | 9.68 ms                                                | 6.88 ms: 1.41x faster                                                     |
| docutils       | 3.30 sec                                               | 2.78 sec: 1.19x faster                                                    |
| html5lib       | 88.9 ms                                                | 66.1 ms: 1.34x faster                                                     |
| tornado_http   | 136 ms                                                 | 94.2 ms: 1.45x faster                                                     |
| Geometric mean | (ref)                                                  | 1.33x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 376 ms: 1.93x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 936 ms: 1.89x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 463 ms: 1.88x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 609 ms: 1.67x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.84x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 89.3 ms: 1.72x faster                                                     |
| float          | 117 ms                                                 | 78.1 ms: 1.50x faster                                                     |
| pidigits       | 191 ms                                                 | 194 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.36x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 133 ms: 1.41x faster                                                      |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                     |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.72 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 298 us: 1.62x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                      |
| tomli_loads          | 3.14 sec                                               | 2.18 sec: 1.44x faster                                                    |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                     |
| xml_etree_process    | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 86.6 ms: 1.15x faster                                                     |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 108 ms: 1.07x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 163 ms: 1.03x faster                                                      |
| pickle_list          | 5.08 us                                                | 5.25 us: 1.03x slower                                                     |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                                     |
| unpickle             | 14.4 us                                                | 16.2 us: 1.12x slower                                                     |
| pickle_dict          | 29.6 us                                                | 34.6 us: 1.17x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                              |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 8.87 ms: 1.50x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako           | 16.3 ms                                                | 10.8 ms: 1.51x faster                                                     |
| genshi_text    | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                     |
| genshi_xml     | 66.0 ms                                                | 53.2 ms: 1.24x faster                                                     |
| Geometric mean | (ref)                                                  | 1.35x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 111 us: 4.91x faster                                                      |
| generators               | 80.1 ms                                                | 29.7 ms: 2.70x faster                                                     |
| deltablue                | 7.91 ms                                                | 3.12 ms: 2.53x faster                                                     |
| raytrace                 | 507 ms                                                 | 257 ms: 1.97x faster                                                      |
| chaos                    | 115 ms                                                 | 59.3 ms: 1.95x faster                                                     |
| async_tree_none          | 728 ms                                                 | 376 ms: 1.93x faster                                                      |
| logging_silent           | 190 ns                                                 | 98.5 ns: 1.93x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 936 ms: 1.89x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 463 ms: 1.88x faster                                                      |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                      |
| richards_super           | 94.7 ms                                                | 51.7 ms: 1.83x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 65.5 ms: 1.80x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 71.0 ms: 1.80x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 513 ms: 1.80x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.76x faster                                                     |
| richards                 | 79.3 ms                                                | 45.7 ms: 1.73x faster                                                     |
| go                       | 240 ms                                                 | 139 ms: 1.73x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.26 ms: 1.72x faster                                                     |
| nbody                    | 154 ms                                                 | 89.3 ms: 1.72x faster                                                     |
| pylint                   | 551 ms                                                 | 321 ms: 1.72x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.10 ms: 1.70x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 609 ms: 1.67x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 298 us: 1.62x faster                                                      |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.61x faster                                                      |
| pyflate                  | 716 ms                                                 | 451 ms: 1.59x faster                                                      |
| coroutines               | 35.1 ms                                                | 22.3 ms: 1.57x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 37.2 us: 1.57x faster                                                     |
| spectral_norm            | 170 ms                                                 | 111 ms: 1.54x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                      |
| mako                     | 16.3 ms                                                | 10.8 ms: 1.51x faster                                                     |
| float                    | 117 ms                                                 | 78.1 ms: 1.50x faster                                                     |
| tornado_http             | 136 ms                                                 | 94.2 ms: 1.45x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 2.18 sec: 1.44x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.87 us: 1.41x faster                                                     |
| regex_compile            | 188 ms                                                 | 133 ms: 1.41x faster                                                      |
| chameleon                | 9.68 ms                                                | 6.88 ms: 1.41x faster                                                     |
| logging_format           | 9.09 us                                                | 6.48 us: 1.40x faster                                                     |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.84 sec: 1.40x faster                                                    |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                    |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 739 ms: 1.38x faster                                                      |
| deepcopy                 | 479 us                                                 | 349 us: 1.37x faster                                                      |
| fannkuch                 | 532 ms                                                 | 389 ms: 1.37x faster                                                      |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                     |
| html5lib                 | 88.9 ms                                                | 66.1 ms: 1.34x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.84 ms: 1.34x faster                                                     |
| thrift                   | 1.07 ms                                                | 808 us: 1.33x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                     |
| unpack_sequence          | 60.0 ns                                                | 45.6 ns: 1.32x faster                                                     |
| scimark_fft              | 466 ms                                                 | 354 ms: 1.32x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 3.17 us: 1.31x faster                                                     |
| genshi_text              | 31.8 ms                                                | 24.3 ms: 1.31x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                      |
| 2to3                     | 348 ms                                                 | 268 ms: 1.30x faster                                                      |
| nqueens                  | 106 ms                                                 | 81.6 ms: 1.30x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 20.1 ms: 1.29x faster                                                     |
| sympy_sum                | 196 ms                                                 | 154 ms: 1.28x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 54.8 ms: 1.26x faster                                                     |
| sympy_str                | 346 ms                                                 | 277 ms: 1.25x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 67.7 ms: 1.25x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 53.2 ms: 1.24x faster                                                     |
| aiohttp                  | 1.44 ms                                                | 1.18 ms: 1.22x faster                                                     |
| sympy_expand             | 566 ms                                                 | 463 ms: 1.22x faster                                                      |
| mypy2                    | 894 ms                                                 | 737 ms: 1.21x faster                                                      |
| gunicorn                 | 1.53 ms                                                | 1.28 ms: 1.20x faster                                                     |
| dask                     | 441 ms                                                 | 369 ms: 1.19x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 826 us: 1.19x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.78 sec: 1.19x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 86.6 ms: 1.15x faster                                                     |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                      |
| pathlib                  | 20.5 ms                                                | 18.6 ms: 1.10x faster                                                     |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.63 sec: 1.08x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 108 ms: 1.07x faster                                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.53 ms: 1.06x faster                                                     |
| json                     | 5.69 ms                                                | 5.47 ms: 1.04x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.92 us: 1.04x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 163 ms: 1.03x faster                                                      |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                      |
| bench_mp_pool            | 24.0 ms                                                | 23.8 ms: 1.01x faster                                                     |
| async_generators         | 444 ms                                                 | 446 ms: 1.01x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 3.67 ms: 1.01x slower                                                     |
| pidigits                 | 191 ms                                                 | 194 ms: 1.02x slower                                                      |
| asyncio_websockets       | 559 ms                                                 | 569 ms: 1.02x slower                                                      |
| regex_effbot             | 3.63 ms                                                | 3.72 ms: 1.03x slower                                                     |
| pickle_list              | 5.08 us                                                | 5.25 us: 1.03x slower                                                     |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                                     |
| unpickle                 | 14.4 us                                                | 16.2 us: 1.12x slower                                                     |
| pickle_dict              | 29.6 us                                                | 34.6 us: 1.17x slower                                                     |
| telco                    | 7.27 ms                                                | 8.50 ms: 1.17x slower                                                     |
| coverage                 | 79.4 ms                                                | 98.3 ms: 1.24x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 8.87 ms: 1.50x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                              |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: django_template, djangocms, flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240326-3.13.0a5+-c05d01d/bm-20240326-linux-x86_64-faster%2dcpython-inline_values-3.13.0a5+-c05d01d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x


# Memory

- memory change: 1.09x