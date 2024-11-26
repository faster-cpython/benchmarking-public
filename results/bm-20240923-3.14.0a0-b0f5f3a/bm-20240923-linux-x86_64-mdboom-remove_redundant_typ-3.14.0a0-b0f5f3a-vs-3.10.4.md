# Results vs. 3.10.4

- fork: mdboom
- ref: remove_redundant_typ
- machine: linux-x86_64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.435x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                                  |
| docutils       | 3.30 sec                                               | 2.63 sec: 1.25x faster                                                |
| html5lib       | 88.9 ms                                                | 61.5 ms: 1.44x faster                                                 |
| tornado_http   | 136 ms                                                 | 90.4 ms: 1.51x faster                                                 |
| Geometric mean | (ref)                                                  | 1.39x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 315 ms: 2.31x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 392 ms: 2.22x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 867 ms: 2.04x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 560 ms: 1.82x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.09x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 86.7 ms: 1.77x faster                                                 |
| float          | 117 ms                                                 | 75.6 ms: 1.55x faster                                                 |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.41x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                  |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                 |
| regex_dna      | 227 ms                                                 | 225 ms: 1.01x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.89 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.06 sec: 1.52x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 84.8 ms: 1.17x faster                                                 |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 103 ms: 1.12x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| pickle_list          | 5.08 us                                                | 4.98 us: 1.02x faster                                                 |
| unpickle             | 14.4 us                                                | 15.5 us: 1.08x slower                                                 |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                                 |
| pickle_dict          | 29.6 us                                                | 32.7 us: 1.11x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.00 ms: 1.18x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                 |
| genshi_text     | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                 |
| django_template | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 48.6 ms: 1.36x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 159 us: 3.42x faster                                                  |
| generators               | 80.1 ms                                                | 28.2 ms: 2.84x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.25 ms: 2.43x faster                                                 |
| async_tree_none          | 728 ms                                                 | 315 ms: 2.31x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 392 ms: 2.22x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 867 ms: 2.04x faster                                                  |
| go                       | 240 ms                                                 | 119 ms: 2.01x faster                                                  |
| chaos                    | 115 ms                                                 | 58.6 ms: 1.97x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 29.9 us: 1.96x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 477 ms: 1.93x faster                                                  |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                                  |
| deepcopy                 | 479 us                                                 | 255 us: 1.88x faster                                                  |
| richards_super           | 94.7 ms                                                | 51.6 ms: 1.83x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 560 ms: 1.82x faster                                                  |
| logging_silent           | 190 ns                                                 | 106 ns: 1.79x faster                                                  |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.78x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 72.0 ms: 1.77x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.2 us: 1.77x faster                                                 |
| nbody                    | 154 ms                                                 | 86.7 ms: 1.77x faster                                                 |
| richards                 | 79.3 ms                                                | 45.4 ms: 1.75x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 68.2 ms: 1.73x faster                                                 |
| pylint                   | 551 ms                                                 | 320 ms: 1.72x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.19 ms: 1.68x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.64 us: 1.58x faster                                                 |
| scimark_lu               | 176 ms                                                 | 112 ms: 1.57x faster                                                  |
| float                    | 117 ms                                                 | 75.6 ms: 1.55x faster                                                 |
| coroutines               | 35.1 ms                                                | 22.8 ms: 1.54x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.06 sec: 1.52x faster                                                |
| pyflate                  | 716 ms                                                 | 473 ms: 1.51x faster                                                  |
| spectral_norm            | 170 ms                                                 | 112 ms: 1.51x faster                                                  |
| tornado_http             | 136 ms                                                 | 90.4 ms: 1.51x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.62 us: 1.48x faster                                                 |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                  |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                 |
| logging_format           | 9.09 us                                                | 6.20 us: 1.47x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                |
| html5lib                 | 88.9 ms                                                | 61.5 ms: 1.44x faster                                                 |
| genshi_text              | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.78 sec: 1.44x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 708 ms: 1.44x faster                                                  |
| django_template          | 48.2 ms                                                | 34.2 ms: 1.41x faster                                                 |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.38x faster                                                 |
| thrift                   | 1.07 ms                                                | 777 us: 1.38x faster                                                  |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 48.6 ms: 1.36x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.35x faster                                                  |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.35x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                                |
| nqueens                  | 106 ms                                                 | 79.4 ms: 1.33x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.32x faster                                                 |
| fannkuch                 | 532 ms                                                 | 404 ms: 1.32x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.95 ms: 1.31x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 53.1 ms: 1.30x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 64.8 ms: 1.30x faster                                                 |
| sympy_str                | 346 ms                                                 | 267 ms: 1.30x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                 |
| scimark_fft              | 466 ms                                                 | 370 ms: 1.26x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.63 sec: 1.25x faster                                                |
| bench_thread_pool        | 986 us                                                 | 789 us: 1.25x faster                                                  |
| sympy_expand             | 566 ms                                                 | 453 ms: 1.25x faster                                                  |
| unpack_sequence          | 60.0 ns                                                | 49.3 ns: 1.22x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 84.8 ms: 1.17x faster                                                 |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                                 |
| json                     | 5.69 ms                                                | 4.94 ms: 1.15x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 103 ms: 1.12x faster                                                  |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.69 sec: 1.06x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.05x faster                                                 |
| async_generators         | 444 ms                                                 | 430 ms: 1.03x faster                                                  |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| pickle_list              | 5.08 us                                                | 4.98 us: 1.02x faster                                                 |
| regex_dna                | 227 ms                                                 | 225 ms: 1.01x faster                                                  |
| coverage                 | 79.4 ms                                                | 83.7 ms: 1.05x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 3.83 ms: 1.06x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.72 ms: 1.06x slower                                                 |
| regex_effbot             | 3.63 ms                                                | 3.89 ms: 1.07x slower                                                 |
| unpickle                 | 14.4 us                                                | 15.5 us: 1.08x slower                                                 |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                                 |
| pickle_dict              | 29.6 us                                                | 32.7 us: 1.11x slower                                                 |
| telco                    | 7.27 ms                                                | 8.43 ms: 1.16x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.00 ms: 1.18x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                          |

Benchmark hidden because not significant (3): unpickle_list, asyncio_websockets, bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-linux-x86_64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.435x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.12x