# Results vs. 3.10.4

- fork: mdboom
- ref: pysequence_tuple
- machine: linux-x86_64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.439x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 253 ms: 1.37x faster                                              |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                            |
| html5lib       | 88.9 ms                                                | 62.9 ms: 1.41x faster                                             |
| tornado_http   | 136 ms                                                 | 89.8 ms: 1.52x faster                                             |
| Geometric mean | (ref)                                                  | 1.39x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 313 ms: 2.32x faster                                              |
| async_tree_memoization  | 870 ms                                                 | 393 ms: 2.21x faster                                              |
| async_tree_io           | 1.77 sec                                               | 866 ms: 2.04x faster                                              |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 567 ms: 1.79x faster                                              |
| Geometric mean          | (ref)                                                  | 2.08x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 87.3 ms: 1.76x faster                                             |
| float          | 117 ms                                                 | 76.8 ms: 1.53x faster                                             |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.40x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.48x faster                                              |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                             |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                              |
| regex_effbot   | 3.63 ms                                                | 3.72 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                  | 1.14x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 301 us: 1.61x faster                                              |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                              |
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.50x faster                                            |
| json_dumps           | 14.2 ms                                                | 10.2 ms: 1.38x faster                                             |
| xml_etree_process    | 79.1 ms                                                | 58.1 ms: 1.36x faster                                             |
| xml_etree_generate   | 99.4 ms                                                | 84.2 ms: 1.18x faster                                             |
| json_loads           | 31.2 us                                                | 27.3 us: 1.14x faster                                             |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                              |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                              |
| unpickle_list        | 5.20 us                                                | 5.37 us: 1.03x slower                                             |
| unpickle             | 14.4 us                                                | 15.1 us: 1.05x slower                                             |
| pickle               | 10.7 us                                                | 11.4 us: 1.07x slower                                             |
| pickle_dict          | 29.6 us                                                | 35.1 us: 1.19x slower                                             |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                      |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                             |
| python_startup_no_site | 5.93 ms                                                | 7.00 ms: 1.18x slower                                             |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.6 ms: 1.47x faster                                             |
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                             |
| django_template | 48.2 ms                                                | 34.4 ms: 1.40x faster                                             |
| genshi_xml      | 66.0 ms                                                | 49.2 ms: 1.34x faster                                             |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.42x faster                                              |
| generators               | 80.1 ms                                                | 27.8 ms: 2.88x faster                                             |
| deltablue                | 7.91 ms                                                | 3.14 ms: 2.52x faster                                             |
| async_tree_none          | 728 ms                                                 | 313 ms: 2.32x faster                                              |
| async_tree_memoization   | 870 ms                                                 | 393 ms: 2.21x faster                                              |
| go                       | 240 ms                                                 | 116 ms: 2.07x faster                                              |
| async_tree_io            | 1.77 sec                                               | 866 ms: 2.04x faster                                              |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                             |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                             |
| raytrace                 | 507 ms                                                 | 260 ms: 1.95x faster                                              |
| asyncio_tcp              | 922 ms                                                 | 478 ms: 1.93x faster                                              |
| logging_silent           | 190 ns                                                 | 98.6 ns: 1.92x faster                                             |
| richards_super           | 94.7 ms                                                | 50.9 ms: 1.86x faster                                             |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 71.0 ms: 1.80x faster                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 567 ms: 1.79x faster                                              |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.77x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 66.9 ms: 1.77x faster                                             |
| nbody                    | 154 ms                                                 | 87.3 ms: 1.76x faster                                             |
| richards                 | 79.3 ms                                                | 45.1 ms: 1.76x faster                                             |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.75x faster                                             |
| pylint                   | 551 ms                                                 | 319 ms: 1.73x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.09 ms: 1.71x faster                                             |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                             |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                             |
| pickle_pure_python       | 484 us                                                 | 301 us: 1.61x faster                                              |
| pyflate                  | 716 ms                                                 | 454 ms: 1.58x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                             |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.57x faster                                              |
| spectral_norm            | 170 ms                                                 | 109 ms: 1.56x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                              |
| float                    | 117 ms                                                 | 76.8 ms: 1.53x faster                                             |
| tornado_http             | 136 ms                                                 | 89.8 ms: 1.52x faster                                             |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                             |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.50x faster                                            |
| logging_simple           | 8.30 us                                                | 5.57 us: 1.49x faster                                             |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                             |
| regex_compile            | 188 ms                                                 | 128 ms: 1.48x faster                                              |
| genshi_text              | 31.8 ms                                                | 21.6 ms: 1.47x faster                                             |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                             |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                            |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                            |
| pprint_safe_repr         | 1.02 sec                                               | 713 ms: 1.43x faster                                              |
| html5lib                 | 88.9 ms                                                | 62.9 ms: 1.41x faster                                             |
| django_template          | 48.2 ms                                                | 34.4 ms: 1.40x faster                                             |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                             |
| json_dumps               | 14.2 ms                                                | 10.2 ms: 1.38x faster                                             |
| thrift                   | 1.07 ms                                                | 776 us: 1.38x faster                                              |
| 2to3                     | 348 ms                                                 | 253 ms: 1.37x faster                                              |
| xml_etree_process        | 79.1 ms                                                | 58.1 ms: 1.36x faster                                             |
| genshi_xml               | 66.0 ms                                                | 49.2 ms: 1.34x faster                                             |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                            |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                              |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                              |
| fannkuch                 | 532 ms                                                 | 399 ms: 1.33x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.87 ms: 1.33x faster                                             |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                             |
| nqueens                  | 106 ms                                                 | 80.0 ms: 1.32x faster                                             |
| sqlglot_optimize         | 69.2 ms                                                | 52.9 ms: 1.31x faster                                             |
| dulwich_log              | 84.3 ms                                                | 64.7 ms: 1.30x faster                                             |
| scimark_fft              | 466 ms                                                 | 359 ms: 1.30x faster                                              |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.30x faster                                             |
| sympy_str                | 346 ms                                                 | 270 ms: 1.28x faster                                              |
| bench_thread_pool        | 986 us                                                 | 791 us: 1.25x faster                                              |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                            |
| sympy_expand             | 566 ms                                                 | 454 ms: 1.24x faster                                              |
| xml_etree_generate       | 99.4 ms                                                | 84.2 ms: 1.18x faster                                             |
| unpack_sequence          | 60.0 ns                                                | 51.4 ns: 1.17x faster                                             |
| json_loads               | 31.2 us                                                | 27.3 us: 1.14x faster                                             |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                             |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                              |
| json                     | 5.69 ms                                                | 5.10 ms: 1.11x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                              |
| mdp                      | 2.85 sec                                               | 2.69 sec: 1.06x faster                                            |
| sqlite_synth             | 3.02 us                                                | 2.88 us: 1.05x faster                                             |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                              |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                              |
| async_generators         | 444 ms                                                 | 440 ms: 1.01x faster                                              |
| regex_effbot             | 3.63 ms                                                | 3.72 ms: 1.02x slower                                             |
| unpickle_list            | 5.20 us                                                | 5.37 us: 1.03x slower                                             |
| unpickle                 | 14.4 us                                                | 15.1 us: 1.05x slower                                             |
| coverage                 | 79.4 ms                                                | 84.0 ms: 1.06x slower                                             |
| create_gc_cycles         | 1.62 ms                                                | 1.73 ms: 1.07x slower                                             |
| pickle                   | 10.7 us                                                | 11.4 us: 1.07x slower                                             |
| gc_traversal             | 3.62 ms                                                | 3.90 ms: 1.08x slower                                             |
| telco                    | 7.27 ms                                                | 8.45 ms: 1.16x slower                                             |
| python_startup_no_site   | 5.93 ms                                                | 7.00 ms: 1.18x slower                                             |
| pickle_dict              | 29.6 us                                                | 35.1 us: 1.19x slower                                             |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                      |

Benchmark hidden because not significant (3): asyncio_websockets, pickle_list, bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-linux-x86_64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.439x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.12x