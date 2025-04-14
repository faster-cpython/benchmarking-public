# Results vs. 3.10.4

- fork: iritkatriel
- ref: binary_subscr_to_op
- machine: linux-x86_64
- commit hash: 875bc77
- commit date: 2025-02-04
- overall geometric mean: 1.462x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.34x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 250 ms: 1.39x faster                                                       |
| docutils       | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                     |
| html5lib       | 88.9 ms                                                | 61.3 ms: 1.45x faster                                                      |
| Geometric mean | (ref)                                                  | 1.37x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 624 ms: 2.84x faster                                                       |
| async_tree_none         | 728 ms                                                 | 267 ms: 2.73x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 327 ms: 2.66x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 502 ms: 2.02x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.54x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 68.5 ms: 1.71x faster                                                      |
| nbody          | 154 ms                                                 | 92.1 ms: 1.67x faster                                                      |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.43x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 124 ms: 1.52x faster                                                       |
| regex_effbot   | 3.63 ms                                                | 3.27 ms: 1.11x faster                                                      |
| regex_v8       | 27.8 ms                                                | 25.6 ms: 1.09x faster                                                      |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                  | 1.17x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                     |
| pickle_pure_python   | 484 us                                                 | 312 us: 1.55x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 214 us: 1.55x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 58.1 ms: 1.36x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                       |
| json_dumps           | 14.2 ms                                                | 11.8 ms: 1.21x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 82.6 ms: 1.20x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 96.9 ms: 1.19x faster                                                      |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 7.03 ms: 1.19x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.4 ms: 1.53x faster                                                      |
| genshi_text     | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                      |
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 47.7 ms: 1.39x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.47x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 157 us: 3.46x faster                                                       |
| generators               | 80.1 ms                                                | 27.8 ms: 2.88x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 624 ms: 2.84x faster                                                       |
| async_tree_none          | 728 ms                                                 | 267 ms: 2.73x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 327 ms: 2.66x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.15 ms: 2.51x faster                                                      |
| go                       | 240 ms                                                 | 115 ms: 2.08x faster                                                       |
| pylint                   | 551 ms                                                 | 270 ms: 2.04x faster                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 502 ms: 2.02x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 29.3 us: 2.00x faster                                                      |
| chaos                    | 115 ms                                                 | 57.9 ms: 1.99x faster                                                      |
| deepcopy                 | 479 us                                                 | 250 us: 1.92x faster                                                       |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                       |
| richards_super           | 94.7 ms                                                | 50.5 ms: 1.87x faster                                                      |
| logging_silent           | 190 ns                                                 | 101 ns: 1.87x faster                                                       |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 69.9 ms: 1.83x faster                                                      |
| richards                 | 79.3 ms                                                | 44.1 ms: 1.80x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 66.2 ms: 1.79x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.2 us: 1.77x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.24 ms: 1.75x faster                                                      |
| spectral_norm            | 170 ms                                                 | 97.0 ms: 1.75x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.05 ms: 1.72x faster                                                      |
| float                    | 117 ms                                                 | 68.5 ms: 1.71x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.54 ms: 1.67x faster                                                      |
| nbody                    | 154 ms                                                 | 92.1 ms: 1.67x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.66 us: 1.57x faster                                                      |
| pyflate                  | 716 ms                                                 | 460 ms: 1.56x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 312 us: 1.55x faster                                                       |
| unpickle_pure_python     | 331 us                                                 | 214 us: 1.55x faster                                                       |
| scimark_lu               | 176 ms                                                 | 114 ms: 1.54x faster                                                       |
| django_template          | 48.2 ms                                                | 31.4 ms: 1.53x faster                                                      |
| regex_compile            | 188 ms                                                 | 124 ms: 1.52x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.51 us: 1.51x faster                                                      |
| genshi_text              | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                                      |
| logging_format           | 9.09 us                                                | 6.14 us: 1.48x faster                                                      |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                      |
| html5lib                 | 88.9 ms                                                | 61.3 ms: 1.45x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 707 ms: 1.44x faster                                                       |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.2 ms: 1.44x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.41x faster                                                     |
| thrift                   | 1.07 ms                                                | 767 us: 1.40x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 103 ms: 1.39x faster                                                       |
| 2to3                     | 348 ms                                                 | 250 ms: 1.39x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 47.7 ms: 1.39x faster                                                      |
| scimark_fft              | 466 ms                                                 | 340 ms: 1.37x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 58.1 ms: 1.36x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.76 ms: 1.36x faster                                                      |
| fannkuch                 | 532 ms                                                 | 394 ms: 1.35x faster                                                       |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.35x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 51.4 ms: 1.35x faster                                                      |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.35x faster                                                       |
| nqueens                  | 106 ms                                                 | 78.9 ms: 1.34x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 19.4 ms: 1.33x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 63.8 ms: 1.32x faster                                                      |
| sympy_str                | 346 ms                                                 | 264 ms: 1.31x faster                                                       |
| pathlib                  | 20.5 ms                                                | 15.7 ms: 1.30x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.57 sec: 1.28x faster                                                     |
| sympy_expand             | 566 ms                                                 | 447 ms: 1.26x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                       |
| json_dumps               | 14.2 ms                                                | 11.8 ms: 1.21x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 82.6 ms: 1.20x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 96.9 ms: 1.19x faster                                                      |
| async_generators         | 444 ms                                                 | 380 ms: 1.17x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.45 sec: 1.16x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 855 us: 1.15x faster                                                       |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                      |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                       |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.27 ms: 1.11x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                                      |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 25.6 ms: 1.09x faster                                                      |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                                       |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                       |
| telco                    | 7.27 ms                                                | 7.98 ms: 1.10x slower                                                      |
| coverage                 | 79.4 ms                                                | 89.7 ms: 1.13x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.03 ms: 1.19x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 5.03 ms: 1.39x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.53x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                | 80.5 ms: 3.35x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                               |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250204-3.14.0a4+-875bc77/bm-20250204-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-875bc77.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.462x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.34x

# Memory
- memory change: 1.26x