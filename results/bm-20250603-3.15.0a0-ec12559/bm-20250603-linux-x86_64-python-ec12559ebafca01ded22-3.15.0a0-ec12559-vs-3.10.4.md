# Results vs. 3.10.4

- fork: python
- ref: ec12559ebafca01ded22
- machine: linux-x86_64
- commit hash: ec12559
- commit date: 2025-06-03
- overall geometric mean: 1.319x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                                  |
| docutils       | 3.30 sec                                               | 2.58 sec: 1.27x faster                                                |
| html5lib       | 88.9 ms                                                | 61.7 ms: 1.44x faster                                                 |
| Geometric mean | (ref)                                                  | 1.36x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 601 ms: 2.95x faster                                                  |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 315 ms: 2.76x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 494 ms: 2.06x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 71.5 ms: 1.64x faster                                                 |
| nbody          | 154 ms                                                 | 98.1 ms: 1.56x faster                                                 |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.38x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                                  |
| regex_v8       | 27.8 ms                                                | 23.2 ms: 1.20x faster                                                 |
| regex_dna      | 227 ms                                                 | 194 ms: 1.17x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.22 ms: 1.13x faster                                                 |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.01 sec: 1.56x faster                                                |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 220 us: 1.50x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.9 ms: 1.30x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.18x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 99.4 ms: 1.16x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 85.9 ms: 1.16x faster                                                 |
| json_loads           | 31.2 us                                                | 27.9 us: 1.12x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.19x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 6.95 ms: 1.17x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.4 ms: 1.49x faster                                                 |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.48x faster                                                 |
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 49.5 ms: 1.33x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.27x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 601 ms: 2.95x faster                                                  |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 315 ms: 2.76x faster                                                  |
| generators               | 80.1 ms                                                | 30.5 ms: 2.63x faster                                                 |
| mdp                      | 2.85 sec                                               | 1.23 sec: 2.31x faster                                                |
| deltablue                | 7.91 ms                                                | 3.52 ms: 2.25x faster                                                 |
| go                       | 240 ms                                                 | 112 ms: 2.15x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 494 ms: 2.06x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 1.99x faster                                                 |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                                  |
| richards_super           | 94.7 ms                                                | 49.6 ms: 1.91x faster                                                 |
| chaos                    | 115 ms                                                 | 61.0 ms: 1.89x faster                                                 |
| raytrace                 | 507 ms                                                 | 270 ms: 1.87x faster                                                  |
| deepcopy                 | 479 us                                                 | 257 us: 1.87x faster                                                  |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                  |
| richards                 | 79.3 ms                                                | 43.4 ms: 1.83x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.0 us: 1.80x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 67.9 ms: 1.74x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.04 ms: 1.72x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 75.5 ms: 1.69x faster                                                 |
| pyflate                  | 716 ms                                                 | 432 ms: 1.66x faster                                                  |
| float                    | 117 ms                                                 | 71.5 ms: 1.64x faster                                                 |
| nbody                    | 154 ms                                                 | 98.1 ms: 1.56x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 2.01 sec: 1.56x faster                                                |
| spectral_norm            | 170 ms                                                 | 109 ms: 1.56x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 220 us: 1.50x faster                                                  |
| django_template          | 48.2 ms                                                | 32.4 ms: 1.49x faster                                                 |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.48x faster                                                 |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                                  |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                 |
| html5lib                 | 88.9 ms                                                | 61.7 ms: 1.44x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 59.7 ms: 1.41x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                                |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.36x faster                                                 |
| coroutines               | 35.1 ms                                                | 26.0 ms: 1.35x faster                                                 |
| logging_simple           | 8.30 us                                                | 6.17 us: 1.35x faster                                                 |
| logging_format           | 9.09 us                                                | 6.81 us: 1.34x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 49.5 ms: 1.33x faster                                                 |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 60.0 ms: 1.32x faster                                                 |
| json_dumps               | 14.2 ms                                                | 10.9 ms: 1.30x faster                                                 |
| nqueens                  | 106 ms                                                 | 81.6 ms: 1.30x faster                                                 |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                                  |
| fannkuch                 | 532 ms                                                 | 417 ms: 1.28x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.58 sec: 1.27x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.66 sec: 1.27x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.12 ms: 1.26x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 812 ms: 1.25x faster                                                  |
| sympy_expand             | 566 ms                                                 | 452 ms: 1.25x faster                                                  |
| scimark_fft              | 466 ms                                                 | 380 ms: 1.23x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 23.2 ms: 1.20x faster                                                 |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.19x faster                                                 |
| pathlib                  | 20.5 ms                                                | 17.2 ms: 1.19x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.18x faster                                                  |
| regex_dna                | 227 ms                                                 | 194 ms: 1.17x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 99.4 ms: 1.16x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 85.9 ms: 1.16x faster                                                 |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.22 ms: 1.13x faster                                                 |
| json_loads               | 31.2 us                                                | 27.9 us: 1.12x faster                                                 |
| json                     | 5.69 ms                                                | 5.15 ms: 1.10x faster                                                 |
| async_generators         | 444 ms                                                 | 416 ms: 1.07x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.05x faster                                                 |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                  |
| telco                    | 7.27 ms                                                | 7.96 ms: 1.10x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 6.95 ms: 1.17x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 5.00 ms: 1.38x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.57 ms: 1.59x slower                                                 |
| logging_silent           | 190 ns                                                 | 475 ns: 2.51x slower                                                  |
| coverage                 | 79.4 ms                                                | 426 ms: 5.36x slower                                                  |
| thrift                   | 1.07 ms                                                | 148 ms: 137.79x slower                                                |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                          |
Ignored benchmarks (24) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250603-3.15.0a0-ec12559/bm-20250603-linux-x86_64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.319x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.31x