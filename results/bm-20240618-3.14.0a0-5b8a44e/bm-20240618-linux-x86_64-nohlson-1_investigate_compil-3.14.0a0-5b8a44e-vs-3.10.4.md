# Results vs. 3.10.4

- fork: nohlson
- ref: 1_investigate_compil
- machine: linux-x86_64
- commit hash: 5b8a44e
- commit date: 2024-06-18
- overall geometric mean: 1.37x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 267 ms: 1.30x faster                                                   |
| docutils       | 3.30 sec                                               | 2.78 sec: 1.19x faster                                                 |
| html5lib       | 88.9 ms                                                | 65.1 ms: 1.37x faster                                                  |
| tornado_http   | 136 ms                                                 | 93.3 ms: 1.46x faster                                                  |
| Geometric mean | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 373 ms: 1.95x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 933 ms: 1.89x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 461 ms: 1.89x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 638 ms: 1.59x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.83x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 87.4 ms: 1.76x faster                                                  |
| float          | 117 ms                                                 | 77.6 ms: 1.51x faster                                                  |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.39x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 133 ms: 1.42x faster                                                   |
| regex_v8       | 27.8 ms                                                | 27.2 ms: 1.02x faster                                                  |
| regex_dna      | 227 ms                                                 | 231 ms: 1.02x slower                                                   |
| regex_effbot   | 3.63 ms                                                | 3.92 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 212 us: 1.56x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 2.18 sec: 1.44x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 59.2 ms: 1.34x faster                                                  |
| json_dumps           | 14.2 ms                                                | 10.7 ms: 1.32x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 85.7 ms: 1.16x faster                                                  |
| json_loads           | 31.2 us                                                | 28.1 us: 1.11x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 107 ms: 1.08x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 159 ms: 1.06x faster                                                   |
| pickle_list          | 5.08 us                                                | 5.04 us: 1.01x faster                                                  |
| unpickle             | 14.4 us                                                | 15.3 us: 1.06x slower                                                  |
| unpickle_list        | 5.20 us                                                | 5.53 us: 1.06x slower                                                  |
| pickle               | 10.7 us                                                | 11.9 us: 1.12x slower                                                  |
| pickle_dict          | 29.6 us                                                | 34.0 us: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.7 ms: 1.36x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.15 ms: 1.21x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                  |
| django_template | 48.2 ms                                                | 34.8 ms: 1.39x faster                                                  |
| genshi_text     | 31.8 ms                                                | 23.4 ms: 1.36x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 50.7 ms: 1.30x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.31x faster                                                   |
| generators               | 80.1 ms                                                | 29.3 ms: 2.73x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.22 ms: 2.46x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.0 us: 2.01x faster                                                  |
| raytrace                 | 507 ms                                                 | 257 ms: 1.97x faster                                                   |
| chaos                    | 115 ms                                                 | 59.0 ms: 1.96x faster                                                  |
| async_tree_none          | 728 ms                                                 | 373 ms: 1.95x faster                                                   |
| logging_silent           | 190 ns                                                 | 97.4 ns: 1.95x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 933 ms: 1.89x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 461 ms: 1.89x faster                                                   |
| asyncio_tcp              | 922 ms                                                 | 500 ms: 1.84x faster                                                   |
| deepcopy                 | 479 us                                                 | 263 us: 1.82x faster                                                   |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.79x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 66.0 ms: 1.79x faster                                                  |
| richards_super           | 94.7 ms                                                | 53.2 ms: 1.78x faster                                                  |
| nbody                    | 154 ms                                                 | 87.4 ms: 1.76x faster                                                  |
| pylint                   | 551 ms                                                 | 315 ms: 1.75x faster                                                   |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 74.2 ms: 1.72x faster                                                  |
| go                       | 240 ms                                                 | 140 ms: 1.72x faster                                                   |
| richards                 | 79.3 ms                                                | 46.8 ms: 1.69x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.20 ms: 1.68x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 638 ms: 1.59x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 212 us: 1.56x faster                                                   |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.55x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.1 ms: 1.52x faster                                                  |
| float                    | 117 ms                                                 | 77.6 ms: 1.51x faster                                                  |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.51x faster                                                   |
| pyflate                  | 716 ms                                                 | 480 ms: 1.49x faster                                                   |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                  |
| tornado_http             | 136 ms                                                 | 93.3 ms: 1.46x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.72 us: 1.45x faster                                                  |
| logging_format           | 9.09 us                                                | 6.30 us: 1.44x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.18 sec: 1.44x faster                                                 |
| regex_compile            | 188 ms                                                 | 133 ms: 1.42x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.84 sec: 1.40x faster                                                 |
| django_template          | 48.2 ms                                                | 34.8 ms: 1.39x faster                                                  |
| fannkuch                 | 532 ms                                                 | 385 ms: 1.38x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                 |
| html5lib                 | 88.9 ms                                                | 65.1 ms: 1.37x faster                                                  |
| genshi_text              | 31.8 ms                                                | 23.4 ms: 1.36x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.7 ms: 1.36x faster                                                  |
| thrift                   | 1.07 ms                                                | 791 us: 1.35x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 759 ms: 1.34x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.83 ms: 1.34x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 59.2 ms: 1.34x faster                                                  |
| nqueens                  | 106 ms                                                 | 79.3 ms: 1.33x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.7 ms: 1.32x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                   |
| scimark_fft              | 466 ms                                                 | 357 ms: 1.30x faster                                                   |
| 2to3                     | 348 ms                                                 | 267 ms: 1.30x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 50.7 ms: 1.30x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 64.8 ms: 1.30x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 20.3 ms: 1.27x faster                                                  |
| sympy_sum                | 196 ms                                                 | 154 ms: 1.27x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 54.6 ms: 1.27x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                  |
| sympy_str                | 346 ms                                                 | 278 ms: 1.24x faster                                                   |
| sympy_expand             | 566 ms                                                 | 470 ms: 1.20x faster                                                   |
| dask                     | 441 ms                                                 | 366 ms: 1.20x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 828 us: 1.19x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.78 sec: 1.19x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 85.7 ms: 1.16x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                                 |
| json_loads               | 31.2 us                                                | 28.1 us: 1.11x faster                                                  |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 107 ms: 1.08x faster                                                   |
| json                     | 5.69 ms                                                | 5.29 ms: 1.08x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 159 ms: 1.06x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.91 us: 1.04x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 27.2 ms: 1.02x faster                                                  |
| pickle_list              | 5.08 us                                                | 5.04 us: 1.01x faster                                                  |
| gc_traversal             | 3.62 ms                                                | 3.60 ms: 1.01x faster                                                  |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                                   |
| async_generators         | 444 ms                                                 | 448 ms: 1.01x slower                                                   |
| asyncio_websockets       | 559 ms                                                 | 566 ms: 1.01x slower                                                   |
| regex_dna                | 227 ms                                                 | 231 ms: 1.02x slower                                                   |
| unpickle                 | 14.4 us                                                | 15.3 us: 1.06x slower                                                  |
| unpickle_list            | 5.20 us                                                | 5.53 us: 1.06x slower                                                  |
| regex_effbot             | 3.63 ms                                                | 3.92 ms: 1.08x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.08x slower                                                  |
| pickle                   | 10.7 us                                                | 11.9 us: 1.12x slower                                                  |
| pickle_dict              | 29.6 us                                                | 34.0 us: 1.15x slower                                                  |
| telco                    | 7.27 ms                                                | 8.38 ms: 1.15x slower                                                  |
| coverage                 | 79.4 ms                                                | 93.4 ms: 1.18x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.15 ms: 1.21x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240618-3.14.0a0-5b8a44e/bm-20240618-linux-x86_64-nohlson-1_investigate_compil-3.14.0a0-5b8a44e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.12x