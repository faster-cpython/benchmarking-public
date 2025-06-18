# Results vs. 3.10.4

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.261x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 299 ms: 1.16x faster                                                  |
| docutils       | 3.30 sec                                               | 2.93 sec: 1.13x faster                                                |
| html5lib       | 88.9 ms                                                | 66.7 ms: 1.33x faster                                                 |
| Geometric mean | (ref)                                                  | 1.20x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 662 ms: 2.67x faster                                                  |
| async_tree_none         | 728 ms                                                 | 290 ms: 2.51x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 348 ms: 2.50x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 597 ms: 1.70x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.31x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.8 ms: 1.68x faster                                                 |
| nbody          | 154 ms                                                 | 97.8 ms: 1.57x faster                                                 |
| pidigits       | 191 ms                                                 | 207 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.34x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 145 ms: 1.30x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.06 ms: 1.19x faster                                                 |
| regex_dna      | 227 ms                                                 | 198 ms: 1.15x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.12x faster                                                 |
| Geometric mean | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                |
| unpickle_pure_python | 331 us                                                 | 234 us: 1.41x faster                                                  |
| pickle_pure_python   | 484 us                                                 | 378 us: 1.28x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 68.6 ms: 1.15x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 159 ms: 1.05x faster                                                  |
| json_dumps           | 14.2 ms                                                | 13.6 ms: 1.04x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 111 ms: 1.04x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 101 ms: 1.02x slower                                                  |
| json_loads           | 31.2 us                                                | 33.5 us: 1.07x slower                                                 |
| unpickle_list        | 5.20 us                                                | 5.93 us: 1.14x slower                                                 |
| pickle_list          | 5.08 us                                                | 5.90 us: 1.16x slower                                                 |
| pickle_dict          | 29.6 us                                                | 38.0 us: 1.28x slower                                                 |
| unpickle             | 14.4 us                                                | 18.8 us: 1.31x slower                                                 |
| pickle               | 10.7 us                                                | 14.9 us: 1.39x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.40 ms: 1.25x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 25.8 ms: 1.24x faster                                                 |
| mako            | 16.3 ms                                                | 13.3 ms: 1.23x faster                                                 |
| django_template | 48.2 ms                                                | 40.9 ms: 1.18x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 58.7 ms: 1.13x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.19x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 662 ms: 2.67x faster                                                  |
| typing_runtime_protocols | 544 us                                                 | 205 us: 2.66x faster                                                  |
| async_tree_none          | 728 ms                                                 | 290 ms: 2.51x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 348 ms: 2.50x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.44 ms: 2.30x faster                                                 |
| generators               | 80.1 ms                                                | 35.4 ms: 2.26x faster                                                 |
| richards_super           | 94.7 ms                                                | 45.9 ms: 2.07x faster                                                 |
| richards                 | 79.3 ms                                                | 39.1 ms: 2.02x faster                                                 |
| mdp                      | 2.85 sec                                               | 1.49 sec: 1.91x faster                                                |
| go                       | 240 ms                                                 | 129 ms: 1.86x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 496 ms: 1.86x faster                                                  |
| pylint                   | 551 ms                                                 | 314 ms: 1.75x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 597 ms: 1.70x faster                                                  |
| float                    | 117 ms                                                 | 69.8 ms: 1.68x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 35.1 us: 1.67x faster                                                 |
| chaos                    | 115 ms                                                 | 69.9 ms: 1.65x faster                                                 |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                                  |
| scimark_sor              | 220 ms                                                 | 136 ms: 1.61x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 73.5 ms: 1.61x faster                                                 |
| raytrace                 | 507 ms                                                 | 321 ms: 1.58x faster                                                  |
| nbody                    | 154 ms                                                 | 97.8 ms: 1.57x faster                                                 |
| pyflate                  | 716 ms                                                 | 458 ms: 1.56x faster                                                  |
| djangocms                | 38.4 us                                                | 24.8 us: 1.55x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 2.08 sec: 1.51x faster                                                |
| deepcopy                 | 479 us                                                 | 318 us: 1.51x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.94 ms: 1.50x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 85.9 ms: 1.49x faster                                                 |
| comprehensions           | 28.8 us                                                | 20.0 us: 1.44x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 234 us: 1.41x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.82 sec: 1.41x faster                                                |
| scimark_fft              | 466 ms                                                 | 341 ms: 1.37x faster                                                  |
| html5lib                 | 88.9 ms                                                | 66.7 ms: 1.33x faster                                                 |
| regex_compile            | 188 ms                                                 | 145 ms: 1.30x faster                                                  |
| scimark_lu               | 176 ms                                                 | 136 ms: 1.29x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 65.5 ms: 1.29x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 378 us: 1.28x faster                                                  |
| coroutines               | 35.1 ms                                                | 27.6 ms: 1.27x faster                                                 |
| genshi_text              | 31.8 ms                                                | 25.8 ms: 1.24x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.28 sec: 1.23x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 3.39 us: 1.23x faster                                                 |
| mako                     | 16.3 ms                                                | 13.3 ms: 1.23x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.38 ms: 1.20x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 21.6 ms: 1.20x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.06 ms: 1.19x faster                                                 |
| django_template          | 48.2 ms                                                | 40.9 ms: 1.18x faster                                                 |
| 2to3                     | 348 ms                                                 | 299 ms: 1.16x faster                                                  |
| sympy_sum                | 196 ms                                                 | 170 ms: 1.16x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 68.6 ms: 1.15x faster                                                 |
| regex_dna                | 227 ms                                                 | 198 ms: 1.15x faster                                                  |
| fannkuch                 | 532 ms                                                 | 465 ms: 1.14x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.93 sec: 1.13x faster                                                |
| genshi_xml               | 66.0 ms                                                | 58.7 ms: 1.13x faster                                                 |
| pathlib                  | 20.5 ms                                                | 18.2 ms: 1.12x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.12x faster                                                 |
| thrift                   | 1.07 ms                                                | 961 us: 1.12x faster                                                  |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                 |
| sympy_str                | 346 ms                                                 | 317 ms: 1.09x faster                                                  |
| logging_simple           | 8.30 us                                                | 7.66 us: 1.08x faster                                                 |
| logging_format           | 9.09 us                                                | 8.58 us: 1.06x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 159 ms: 1.05x faster                                                  |
| json_dumps               | 14.2 ms                                                | 13.6 ms: 1.04x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 111 ms: 1.04x faster                                                  |
| nqueens                  | 106 ms                                                 | 102 ms: 1.04x faster                                                  |
| meteor_contest           | 120 ms                                                 | 116 ms: 1.04x faster                                                  |
| sympy_expand             | 566 ms                                                 | 552 ms: 1.03x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 966 us: 1.02x faster                                                  |
| async_generators         | 444 ms                                                 | 438 ms: 1.01x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 3.05 us: 1.01x slower                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 1.03 sec: 1.01x slower                                                |
| xml_etree_generate       | 99.4 ms                                                | 101 ms: 1.02x slower                                                  |
| json                     | 5.69 ms                                                | 6.09 ms: 1.07x slower                                                 |
| json_loads               | 31.2 us                                                | 33.5 us: 1.07x slower                                                 |
| pidigits                 | 191 ms                                                 | 207 ms: 1.09x slower                                                  |
| unpickle_list            | 5.20 us                                                | 5.93 us: 1.14x slower                                                 |
| pickle_list              | 5.08 us                                                | 5.90 us: 1.16x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.40 ms: 1.25x slower                                                 |
| unpack_sequence          | 60.0 ns                                                | 76.8 ns: 1.28x slower                                                 |
| pickle_dict              | 29.6 us                                                | 38.0 us: 1.28x slower                                                 |
| coverage                 | 79.4 ms                                                | 103 ms: 1.29x slower                                                  |
| unpickle                 | 14.4 us                                                | 18.8 us: 1.31x slower                                                 |
| telco                    | 7.27 ms                                                | 9.58 ms: 1.32x slower                                                 |
| pickle                   | 10.7 us                                                | 14.9 us: 1.39x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 5.19 ms: 1.43x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.64 ms: 1.63x slower                                                 |
| logging_silent           | 190 ns                                                 | 633 ns: 3.34x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 105 ms: 4.37x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (1): pprint_pformat
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.261x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: 1.33x