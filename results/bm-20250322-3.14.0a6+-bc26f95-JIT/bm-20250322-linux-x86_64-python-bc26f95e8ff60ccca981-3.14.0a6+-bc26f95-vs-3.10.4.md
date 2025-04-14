# Results vs. 3.10.4

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.440x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 264 ms: 1.32x faster                                                   |
| docutils       | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                 |
| html5lib       | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                  |
| Geometric mean | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 615 ms: 2.88x faster                                                   |
| async_tree_none         | 728 ms                                                 | 260 ms: 2.81x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.77x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 489 ms: 2.08x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 65.1 ms: 1.80x faster                                                  |
| nbody          | 154 ms                                                 | 88.1 ms: 1.74x faster                                                  |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                  | 1.48x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                   |
| regex_v8       | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.55 ms: 1.02x faster                                                  |
| regex_dna      | 227 ms                                                 | 227 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.55x faster                                                   |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.52x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 56.6 ms: 1.40x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 79.9 ms: 1.24x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 97.3 ms: 1.19x faster                                                  |
| json_loads           | 31.2 us                                                | 29.7 us: 1.05x faster                                                  |
| unpickle             | 14.4 us                                                | 14.6 us: 1.02x slower                                                  |
| pickle_list          | 5.08 us                                                | 5.24 us: 1.03x slower                                                  |
| unpickle_list        | 5.20 us                                                | 5.56 us: 1.07x slower                                                  |
| pickle_dict          | 29.6 us                                                | 35.9 us: 1.21x slower                                                  |
| pickle               | 10.7 us                                                | 13.0 us: 1.22x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 8.15 ms: 1.37x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                  |
| django_template | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                  |
| mako            | 16.3 ms                                                | 11.0 ms: 1.48x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 49.7 ms: 1.33x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.21x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 615 ms: 2.88x faster                                                   |
| generators               | 80.1 ms                                                | 28.2 ms: 2.84x faster                                                  |
| async_tree_none          | 728 ms                                                 | 260 ms: 2.81x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.77x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.05 ms: 2.60x faster                                                  |
| richards_super           | 94.7 ms                                                | 41.3 ms: 2.29x faster                                                  |
| richards                 | 79.3 ms                                                | 36.4 ms: 2.18x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 489 ms: 2.08x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 28.9 us: 2.02x faster                                                  |
| pylint                   | 551 ms                                                 | 281 ms: 1.96x faster                                                   |
| logging_silent           | 190 ns                                                 | 97.0 ns: 1.96x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 477 ms: 1.93x faster                                                   |
| chaos                    | 115 ms                                                 | 60.3 ms: 1.91x faster                                                  |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                   |
| go                       | 240 ms                                                 | 129 ms: 1.86x faster                                                   |
| deepcopy                 | 479 us                                                 | 261 us: 1.83x faster                                                   |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                   |
| float                    | 117 ms                                                 | 65.1 ms: 1.80x faster                                                  |
| nbody                    | 154 ms                                                 | 88.1 ms: 1.74x faster                                                  |
| spectral_norm            | 170 ms                                                 | 98.8 ms: 1.72x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 68.9 ms: 1.72x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.88 sec: 1.67x faster                                                 |
| pyflate                  | 716 ms                                                 | 434 ms: 1.65x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 79.9 ms: 1.60x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.55x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                                  |
| comprehensions           | 28.8 us                                                | 19.0 us: 1.52x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.52x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.90 ms: 1.51x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                  |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                   |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.50x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                                  |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.48x faster                                                  |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                   |
| logging_format           | 9.09 us                                                | 6.14 us: 1.48x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.7 ms: 1.48x faster                                                  |
| scimark_fft              | 466 ms                                                 | 317 ms: 1.47x faster                                                   |
| html5lib                 | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 59.9 ms: 1.41x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 56.6 ms: 1.40x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.71 ms: 1.37x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.1 ms: 1.37x faster                                                  |
| thrift                   | 1.07 ms                                                | 786 us: 1.36x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.36x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 764 ms: 1.33x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 49.7 ms: 1.33x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.33x faster                                                 |
| 2to3                     | 348 ms                                                 | 264 ms: 1.32x faster                                                   |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.29x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 20.1 ms: 1.29x faster                                                  |
| fannkuch                 | 532 ms                                                 | 415 ms: 1.28x faster                                                   |
| nqueens                  | 106 ms                                                 | 84.1 ms: 1.26x faster                                                  |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 79.9 ms: 1.24x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.70 sec: 1.22x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| sympy_expand             | 566 ms                                                 | 475 ms: 1.19x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 97.3 ms: 1.19x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.46 sec: 1.16x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 24.2 ms: 1.15x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.70 us: 1.12x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 880 us: 1.12x faster                                                   |
| python_startup           | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                  |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                                   |
| json                     | 5.69 ms                                                | 5.27 ms: 1.08x faster                                                  |
| async_generators         | 444 ms                                                 | 418 ms: 1.06x faster                                                   |
| json_loads               | 31.2 us                                                | 29.7 us: 1.05x faster                                                  |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.55 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                   |
| regex_dna                | 227 ms                                                 | 227 ms: 1.00x slower                                                   |
| unpickle                 | 14.4 us                                                | 14.6 us: 1.02x slower                                                  |
| pickle_list              | 5.08 us                                                | 5.24 us: 1.03x slower                                                  |
| unpickle_list            | 5.20 us                                                | 5.56 us: 1.07x slower                                                  |
| coverage                 | 79.4 ms                                                | 87.0 ms: 1.09x slower                                                  |
| telco                    | 7.27 ms                                                | 8.06 ms: 1.11x slower                                                  |
| pickle_dict              | 29.6 us                                                | 35.9 us: 1.21x slower                                                  |
| pickle                   | 10.7 us                                                | 13.0 us: 1.22x slower                                                  |
| unpack_sequence          | 60.0 ns                                                | 73.4 ns: 1.22x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.64 ms: 1.28x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 8.15 ms: 1.37x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 82.5 ms: 3.44x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                           |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.440x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.30x