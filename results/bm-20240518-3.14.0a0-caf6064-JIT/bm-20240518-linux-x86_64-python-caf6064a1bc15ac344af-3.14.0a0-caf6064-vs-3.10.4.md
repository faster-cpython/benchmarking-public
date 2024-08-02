# Results vs. 3.10.4

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-x86_64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 280 ms: 1.24x faster                                                  |
| chameleon      | 9.68 ms                                                | 7.06 ms: 1.37x faster                                                 |
| docutils       | 3.30 sec                                               | 2.94 sec: 1.12x faster                                                |
| html5lib       | 88.9 ms                                                | 66.0 ms: 1.35x faster                                                 |
| tornado_http   | 136 ms                                                 | 96.6 ms: 1.41x faster                                                 |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 363 ms: 2.00x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 945 ms: 1.87x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 479 ms: 1.82x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 625 ms: 1.63x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.82x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.4 ms: 1.91x faster                                                 |
| float          | 117 ms                                                 | 71.9 ms: 1.63x faster                                                 |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.47x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.36x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                 |
| regex_dna      | 227 ms                                                 | 209 ms: 1.09x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.47 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                |
| pickle_pure_python   | 484 us                                                 | 300 us: 1.62x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 58.1 ms: 1.36x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 82.4 ms: 1.21x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.14x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 151 ms: 1.12x faster                                                  |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                 |
| unpickle_list        | 5.20 us                                                | 5.38 us: 1.04x slower                                                 |
| unpickle             | 14.4 us                                                | 15.2 us: 1.06x slower                                                 |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                                 |
| pickle_list          | 5.08 us                                                | 5.57 us: 1.10x slower                                                 |
| pickle_dict          | 29.6 us                                                | 34.2 us: 1.16x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.9 ms: 1.34x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.59 ms: 1.28x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.62 ms: 1.70x faster                                                 |
| django_template | 48.2 ms                                                | 36.7 ms: 1.31x faster                                                 |
| genshi_text     | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 58.0 ms: 1.14x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.34x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 173 us: 3.15x faster                                                  |
| generators               | 80.1 ms                                                | 30.0 ms: 2.67x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.71 ms: 2.13x faster                                                 |
| async_tree_none          | 728 ms                                                 | 363 ms: 2.00x faster                                                  |
| richards_super           | 94.7 ms                                                | 48.0 ms: 1.97x faster                                                 |
| chaos                    | 115 ms                                                 | 59.5 ms: 1.94x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 66.7 ms: 1.92x faster                                                 |
| nbody                    | 154 ms                                                 | 80.4 ms: 1.91x faster                                                 |
| richards                 | 79.3 ms                                                | 42.1 ms: 1.88x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 63.1 ms: 1.87x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 945 ms: 1.87x faster                                                  |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 479 ms: 1.82x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 522 ms: 1.77x faster                                                  |
| logging_silent           | 190 ns                                                 | 108 ns: 1.76x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                 |
| mako                     | 16.3 ms                                                | 9.62 ms: 1.70x faster                                                 |
| spectral_norm            | 170 ms                                                 | 101 ms: 1.68x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                 |
| scimark_sor              | 220 ms                                                 | 133 ms: 1.65x faster                                                  |
| pyflate                  | 716 ms                                                 | 437 ms: 1.64x faster                                                  |
| go                       | 240 ms                                                 | 147 ms: 1.64x faster                                                  |
| float                    | 117 ms                                                 | 71.9 ms: 1.63x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 625 ms: 1.63x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.62x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                 |
| pylint                   | 551 ms                                                 | 352 ms: 1.56x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.68 ms: 1.56x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 37.7 us: 1.55x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                  |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                  |
| fannkuch                 | 532 ms                                                 | 359 ms: 1.48x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.69 us: 1.46x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.45 ms: 1.45x faster                                                 |
| logging_format           | 9.09 us                                                | 6.31 us: 1.44x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                |
| tornado_http             | 136 ms                                                 | 96.6 ms: 1.41x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 721 ms: 1.41x faster                                                  |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.41x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                                |
| chameleon                | 9.68 ms                                                | 7.06 ms: 1.37x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                |
| regex_compile            | 188 ms                                                 | 138 ms: 1.36x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 58.1 ms: 1.36x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.4 ms: 1.36x faster                                                 |
| html5lib                 | 88.9 ms                                                | 66.0 ms: 1.35x faster                                                 |
| python_startup           | 14.6 ms                                                | 10.9 ms: 1.34x faster                                                 |
| django_template          | 48.2 ms                                                | 36.7 ms: 1.31x faster                                                 |
| deepcopy                 | 479 us                                                 | 366 us: 1.31x faster                                                  |
| thrift                   | 1.07 ms                                                | 823 us: 1.30x faster                                                  |
| genshi_text              | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 3.31 us: 1.26x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.26x faster                                                  |
| 2to3                     | 348 ms                                                 | 280 ms: 1.24x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 69.5 ms: 1.21x faster                                                 |
| nqueens                  | 106 ms                                                 | 87.3 ms: 1.21x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 57.1 ms: 1.21x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 82.4 ms: 1.21x faster                                                 |
| dask                     | 441 ms                                                 | 378 ms: 1.16x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                 |
| sympy_str                | 346 ms                                                 | 300 ms: 1.15x faster                                                  |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 860 us: 1.15x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 22.5 ms: 1.14x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 58.0 ms: 1.14x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.14x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.94 sec: 1.12x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 151 ms: 1.12x faster                                                  |
| sympy_expand             | 566 ms                                                 | 508 ms: 1.11x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.59 sec: 1.10x faster                                                |
| regex_dna                | 227 ms                                                 | 209 ms: 1.09x faster                                                  |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                 |
| meteor_contest           | 120 ms                                                 | 112 ms: 1.07x faster                                                  |
| json                     | 5.69 ms                                                | 5.32 ms: 1.07x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.47 ms: 1.05x faster                                                 |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.02x slower                                                  |
| unpickle_list            | 5.20 us                                                | 5.38 us: 1.04x slower                                                 |
| async_generators         | 444 ms                                                 | 462 ms: 1.04x slower                                                  |
| unpickle                 | 14.4 us                                                | 15.2 us: 1.06x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 3.84 ms: 1.06x slower                                                 |
| flaskblogging            | 8.58 ms                                                | 9.18 ms: 1.07x slower                                                 |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                                 |
| pickle_list              | 5.08 us                                                | 5.57 us: 1.10x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.82 ms: 1.13x slower                                                 |
| pickle_dict              | 29.6 us                                                | 34.2 us: 1.16x slower                                                 |
| coverage                 | 79.4 ms                                                | 95.9 ms: 1.21x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.59 ms: 1.28x slower                                                 |
| telco                    | 7.27 ms                                                | 172 ms: 23.64x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.21x