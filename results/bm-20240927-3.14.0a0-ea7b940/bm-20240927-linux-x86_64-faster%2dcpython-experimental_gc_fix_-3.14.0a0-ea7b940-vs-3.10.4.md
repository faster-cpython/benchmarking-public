# Results vs. 3.10.4

- fork: faster-cpython
- ref: experimental_gc_fix_
- machine: linux-x86_64
- commit hash: ea7b940
- commit date: 2024-09-27
- overall geometric mean: 1.422x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 268 ms: 1.30x faster                                                            |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                          |
| html5lib       | 88.9 ms                                                | 68.0 ms: 1.31x faster                                                           |
| tornado_http   | 136 ms                                                 | 91.1 ms: 1.50x faster                                                           |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 650 ms: 2.72x faster                                                            |
| async_tree_none         | 728 ms                                                 | 300 ms: 2.43x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 365 ms: 2.38x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 521 ms: 1.95x faster                                                            |
| Geometric mean          | (ref)                                                  | 2.35x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 89.6 ms: 1.71x faster                                                           |
| float          | 117 ms                                                 | 94.2 ms: 1.24x faster                                                           |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                            |
| regex_v8       | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                           |
| regex_dna      | 227 ms                                                 | 229 ms: 1.01x slower                                                            |
| regex_effbot   | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 307 us: 1.58x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 221 us: 1.50x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.13 sec: 1.48x faster                                                          |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 61.9 ms: 1.28x faster                                                           |
| json_loads           | 31.2 us                                                | 26.9 us: 1.16x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 87.9 ms: 1.13x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 163 ms: 1.03x faster                                                            |
| pickle_list          | 5.08 us                                                | 5.06 us: 1.00x faster                                                           |
| unpickle_list        | 5.20 us                                                | 5.41 us: 1.04x slower                                                           |
| unpickle             | 14.4 us                                                | 15.1 us: 1.05x slower                                                           |
| pickle               | 10.7 us                                                | 11.4 us: 1.07x slower                                                           |
| pickle_dict          | 29.6 us                                                | 33.6 us: 1.14x slower                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 134 ms: 1.16x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.7 ms: 1.37x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                           |
| genshi_text     | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                           |
| django_template | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 52.6 ms: 1.26x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.38x faster                                                            |
| generators               | 80.1 ms                                                | 27.6 ms: 2.90x faster                                                           |
| async_tree_io            | 1.77 sec                                               | 650 ms: 2.72x faster                                                            |
| async_tree_none          | 728 ms                                                 | 300 ms: 2.43x faster                                                            |
| deltablue                | 7.91 ms                                                | 3.32 ms: 2.38x faster                                                           |
| async_tree_memoization   | 870 ms                                                 | 365 ms: 2.38x faster                                                            |
| go                       | 240 ms                                                 | 121 ms: 1.98x faster                                                            |
| pylint                   | 551 ms                                                 | 279 ms: 1.98x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 521 ms: 1.95x faster                                                            |
| chaos                    | 115 ms                                                 | 60.0 ms: 1.92x faster                                                           |
| asyncio_tcp              | 922 ms                                                 | 479 ms: 1.92x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 30.6 us: 1.91x faster                                                           |
| raytrace                 | 507 ms                                                 | 266 ms: 1.91x faster                                                            |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                            |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                            |
| richards_super           | 94.7 ms                                                | 52.7 ms: 1.80x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 71.6 ms: 1.78x faster                                                           |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.77x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 67.9 ms: 1.74x faster                                                           |
| nbody                    | 154 ms                                                 | 89.6 ms: 1.71x faster                                                           |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                           |
| richards                 | 79.3 ms                                                | 46.5 ms: 1.70x faster                                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.66x faster                                                           |
| hexiom                   | 10.4 ms                                                | 6.25 ms: 1.66x faster                                                           |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 307 us: 1.58x faster                                                            |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.57x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                           |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                                           |
| tornado_http             | 136 ms                                                 | 91.1 ms: 1.50x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 221 us: 1.50x faster                                                            |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.50x faster                                                            |
| pyflate                  | 716 ms                                                 | 480 ms: 1.49x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 2.13 sec: 1.48x faster                                                          |
| logging_simple           | 8.30 us                                                | 5.66 us: 1.47x faster                                                           |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                            |
| logging_format           | 9.09 us                                                | 6.32 us: 1.44x faster                                                           |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                           |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                                          |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                          |
| genshi_text              | 31.8 ms                                                | 22.3 ms: 1.43x faster                                                           |
| pprint_safe_repr         | 1.02 sec                                               | 718 ms: 1.42x faster                                                            |
| django_template          | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                           |
| thrift                   | 1.07 ms                                                | 769 us: 1.39x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.65 ms: 1.39x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                           |
| python_startup           | 14.6 ms                                                | 10.7 ms: 1.37x faster                                                           |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                          |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                            |
| nqueens                  | 106 ms                                                 | 79.8 ms: 1.33x faster                                                           |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.32x faster                                                           |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                                            |
| unpack_sequence          | 60.0 ns                                                | 45.6 ns: 1.32x faster                                                           |
| html5lib                 | 88.9 ms                                                | 68.0 ms: 1.31x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 64.6 ms: 1.31x faster                                                           |
| scimark_fft              | 466 ms                                                 | 357 ms: 1.31x faster                                                            |
| 2to3                     | 348 ms                                                 | 268 ms: 1.30x faster                                                            |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                                            |
| sqlglot_optimize         | 69.2 ms                                                | 53.8 ms: 1.29x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 61.9 ms: 1.28x faster                                                           |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                           |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                          |
| genshi_xml               | 66.0 ms                                                | 52.6 ms: 1.26x faster                                                           |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 793 us: 1.24x faster                                                            |
| float                    | 117 ms                                                 | 94.2 ms: 1.24x faster                                                           |
| json_loads               | 31.2 us                                                | 26.9 us: 1.16x faster                                                           |
| json                     | 5.69 ms                                                | 4.96 ms: 1.15x faster                                                           |
| regex_v8                 | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 87.9 ms: 1.13x faster                                                           |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.71 sec: 1.05x faster                                                          |
| xml_etree_parse          | 168 ms                                                 | 163 ms: 1.03x faster                                                            |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                            |
| pickle_list              | 5.08 us                                                | 5.06 us: 1.00x faster                                                           |
| regex_dna                | 227 ms                                                 | 229 ms: 1.01x slower                                                            |
| async_generators         | 444 ms                                                 | 455 ms: 1.03x slower                                                            |
| regex_effbot             | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                           |
| unpickle_list            | 5.20 us                                                | 5.41 us: 1.04x slower                                                           |
| unpickle                 | 14.4 us                                                | 15.1 us: 1.05x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.70 ms: 1.05x slower                                                           |
| pickle                   | 10.7 us                                                | 11.4 us: 1.07x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 3.89 ms: 1.07x slower                                                           |
| coverage                 | 79.4 ms                                                | 85.8 ms: 1.08x slower                                                           |
| pickle_dict              | 29.6 us                                                | 33.6 us: 1.14x slower                                                           |
| telco                    | 7.27 ms                                                | 8.33 ms: 1.15x slower                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 134 ms: 1.16x slower                                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                                    |

Benchmark hidden because not significant (2): bench_mp_pool, asyncio_websockets
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240927-3.14.0a0-ea7b940/bm-20240927-linux-x86_64-faster%2dcpython-experimental_gc_fix_-3.14.0a0-ea7b940.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.422x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.11x