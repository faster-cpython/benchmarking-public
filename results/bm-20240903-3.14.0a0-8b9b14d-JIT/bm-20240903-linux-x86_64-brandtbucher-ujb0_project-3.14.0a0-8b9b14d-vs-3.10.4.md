# Results vs. 3.10.4

- fork: brandtbucher
- ref: ujb0_project
- machine: linux-x86_64
- commit hash: 8b9b14d
- commit date: 2024-09-03
- overall geometric mean: 1.36x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 296 ms: 1.18x faster                                                |
| docutils       | 3.30 sec                                               | 3.51 sec: 1.06x slower                                              |
| html5lib       | 88.9 ms                                                | 75.0 ms: 1.19x faster                                               |
| tornado_http   | 136 ms                                                 | 117 ms: 1.16x faster                                                |
| Geometric mean | (ref)                                                  | 1.11x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 340 ms: 2.14x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 426 ms: 2.04x faster                                                |
| async_tree_io           | 1.77 sec                                               | 953 ms: 1.86x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 572 ms: 1.78x faster                                                |
| Geometric mean          | (ref)                                                  | 1.95x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.7 ms: 1.90x faster                                               |
| float          | 117 ms                                                 | 69.1 ms: 1.69x faster                                               |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.49x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 155 ms: 1.22x faster                                                |
| regex_v8       | 27.8 ms                                                | 26.4 ms: 1.05x faster                                               |
| regex_dna      | 227 ms                                                 | 230 ms: 1.02x slower                                                |
| regex_effbot   | 3.63 ms                                                | 3.87 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 197 us: 1.67x faster                                                |
| pickle_pure_python   | 484 us                                                 | 314 us: 1.54x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 54.2 ms: 1.46x faster                                               |
| tomli_loads          | 3.14 sec                                               | 2.15 sec: 1.46x faster                                              |
| json_dumps           | 14.2 ms                                                | 9.96 ms: 1.42x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 78.4 ms: 1.27x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 98.5 ms: 1.17x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                |
| json_loads           | 31.2 us                                                | 29.6 us: 1.06x faster                                               |
| Geometric mean       | (ref)                                                  | 1.34x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 7.15 ms: 1.20x slower                                               |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.92 ms: 1.65x faster                                               |
| genshi_text     | 31.8 ms                                                | 22.8 ms: 1.40x faster                                               |
| django_template | 48.2 ms                                                | 39.7 ms: 1.21x faster                                               |
| genshi_xml      | 66.0 ms                                                | 60.8 ms: 1.09x faster                                               |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.37x faster                                                |
| generators               | 80.1 ms                                                | 34.6 ms: 2.31x faster                                               |
| deltablue                | 7.91 ms                                                | 3.53 ms: 2.24x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 26.1 us: 2.24x faster                                               |
| async_tree_none          | 728 ms                                                 | 340 ms: 2.14x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 426 ms: 2.04x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 58.2 ms: 2.03x faster                                               |
| chaos                    | 115 ms                                                 | 59.4 ms: 1.94x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 65.9 ms: 1.94x faster                                               |
| nbody                    | 154 ms                                                 | 80.7 ms: 1.90x faster                                               |
| logging_silent           | 190 ns                                                 | 99.8 ns: 1.90x faster                                               |
| async_tree_io            | 1.77 sec                                               | 953 ms: 1.86x faster                                                |
| deepcopy                 | 479 us                                                 | 261 us: 1.84x faster                                                |
| richards_super           | 94.7 ms                                                | 52.5 ms: 1.80x faster                                               |
| richards                 | 79.3 ms                                                | 43.9 ms: 1.80x faster                                               |
| raytrace                 | 507 ms                                                 | 284 ms: 1.79x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 572 ms: 1.78x faster                                                |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.77x faster                                                |
| asyncio_tcp              | 922 ms                                                 | 529 ms: 1.74x faster                                                |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                               |
| float                    | 117 ms                                                 | 69.1 ms: 1.69x faster                                               |
| unpickle_pure_python     | 331 us                                                 | 197 us: 1.67x faster                                                |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.67x faster                                                |
| mako                     | 16.3 ms                                                | 9.92 ms: 1.65x faster                                               |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.60x faster                                                |
| pyflate                  | 716 ms                                                 | 461 ms: 1.55x faster                                                |
| pickle_pure_python       | 484 us                                                 | 314 us: 1.54x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.79 us: 1.49x faster                                               |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 54.2 ms: 1.46x faster                                               |
| tomli_loads              | 3.14 sec                                               | 2.15 sec: 1.46x faster                                              |
| fannkuch                 | 532 ms                                                 | 367 ms: 1.45x faster                                                |
| coroutines               | 35.1 ms                                                | 24.5 ms: 1.43x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.52 ms: 1.43x faster                                               |
| json_dumps               | 14.2 ms                                                | 9.96 ms: 1.42x faster                                               |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.82 sec: 1.41x faster                                              |
| hexiom                   | 10.4 ms                                                | 7.42 ms: 1.40x faster                                               |
| genshi_text              | 31.8 ms                                                | 22.8 ms: 1.40x faster                                               |
| logging_simple           | 8.30 us                                                | 5.95 us: 1.39x faster                                               |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 743 ms: 1.37x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.37x faster                                              |
| logging_format           | 9.09 us                                                | 6.68 us: 1.36x faster                                               |
| go                       | 240 ms                                                 | 179 ms: 1.34x faster                                                |
| pathlib                  | 20.5 ms                                                | 15.6 ms: 1.31x faster                                               |
| thrift                   | 1.07 ms                                                | 827 us: 1.30x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 78.4 ms: 1.27x faster                                               |
| nqueens                  | 106 ms                                                 | 83.5 ms: 1.27x faster                                               |
| sqlglot_parse            | 2.17 ms                                                | 1.72 ms: 1.26x faster                                               |
| regex_compile            | 188 ms                                                 | 155 ms: 1.22x faster                                                |
| django_template          | 48.2 ms                                                | 39.7 ms: 1.21x faster                                               |
| sqlglot_transpile        | 2.57 ms                                                | 2.17 ms: 1.19x faster                                               |
| pycparser                | 1.58 sec                                               | 1.33 sec: 1.19x faster                                              |
| html5lib                 | 88.9 ms                                                | 75.0 ms: 1.19x faster                                               |
| 2to3                     | 348 ms                                                 | 296 ms: 1.18x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 98.5 ms: 1.17x faster                                               |
| tornado_http             | 136 ms                                                 | 117 ms: 1.16x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                |
| pylint                   | 551 ms                                                 | 480 ms: 1.15x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 125 ms: 1.14x faster                                                |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                |
| bench_thread_pool        | 986 us                                                 | 894 us: 1.10x faster                                                |
| genshi_xml               | 66.0 ms                                                | 60.8 ms: 1.09x faster                                               |
| json                     | 5.69 ms                                                | 5.25 ms: 1.08x faster                                               |
| json_loads               | 31.2 us                                                | 29.6 us: 1.06x faster                                               |
| regex_v8                 | 27.8 ms                                                | 26.4 ms: 1.05x faster                                               |
| mdp                      | 2.85 sec                                               | 2.73 sec: 1.04x faster                                              |
| sqlglot_optimize         | 69.2 ms                                                | 67.1 ms: 1.03x faster                                               |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                |
| sympy_expand             | 566 ms                                                 | 559 ms: 1.01x faster                                                |
| gc_traversal             | 3.62 ms                                                | 3.60 ms: 1.01x faster                                               |
| sympy_str                | 346 ms                                                 | 344 ms: 1.00x faster                                                |
| regex_dna                | 227 ms                                                 | 230 ms: 1.02x slower                                                |
| async_generators         | 444 ms                                                 | 459 ms: 1.03x slower                                                |
| bench_mp_pool            | 24.0 ms                                                | 25.0 ms: 1.04x slower                                               |
| sympy_integrate          | 25.8 ms                                                | 27.4 ms: 1.06x slower                                               |
| docutils                 | 3.30 sec                                               | 3.51 sec: 1.06x slower                                              |
| regex_effbot             | 3.63 ms                                                | 3.87 ms: 1.07x slower                                               |
| coverage                 | 79.4 ms                                                | 86.6 ms: 1.09x slower                                               |
| sympy_sum                | 196 ms                                                 | 217 ms: 1.11x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 1.79 ms: 1.11x slower                                               |
| telco                    | 7.27 ms                                                | 8.13 ms: 1.12x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 7.15 ms: 1.20x slower                                               |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                        |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240903-3.14.0a0-8b9b14d-JIT/bm-20240903-linux-x86_64-brandtbucher-ujb0_project-3.14.0a0-8b9b14d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.37x