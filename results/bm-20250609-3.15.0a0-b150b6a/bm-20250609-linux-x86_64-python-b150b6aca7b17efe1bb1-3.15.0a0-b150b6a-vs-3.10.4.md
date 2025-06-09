# Results vs. 3.10.4

- fork: python
- ref: b150b6aca7b17efe1bb1
- machine: linux-x86_64
- commit hash: b150b6a
- commit date: 2025-06-09
- overall geometric mean: 1.321x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                                  |
| docutils       | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                |
| html5lib       | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                 |
| Geometric mean | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 602 ms: 2.94x faster                                                  |
| async_tree_none         | 728 ms                                                 | 264 ms: 2.76x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 317 ms: 2.75x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 495 ms: 2.05x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.60x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 72.8 ms: 1.61x faster                                                 |
| nbody          | 154 ms                                                 | 102 ms: 1.50x faster                                                  |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                  |
| regex_v8       | 27.8 ms                                                | 22.0 ms: 1.26x faster                                                 |
| regex_dna      | 227 ms                                                 | 181 ms: 1.25x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.07 ms: 1.18x faster                                                 |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.03 sec: 1.55x faster                                                |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.50x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 220 us: 1.50x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                 |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 143 ms: 1.18x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 85.5 ms: 1.16x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 99.4 ms: 1.16x faster                                                 |
| json_loads           | 31.2 us                                                | 28.2 us: 1.11x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.1 ms: 1.20x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 6.90 ms: 1.16x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                 |
| django_template | 48.2 ms                                                | 32.6 ms: 1.48x faster                                                 |
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 50.2 ms: 1.32x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.29x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 602 ms: 2.94x faster                                                  |
| async_tree_none          | 728 ms                                                 | 264 ms: 2.76x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 317 ms: 2.75x faster                                                  |
| generators               | 80.1 ms                                                | 29.9 ms: 2.67x faster                                                 |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.32x faster                                                |
| deltablue                | 7.91 ms                                                | 3.51 ms: 2.25x faster                                                 |
| go                       | 240 ms                                                 | 112 ms: 2.15x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 495 ms: 2.05x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.1 us: 2.01x faster                                                 |
| pylint                   | 551 ms                                                 | 279 ms: 1.97x faster                                                  |
| richards_super           | 94.7 ms                                                | 49.8 ms: 1.90x faster                                                 |
| deepcopy                 | 479 us                                                 | 255 us: 1.88x faster                                                  |
| chaos                    | 115 ms                                                 | 61.9 ms: 1.87x faster                                                 |
| raytrace                 | 507 ms                                                 | 272 ms: 1.87x faster                                                  |
| richards                 | 79.3 ms                                                | 43.6 ms: 1.82x faster                                                 |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.2 us: 1.78x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 68.6 ms: 1.72x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.08 ms: 1.71x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 76.1 ms: 1.68x faster                                                 |
| pyflate                  | 716 ms                                                 | 433 ms: 1.65x faster                                                  |
| float                    | 117 ms                                                 | 72.8 ms: 1.61x faster                                                 |
| spectral_norm            | 170 ms                                                 | 109 ms: 1.56x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.03 sec: 1.55x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.77 us: 1.51x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.50x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 220 us: 1.50x faster                                                  |
| nbody                    | 154 ms                                                 | 102 ms: 1.50x faster                                                  |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                 |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                  |
| django_template          | 48.2 ms                                                | 32.6 ms: 1.48x faster                                                 |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                 |
| html5lib                 | 88.9 ms                                                | 62.0 ms: 1.43x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.42x faster                                                |
| dulwich_log              | 84.3 ms                                                | 59.9 ms: 1.41x faster                                                 |
| logging_simple           | 8.30 us                                                | 6.05 us: 1.37x faster                                                 |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                                  |
| coroutines               | 35.1 ms                                                | 25.8 ms: 1.36x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.36x faster                                                 |
| logging_format           | 9.09 us                                                | 6.84 us: 1.33x faster                                                 |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 50.2 ms: 1.32x faster                                                 |
| nqueens                  | 106 ms                                                 | 81.1 ms: 1.31x faster                                                 |
| sympy_str                | 346 ms                                                 | 266 ms: 1.30x faster                                                  |
| fannkuch                 | 532 ms                                                 | 413 ms: 1.29x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.64 sec: 1.28x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.04 ms: 1.28x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 797 ms: 1.28x faster                                                  |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 22.0 ms: 1.26x faster                                                 |
| sympy_expand             | 566 ms                                                 | 451 ms: 1.25x faster                                                  |
| scimark_fft              | 466 ms                                                 | 373 ms: 1.25x faster                                                  |
| regex_dna                | 227 ms                                                 | 181 ms: 1.25x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.22x faster                                                 |
| python_startup           | 14.6 ms                                                | 12.1 ms: 1.20x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 3.07 ms: 1.18x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 143 ms: 1.18x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 85.5 ms: 1.16x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 99.4 ms: 1.16x faster                                                 |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                  |
| json_loads               | 31.2 us                                                | 28.2 us: 1.11x faster                                                 |
| async_generators         | 444 ms                                                 | 406 ms: 1.09x faster                                                  |
| json                     | 5.69 ms                                                | 5.23 ms: 1.09x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.85 us: 1.06x faster                                                 |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                  |
| telco                    | 7.27 ms                                                | 7.95 ms: 1.09x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 6.90 ms: 1.16x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 5.00 ms: 1.38x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                                 |
| logging_silent           | 190 ns                                                 | 475 ns: 2.50x slower                                                  |
| coverage                 | 79.4 ms                                                | 426 ms: 5.36x slower                                                  |
| thrift                   | 1.07 ms                                                | 148 ms: 137.75x slower                                                |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |
Ignored benchmarks (24) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250609-3.15.0a0-b150b6a/bm-20250609-linux-x86_64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.321x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.31x