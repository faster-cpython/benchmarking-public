# Results vs. 3.10.4

- fork: iritkatriel
- ref: brainfart
- machine: linux-x86_64
- commit hash: 157cdcb
- commit date: 2025-04-04
- overall geometric mean: 1.477x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-linux-x86_64-iritkatriel-brainfart-3.14.0a6+-157cdcb |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 247 ms: 1.41x faster                                             |
| docutils       | 3.30 sec                                               | 2.62 sec: 1.26x faster                                           |
| html5lib       | 88.9 ms                                                | 60.3 ms: 1.47x faster                                            |
| Geometric mean | (ref)                                                  | 1.38x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-linux-x86_64-iritkatriel-brainfart-3.14.0a6+-157cdcb |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 612 ms: 2.89x faster                                             |
| async_tree_none         | 728 ms                                                 | 259 ms: 2.81x faster                                             |
| async_tree_memoization  | 870 ms                                                 | 311 ms: 2.80x faster                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 476 ms: 2.13x faster                                             |
| Geometric mean          | (ref)                                                  | 2.64x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-linux-x86_64-iritkatriel-brainfart-3.14.0a6+-157cdcb |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 117 ms                                                 | 67.2 ms: 1.74x faster                                            |
| nbody          | 154 ms                                                 | 90.1 ms: 1.70x faster                                            |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.45x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-linux-x86_64-iritkatriel-brainfart-3.14.0a6+-157cdcb |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 124 ms: 1.52x faster                                             |
| regex_v8       | 27.8 ms                                                | 23.9 ms: 1.16x faster                                            |
| regex_effbot   | 3.63 ms                                                | 3.18 ms: 1.14x faster                                            |
| regex_dna      | 227 ms                                                 | 214 ms: 1.06x faster                                             |
| Geometric mean | (ref)                                                  | 1.21x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-linux-x86_64-iritkatriel-brainfart-3.14.0a6+-157cdcb |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                           |
| pickle_pure_python   | 484 us                                                 | 311 us: 1.56x faster                                             |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                             |
| xml_etree_process    | 79.1 ms                                                | 58.5 ms: 1.35x faster                                            |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.23x faster                                            |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                             |
| xml_etree_generate   | 99.4 ms                                                | 83.9 ms: 1.18x faster                                            |
| xml_etree_iterparse  | 115 ms                                                 | 97.8 ms: 1.18x faster                                            |
| json_loads           | 31.2 us                                                | 29.7 us: 1.05x faster                                            |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-linux-x86_64-iritkatriel-brainfart-3.14.0a6+-157cdcb |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                            |
| python_startup_no_site | 5.93 ms                                                | 8.20 ms: 1.38x slower                                            |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-linux-x86_64-iritkatriel-brainfart-3.14.0a6+-157cdcb |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 20.7 ms: 1.54x faster                                            |
| django_template | 48.2 ms                                                | 31.5 ms: 1.53x faster                                            |
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                            |
| genshi_xml      | 66.0 ms                                                | 48.6 ms: 1.36x faster                                            |
| Geometric mean  | (ref)                                                  | 1.47x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-linux-x86_64-iritkatriel-brainfart-3.14.0a6+-157cdcb |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.37x faster                                             |
| async_tree_io            | 1.77 sec                                               | 612 ms: 2.89x faster                                             |
| async_tree_none          | 728 ms                                                 | 259 ms: 2.81x faster                                             |
| async_tree_memoization   | 870 ms                                                 | 311 ms: 2.80x faster                                             |
| generators               | 80.1 ms                                                | 29.4 ms: 2.72x faster                                            |
| deltablue                | 7.91 ms                                                | 3.29 ms: 2.40x faster                                            |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.34x faster                                           |
| go                       | 240 ms                                                 | 109 ms: 2.21x faster                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 476 ms: 2.13x faster                                             |
| chaos                    | 115 ms                                                 | 55.1 ms: 2.09x faster                                            |
| deepcopy_memo            | 58.5 us                                                | 28.4 us: 2.06x faster                                            |
| logging_silent           | 190 ns                                                 | 94.0 ns: 2.02x faster                                            |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                             |
| raytrace                 | 507 ms                                                 | 255 ms: 1.99x faster                                             |
| deepcopy                 | 479 us                                                 | 250 us: 1.91x faster                                             |
| richards_super           | 94.7 ms                                                | 49.6 ms: 1.91x faster                                            |
| scimark_sor              | 220 ms                                                 | 116 ms: 1.90x faster                                             |
| richards                 | 79.3 ms                                                | 42.9 ms: 1.85x faster                                            |
| scimark_monte_carlo      | 118 ms                                                 | 64.1 ms: 1.84x faster                                            |
| spectral_norm            | 170 ms                                                 | 94.5 ms: 1.80x faster                                            |
| crypto_pyaes             | 128 ms                                                 | 72.2 ms: 1.77x faster                                            |
| float                    | 117 ms                                                 | 67.2 ms: 1.74x faster                                            |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                            |
| nbody                    | 154 ms                                                 | 90.1 ms: 1.70x faster                                            |
| hexiom                   | 10.4 ms                                                | 6.13 ms: 1.69x faster                                            |
| pyflate                  | 716 ms                                                 | 441 ms: 1.63x faster                                             |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                           |
| pickle_pure_python       | 484 us                                                 | 311 us: 1.56x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                            |
| genshi_text              | 31.8 ms                                                | 20.7 ms: 1.54x faster                                            |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.54x faster                                             |
| django_template          | 48.2 ms                                                | 31.5 ms: 1.53x faster                                            |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                             |
| logging_simple           | 8.30 us                                                | 5.45 us: 1.52x faster                                            |
| regex_compile            | 188 ms                                                 | 124 ms: 1.52x faster                                             |
| logging_format           | 9.09 us                                                | 6.03 us: 1.51x faster                                            |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.49x faster                                            |
| html5lib                 | 88.9 ms                                                | 60.3 ms: 1.47x faster                                            |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                            |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                           |
| dulwich_log              | 84.3 ms                                                | 58.7 ms: 1.44x faster                                            |
| pprint_safe_repr         | 1.02 sec                                               | 713 ms: 1.43x faster                                             |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.42x faster                                           |
| 2to3                     | 348 ms                                                 | 247 ms: 1.41x faster                                             |
| scimark_fft              | 466 ms                                                 | 331 ms: 1.41x faster                                             |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                            |
| genshi_xml               | 66.0 ms                                                | 48.6 ms: 1.36x faster                                            |
| xml_etree_process        | 79.1 ms                                                | 58.5 ms: 1.35x faster                                            |
| sympy_integrate          | 25.8 ms                                                | 19.1 ms: 1.35x faster                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.79 ms: 1.35x faster                                            |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                             |
| nqueens                  | 106 ms                                                 | 80.9 ms: 1.31x faster                                            |
| fannkuch                 | 532 ms                                                 | 407 ms: 1.31x faster                                             |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.31x faster                                             |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                             |
| docutils                 | 3.30 sec                                               | 2.62 sec: 1.26x faster                                           |
| pathlib                  | 20.5 ms                                                | 16.5 ms: 1.24x faster                                            |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                             |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.23x faster                                            |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                             |
| xml_etree_generate       | 99.4 ms                                                | 83.9 ms: 1.18x faster                                            |
| xml_etree_iterparse      | 115 ms                                                 | 97.8 ms: 1.18x faster                                            |
| regex_v8                 | 27.8 ms                                                | 23.9 ms: 1.16x faster                                            |
| async_generators         | 444 ms                                                 | 388 ms: 1.14x faster                                             |
| regex_effbot             | 3.63 ms                                                | 3.18 ms: 1.14x faster                                            |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                             |
| bench_thread_pool        | 986 us                                                 | 882 us: 1.12x faster                                             |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                            |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                            |
| json                     | 5.69 ms                                                | 5.33 ms: 1.07x faster                                            |
| regex_dna                | 227 ms                                                 | 214 ms: 1.06x faster                                             |
| json_loads               | 31.2 us                                                | 29.7 us: 1.05x faster                                            |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                             |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                             |
| coverage                 | 79.4 ms                                                | 84.9 ms: 1.07x slower                                            |
| telco                    | 7.27 ms                                                | 7.84 ms: 1.08x slower                                            |
| gc_traversal             | 3.62 ms                                                | 4.75 ms: 1.31x slower                                            |
| python_startup_no_site   | 5.93 ms                                                | 8.20 ms: 1.38x slower                                            |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                            |
| bench_mp_pool            | 24.0 ms                                                | 82.1 ms: 3.42x slower                                            |
| Geometric mean           | (ref)                                                  | 1.45x faster                                                     |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250404-3.14.0a6+-157cdcb/bm-20250404-linux-x86_64-iritkatriel-brainfart-3.14.0a6+-157cdcb.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.477x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.38x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: 1.27x