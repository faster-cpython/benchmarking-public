# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_hot
- machine: linux-x86_64
- commit hash: 4cfabf5
- commit date: 2025-06-20
- overall geometric mean: 1.462x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 260 ms: 1.34x faster                                              |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                            |
| html5lib       | 88.9 ms                                                | 61.9 ms: 1.44x faster                                             |
| Geometric mean | (ref)                                                  | 1.34x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 604 ms: 2.93x faster                                              |
| async_tree_none         | 728 ms                                                 | 265 ms: 2.75x faster                                              |
| async_tree_memoization  | 870 ms                                                 | 319 ms: 2.73x faster                                              |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 500 ms: 2.03x faster                                              |
| Geometric mean          | (ref)                                                  | 2.58x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| float          | 117 ms                                                 | 64.9 ms: 1.81x faster                                             |
| nbody          | 154 ms                                                 | 92.2 ms: 1.66x faster                                             |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                              |
| Geometric mean | (ref)                                                  | 1.45x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                              |
| regex_v8       | 27.8 ms                                                | 22.8 ms: 1.22x faster                                             |
| regex_dna      | 227 ms                                                 | 197 ms: 1.15x faster                                              |
| regex_effbot   | 3.63 ms                                                | 3.31 ms: 1.10x faster                                             |
| Geometric mean | (ref)                                                  | 1.23x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 199 us: 1.66x faster                                              |
| tomli_loads          | 3.14 sec                                               | 1.90 sec: 1.65x faster                                            |
| pickle_pure_python   | 484 us                                                 | 329 us: 1.47x faster                                              |
| xml_etree_process    | 79.1 ms                                                | 56.0 ms: 1.41x faster                                             |
| json_dumps           | 14.2 ms                                                | 11.3 ms: 1.25x faster                                             |
| xml_etree_generate   | 99.4 ms                                                | 80.1 ms: 1.24x faster                                             |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                              |
| xml_etree_iterparse  | 115 ms                                                 | 100 ms: 1.15x faster                                              |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                             |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.2 ms: 1.20x faster                                             |
| python_startup_no_site | 5.93 ms                                                | 6.95 ms: 1.17x slower                                             |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.6 ms: 1.54x faster                                             |
| django_template | 48.2 ms                                                | 32.8 ms: 1.47x faster                                             |
| genshi_text     | 31.8 ms                                                | 21.7 ms: 1.46x faster                                             |
| genshi_xml      | 66.0 ms                                                | 50.0 ms: 1.32x faster                                             |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 170 us: 3.21x faster                                              |
| async_tree_io            | 1.77 sec                                               | 604 ms: 2.93x faster                                              |
| async_tree_none          | 728 ms                                                 | 265 ms: 2.75x faster                                              |
| async_tree_memoization   | 870 ms                                                 | 319 ms: 2.73x faster                                              |
| generators               | 80.1 ms                                                | 30.9 ms: 2.59x faster                                             |
| deltablue                | 7.91 ms                                                | 3.12 ms: 2.54x faster                                             |
| richards_super           | 94.7 ms                                                | 39.4 ms: 2.40x faster                                             |
| richards                 | 79.3 ms                                                | 34.1 ms: 2.32x faster                                             |
| mdp                      | 2.85 sec                                               | 1.27 sec: 2.24x faster                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 500 ms: 2.03x faster                                              |
| go                       | 240 ms                                                 | 122 ms: 1.97x faster                                              |
| deepcopy_memo            | 58.5 us                                                | 29.9 us: 1.95x faster                                             |
| pylint                   | 551 ms                                                 | 284 ms: 1.94x faster                                              |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                              |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                              |
| chaos                    | 115 ms                                                 | 62.4 ms: 1.85x faster                                             |
| float                    | 117 ms                                                 | 64.9 ms: 1.81x faster                                             |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.79x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 66.8 ms: 1.77x faster                                             |
| crypto_pyaes             | 128 ms                                                 | 74.9 ms: 1.71x faster                                             |
| pyflate                  | 716 ms                                                 | 422 ms: 1.70x faster                                              |
| djangocms                | 38.4 us                                                | 22.8 us: 1.69x faster                                             |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                             |
| nbody                    | 154 ms                                                 | 92.2 ms: 1.66x faster                                             |
| unpickle_pure_python     | 331 us                                                 | 199 us: 1.66x faster                                              |
| tomli_loads              | 3.14 sec                                               | 1.90 sec: 1.65x faster                                            |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                              |
| hexiom                   | 10.4 ms                                                | 6.44 ms: 1.61x faster                                             |
| mako                     | 16.3 ms                                                | 10.6 ms: 1.54x faster                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                             |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                              |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                              |
| pickle_pure_python       | 484 us                                                 | 329 us: 1.47x faster                                              |
| django_template          | 48.2 ms                                                | 32.8 ms: 1.47x faster                                             |
| genshi_text              | 31.8 ms                                                | 21.7 ms: 1.46x faster                                             |
| html5lib                 | 88.9 ms                                                | 61.9 ms: 1.44x faster                                             |
| dulwich_log              | 84.3 ms                                                | 59.5 ms: 1.42x faster                                             |
| xml_etree_process        | 79.1 ms                                                | 56.0 ms: 1.41x faster                                             |
| scimark_fft              | 466 ms                                                 | 330 ms: 1.41x faster                                              |
| coroutines               | 35.1 ms                                                | 25.3 ms: 1.39x faster                                             |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                            |
| thrift                   | 1.07 ms                                                | 787 us: 1.36x faster                                              |
| 2to3                     | 348 ms                                                 | 260 ms: 1.34x faster                                              |
| logging_format           | 9.09 us                                                | 6.83 us: 1.33x faster                                             |
| logging_simple           | 8.30 us                                                | 6.25 us: 1.33x faster                                             |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                             |
| genshi_xml               | 66.0 ms                                                | 50.0 ms: 1.32x faster                                             |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.95 ms: 1.31x faster                                             |
| fannkuch                 | 532 ms                                                 | 409 ms: 1.30x faster                                              |
| nqueens                  | 106 ms                                                 | 82.9 ms: 1.28x faster                                             |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                              |
| pprint_pformat           | 2.10 sec                                               | 1.66 sec: 1.26x faster                                            |
| json_dumps               | 14.2 ms                                                | 11.3 ms: 1.25x faster                                             |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                            |
| xml_etree_generate       | 99.4 ms                                                | 80.1 ms: 1.24x faster                                             |
| regex_v8                 | 27.8 ms                                                | 22.8 ms: 1.22x faster                                             |
| pprint_safe_repr         | 1.02 sec                                               | 835 ms: 1.22x faster                                              |
| sympy_expand             | 566 ms                                                 | 466 ms: 1.21x faster                                              |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                             |
| python_startup           | 14.6 ms                                                | 12.2 ms: 1.20x faster                                             |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                              |
| xml_etree_iterparse      | 115 ms                                                 | 100 ms: 1.15x faster                                              |
| regex_dna                | 227 ms                                                 | 197 ms: 1.15x faster                                              |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                              |
| regex_effbot             | 3.63 ms                                                | 3.31 ms: 1.10x faster                                             |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                             |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                             |
| json                     | 5.69 ms                                                | 5.28 ms: 1.08x faster                                             |
| async_generators         | 444 ms                                                 | 432 ms: 1.03x faster                                              |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                              |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                              |
| telco                    | 7.27 ms                                                | 7.67 ms: 1.06x slower                                             |
| coverage                 | 79.4 ms                                                | 87.6 ms: 1.10x slower                                             |
| python_startup_no_site   | 5.93 ms                                                | 6.95 ms: 1.17x slower                                             |
| gc_traversal             | 3.62 ms                                                | 4.75 ms: 1.31x slower                                             |
| create_gc_cycles         | 1.62 ms                                                | 2.59 ms: 1.60x slower                                             |
| logging_silent           | 190 ns                                                 | 472 ns: 2.49x slower                                              |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                      |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250620-3.15.0a0-4cfabf5-JIT/bm-20250620-linux-x86_64-brandtbucher-justin_hot-3.15.0a0-4cfabf5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.462x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.33x