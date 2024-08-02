# Results vs. 3.10.4

- fork: faster-cpython
- ref: dynamic_underflow
- machine: linux-x86_64
- commit hash: 6f75dbe
- commit date: 2024-05-04
- overall geometric mean: 1.31x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 285 ms: 1.22x faster                                                          |
| chameleon      | 9.68 ms                                                | 7.31 ms: 1.32x faster                                                         |
| html5lib       | 88.9 ms                                                | 70.6 ms: 1.26x faster                                                         |
| tornado_http   | 136 ms                                                 | 105 ms: 1.30x faster                                                          |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 371 ms: 1.96x faster                                                          |
| async_tree_io           | 1.77 sec                                               | 931 ms: 1.90x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 474 ms: 1.84x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 639 ms: 1.59x faster                                                          |
| Geometric mean          | (ref)                                                  | 1.82x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.6 ms: 1.93x faster                                                         |
| float          | 117 ms                                                 | 73.2 ms: 1.60x faster                                                         |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                  | 1.46x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 143 ms: 1.32x faster                                                          |
| regex_v8       | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                         |
| regex_dna      | 227 ms                                                 | 227 ms: 1.00x slower                                                          |
| regex_effbot   | 3.63 ms                                                | 3.71 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 299 us: 1.62x faster                                                          |
| unpickle_pure_python | 331 us                                                 | 209 us: 1.58x faster                                                          |
| tomli_loads          | 3.14 sec                                               | 2.02 sec: 1.56x faster                                                        |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 58.4 ms: 1.35x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 83.9 ms: 1.19x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                          |
| json_loads           | 31.2 us                                                | 27.6 us: 1.13x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                          |
| pickle_list          | 5.08 us                                                | 4.92 us: 1.03x faster                                                         |
| unpickle_list        | 5.20 us                                                | 5.26 us: 1.01x slower                                                         |
| unpickle             | 14.4 us                                                | 15.5 us: 1.08x slower                                                         |
| pickle               | 10.7 us                                                | 11.9 us: 1.12x slower                                                         |
| pickle_dict          | 29.6 us                                                | 35.0 us: 1.18x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.1 ms: 1.31x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 7.65 ms: 1.29x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.66 ms: 1.69x faster                                                         |
| genshi_text     | 31.8 ms                                                | 23.5 ms: 1.35x faster                                                         |
| django_template | 48.2 ms                                                | 36.7 ms: 1.31x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 62.7 ms: 1.05x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 174 us: 3.13x faster                                                          |
| generators               | 80.1 ms                                                | 30.3 ms: 2.64x faster                                                         |
| chaos                    | 115 ms                                                 | 57.5 ms: 2.01x faster                                                         |
| async_tree_none          | 728 ms                                                 | 371 ms: 1.96x faster                                                          |
| logging_silent           | 190 ns                                                 | 98.0 ns: 1.94x faster                                                         |
| nbody                    | 154 ms                                                 | 79.6 ms: 1.93x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 61.6 ms: 1.92x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 931 ms: 1.90x faster                                                          |
| deltablue                | 7.91 ms                                                | 4.21 ms: 1.88x faster                                                         |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                                          |
| richards_super           | 94.7 ms                                                | 51.5 ms: 1.84x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 474 ms: 1.84x faster                                                          |
| crypto_pyaes             | 128 ms                                                 | 69.7 ms: 1.83x faster                                                         |
| asyncio_tcp              | 922 ms                                                 | 530 ms: 1.74x faster                                                          |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                         |
| richards                 | 79.3 ms                                                | 45.9 ms: 1.73x faster                                                         |
| mako                     | 16.3 ms                                                | 9.66 ms: 1.69x faster                                                         |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.69x faster                                                          |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.65x faster                                                         |
| go                       | 240 ms                                                 | 146 ms: 1.64x faster                                                          |
| pickle_pure_python       | 484 us                                                 | 299 us: 1.62x faster                                                          |
| pyflate                  | 716 ms                                                 | 447 ms: 1.60x faster                                                          |
| float                    | 117 ms                                                 | 73.2 ms: 1.60x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 639 ms: 1.59x faster                                                          |
| unpickle_pure_python     | 331 us                                                 | 209 us: 1.58x faster                                                          |
| hexiom                   | 10.4 ms                                                | 6.64 ms: 1.57x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 2.02 sec: 1.56x faster                                                        |
| scimark_sor              | 220 ms                                                 | 142 ms: 1.55x faster                                                          |
| deepcopy_memo            | 58.5 us                                                | 38.1 us: 1.54x faster                                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.70 ms: 1.52x faster                                                         |
| scimark_fft              | 466 ms                                                 | 322 ms: 1.45x faster                                                          |
| fannkuch                 | 532 ms                                                 | 371 ms: 1.43x faster                                                          |
| coroutines               | 35.1 ms                                                | 24.5 ms: 1.43x faster                                                         |
| logging_simple           | 8.30 us                                                | 5.92 us: 1.40x faster                                                         |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.39x faster                                                         |
| logging_format           | 9.09 us                                                | 6.58 us: 1.38x faster                                                         |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.71 ms: 1.37x faster                                                         |
| scimark_lu               | 176 ms                                                 | 129 ms: 1.37x faster                                                          |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.36x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 751 ms: 1.36x faster                                                          |
| xml_etree_process        | 79.1 ms                                                | 58.4 ms: 1.35x faster                                                         |
| genshi_text              | 31.8 ms                                                | 23.5 ms: 1.35x faster                                                         |
| pylint                   | 551 ms                                                 | 409 ms: 1.35x faster                                                          |
| thrift                   | 1.07 ms                                                | 802 us: 1.34x faster                                                          |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                        |
| chameleon                | 9.68 ms                                                | 7.31 ms: 1.32x faster                                                         |
| regex_compile            | 188 ms                                                 | 143 ms: 1.32x faster                                                          |
| django_template          | 48.2 ms                                                | 36.7 ms: 1.31x faster                                                         |
| python_startup           | 14.6 ms                                                | 11.1 ms: 1.31x faster                                                         |
| deepcopy                 | 479 us                                                 | 367 us: 1.31x faster                                                          |
| tornado_http             | 136 ms                                                 | 105 ms: 1.30x faster                                                          |
| deepcopy_reduce          | 4.17 us                                                | 3.24 us: 1.29x faster                                                         |
| html5lib                 | 88.9 ms                                                | 70.6 ms: 1.26x faster                                                         |
| nqueens                  | 106 ms                                                 | 84.7 ms: 1.25x faster                                                         |
| 2to3                     | 348 ms                                                 | 285 ms: 1.22x faster                                                          |
| sqlglot_normalize        | 143 ms                                                 | 119 ms: 1.20x faster                                                          |
| sqlglot_optimize         | 69.2 ms                                                | 58.2 ms: 1.19x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 83.9 ms: 1.19x faster                                                         |
| djangocms                | 38.4 us                                                | 33.3 us: 1.15x faster                                                         |
| dask                     | 441 ms                                                 | 383 ms: 1.15x faster                                                          |
| pathlib                  | 20.5 ms                                                | 17.8 ms: 1.15x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                          |
| dulwich_log              | 84.3 ms                                                | 74.4 ms: 1.13x faster                                                         |
| json_loads               | 31.2 us                                                | 27.6 us: 1.13x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                          |
| bench_thread_pool        | 986 us                                                 | 882 us: 1.12x faster                                                          |
| json                     | 5.69 ms                                                | 5.11 ms: 1.11x faster                                                         |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 25.2 ms: 1.10x faster                                                         |
| aiohttp                  | 1.44 ms                                                | 1.31 ms: 1.10x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.59 sec: 1.10x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 23.6 ms: 1.09x faster                                                         |
| sympy_str                | 346 ms                                                 | 317 ms: 1.09x faster                                                          |
| gunicorn                 | 1.53 ms                                                | 1.43 ms: 1.07x faster                                                         |
| sympy_expand             | 566 ms                                                 | 528 ms: 1.07x faster                                                          |
| sympy_sum                | 196 ms                                                 | 184 ms: 1.07x faster                                                          |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.06x faster                                                         |
| genshi_xml               | 66.0 ms                                                | 62.7 ms: 1.05x faster                                                         |
| pickle_list              | 5.08 us                                                | 4.92 us: 1.03x faster                                                         |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                          |
| regex_dna                | 227 ms                                                 | 227 ms: 1.00x slower                                                          |
| unpickle_list            | 5.20 us                                                | 5.26 us: 1.01x slower                                                         |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.01x slower                                                          |
| regex_effbot             | 3.63 ms                                                | 3.71 ms: 1.02x slower                                                         |
| mypy2                    | 894 ms                                                 | 926 ms: 1.04x slower                                                          |
| async_generators         | 444 ms                                                 | 463 ms: 1.04x slower                                                          |
| gc_traversal             | 3.62 ms                                                | 3.86 ms: 1.07x slower                                                         |
| unpickle                 | 14.4 us                                                | 15.5 us: 1.08x slower                                                         |
| coverage                 | 79.4 ms                                                | 87.4 ms: 1.10x slower                                                         |
| flaskblogging            | 8.58 ms                                                | 9.55 ms: 1.11x slower                                                         |
| pickle                   | 10.7 us                                                | 11.9 us: 1.12x slower                                                         |
| telco                    | 7.27 ms                                                | 8.18 ms: 1.13x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 1.85 ms: 1.14x slower                                                         |
| pickle_dict              | 29.6 us                                                | 35.0 us: 1.18x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 7.65 ms: 1.29x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.31x faster                                                                  |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240504-3.13.0a6+-6f75dbe-JIT/bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.22x