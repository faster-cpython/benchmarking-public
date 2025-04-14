# Results vs. 3.10.4

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.272x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.54x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 296 ms: 1.18x faster                                                   |
| docutils       | 3.30 sec                                               | 2.78 sec: 1.19x faster                                                 |
| html5lib       | 88.9 ms                                                | 68.0 ms: 1.31x faster                                                  |
| Geometric mean | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 577 ms: 3.06x faster                                                   |
| async_tree_none         | 728 ms                                                 | 283 ms: 2.57x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 352 ms: 2.47x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 507 ms: 2.00x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.50x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 75.5 ms: 1.55x faster                                                  |
| nbody          | 154 ms                                                 | 134 ms: 1.14x faster                                                   |
| pidigits       | 191 ms                                                 | 181 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 27.8 ms                                                | 21.8 ms: 1.28x faster                                                  |
| regex_compile  | 188 ms                                                 | 149 ms: 1.27x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.31 ms: 1.10x faster                                                  |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 351 us: 1.38x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 2.33 sec: 1.35x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 252 us: 1.31x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 95.2 ms: 1.21x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 66.9 ms: 1.18x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                                   |
| json_dumps           | 14.2 ms                                                | 12.9 ms: 1.10x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 94.4 ms: 1.05x faster                                                  |
| pickle_list          | 5.08 us                                                | 5.13 us: 1.01x slower                                                  |
| json_loads           | 31.2 us                                                | 33.0 us: 1.06x slower                                                  |
| unpickle_list        | 5.20 us                                                | 5.85 us: 1.12x slower                                                  |
| pickle               | 10.7 us                                                | 12.3 us: 1.15x slower                                                  |
| unpickle             | 14.4 us                                                | 16.6 us: 1.16x slower                                                  |
| pickle_dict          | 29.6 us                                                | 35.0 us: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 15.5 ms: 1.07x slower                                                  |
| python_startup_no_site | 5.93 ms                                                | 10.9 ms: 1.84x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.40x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 40.1 ms: 1.20x faster                                                  |
| genshi_text     | 31.8 ms                                                | 28.5 ms: 1.12x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 59.5 ms: 1.11x faster                                                  |
| mako            | 16.3 ms                                                | 16.2 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 577 ms: 3.06x faster                                                   |
| typing_runtime_protocols | 544 us                                                 | 202 us: 2.69x faster                                                   |
| generators               | 80.1 ms                                                | 30.3 ms: 2.65x faster                                                  |
| async_tree_none          | 728 ms                                                 | 283 ms: 2.57x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 352 ms: 2.47x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.91 ms: 2.03x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 507 ms: 2.00x faster                                                   |
| pylint                   | 551 ms                                                 | 308 ms: 1.79x faster                                                   |
| asyncio_tcp              | 922 ms                                                 | 526 ms: 1.75x faster                                                   |
| go                       | 240 ms                                                 | 142 ms: 1.69x faster                                                   |
| gc_traversal             | 3.62 ms                                                | 2.17 ms: 1.67x faster                                                  |
| logging_silent           | 190 ns                                                 | 115 ns: 1.65x faster                                                   |
| chaos                    | 115 ms                                                 | 70.1 ms: 1.65x faster                                                  |
| scimark_sor              | 220 ms                                                 | 138 ms: 1.59x faster                                                   |
| deepcopy                 | 479 us                                                 | 308 us: 1.56x faster                                                   |
| float                    | 117 ms                                                 | 75.5 ms: 1.55x faster                                                  |
| raytrace                 | 507 ms                                                 | 335 ms: 1.51x faster                                                   |
| richards_super           | 94.7 ms                                                | 62.6 ms: 1.51x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 38.7 us: 1.51x faster                                                  |
| richards                 | 79.3 ms                                                | 53.4 ms: 1.49x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.47x faster                                                  |
| spectral_norm            | 170 ms                                                 | 119 ms: 1.43x faster                                                   |
| comprehensions           | 28.8 us                                                | 20.1 us: 1.43x faster                                                  |
| pyflate                  | 716 ms                                                 | 504 ms: 1.42x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 90.2 ms: 1.42x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.39x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 351 us: 1.38x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 87.2 ms: 1.35x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.33 sec: 1.35x faster                                                 |
| hexiom                   | 10.4 ms                                                | 7.76 ms: 1.34x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 63.1 ms: 1.34x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 252 us: 1.31x faster                                                   |
| html5lib                 | 88.9 ms                                                | 68.0 ms: 1.31x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 3.20 us: 1.30x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 21.8 ms: 1.28x faster                                                  |
| regex_compile            | 188 ms                                                 | 149 ms: 1.27x faster                                                   |
| asyncio_tcp_ssl          | 2.57 sec                                               | 2.03 sec: 1.26x faster                                                 |
| logging_simple           | 8.30 us                                                | 6.65 us: 1.25x faster                                                  |
| scimark_lu               | 176 ms                                                 | 144 ms: 1.22x faster                                                   |
| pprint_safe_repr         | 1.02 sec                                               | 837 ms: 1.22x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.73 sec: 1.21x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 95.2 ms: 1.21x faster                                                  |
| logging_format           | 9.09 us                                                | 7.50 us: 1.21x faster                                                  |
| thrift                   | 1.07 ms                                                | 886 us: 1.21x faster                                                   |
| django_template          | 48.2 ms                                                | 40.1 ms: 1.20x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.78 sec: 1.19x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 66.9 ms: 1.18x faster                                                  |
| pathlib                  | 20.5 ms                                                | 17.3 ms: 1.18x faster                                                  |
| 2to3                     | 348 ms                                                 | 296 ms: 1.18x faster                                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 20.3 ms: 1.15x faster                                                  |
| nbody                    | 154 ms                                                 | 134 ms: 1.14x faster                                                   |
| sympy_sum                | 196 ms                                                 | 174 ms: 1.13x faster                                                   |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 23.0 ms: 1.12x faster                                                  |
| genshi_text              | 31.8 ms                                                | 28.5 ms: 1.12x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 59.5 ms: 1.11x faster                                                  |
| scimark_fft              | 466 ms                                                 | 422 ms: 1.10x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                                  |
| json_dumps               | 14.2 ms                                                | 12.9 ms: 1.10x faster                                                  |
| sympy_str                | 346 ms                                                 | 315 ms: 1.10x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.31 ms: 1.10x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 159 ms: 1.09x faster                                                   |
| nqueens                  | 106 ms                                                 | 98.9 ms: 1.07x faster                                                  |
| sympy_expand             | 566 ms                                                 | 530 ms: 1.07x faster                                                   |
| pidigits                 | 191 ms                                                 | 181 ms: 1.05x faster                                                   |
| xml_etree_generate       | 99.4 ms                                                | 94.4 ms: 1.05x faster                                                  |
| fannkuch                 | 532 ms                                                 | 511 ms: 1.04x faster                                                   |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                                   |
| unpack_sequence          | 60.0 ns                                                | 58.9 ns: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 550 ms: 1.02x faster                                                   |
| mako                     | 16.3 ms                                                | 16.2 ms: 1.01x faster                                                  |
| json                     | 5.69 ms                                                | 5.64 ms: 1.01x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.87 sec: 1.01x slower                                                 |
| async_generators         | 444 ms                                                 | 448 ms: 1.01x slower                                                   |
| pickle_list              | 5.08 us                                                | 5.13 us: 1.01x slower                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.56 ms: 1.01x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 1.68 ms: 1.04x slower                                                  |
| json_loads               | 31.2 us                                                | 33.0 us: 1.06x slower                                                  |
| python_startup           | 14.6 ms                                                | 15.5 ms: 1.07x slower                                                  |
| meteor_contest           | 120 ms                                                 | 131 ms: 1.09x slower                                                   |
| unpickle_list            | 5.20 us                                                | 5.85 us: 1.12x slower                                                  |
| pickle                   | 10.7 us                                                | 12.3 us: 1.15x slower                                                  |
| unpickle                 | 14.4 us                                                | 16.6 us: 1.16x slower                                                  |
| pickle_dict              | 29.6 us                                                | 35.0 us: 1.18x slower                                                  |
| telco                    | 7.27 ms                                                | 9.31 ms: 1.28x slower                                                  |
| coverage                 | 79.4 ms                                                | 121 ms: 1.52x slower                                                   |
| python_startup_no_site   | 5.93 ms                                                | 10.9 ms: 1.84x slower                                                  |
| bench_thread_pool        | 986 us                                                 | 3.26 ms: 3.31x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 91.0 ms: 3.79x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.21x faster                                                           |
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250322-3.14.0a6+-bc26f95-NOGIL/bm-20250322-linux-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.272x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.54x