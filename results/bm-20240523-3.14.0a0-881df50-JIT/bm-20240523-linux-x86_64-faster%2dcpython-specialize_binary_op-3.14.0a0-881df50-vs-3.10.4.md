# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_binary_op
- machine: linux-x86_64
- commit hash: 881df50
- commit date: 2024-05-23
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 279 ms: 1.25x faster                                                            |
| chameleon      | 9.68 ms                                                | 7.12 ms: 1.36x faster                                                           |
| docutils       | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                          |
| html5lib       | 88.9 ms                                                | 67.3 ms: 1.32x faster                                                           |
| tornado_http   | 136 ms                                                 | 97.1 ms: 1.40x faster                                                           |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 386 ms: 1.89x faster                                                            |
| async_tree_memoization  | 870 ms                                                 | 463 ms: 1.88x faster                                                            |
| async_tree_io           | 1.77 sec                                               | 965 ms: 1.83x faster                                                            |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 620 ms: 1.64x faster                                                            |
| Geometric mean          | (ref)                                                  | 1.81x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.0 ms: 1.90x faster                                                           |
| float          | 117 ms                                                 | 72.5 ms: 1.62x faster                                                           |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.46x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 136 ms: 1.38x faster                                                            |
| regex_v8       | 27.8 ms                                                | 26.5 ms: 1.05x faster                                                           |
| regex_dna      | 227 ms                                                 | 233 ms: 1.03x slower                                                            |
| regex_effbot   | 3.63 ms                                                | 3.87 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                                            |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                            |
| tomli_loads          | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 57.9 ms: 1.37x faster                                                           |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.36x faster                                                           |
| xml_etree_generate   | 99.4 ms                                                | 82.5 ms: 1.20x faster                                                           |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.15x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                            |
| json_loads           | 31.2 us                                                | 28.9 us: 1.08x faster                                                           |
| pickle_list          | 5.08 us                                                | 5.15 us: 1.01x slower                                                           |
| unpickle_list        | 5.20 us                                                | 5.31 us: 1.02x slower                                                           |
| unpickle             | 14.4 us                                                | 15.2 us: 1.05x slower                                                           |
| pickle               | 10.7 us                                                | 12.0 us: 1.12x slower                                                           |
| pickle_dict          | 29.6 us                                                | 35.6 us: 1.20x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.9 ms: 1.34x faster                                                           |
| python_startup_no_site | 5.93 ms                                                | 7.59 ms: 1.28x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                           |
| django_template | 48.2 ms                                                | 36.7 ms: 1.31x faster                                                           |
| genshi_text     | 31.8 ms                                                | 25.6 ms: 1.24x faster                                                           |
| genshi_xml      | 66.0 ms                                                | 58.5 ms: 1.13x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.18x faster                                                            |
| generators               | 80.1 ms                                                | 31.2 ms: 2.57x faster                                                           |
| deltablue                | 7.91 ms                                                | 3.79 ms: 2.09x faster                                                           |
| chaos                    | 115 ms                                                 | 57.7 ms: 2.00x faster                                                           |
| richards_super           | 94.7 ms                                                | 48.2 ms: 1.96x faster                                                           |
| crypto_pyaes             | 128 ms                                                 | 66.6 ms: 1.92x faster                                                           |
| scimark_monte_carlo      | 118 ms                                                 | 62.3 ms: 1.90x faster                                                           |
| nbody                    | 154 ms                                                 | 81.0 ms: 1.90x faster                                                           |
| async_tree_none          | 728 ms                                                 | 386 ms: 1.89x faster                                                            |
| async_tree_memoization   | 870 ms                                                 | 463 ms: 1.88x faster                                                            |
| richards                 | 79.3 ms                                                | 42.2 ms: 1.88x faster                                                           |
| async_tree_io            | 1.77 sec                                               | 965 ms: 1.83x faster                                                            |
| raytrace                 | 507 ms                                                 | 281 ms: 1.80x faster                                                            |
| logging_silent           | 190 ns                                                 | 107 ns: 1.78x faster                                                            |
| asyncio_tcp              | 922 ms                                                 | 519 ms: 1.78x faster                                                            |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.74x faster                                                           |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                                           |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 620 ms: 1.64x faster                                                            |
| scimark_sor              | 220 ms                                                 | 134 ms: 1.64x faster                                                            |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                           |
| float                    | 117 ms                                                 | 72.5 ms: 1.62x faster                                                           |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                                            |
| pyflate                  | 716 ms                                                 | 450 ms: 1.59x faster                                                            |
| go                       | 240 ms                                                 | 151 ms: 1.59x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.60 ms: 1.57x faster                                                           |
| pylint                   | 551 ms                                                 | 353 ms: 1.56x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.67 ms: 1.55x faster                                                           |
| deepcopy_memo            | 58.5 us                                                | 38.5 us: 1.52x faster                                                           |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.50x faster                                                           |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                          |
| fannkuch                 | 532 ms                                                 | 360 ms: 1.48x faster                                                            |
| spectral_norm            | 170 ms                                                 | 116 ms: 1.47x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.68 us: 1.46x faster                                                           |
| logging_format           | 9.09 us                                                | 6.24 us: 1.46x faster                                                           |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                          |
| pprint_safe_repr         | 1.02 sec                                               | 708 ms: 1.44x faster                                                            |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.40x faster                                                            |
| tornado_http             | 136 ms                                                 | 97.1 ms: 1.40x faster                                                           |
| scimark_fft              | 466 ms                                                 | 334 ms: 1.39x faster                                                            |
| regex_compile            | 188 ms                                                 | 136 ms: 1.38x faster                                                            |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.38x faster                                                          |
| xml_etree_process        | 79.1 ms                                                | 57.9 ms: 1.37x faster                                                           |
| chameleon                | 9.68 ms                                                | 7.12 ms: 1.36x faster                                                           |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.36x faster                                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.82 ms: 1.34x faster                                                           |
| python_startup           | 14.6 ms                                                | 10.9 ms: 1.34x faster                                                           |
| html5lib                 | 88.9 ms                                                | 67.3 ms: 1.32x faster                                                           |
| django_template          | 48.2 ms                                                | 36.7 ms: 1.31x faster                                                           |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.30x faster                                                          |
| thrift                   | 1.07 ms                                                | 823 us: 1.30x faster                                                            |
| deepcopy                 | 479 us                                                 | 370 us: 1.30x faster                                                            |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.26x faster                                                            |
| 2to3                     | 348 ms                                                 | 279 ms: 1.25x faster                                                            |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                           |
| genshi_text              | 31.8 ms                                                | 25.6 ms: 1.24x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 3.36 us: 1.24x faster                                                           |
| sqlglot_optimize         | 69.2 ms                                                | 56.8 ms: 1.22x faster                                                           |
| dulwich_log              | 84.3 ms                                                | 69.4 ms: 1.22x faster                                                           |
| nqueens                  | 106 ms                                                 | 87.2 ms: 1.21x faster                                                           |
| xml_etree_generate       | 99.4 ms                                                | 82.5 ms: 1.20x faster                                                           |
| dask                     | 441 ms                                                 | 380 ms: 1.16x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 22.4 ms: 1.15x faster                                                           |
| sympy_sum                | 196 ms                                                 | 171 ms: 1.15x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.15x faster                                                            |
| sympy_str                | 346 ms                                                 | 301 ms: 1.15x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 865 us: 1.14x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 58.5 ms: 1.13x faster                                                           |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                          |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                            |
| sympy_expand             | 566 ms                                                 | 514 ms: 1.10x faster                                                            |
| json                     | 5.69 ms                                                | 5.25 ms: 1.08x faster                                                           |
| json_loads               | 31.2 us                                                | 28.9 us: 1.08x faster                                                           |
| mdp                      | 2.85 sec                                               | 2.64 sec: 1.08x faster                                                          |
| regex_v8                 | 27.8 ms                                                | 26.5 ms: 1.05x faster                                                           |
| sqlite_synth             | 3.02 us                                                | 2.89 us: 1.05x faster                                                           |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                            |
| pickle_list              | 5.08 us                                                | 5.15 us: 1.01x slower                                                           |
| asyncio_websockets       | 559 ms                                                 | 570 ms: 1.02x slower                                                            |
| unpickle_list            | 5.20 us                                                | 5.31 us: 1.02x slower                                                           |
| regex_dna                | 227 ms                                                 | 233 ms: 1.03x slower                                                            |
| async_generators         | 444 ms                                                 | 463 ms: 1.04x slower                                                            |
| unpickle                 | 14.4 us                                                | 15.2 us: 1.05x slower                                                           |
| regex_effbot             | 3.63 ms                                                | 3.87 ms: 1.07x slower                                                           |
| flaskblogging            | 8.58 ms                                                | 9.25 ms: 1.08x slower                                                           |
| create_gc_cycles         | 1.62 ms                                                | 1.82 ms: 1.12x slower                                                           |
| pickle                   | 10.7 us                                                | 12.0 us: 1.12x slower                                                           |
| gc_traversal             | 3.62 ms                                                | 4.08 ms: 1.13x slower                                                           |
| telco                    | 7.27 ms                                                | 8.34 ms: 1.15x slower                                                           |
| coverage                 | 79.4 ms                                                | 93.8 ms: 1.18x slower                                                           |
| pickle_dict              | 29.6 us                                                | 35.6 us: 1.20x slower                                                           |
| python_startup_no_site   | 5.93 ms                                                | 7.59 ms: 1.28x slower                                                           |
| Geometric mean           | (ref)                                                  | 1.33x faster                                                                    |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240523-3.14.0a0-881df50-JIT/bm-20240523-linux-x86_64-faster%2dcpython-specialize_binary_op-3.14.0a0-881df50.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.21x