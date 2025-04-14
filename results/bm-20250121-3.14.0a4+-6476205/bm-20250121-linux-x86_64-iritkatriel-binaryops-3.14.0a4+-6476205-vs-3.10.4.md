# Results vs. 3.10.4

- fork: iritkatriel
- ref: binaryops
- machine: linux-x86_64
- commit hash: 6476205
- commit date: 2025-01-21
- overall geometric mean: 1.452x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-6476205 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                             |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                           |
| html5lib       | 88.9 ms                                                | 59.7 ms: 1.49x faster                                            |
| Geometric mean | (ref)                                                  | 1.37x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-6476205 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 600 ms: 2.95x faster                                             |
| async_tree_none         | 728 ms                                                 | 257 ms: 2.83x faster                                             |
| async_tree_memoization  | 870 ms                                                 | 327 ms: 2.66x faster                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 481 ms: 2.11x faster                                             |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-6476205 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.6 ms: 1.66x faster                                            |
| nbody          | 154 ms                                                 | 94.1 ms: 1.63x faster                                            |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.41x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-6476205 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                             |
| regex_effbot   | 3.63 ms                                                | 3.15 ms: 1.15x faster                                            |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                            |
| regex_dna      | 227 ms                                                 | 210 ms: 1.08x faster                                             |
| Geometric mean | (ref)                                                  | 1.20x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-6476205 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.59x faster                                           |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                             |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.52x faster                                             |
| xml_etree_process    | 79.1 ms                                                | 59.4 ms: 1.33x faster                                            |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.22x faster                                             |
| xml_etree_iterparse  | 115 ms                                                 | 96.9 ms: 1.19x faster                                            |
| xml_etree_generate   | 99.4 ms                                                | 84.2 ms: 1.18x faster                                            |
| json_dumps           | 14.2 ms                                                | 12.1 ms: 1.18x faster                                            |
| json_loads           | 31.2 us                                                | 29.6 us: 1.05x faster                                            |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-6476205 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                            |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                            |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-6476205 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.1 ms: 1.50x faster                                            |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                            |
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                            |
| genshi_xml      | 66.0 ms                                                | 48.1 ms: 1.37x faster                                            |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-6476205 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.39x faster                                             |
| async_tree_io            | 1.77 sec                                               | 600 ms: 2.95x faster                                             |
| generators               | 80.1 ms                                                | 27.3 ms: 2.94x faster                                            |
| async_tree_none          | 728 ms                                                 | 257 ms: 2.83x faster                                             |
| async_tree_memoization   | 870 ms                                                 | 327 ms: 2.66x faster                                             |
| deltablue                | 7.91 ms                                                | 3.20 ms: 2.48x faster                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 481 ms: 2.11x faster                                             |
| go                       | 240 ms                                                 | 117 ms: 2.04x faster                                             |
| pylint                   | 551 ms                                                 | 275 ms: 2.01x faster                                             |
| chaos                    | 115 ms                                                 | 57.8 ms: 2.00x faster                                            |
| raytrace                 | 507 ms                                                 | 269 ms: 1.88x faster                                             |
| deepcopy_memo            | 58.5 us                                                | 31.2 us: 1.88x faster                                            |
| richards_super           | 94.7 ms                                                | 50.6 ms: 1.87x faster                                            |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                             |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                             |
| richards                 | 79.3 ms                                                | 44.1 ms: 1.80x faster                                            |
| crypto_pyaes             | 128 ms                                                 | 71.3 ms: 1.79x faster                                            |
| logging_silent           | 190 ns                                                 | 107 ns: 1.77x faster                                             |
| scimark_monte_carlo      | 118 ms                                                 | 67.3 ms: 1.76x faster                                            |
| spectral_norm            | 170 ms                                                 | 97.0 ms: 1.75x faster                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.25 ms: 1.73x faster                                            |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                            |
| hexiom                   | 10.4 ms                                                | 6.25 ms: 1.66x faster                                            |
| float                    | 117 ms                                                 | 70.6 ms: 1.66x faster                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.56 ms: 1.65x faster                                            |
| nbody                    | 154 ms                                                 | 94.1 ms: 1.63x faster                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.61 us: 1.60x faster                                            |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.59x faster                                           |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                             |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                             |
| pyflate                  | 716 ms                                                 | 470 ms: 1.52x faster                                             |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.52x faster                                             |
| logging_simple           | 8.30 us                                                | 5.49 us: 1.51x faster                                            |
| logging_format           | 9.09 us                                                | 6.04 us: 1.50x faster                                            |
| django_template          | 48.2 ms                                                | 32.1 ms: 1.50x faster                                            |
| html5lib                 | 88.9 ms                                                | 59.7 ms: 1.49x faster                                            |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                             |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                            |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.48x faster                                            |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                            |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.4 ms: 1.42x faster                                            |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                           |
| pprint_safe_repr         | 1.02 sec                                               | 722 ms: 1.41x faster                                             |
| thrift                   | 1.07 ms                                                | 761 us: 1.41x faster                                             |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.70 ms: 1.38x faster                                            |
| genshi_xml               | 66.0 ms                                                | 48.1 ms: 1.37x faster                                            |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                             |
| sqlglot_normalize        | 143 ms                                                 | 105 ms: 1.36x faster                                             |
| scimark_fft              | 466 ms                                                 | 346 ms: 1.35x faster                                             |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                             |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.33x faster                                             |
| xml_etree_process        | 79.1 ms                                                | 59.4 ms: 1.33x faster                                            |
| nqueens                  | 106 ms                                                 | 80.2 ms: 1.32x faster                                            |
| dulwich_log              | 84.3 ms                                                | 64.0 ms: 1.32x faster                                            |
| sqlglot_optimize         | 69.2 ms                                                | 52.6 ms: 1.31x faster                                            |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                            |
| sympy_str                | 346 ms                                                 | 267 ms: 1.30x faster                                             |
| fannkuch                 | 532 ms                                                 | 413 ms: 1.29x faster                                             |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                            |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                           |
| sympy_expand             | 566 ms                                                 | 451 ms: 1.25x faster                                             |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.22x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 96.9 ms: 1.19x faster                                            |
| xml_etree_generate       | 99.4 ms                                                | 84.2 ms: 1.18x faster                                            |
| json_dumps               | 14.2 ms                                                | 12.1 ms: 1.18x faster                                            |
| regex_effbot             | 3.63 ms                                                | 3.15 ms: 1.15x faster                                            |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.14x faster                                           |
| async_generators         | 444 ms                                                 | 389 ms: 1.14x faster                                             |
| bench_thread_pool        | 986 us                                                 | 866 us: 1.14x faster                                             |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                            |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                             |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                            |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                            |
| regex_dna                | 227 ms                                                 | 210 ms: 1.08x faster                                             |
| json                     | 5.69 ms                                                | 5.27 ms: 1.08x faster                                            |
| json_loads               | 31.2 us                                                | 29.6 us: 1.05x faster                                            |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                             |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                             |
| telco                    | 7.27 ms                                                | 7.97 ms: 1.10x slower                                            |
| coverage                 | 79.4 ms                                                | 90.7 ms: 1.14x slower                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                            |
| gc_traversal             | 3.62 ms                                                | 4.58 ms: 1.26x slower                                            |
| create_gc_cycles         | 1.62 ms                                                | 2.44 ms: 1.51x slower                                            |
| bench_mp_pool            | 24.0 ms                                                | 81.5 ms: 3.39x slower                                            |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                     |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250121-3.14.0a4+-6476205/bm-20250121-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-6476205.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.452x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.26x