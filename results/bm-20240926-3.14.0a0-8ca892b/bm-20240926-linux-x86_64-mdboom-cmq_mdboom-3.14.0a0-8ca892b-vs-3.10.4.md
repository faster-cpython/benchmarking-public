# Results vs. 3.10.4

- fork: mdboom
- ref: cmq_mdboom
- machine: linux-x86_64
- commit hash: 8ca892b
- commit date: 2024-09-26
- overall geometric mean: 1.40x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 253 ms: 1.38x faster                                        |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                      |
| html5lib       | 88.9 ms                                                | 63.9 ms: 1.39x faster                                       |
| tornado_http   | 136 ms                                                 | 90.4 ms: 1.51x faster                                       |
| Geometric mean | (ref)                                                  | 1.37x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 315 ms: 2.31x faster                                        |
| async_tree_memoization  | 870 ms                                                 | 392 ms: 2.22x faster                                        |
| async_tree_io           | 1.77 sec                                               | 855 ms: 2.07x faster                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 560 ms: 1.81x faster                                        |
| Geometric mean          | (ref)                                                  | 2.09x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.0 ms: 1.74x faster                                       |
| float          | 117 ms                                                 | 76.0 ms: 1.54x faster                                       |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                  | 1.40x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                        |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                       |
| regex_dna      | 227 ms                                                 | 229 ms: 1.01x slower                                        |
| regex_effbot   | 3.63 ms                                                | 3.70 ms: 1.02x slower                                       |
| Geometric mean | (ref)                                                  | 1.13x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 307 us: 1.58x faster                                        |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.54x faster                                        |
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.50x faster                                      |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                       |
| xml_etree_process    | 79.1 ms                                                | 58.4 ms: 1.36x faster                                       |
| xml_etree_generate   | 99.4 ms                                                | 84.8 ms: 1.17x faster                                       |
| json_loads           | 31.2 us                                                | 26.8 us: 1.16x faster                                       |
| xml_etree_iterparse  | 115 ms                                                 | 104 ms: 1.11x faster                                        |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                        |
| pickle               | 10.7 us                                                | 11.8 us: 1.10x slower                                       |
| pickle_dict          | 29.6 us                                                | 33.9 us: 1.14x slower                                       |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                |

