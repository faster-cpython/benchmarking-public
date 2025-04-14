# Results vs. 3.10.4

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.480x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 251 ms: 1.39x faster                                                   |
| docutils       | 3.30 sec                                               | 2.56 sec: 1.29x faster                                                 |
| html5lib       | 88.9 ms                                                | 61.7 ms: 1.44x faster                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 602 ms: 2.94x faster                                                   |
| async_tree_none         | 728 ms                                                 | 252 ms: 2.89x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 305 ms: 2.85x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 496 ms: 2.05x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.65x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 90.8 ms: 1.69x faster                                                  |
| float          | 117 ms                                                 | 69.8 ms: 1.68x faster                                                  |
| pidigits       | 191 ms                                                 | 202 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                  | 1.39x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.50x faster                                                   |
| regex_dna      | 227 ms                                                 | 186 ms: 1.22x faster                                                   |
| regex_v8       | 27.8 ms                                                | 22.8 ms: 1.22x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.04 ms: 1.19x faster                                                  |
| Geometric mean | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.92 sec: 1.64x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 312 us: 1.55x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 58.3 ms: 1.36x faster                                                  |
| json_dumps           | 14.2 ms                                                | 12.2 ms: 1.16x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 86.0 ms: 1.16x faster                                                  |
| unpickle_list        | 5.20 us                                                | 4.52 us: 1.15x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                   |
| json_loads           | 31.2 us                                                | 28.8 us: 1.09x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 159 ms: 1.06x faster                                                   |
| pickle_list          | 5.08 us                                                | 5.34 us: 1.05x slower                                                  |
| pickle_dict          | 29.6 us                                                | 33.9 us: 1.15x slower                                                  |
| pickle               | 10.7 us                                                | 13.5 us: 1.27x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 8.11 ms: 1.37x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 30.8 ms: 1.56x faster                                                  |
| genshi_text     | 31.8 ms                                                | 20.6 ms: 1.54x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 47.8 ms: 1.38x faster                                                  |
| mako            | 16.3 ms                                                | 11.9 ms: 1.37x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 154 us: 3.54x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 602 ms: 2.94x faster                                                   |
| async_tree_none          | 728 ms                                                 | 252 ms: 2.89x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 305 ms: 2.85x faster                                                   |
| generators               | 80.1 ms                                                | 28.6 ms: 2.80x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.04 ms: 2.60x faster                                                  |
| go                       | 240 ms                                                 | 113 ms: 2.12x faster                                                   |
| logging_silent           | 190 ns                                                 | 90.4 ns: 2.10x faster                                                  |
| chaos                    | 115 ms                                                 | 55.7 ms: 2.07x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 496 ms: 2.05x faster                                                   |
| scimark_sor              | 220 ms                                                 | 108 ms: 2.04x faster                                                   |
| pylint                   | 551 ms                                                 | 272 ms: 2.03x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 28.9 us: 2.02x faster                                                  |
| richards_super           | 94.7 ms                                                | 47.7 ms: 1.99x faster                                                  |
| spectral_norm            | 170 ms                                                 | 85.8 ms: 1.98x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 469 ms: 1.96x faster                                                   |
| deepcopy                 | 479 us                                                 | 244 us: 1.96x faster                                                   |
| raytrace                 | 507 ms                                                 | 258 ms: 1.96x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 61.6 ms: 1.92x faster                                                  |
| richards                 | 79.3 ms                                                | 41.7 ms: 1.90x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.3 us: 1.76x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.00 ms: 1.73x faster                                                  |
| pyflate                  | 716 ms                                                 | 415 ms: 1.73x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 74.3 ms: 1.72x faster                                                  |
| scimark_lu               | 176 ms                                                 | 104 ms: 1.70x faster                                                   |
| nbody                    | 154 ms                                                 | 90.8 ms: 1.69x faster                                                  |
| float                    | 117 ms                                                 | 69.8 ms: 1.68x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.92 sec: 1.64x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 3.95 ms: 1.64x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.58 us: 1.62x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.2 ms: 1.58x faster                                                  |
| django_template          | 48.2 ms                                                | 30.8 ms: 1.56x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 312 us: 1.55x faster                                                   |
| scimark_fft              | 466 ms                                                 | 300 ms: 1.55x faster                                                   |
| genshi_text              | 31.8 ms                                                | 20.6 ms: 1.54x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.48 us: 1.51x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                   |
| logging_format           | 9.09 us                                                | 6.04 us: 1.50x faster                                                  |
| regex_compile            | 188 ms                                                 | 126 ms: 1.50x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 57.4 ms: 1.47x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.1 ms: 1.45x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.78 sec: 1.44x faster                                                 |
| html5lib                 | 88.9 ms                                                | 61.7 ms: 1.44x faster                                                  |
| thrift                   | 1.07 ms                                                | 751 us: 1.43x faster                                                   |
| 2to3                     | 348 ms                                                 | 251 ms: 1.39x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 47.8 ms: 1.38x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                 |
| mako                     | 16.3 ms                                                | 11.9 ms: 1.37x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 18.9 ms: 1.37x faster                                                  |
| pathlib                  | 20.5 ms                                                | 15.0 ms: 1.36x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.36x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 58.3 ms: 1.36x faster                                                  |
| sympy_sum                | 196 ms                                                 | 145 ms: 1.36x faster                                                   |
| sqlalchemy_declarative   | 172 ms                                                 | 127 ms: 1.36x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 755 ms: 1.35x faster                                                   |
| nqueens                  | 106 ms                                                 | 79.4 ms: 1.33x faster                                                  |
| sympy_str                | 346 ms                                                 | 262 ms: 1.32x faster                                                   |
| fannkuch                 | 532 ms                                                 | 410 ms: 1.30x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.56 sec: 1.29x faster                                                 |
| sympy_expand             | 566 ms                                                 | 445 ms: 1.27x faster                                                   |
| regex_dna                | 227 ms                                                 | 186 ms: 1.22x faster                                                   |
| regex_v8                 | 27.8 ms                                                | 22.8 ms: 1.22x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.04 ms: 1.19x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 839 us: 1.18x faster                                                   |
| json_dumps               | 14.2 ms                                                | 12.2 ms: 1.16x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 86.0 ms: 1.16x faster                                                  |
| async_generators         | 444 ms                                                 | 385 ms: 1.15x faster                                                   |
| unpickle_list            | 5.20 us                                                | 4.52 us: 1.15x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.67 us: 1.13x faster                                                  |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                  |
| json_loads               | 31.2 us                                                | 28.8 us: 1.09x faster                                                  |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.08x faster                                                   |
| json                     | 5.69 ms                                                | 5.26 ms: 1.08x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 159 ms: 1.06x faster                                                   |
| unpack_sequence          | 60.0 ns                                                | 57.0 ns: 1.05x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                   |
| coverage                 | 79.4 ms                                                | 80.8 ms: 1.02x slower                                                  |
| mdp                      | 2.85 sec                                               | 2.92 sec: 1.02x slower                                                 |
| telco                    | 7.27 ms                                                | 7.47 ms: 1.03x slower                                                  |
| pickle_list              | 5.08 us                                                | 5.34 us: 1.05x slower                                                  |
| pidigits                 | 191 ms                                                 | 202 ms: 1.06x slower                                                   |
| pickle_dict              | 29.6 us                                                | 33.9 us: 1.15x slower                                                  |
| pickle                   | 10.7 us                                                | 13.5 us: 1.27x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.86 ms: 1.34x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 8.11 ms: 1.37x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.55 ms: 1.58x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                           |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.480x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.34x

# Memory
- memory change: 1.28x