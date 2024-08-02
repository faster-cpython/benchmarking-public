# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: 144a6fa
- commit date: 2024-05-11
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 283 ms: 1.23x faster                                                    |
| chameleon      | 9.68 ms                                                | 7.80 ms: 1.24x faster                                                   |
| docutils       | 3.30 sec                                               | 2.89 sec: 1.14x faster                                                  |
| html5lib       | 88.9 ms                                                | 69.6 ms: 1.28x faster                                                   |
| tornado_http   | 136 ms                                                 | 97.8 ms: 1.39x faster                                                   |
| Geometric mean | (ref)                                                  | 1.25x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 382 ms: 1.91x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 960 ms: 1.84x faster                                                    |
| async_tree_memoization  | 870 ms                                                 | 499 ms: 1.74x faster                                                    |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 636 ms: 1.60x faster                                                    |
| Geometric mean          | (ref)                                                  | 1.77x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 105 ms: 1.46x faster                                                    |
| float          | 117 ms                                                 | 86.7 ms: 1.35x faster                                                   |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                                    |
| Geometric mean | (ref)                                                  | 1.26x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 144 ms: 1.31x faster                                                    |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                   |
| regex_dna      | 227 ms                                                 | 217 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                  | 1.12x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 335 us: 1.45x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 243 us: 1.36x faster                                                    |
| tomli_loads          | 3.14 sec                                               | 2.34 sec: 1.34x faster                                                  |
| json_dumps           | 14.2 ms                                                | 10.8 ms: 1.31x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 65.1 ms: 1.21x faster                                                   |
| json_loads           | 31.2 us                                                | 29.1 us: 1.07x faster                                                   |
| xml_etree_generate   | 99.4 ms                                                | 93.4 ms: 1.06x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 112 ms: 1.03x faster                                                    |
| xml_etree_parse      | 168 ms                                                 | 163 ms: 1.03x faster                                                    |
| unpickle             | 14.4 us                                                | 15.2 us: 1.06x slower                                                   |
| pickle_list          | 5.08 us                                                | 5.41 us: 1.07x slower                                                   |
| unpickle_list        | 5.20 us                                                | 5.55 us: 1.07x slower                                                   |
| pickle               | 10.7 us                                                | 11.7 us: 1.10x slower                                                   |
| pickle_dict          | 29.6 us                                                | 33.9 us: 1.15x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                   |
| python_startup_no_site | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                   |
| mako            | 16.3 ms                                                | 12.7 ms: 1.28x faster                                                   |
| django_template | 48.2 ms                                                | 38.2 ms: 1.26x faster                                                   |
| genshi_xml      | 66.0 ms                                                | 55.7 ms: 1.19x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.25x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 178 us: 3.05x faster                                                    |
| generators               | 80.1 ms                                                | 31.3 ms: 2.56x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.60 ms: 2.20x faster                                                   |
| async_tree_none          | 728 ms                                                 | 382 ms: 1.91x faster                                                    |
| async_tree_io            | 1.77 sec                                               | 960 ms: 1.84x faster                                                    |
| asyncio_tcp              | 922 ms                                                 | 516 ms: 1.79x faster                                                    |
| raytrace                 | 507 ms                                                 | 289 ms: 1.76x faster                                                    |
| async_tree_memoization   | 870 ms                                                 | 499 ms: 1.74x faster                                                    |
| chaos                    | 115 ms                                                 | 66.8 ms: 1.73x faster                                                   |
| logging_silent           | 190 ns                                                 | 112 ns: 1.69x faster                                                    |
| pylint                   | 551 ms                                                 | 332 ms: 1.66x faster                                                    |
| crypto_pyaes             | 128 ms                                                 | 78.1 ms: 1.64x faster                                                   |
| richards_super           | 94.7 ms                                                | 58.5 ms: 1.62x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 636 ms: 1.60x faster                                                    |
| scimark_sor              | 220 ms                                                 | 141 ms: 1.56x faster                                                    |
| richards                 | 79.3 ms                                                | 51.2 ms: 1.55x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 76.7 ms: 1.54x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.82 ms: 1.53x faster                                                   |
| go                       | 240 ms                                                 | 158 ms: 1.52x faster                                                    |
| comprehensions           | 28.8 us                                                | 19.0 us: 1.52x faster                                                   |
| sqlglot_parse            | 2.17 ms                                                | 1.43 ms: 1.51x faster                                                   |
| sqlglot_transpile        | 2.57 ms                                                | 1.76 ms: 1.46x faster                                                   |
| nbody                    | 154 ms                                                 | 105 ms: 1.46x faster                                                    |
| pickle_pure_python       | 484 us                                                 | 335 us: 1.45x faster                                                    |
| scimark_lu               | 176 ms                                                 | 125 ms: 1.41x faster                                                    |
| spectral_norm            | 170 ms                                                 | 121 ms: 1.40x faster                                                    |
| pyflate                  | 716 ms                                                 | 512 ms: 1.40x faster                                                    |
| tornado_http             | 136 ms                                                 | 97.8 ms: 1.39x faster                                                   |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                                  |
| coroutines               | 35.1 ms                                                | 25.5 ms: 1.37x faster                                                   |
| logging_simple           | 8.30 us                                                | 6.06 us: 1.37x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 243 us: 1.36x faster                                                    |
| logging_format           | 9.09 us                                                | 6.72 us: 1.35x faster                                                   |
| float                    | 117 ms                                                 | 86.7 ms: 1.35x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 2.34 sec: 1.34x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.8 ms: 1.31x faster                                                   |
| regex_compile            | 188 ms                                                 | 144 ms: 1.31x faster                                                    |
| deepcopy_memo            | 58.5 us                                                | 45.1 us: 1.30x faster                                                   |
| genshi_text              | 31.8 ms                                                | 24.8 ms: 1.28x faster                                                   |
| mako                     | 16.3 ms                                                | 12.7 ms: 1.28x faster                                                   |
| html5lib                 | 88.9 ms                                                | 69.6 ms: 1.28x faster                                                   |
| django_template          | 48.2 ms                                                | 38.2 ms: 1.26x faster                                                   |
| pycparser                | 1.58 sec                                               | 1.26 sec: 1.25x faster                                                  |
| thrift                   | 1.07 ms                                                | 856 us: 1.25x faster                                                    |
| chameleon                | 9.68 ms                                                | 7.80 ms: 1.24x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 116 ms: 1.24x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 68.3 ms: 1.23x faster                                                   |
| 2to3                     | 348 ms                                                 | 283 ms: 1.23x faster                                                    |
| sympy_sum                | 196 ms                                                 | 161 ms: 1.22x faster                                                    |
| sympy_integrate          | 25.8 ms                                                | 21.2 ms: 1.21x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 65.1 ms: 1.21x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.74 sec: 1.21x faster                                                  |
| deepcopy                 | 479 us                                                 | 401 us: 1.19x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 853 ms: 1.19x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 58.1 ms: 1.19x faster                                                   |
| sympy_str                | 346 ms                                                 | 291 ms: 1.19x faster                                                    |
| nqueens                  | 106 ms                                                 | 89.1 ms: 1.19x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 55.7 ms: 1.19x faster                                                   |
| fannkuch                 | 532 ms                                                 | 449 ms: 1.18x faster                                                    |
| dask                     | 441 ms                                                 | 380 ms: 1.16x faster                                                    |
| deepcopy_reduce          | 4.17 us                                                | 3.60 us: 1.16x faster                                                   |
| sympy_expand             | 566 ms                                                 | 491 ms: 1.15x faster                                                    |
| pathlib                  | 20.5 ms                                                | 17.9 ms: 1.14x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.89 sec: 1.14x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 865 us: 1.14x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                   |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.72 ms: 1.13x faster                                                   |
| scimark_fft              | 466 ms                                                 | 414 ms: 1.13x faster                                                    |
| json_loads               | 31.2 us                                                | 29.1 us: 1.07x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.66 sec: 1.07x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 93.4 ms: 1.06x faster                                                   |
| regex_dna                | 227 ms                                                 | 217 ms: 1.04x faster                                                    |
| meteor_contest           | 120 ms                                                 | 115 ms: 1.04x faster                                                    |
| xml_etree_iterparse      | 115 ms                                                 | 112 ms: 1.03x faster                                                    |
| xml_etree_parse          | 168 ms                                                 | 163 ms: 1.03x faster                                                    |
| json                     | 5.69 ms                                                | 5.57 ms: 1.02x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.97 us: 1.02x faster                                                   |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                                    |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.02x slower                                                    |
| async_generators         | 444 ms                                                 | 458 ms: 1.03x slower                                                    |
| gc_traversal             | 3.62 ms                                                | 3.81 ms: 1.05x slower                                                   |
| unpickle                 | 14.4 us                                                | 15.2 us: 1.06x slower                                                   |
| pickle_list              | 5.08 us                                                | 5.41 us: 1.07x slower                                                   |
| unpickle_list            | 5.20 us                                                | 5.55 us: 1.07x slower                                                   |
| flaskblogging            | 8.58 ms                                                | 9.25 ms: 1.08x slower                                                   |
| pickle                   | 10.7 us                                                | 11.7 us: 1.10x slower                                                   |
| create_gc_cycles         | 1.62 ms                                                | 1.80 ms: 1.11x slower                                                   |
| pickle_dict              | 29.6 us                                                | 33.9 us: 1.15x slower                                                   |
| coverage                 | 79.4 ms                                                | 92.7 ms: 1.17x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 7.16 ms: 1.21x slower                                                   |
| telco                    | 7.27 ms                                                | 185 ms: 25.43x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.23x faster                                                            |

Benchmark hidden because not significant (2): regex_effbot, bench_mp_pool
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, djangocms, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240511-3.14.0a0-144a6fa/bm-20240511-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-144a6fa.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.11x