Benchmark hidden because not significant (3): pickle_list, unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                       |
| python_startup_no_site | 5.93 ms                                                | 6.98 ms: 1.18x slower                                       |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.8 ms: 1.46x faster                                       |
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                       |
| django_template | 48.2 ms                                                | 34.0 ms: 1.42x faster                                       |
| genshi_xml      | 66.0 ms                                                | 49.2 ms: 1.34x faster                                       |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.43x faster                                        |
| generators               | 80.1 ms                                                | 27.8 ms: 2.88x faster                                       |
| deltablue                | 7.91 ms                                                | 3.24 ms: 2.44x faster                                       |
| async_tree_none          | 728 ms                                                 | 315 ms: 2.31x faster                                        |
| async_tree_memoization   | 870 ms                                                 | 392 ms: 2.22x faster                                        |
| async_tree_io            | 1.77 sec                                               | 855 ms: 2.07x faster                                        |
| go                       | 240 ms                                                 | 117 ms: 2.06x faster                                        |
| chaos                    | 115 ms                                                 | 57.7 ms: 2.00x faster                                       |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                       |
| raytrace                 | 507 ms                                                 | 262 ms: 1.93x faster                                        |
| asyncio_tcp              | 922 ms                                                 | 481 ms: 1.92x faster                                        |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                        |
| richards_super           | 94.7 ms                                                | 52.2 ms: 1.82x faster                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 560 ms: 1.81x faster                                        |
| logging_silent           | 190 ns                                                 | 105 ns: 1.80x faster                                        |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.78x faster                                        |
| scimark_monte_carlo      | 118 ms                                                 | 67.2 ms: 1.76x faster                                       |
| crypto_pyaes             | 128 ms                                                 | 72.7 ms: 1.76x faster                                       |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.75x faster                                       |
| nbody                    | 154 ms                                                 | 88.0 ms: 1.74x faster                                       |
| pylint                   | 551 ms                                                 | 320 ms: 1.72x faster                                        |
| richards                 | 79.3 ms                                                | 46.2 ms: 1.71x faster                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                       |
| hexiom                   | 10.4 ms                                                | 6.20 ms: 1.68x faster                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.63x faster                                       |
| pickle_pure_python       | 484 us                                                 | 307 us: 1.58x faster                                        |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.57x faster                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                       |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.54x faster                                        |
| float                    | 117 ms                                                 | 76.0 ms: 1.54x faster                                       |
| tornado_http             | 136 ms                                                 | 90.4 ms: 1.51x faster                                       |
| pyflate                  | 716 ms                                                 | 476 ms: 1.51x faster                                        |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.50x faster                                      |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                       |
| logging_simple           | 8.30 us                                                | 5.55 us: 1.50x faster                                       |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.49x faster                                        |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                        |
| logging_format           | 9.09 us                                                | 6.17 us: 1.47x faster                                       |
| genshi_text              | 31.8 ms                                                | 21.8 ms: 1.46x faster                                       |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                       |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.44x faster                                      |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                      |
| django_template          | 48.2 ms                                                | 34.0 ms: 1.42x faster                                       |
| pprint_safe_repr         | 1.02 sec                                               | 721 ms: 1.41x faster                                        |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.40x faster                                      |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                       |
| html5lib                 | 88.9 ms                                                | 63.9 ms: 1.39x faster                                       |
| thrift                   | 1.07 ms                                                | 774 us: 1.39x faster                                        |
| 2to3                     | 348 ms                                                 | 253 ms: 1.38x faster                                        |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                       |
| xml_etree_process        | 79.1 ms                                                | 58.4 ms: 1.36x faster                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.79 ms: 1.35x faster                                       |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.35x faster                                        |
| genshi_xml               | 66.0 ms                                                | 49.2 ms: 1.34x faster                                       |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                        |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                       |
| nqueens                  | 106 ms                                                 | 80.4 ms: 1.32x faster                                       |
| dulwich_log              | 84.3 ms                                                | 64.3 ms: 1.31x faster                                       |
| fannkuch                 | 532 ms                                                 | 405 ms: 1.31x faster                                        |
| sqlglot_optimize         | 69.2 ms                                                | 53.0 ms: 1.30x faster                                       |
| scimark_fft              | 466 ms                                                 | 358 ms: 1.30x faster                                        |
| sympy_str                | 346 ms                                                 | 267 ms: 1.30x faster                                        |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                       |
| bench_thread_pool        | 986 us                                                 | 789 us: 1.25x faster                                        |
| sympy_expand             | 566 ms                                                 | 453 ms: 1.25x faster                                        |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                      |
| xml_etree_generate       | 99.4 ms                                                | 84.8 ms: 1.17x faster                                       |
| json_loads               | 31.2 us                                                | 26.8 us: 1.16x faster                                       |
| json                     | 5.69 ms                                                | 4.90 ms: 1.16x faster                                       |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                       |
| unpack_sequence          | 60.0 ns                                                | 53.2 ns: 1.13x faster                                       |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.12x faster                                        |
| mdp                      | 2.85 sec                                               | 2.57 sec: 1.11x faster                                      |
| xml_etree_iterparse      | 115 ms                                                 | 104 ms: 1.11x faster                                        |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                        |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.08x faster                                       |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                        |
| async_generators         | 444 ms                                                 | 434 ms: 1.02x faster                                        |
| regex_dna                | 227 ms                                                 | 229 ms: 1.01x slower                                        |
| regex_effbot             | 3.63 ms                                                | 3.70 ms: 1.02x slower                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.71 ms: 1.06x slower                                       |
| gc_traversal             | 3.62 ms                                                | 3.92 ms: 1.08x slower                                       |
| pickle                   | 10.7 us                                                | 11.8 us: 1.10x slower                                       |
| coverage                 | 79.4 ms                                                | 89.8 ms: 1.13x slower                                       |
| pickle_dict              | 29.6 us                                                | 33.9 us: 1.14x slower                                       |
| telco                    | 7.27 ms                                                | 8.37 ms: 1.15x slower                                       |
| python_startup_no_site   | 5.93 ms                                                | 6.98 ms: 1.18x slower                                       |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                |

Benchmark hidden because not significant (5): bench_mp_pool, asyncio_websockets, pickle_list, unpickle_list, unpickle
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240926-3.14.0a0-8ca892b/bm-20240926-linux-x86_64-mdboom-cmq_mdboom-3.14.0a0-8ca892b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.12x