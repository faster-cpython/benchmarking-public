# Results vs. 3.10.4

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.250x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 292 ms: 1.19x faster                                                  |
| docutils       | 3.30 sec                                               | 2.85 sec: 1.16x faster                                                |
| html5lib       | 88.9 ms                                                | 64.8 ms: 1.37x faster                                                 |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 663 ms: 2.67x faster                                                  |
| async_tree_none         | 728 ms                                                 | 289 ms: 2.52x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 347 ms: 2.51x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 602 ms: 1.69x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.31x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 75.3 ms: 1.56x faster                                                 |
| nbody          | 154 ms                                                 | 106 ms: 1.45x faster                                                  |
| pidigits       | 191 ms                                                 | 205 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 144 ms: 1.31x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 2.93 ms: 1.24x faster                                                 |
| regex_dna      | 227 ms                                                 | 197 ms: 1.15x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                 |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.22 sec: 1.41x faster                                                |
| pickle_pure_python   | 484 us                                                 | 374 us: 1.30x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 259 us: 1.28x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 74.4 ms: 1.06x faster                                                 |
| json_dumps           | 14.2 ms                                                | 13.4 ms: 1.05x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 162 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 112 ms: 1.03x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 108 ms: 1.09x slower                                                  |
| json_loads           | 31.2 us                                                | 34.0 us: 1.09x slower                                                 |
| unpickle_list        | 5.20 us                                                | 5.68 us: 1.09x slower                                                 |
| pickle_list          | 5.08 us                                                | 6.06 us: 1.19x slower                                                 |
| pickle_dict          | 29.6 us                                                | 38.2 us: 1.29x slower                                                 |
| unpickle             | 14.4 us                                                | 19.1 us: 1.33x slower                                                 |
| pickle               | 10.7 us                                                | 15.1 us: 1.42x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                          |

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
| genshi_text     | 31.8 ms                                                | 25.7 ms: 1.24x faster                                                 |
| mako            | 16.3 ms                                                | 13.6 ms: 1.20x faster                                                 |
| django_template | 48.2 ms                                                | 40.8 ms: 1.18x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 57.2 ms: 1.16x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.19x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 198 us: 2.75x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 663 ms: 2.67x faster                                                  |
| async_tree_none          | 728 ms                                                 | 289 ms: 2.52x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 347 ms: 2.51x faster                                                  |
| generators               | 80.1 ms                                                | 33.0 ms: 2.43x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.86 ms: 2.05x faster                                                 |
| go                       | 240 ms                                                 | 119 ms: 2.02x faster                                                  |
| mdp                      | 2.85 sec                                               | 1.47 sec: 1.94x faster                                                |
| asyncio_tcp              | 922 ms                                                 | 488 ms: 1.89x faster                                                  |
| pylint                   | 551 ms                                                 | 311 ms: 1.77x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 34.1 us: 1.71x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 602 ms: 1.69x faster                                                  |
| chaos                    | 115 ms                                                 | 68.8 ms: 1.68x faster                                                 |
| scimark_sor              | 220 ms                                                 | 134 ms: 1.64x faster                                                  |
| raytrace                 | 507 ms                                                 | 320 ms: 1.58x faster                                                  |
| djangocms                | 38.4 us                                                | 24.4 us: 1.58x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.65 ms: 1.56x faster                                                 |
| float                    | 117 ms                                                 | 75.3 ms: 1.56x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 76.4 ms: 1.55x faster                                                 |
| pyflate                  | 716 ms                                                 | 465 ms: 1.54x faster                                                  |
| richards_super           | 94.7 ms                                                | 62.2 ms: 1.52x faster                                                 |
| deepcopy                 | 479 us                                                 | 315 us: 1.52x faster                                                  |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.50x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 85.6 ms: 1.49x faster                                                 |
| comprehensions           | 28.8 us                                                | 19.3 us: 1.49x faster                                                 |
| richards                 | 79.3 ms                                                | 54.3 ms: 1.46x faster                                                 |
| nbody                    | 154 ms                                                 | 106 ms: 1.45x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                |
| tomli_loads              | 3.14 sec                                               | 2.22 sec: 1.41x faster                                                |
| html5lib                 | 88.9 ms                                                | 64.8 ms: 1.37x faster                                                 |
| scimark_lu               | 176 ms                                                 | 133 ms: 1.33x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 63.8 ms: 1.32x faster                                                 |
| regex_compile            | 188 ms                                                 | 144 ms: 1.31x faster                                                  |
| coroutines               | 35.1 ms                                                | 26.8 ms: 1.31x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 374 us: 1.30x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 259 us: 1.28x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 3.32 us: 1.25x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.26 sec: 1.25x faster                                                |
| regex_effbot             | 3.63 ms                                                | 2.93 ms: 1.24x faster                                                 |
| genshi_text              | 31.8 ms                                                | 25.7 ms: 1.24x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 20.9 ms: 1.23x faster                                                 |
| mako                     | 16.3 ms                                                | 13.6 ms: 1.20x faster                                                 |
| 2to3                     | 348 ms                                                 | 292 ms: 1.19x faster                                                  |
| sympy_sum                | 196 ms                                                 | 166 ms: 1.18x faster                                                  |
| django_template          | 48.2 ms                                                | 40.8 ms: 1.18x faster                                                 |
| scimark_fft              | 466 ms                                                 | 403 ms: 1.16x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.85 sec: 1.16x faster                                                |
| genshi_xml               | 66.0 ms                                                | 57.2 ms: 1.16x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.61 ms: 1.15x faster                                                 |
| regex_dna                | 227 ms                                                 | 197 ms: 1.15x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                 |
| unpack_sequence          | 60.0 ns                                                | 53.0 ns: 1.13x faster                                                 |
| sympy_str                | 346 ms                                                 | 308 ms: 1.12x faster                                                  |
| thrift                   | 1.07 ms                                                | 956 us: 1.12x faster                                                  |
| logging_simple           | 8.30 us                                                | 7.47 us: 1.11x faster                                                 |
| pathlib                  | 20.5 ms                                                | 18.4 ms: 1.11x faster                                                 |
| fannkuch                 | 532 ms                                                 | 479 ms: 1.11x faster                                                  |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                 |
| logging_format           | 9.09 us                                                | 8.43 us: 1.08x faster                                                 |
| nqueens                  | 106 ms                                                 | 98.2 ms: 1.08x faster                                                 |
| async_generators         | 444 ms                                                 | 413 ms: 1.07x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 74.4 ms: 1.06x faster                                                 |
| json_dumps               | 14.2 ms                                                | 13.4 ms: 1.05x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 2.01 sec: 1.05x faster                                                |
| sympy_expand             | 566 ms                                                 | 541 ms: 1.05x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 162 ms: 1.04x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 112 ms: 1.03x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 958 us: 1.03x faster                                                  |
| meteor_contest           | 120 ms                                                 | 116 ms: 1.03x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 993 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 3.18 us: 1.05x slower                                                 |
| json                     | 5.69 ms                                                | 6.08 ms: 1.07x slower                                                 |
| pidigits                 | 191 ms                                                 | 205 ms: 1.07x slower                                                  |
| xml_etree_generate       | 99.4 ms                                                | 108 ms: 1.09x slower                                                  |
| json_loads               | 31.2 us                                                | 34.0 us: 1.09x slower                                                 |
| unpickle_list            | 5.20 us                                                | 5.68 us: 1.09x slower                                                 |
| pickle_list              | 5.08 us                                                | 6.06 us: 1.19x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.40 ms: 1.25x slower                                                 |
| coverage                 | 79.4 ms                                                | 102 ms: 1.28x slower                                                  |
| pickle_dict              | 29.6 us                                                | 38.2 us: 1.29x slower                                                 |
| telco                    | 7.27 ms                                                | 9.52 ms: 1.31x slower                                                 |
| unpickle                 | 14.4 us                                                | 19.1 us: 1.33x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 5.14 ms: 1.42x slower                                                 |
| pickle                   | 10.7 us                                                | 15.1 us: 1.42x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.63 ms: 1.63x slower                                                 |
| logging_silent           | 190 ns                                                 | 623 ns: 3.28x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 105 ms: 4.39x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.20x faster                                                          |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.250x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: 1.31x