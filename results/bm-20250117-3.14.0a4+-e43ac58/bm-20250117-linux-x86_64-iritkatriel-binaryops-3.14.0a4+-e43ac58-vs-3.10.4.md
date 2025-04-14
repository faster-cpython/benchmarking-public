# Results vs. 3.10.4

- fork: iritkatriel
- ref: binaryops
- machine: linux-x86_64
- commit hash: e43ac58
- commit date: 2025-01-17
- overall geometric mean: 1.451x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                             |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                           |
| html5lib       | 88.9 ms                                                | 60.9 ms: 1.46x faster                                            |
| Geometric mean | (ref)                                                  | 1.37x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 600 ms: 2.95x faster                                             |
| async_tree_none         | 728 ms                                                 | 258 ms: 2.83x faster                                             |
| async_tree_memoization  | 870 ms                                                 | 325 ms: 2.68x faster                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 482 ms: 2.11x faster                                             |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.4 ms: 1.66x faster                                            |
| nbody          | 154 ms                                                 | 95.4 ms: 1.61x faster                                            |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.40x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.50x faster                                             |
| regex_dna      | 227 ms                                                 | 205 ms: 1.11x faster                                             |
| regex_effbot   | 3.63 ms                                                | 3.29 ms: 1.10x faster                                            |
| regex_v8       | 27.8 ms                                                | 25.8 ms: 1.08x faster                                            |
| Geometric mean | (ref)                                                  | 1.19x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.59x faster                                           |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                             |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                             |
| xml_etree_process    | 79.1 ms                                                | 60.0 ms: 1.32x faster                                            |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                             |
| xml_etree_iterparse  | 115 ms                                                 | 97.5 ms: 1.18x faster                                            |
| json_dumps           | 14.2 ms                                                | 12.0 ms: 1.18x faster                                            |
| xml_etree_generate   | 99.4 ms                                                | 84.6 ms: 1.18x faster                                            |
| json_loads           | 31.2 us                                                | 29.5 us: 1.06x faster                                            |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                            |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                            |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.3 ms: 1.50x faster                                            |
| django_template | 48.2 ms                                                | 32.3 ms: 1.49x faster                                            |
| mako            | 16.3 ms                                                | 11.5 ms: 1.41x faster                                            |
| genshi_xml      | 66.0 ms                                                | 48.0 ms: 1.38x faster                                            |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.37x faster                                             |
| async_tree_io            | 1.77 sec                                               | 600 ms: 2.95x faster                                             |
| generators               | 80.1 ms                                                | 27.3 ms: 2.93x faster                                            |
| async_tree_none          | 728 ms                                                 | 258 ms: 2.83x faster                                             |
| async_tree_memoization   | 870 ms                                                 | 325 ms: 2.68x faster                                             |
| deltablue                | 7.91 ms                                                | 3.17 ms: 2.50x faster                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 482 ms: 2.11x faster                                             |
| go                       | 240 ms                                                 | 117 ms: 2.06x faster                                             |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                             |
| chaos                    | 115 ms                                                 | 57.8 ms: 2.00x faster                                            |
| richards_super           | 94.7 ms                                                | 49.8 ms: 1.90x faster                                            |
| deepcopy_memo            | 58.5 us                                                | 30.9 us: 1.89x faster                                            |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                             |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                             |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.82x faster                                             |
| richards                 | 79.3 ms                                                | 43.8 ms: 1.81x faster                                            |
| crypto_pyaes             | 128 ms                                                 | 71.6 ms: 1.79x faster                                            |
| logging_silent           | 190 ns                                                 | 107 ns: 1.77x faster                                             |
| scimark_monte_carlo      | 118 ms                                                 | 67.3 ms: 1.76x faster                                            |
| spectral_norm            | 170 ms                                                 | 97.8 ms: 1.74x faster                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.26 ms: 1.73x faster                                            |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                            |
| hexiom                   | 10.4 ms                                                | 6.23 ms: 1.67x faster                                            |
| float                    | 117 ms                                                 | 70.4 ms: 1.66x faster                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.56 ms: 1.65x faster                                            |
| nbody                    | 154 ms                                                 | 95.4 ms: 1.61x faster                                            |
| pyflate                  | 716 ms                                                 | 449 ms: 1.60x faster                                             |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.59x faster                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                            |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                             |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                             |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                             |
| logging_simple           | 8.30 us                                                | 5.53 us: 1.50x faster                                            |
| regex_compile            | 188 ms                                                 | 126 ms: 1.50x faster                                             |
| genshi_text              | 31.8 ms                                                | 21.3 ms: 1.50x faster                                            |
| django_template          | 48.2 ms                                                | 32.3 ms: 1.49x faster                                            |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.49x faster                                            |
| logging_format           | 9.09 us                                                | 6.16 us: 1.48x faster                                            |
| html5lib                 | 88.9 ms                                                | 60.9 ms: 1.46x faster                                            |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                           |
| pprint_safe_repr         | 1.02 sec                                               | 712 ms: 1.43x faster                                             |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.4 ms: 1.42x faster                                            |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.41x faster                                            |
| thrift                   | 1.07 ms                                                | 762 us: 1.41x faster                                             |
| genshi_xml               | 66.0 ms                                                | 48.0 ms: 1.38x faster                                            |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                             |
| sqlglot_normalize        | 143 ms                                                 | 105 ms: 1.36x faster                                             |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                           |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.76 ms: 1.36x faster                                            |
| scimark_fft              | 466 ms                                                 | 347 ms: 1.34x faster                                             |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                             |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.33x faster                                             |
| fannkuch                 | 532 ms                                                 | 401 ms: 1.33x faster                                             |
| xml_etree_process        | 79.1 ms                                                | 60.0 ms: 1.32x faster                                            |
| sqlglot_optimize         | 69.2 ms                                                | 52.6 ms: 1.32x faster                                            |
| nqueens                  | 106 ms                                                 | 80.5 ms: 1.31x faster                                            |
| dulwich_log              | 84.3 ms                                                | 64.2 ms: 1.31x faster                                            |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.31x faster                                            |
| sympy_str                | 346 ms                                                 | 266 ms: 1.30x faster                                             |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                            |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                           |
| sympy_expand             | 566 ms                                                 | 451 ms: 1.25x faster                                             |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 97.5 ms: 1.18x faster                                            |
| json_dumps               | 14.2 ms                                                | 12.0 ms: 1.18x faster                                            |
| xml_etree_generate       | 99.4 ms                                                | 84.6 ms: 1.18x faster                                            |
| async_generators         | 444 ms                                                 | 388 ms: 1.14x faster                                             |
| bench_thread_pool        | 986 us                                                 | 865 us: 1.14x faster                                             |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                            |
| mdp                      | 2.85 sec                                               | 2.52 sec: 1.13x faster                                           |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                             |
| regex_dna                | 227 ms                                                 | 205 ms: 1.11x faster                                             |
| regex_effbot             | 3.63 ms                                                | 3.29 ms: 1.10x faster                                            |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                            |
| json                     | 5.69 ms                                                | 5.24 ms: 1.09x faster                                            |
| regex_v8                 | 27.8 ms                                                | 25.8 ms: 1.08x faster                                            |
| json_loads               | 31.2 us                                                | 29.5 us: 1.06x faster                                            |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                             |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                             |
| telco                    | 7.27 ms                                                | 7.77 ms: 1.07x slower                                            |
| coverage                 | 79.4 ms                                                | 89.6 ms: 1.13x slower                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                            |
| gc_traversal             | 3.62 ms                                                | 4.59 ms: 1.27x slower                                            |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                            |
| bench_mp_pool            | 24.0 ms                                                | 81.3 ms: 3.39x slower                                            |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                     |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250117-3.14.0a4+-e43ac58/bm-20250117-linux-x86_64-iritkatriel-binaryops-3.14.0a4+-e43ac58.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.451x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.26x