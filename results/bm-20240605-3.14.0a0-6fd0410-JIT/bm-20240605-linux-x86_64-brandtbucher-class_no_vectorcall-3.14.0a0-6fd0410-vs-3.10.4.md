# Results vs. 3.10.4

- fork: brandtbucher
- ref: class_no_vectorcall
- machine: linux-x86_64
- commit hash: 6fd0410
- commit date: 2024-06-05
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 279 ms: 1.25x faster                                                       |
| docutils       | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                     |
| html5lib       | 88.9 ms                                                | 67.8 ms: 1.31x faster                                                      |
| tornado_http   | 136 ms                                                 | 97.8 ms: 1.39x faster                                                      |
| Geometric mean | (ref)                                                  | 1.26x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 378 ms: 1.93x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 467 ms: 1.86x faster                                                       |
| async_tree_io           | 1.77 sec                                               | 954 ms: 1.85x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 632 ms: 1.61x faster                                                       |
| Geometric mean          | (ref)                                                  | 1.81x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.6 ms: 1.91x faster                                                      |
| float          | 117 ms                                                 | 72.5 ms: 1.61x faster                                                      |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.46x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.37x faster                                                       |
| regex_v8       | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                      |
| regex_dna      | 227 ms                                                 | 229 ms: 1.01x slower                                                       |
| regex_effbot   | 3.63 ms                                                | 3.81 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 297 us: 1.63x faster                                                       |
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.61x faster                                                     |
| unpickle_pure_python | 331 us                                                 | 220 us: 1.50x faster                                                       |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 57.7 ms: 1.37x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 81.1 ms: 1.23x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.15x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                       |
| json_loads           | 31.2 us                                                | 29.1 us: 1.07x faster                                                      |
| pickle_list          | 5.08 us                                                | 5.29 us: 1.04x slower                                                      |
| unpickle_list        | 5.20 us                                                | 5.46 us: 1.05x slower                                                      |
| unpickle             | 14.4 us                                                | 15.9 us: 1.11x slower                                                      |
| pickle               | 10.7 us                                                | 11.9 us: 1.12x slower                                                      |
| pickle_dict          | 29.6 us                                                | 35.9 us: 1.21x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.2 ms: 1.31x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 7.61 ms: 1.28x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.98 ms: 1.64x faster                                                      |
| django_template | 48.2 ms                                                | 36.8 ms: 1.31x faster                                                      |
| genshi_text     | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 57.0 ms: 1.16x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.29x faster                                                       |
| generators               | 80.1 ms                                                | 30.7 ms: 2.61x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.73 ms: 2.12x faster                                                      |
| richards_super           | 94.7 ms                                                | 47.9 ms: 1.98x faster                                                      |
| async_tree_none          | 728 ms                                                 | 378 ms: 1.93x faster                                                       |
| chaos                    | 115 ms                                                 | 60.3 ms: 1.91x faster                                                      |
| richards                 | 79.3 ms                                                | 41.5 ms: 1.91x faster                                                      |
| nbody                    | 154 ms                                                 | 80.6 ms: 1.91x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 63.0 ms: 1.88x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 68.4 ms: 1.87x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 467 ms: 1.86x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 954 ms: 1.85x faster                                                       |
| raytrace                 | 507 ms                                                 | 279 ms: 1.82x faster                                                       |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                       |
| asyncio_tcp              | 922 ms                                                 | 521 ms: 1.77x faster                                                       |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                      |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.72x faster                                                       |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.67x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                      |
| mako                     | 16.3 ms                                                | 9.98 ms: 1.64x faster                                                      |
| go                       | 240 ms                                                 | 147 ms: 1.63x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 297 us: 1.63x faster                                                       |
| float                    | 117 ms                                                 | 72.5 ms: 1.61x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 632 ms: 1.61x faster                                                       |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.61x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.59 ms: 1.58x faster                                                      |
| pyflate                  | 716 ms                                                 | 454 ms: 1.58x faster                                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.64 ms: 1.57x faster                                                      |
| pylint                   | 551 ms                                                 | 353 ms: 1.56x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 38.1 us: 1.53x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 220 us: 1.50x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.61 us: 1.48x faster                                                      |
| fannkuch                 | 532 ms                                                 | 361 ms: 1.47x faster                                                       |
| scimark_fft              | 466 ms                                                 | 318 ms: 1.46x faster                                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.43 ms: 1.46x faster                                                      |
| logging_format           | 9.09 us                                                | 6.29 us: 1.45x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                     |
| scimark_lu               | 176 ms                                                 | 124 ms: 1.42x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 723 ms: 1.41x faster                                                       |
| tornado_http             | 136 ms                                                 | 97.8 ms: 1.39x faster                                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                                     |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 57.7 ms: 1.37x faster                                                      |
| regex_compile            | 188 ms                                                 | 138 ms: 1.37x faster                                                       |
| html5lib                 | 88.9 ms                                                | 67.8 ms: 1.31x faster                                                      |
| django_template          | 48.2 ms                                                | 36.8 ms: 1.31x faster                                                      |
| python_startup           | 14.6 ms                                                | 11.2 ms: 1.31x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.30x faster                                                     |
| thrift                   | 1.07 ms                                                | 822 us: 1.30x faster                                                       |
| genshi_text              | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                      |
| deepcopy                 | 479 us                                                 | 374 us: 1.28x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 3.27 us: 1.28x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                       |
| 2to3                     | 348 ms                                                 | 279 ms: 1.25x faster                                                       |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                      |
| nqueens                  | 106 ms                                                 | 85.7 ms: 1.23x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 81.1 ms: 1.23x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 56.6 ms: 1.22x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 69.7 ms: 1.21x faster                                                      |
| dask                     | 441 ms                                                 | 379 ms: 1.16x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 57.0 ms: 1.16x faster                                                      |
| sympy_str                | 346 ms                                                 | 300 ms: 1.15x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.15x faster                                                       |
| sympy_integrate          | 25.8 ms                                                | 22.5 ms: 1.14x faster                                                      |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.14x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 877 us: 1.12x faster                                                       |
| sympy_expand             | 566 ms                                                 | 506 ms: 1.12x faster                                                       |
| docutils                 | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                     |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                       |
| json_loads               | 31.2 us                                                | 29.1 us: 1.07x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                                      |
| json                     | 5.69 ms                                                | 5.43 ms: 1.05x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.77 sec: 1.03x faster                                                     |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                                       |
| gc_traversal             | 3.62 ms                                                | 3.66 ms: 1.01x slower                                                      |
| regex_dna                | 227 ms                                                 | 229 ms: 1.01x slower                                                       |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.02x slower                                                       |
| pickle_list              | 5.08 us                                                | 5.29 us: 1.04x slower                                                      |
| async_generators         | 444 ms                                                 | 464 ms: 1.04x slower                                                       |
| unpickle_list            | 5.20 us                                                | 5.46 us: 1.05x slower                                                      |
| regex_effbot             | 3.63 ms                                                | 3.81 ms: 1.05x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.79 ms: 1.10x slower                                                      |
| telco                    | 7.27 ms                                                | 8.04 ms: 1.11x slower                                                      |
| unpickle                 | 14.4 us                                                | 15.9 us: 1.11x slower                                                      |
| pickle                   | 10.7 us                                                | 11.9 us: 1.12x slower                                                      |
| coverage                 | 79.4 ms                                                | 94.2 ms: 1.19x slower                                                      |
| pickle_dict              | 29.6 us                                                | 35.9 us: 1.21x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.61 ms: 1.28x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                               |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240605-3.14.0a0-6fd0410-JIT/bm-20240605-linux-x86_64-brandtbucher-class_no_vectorcall-3.14.0a0-6fd0410.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.21x