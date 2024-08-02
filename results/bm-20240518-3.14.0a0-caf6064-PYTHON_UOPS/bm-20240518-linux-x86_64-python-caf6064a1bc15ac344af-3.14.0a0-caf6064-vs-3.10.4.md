# Results vs. 3.10.4

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-x86_64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.03x slower
- HPT reliability: 98.10%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 379 ms: 1.09x slower                                                  |
| chameleon      | 9.68 ms                                                | 8.87 ms: 1.09x faster                                                 |
| docutils       | 3.30 sec                                               | 3.57 sec: 1.08x slower                                                |
| html5lib       | 88.9 ms                                                | 85.0 ms: 1.05x faster                                                 |
| tornado_http   | 136 ms                                                 | 107 ms: 1.27x faster                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 409 ms: 1.78x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 998 ms: 1.77x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 532 ms: 1.64x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 665 ms: 1.53x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.68x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 191 ms                                                 | 193 ms: 1.01x slower                                                  |
| float          | 117 ms                                                 | 131 ms: 1.12x slower                                                  |
| nbody          | 154 ms                                                 | 198 ms: 1.29x slower                                                  |
| Geometric mean | (ref)                                                  | 1.14x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 27.8 ms                                                | 25.6 ms: 1.09x faster                                                 |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.76 ms: 1.03x slower                                                 |
| regex_compile  | 188 ms                                                 | 239 ms: 1.27x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                 |
| json_loads           | 31.2 us                                                | 28.9 us: 1.08x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 80.1 ms: 1.01x slower                                                 |
| unpickle             | 14.4 us                                                | 15.5 us: 1.08x slower                                                 |
| pickle_list          | 5.08 us                                                | 5.54 us: 1.09x slower                                                 |
| unpickle_list        | 5.20 us                                                | 5.70 us: 1.10x slower                                                 |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 128 ms: 1.11x slower                                                  |
| pickle_dict          | 29.6 us                                                | 33.5 us: 1.13x slower                                                 |
| pickle_pure_python   | 484 us                                                 | 556 us: 1.15x slower                                                  |
| tomli_loads          | 3.14 sec                                               | 3.61 sec: 1.15x slower                                                |
| xml_etree_generate   | 99.4 ms                                                | 116 ms: 1.16x slower                                                  |
| unpickle_pure_python | 331 us                                                 | 405 us: 1.23x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 49.6 ms: 1.03x slower                                                 |
| genshi_text     | 31.8 ms                                                | 40.6 ms: 1.28x slower                                                 |
| mako            | 16.3 ms                                                | 20.9 ms: 1.28x slower                                                 |
| genshi_xml      | 66.0 ms                                                | 86.0 ms: 1.30x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.22x slower                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 213 us: 2.55x faster                                                  |
| generators               | 80.1 ms                                                | 32.1 ms: 2.49x faster                                                 |
| async_tree_none          | 728 ms                                                 | 409 ms: 1.78x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 998 ms: 1.77x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 532 ms: 1.73x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 532 ms: 1.64x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 665 ms: 1.53x faster                                                  |
| deltablue                | 7.91 ms                                                | 5.36 ms: 1.48x faster                                                 |
| coroutines               | 35.1 ms                                                | 24.8 ms: 1.41x faster                                                 |
| pylint                   | 551 ms                                                 | 391 ms: 1.41x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.87 sec: 1.37x faster                                                |
| raytrace                 | 507 ms                                                 | 379 ms: 1.34x faster                                                  |
| thrift                   | 1.07 ms                                                | 841 us: 1.27x faster                                                  |
| tornado_http             | 136 ms                                                 | 107 ms: 1.27x faster                                                  |
| logging_simple           | 8.30 us                                                | 6.78 us: 1.22x faster                                                 |
| scimark_sor              | 220 ms                                                 | 179 ms: 1.22x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                 |
| logging_format           | 9.09 us                                                | 7.54 us: 1.21x faster                                                 |
| pathlib                  | 20.5 ms                                                | 17.9 ms: 1.14x faster                                                 |
| dask                     | 441 ms                                                 | 400 ms: 1.10x faster                                                  |
| chameleon                | 9.68 ms                                                | 8.87 ms: 1.09x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 25.6 ms: 1.09x faster                                                 |
| go                       | 240 ms                                                 | 222 ms: 1.08x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 77.9 ms: 1.08x faster                                                 |
| json_loads               | 31.2 us                                                | 28.9 us: 1.08x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| richards_super           | 94.7 ms                                                | 88.7 ms: 1.07x faster                                                 |
| html5lib                 | 88.9 ms                                                | 85.0 ms: 1.05x faster                                                 |
| chaos                    | 115 ms                                                 | 111 ms: 1.04x faster                                                  |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 2.15 ms: 1.01x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 128 ms: 1.01x slower                                                  |
| json                     | 5.69 ms                                                | 5.76 ms: 1.01x slower                                                 |
| xml_etree_process        | 79.1 ms                                                | 80.1 ms: 1.01x slower                                                 |
| pidigits                 | 191 ms                                                 | 193 ms: 1.01x slower                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 2.61 ms: 1.01x slower                                                 |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.01x slower                                                  |
| bench_thread_pool        | 986 us                                                 | 1.01 ms: 1.02x slower                                                 |
| pycparser                | 1.58 sec                                               | 1.62 sec: 1.03x slower                                                |
| django_template          | 48.2 ms                                                | 49.6 ms: 1.03x slower                                                 |
| richards                 | 79.3 ms                                                | 81.7 ms: 1.03x slower                                                 |
| sympy_sum                | 196 ms                                                 | 203 ms: 1.03x slower                                                  |
| sqlite_synth             | 3.02 us                                                | 3.13 us: 1.03x slower                                                 |
| regex_effbot             | 3.63 ms                                                | 3.76 ms: 1.03x slower                                                 |
| deepcopy_reduce          | 4.17 us                                                | 4.41 us: 1.06x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 3.85 ms: 1.06x slower                                                 |
| unpickle                 | 14.4 us                                                | 15.5 us: 1.08x slower                                                 |
| mdp                      | 2.85 sec                                               | 3.08 sec: 1.08x slower                                                |
| docutils                 | 3.30 sec                                               | 3.57 sec: 1.08x slower                                                |
| sympy_expand             | 566 ms                                                 | 614 ms: 1.09x slower                                                  |
| 2to3                     | 348 ms                                                 | 379 ms: 1.09x slower                                                  |
| pickle_list              | 5.08 us                                                | 5.54 us: 1.09x slower                                                 |
| sqlglot_normalize        | 143 ms                                                 | 156 ms: 1.09x slower                                                  |
| sympy_str                | 346 ms                                                 | 379 ms: 1.10x slower                                                  |
| unpickle_list            | 5.20 us                                                | 5.70 us: 1.10x slower                                                 |
| sympy_integrate          | 25.8 ms                                                | 28.5 ms: 1.10x slower                                                 |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 128 ms: 1.11x slower                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 77.5 ms: 1.12x slower                                                 |
| float                    | 117 ms                                                 | 131 ms: 1.12x slower                                                  |
| async_generators         | 444 ms                                                 | 499 ms: 1.12x slower                                                  |
| flaskblogging            | 8.58 ms                                                | 9.68 ms: 1.13x slower                                                 |
| pickle_dict              | 29.6 us                                                | 33.5 us: 1.13x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.84 ms: 1.13x slower                                                 |
| scimark_lu               | 176 ms                                                 | 200 ms: 1.14x slower                                                  |
| pickle_pure_python       | 484 us                                                 | 556 us: 1.15x slower                                                  |
| tomli_loads              | 3.14 sec                                               | 3.61 sec: 1.15x slower                                                |
| scimark_monte_carlo      | 118 ms                                                 | 136 ms: 1.15x slower                                                  |
| xml_etree_generate       | 99.4 ms                                                | 116 ms: 1.16x slower                                                  |
| deepcopy                 | 479 us                                                 | 561 us: 1.17x slower                                                  |
| coverage                 | 79.4 ms                                                | 93.1 ms: 1.17x slower                                                 |
| logging_silent           | 190 ns                                                 | 223 ns: 1.18x slower                                                  |
| pyflate                  | 716 ms                                                 | 849 ms: 1.19x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.17 ms: 1.21x slower                                                 |
| unpickle_pure_python     | 331 us                                                 | 405 us: 1.23x slower                                                  |
| meteor_contest           | 120 ms                                                 | 148 ms: 1.24x slower                                                  |
| regex_compile            | 188 ms                                                 | 239 ms: 1.27x slower                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 1.30 sec: 1.28x slower                                                |
| genshi_text              | 31.8 ms                                                | 40.6 ms: 1.28x slower                                                 |
| pprint_pformat           | 2.10 sec                                               | 2.69 sec: 1.28x slower                                                |
| mako                     | 16.3 ms                                                | 20.9 ms: 1.28x slower                                                 |
| scimark_fft              | 466 ms                                                 | 599 ms: 1.29x slower                                                  |
| nbody                    | 154 ms                                                 | 198 ms: 1.29x slower                                                  |
| genshi_xml               | 66.0 ms                                                | 86.0 ms: 1.30x slower                                                 |
| spectral_norm            | 170 ms                                                 | 223 ms: 1.31x slower                                                  |
| comprehensions           | 28.8 us                                                | 38.1 us: 1.32x slower                                                 |
| deepcopy_memo            | 58.5 us                                                | 77.9 us: 1.33x slower                                                 |
| fannkuch                 | 532 ms                                                 | 726 ms: 1.36x slower                                                  |
| nqueens                  | 106 ms                                                 | 144 ms: 1.37x slower                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 8.96 ms: 1.39x slower                                                 |
| hexiom                   | 10.4 ms                                                | 15.2 ms: 1.46x slower                                                 |
| telco                    | 7.27 ms                                                | 182 ms: 25.06x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 98.10% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.13x