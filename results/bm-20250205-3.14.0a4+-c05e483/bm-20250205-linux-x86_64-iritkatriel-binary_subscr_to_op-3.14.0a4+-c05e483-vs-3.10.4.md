# Results vs. 3.10.4

- fork: iritkatriel
- ref: binary_subscr_to_op
- machine: linux-x86_64
- commit hash: c05e483
- commit date: 2025-02-05
- overall geometric mean: 1.454x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 252 ms: 1.38x faster                                                       |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                     |
| html5lib       | 88.9 ms                                                | 61.6 ms: 1.44x faster                                                      |
| Geometric mean | (ref)                                                  | 1.36x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 614 ms: 2.88x faster                                                       |
| async_tree_none         | 728 ms                                                 | 261 ms: 2.79x faster                                                       |
| async_tree_memoization  | 870 ms                                                 | 322 ms: 2.70x faster                                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 488 ms: 2.08x faster                                                       |
| Geometric mean          | (ref)                                                  | 2.59x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 68.8 ms: 1.70x faster                                                      |
| nbody          | 154 ms                                                 | 94.7 ms: 1.62x faster                                                      |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.42x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                       |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.36 ms: 1.08x faster                                                      |
| regex_dna      | 227 ms                                                 | 213 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                  | 1.17x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                     |
| pickle_pure_python   | 484 us                                                 | 312 us: 1.55x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                       |
| xml_etree_process    | 79.1 ms                                                | 58.1 ms: 1.36x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                       |
| json_dumps           | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 83.5 ms: 1.19x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 97.5 ms: 1.18x faster                                                      |
| json_loads           | 31.2 us                                                | 28.9 us: 1.08x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                      |
| python_startup_no_site | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.5 ms: 1.53x faster                                                      |
| mako            | 16.3 ms                                                | 10.8 ms: 1.51x faster                                                      |
| genshi_text     | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                      |
| genshi_xml      | 66.0 ms                                                | 48.1 ms: 1.37x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.48x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.39x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 614 ms: 2.88x faster                                                       |
| generators               | 80.1 ms                                                | 28.1 ms: 2.85x faster                                                      |
| async_tree_none          | 728 ms                                                 | 261 ms: 2.79x faster                                                       |
| async_tree_memoization   | 870 ms                                                 | 322 ms: 2.70x faster                                                       |
| deltablue                | 7.91 ms                                                | 3.16 ms: 2.51x faster                                                      |
| go                       | 240 ms                                                 | 115 ms: 2.08x faster                                                       |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 488 ms: 2.08x faster                                                       |
| pylint                   | 551 ms                                                 | 275 ms: 2.00x faster                                                       |
| chaos                    | 115 ms                                                 | 58.7 ms: 1.97x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 30.1 us: 1.94x faster                                                      |
| richards_super           | 94.7 ms                                                | 49.3 ms: 1.92x faster                                                      |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                       |
| deepcopy                 | 479 us                                                 | 257 us: 1.87x faster                                                       |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                       |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                       |
| richards                 | 79.3 ms                                                | 43.4 ms: 1.83x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 71.1 ms: 1.80x faster                                                      |
| spectral_norm            | 170 ms                                                 | 95.5 ms: 1.78x faster                                                      |
| comprehensions           | 28.8 us                                                | 16.2 us: 1.77x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.23 ms: 1.77x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 67.1 ms: 1.76x faster                                                      |
| float                    | 117 ms                                                 | 68.8 ms: 1.70x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.54 ms: 1.68x faster                                                      |
| hexiom                   | 10.4 ms                                                | 6.33 ms: 1.64x faster                                                      |
| nbody                    | 154 ms                                                 | 94.7 ms: 1.62x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                     |
| pyflate                  | 716 ms                                                 | 460 ms: 1.56x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 312 us: 1.55x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.42 us: 1.53x faster                                                      |
| django_template          | 48.2 ms                                                | 31.5 ms: 1.53x faster                                                      |
| logging_format           | 9.09 us                                                | 5.98 us: 1.52x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                       |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                       |
| mako                     | 16.3 ms                                                | 10.8 ms: 1.51x faster                                                      |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                       |
| genshi_text              | 31.8 ms                                                | 21.1 ms: 1.51x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 703 ms: 1.45x faster                                                       |
| html5lib                 | 88.9 ms                                                | 61.6 ms: 1.44x faster                                                      |
| thrift                   | 1.07 ms                                                | 759 us: 1.41x faster                                                       |
| sqlglot_normalize        | 143 ms                                                 | 103 ms: 1.39x faster                                                       |
| 2to3                     | 348 ms                                                 | 252 ms: 1.38x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 48.1 ms: 1.37x faster                                                      |
| scimark_fft              | 466 ms                                                 | 341 ms: 1.37x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 58.1 ms: 1.36x faster                                                      |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.3 ms: 1.35x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 51.7 ms: 1.34x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.85 ms: 1.33x faster                                                      |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.33x faster                                                       |
| nqueens                  | 106 ms                                                 | 79.9 ms: 1.32x faster                                                      |
| fannkuch                 | 532 ms                                                 | 407 ms: 1.31x faster                                                       |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                                      |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                                       |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.29x faster                                                       |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.29x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 66.9 ms: 1.26x faster                                                      |
| sympy_expand             | 566 ms                                                 | 450 ms: 1.26x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                       |
| json_dumps               | 14.2 ms                                                | 11.8 ms: 1.20x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 83.5 ms: 1.19x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 97.5 ms: 1.18x faster                                                      |
| async_generators         | 444 ms                                                 | 381 ms: 1.17x faster                                                       |
| mdp                      | 2.85 sec                                               | 2.46 sec: 1.16x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 872 us: 1.13x faster                                                       |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                       |
| python_startup           | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                      |
| json                     | 5.69 ms                                                | 5.08 ms: 1.12x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.09x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.36 ms: 1.08x faster                                                      |
| json_loads               | 31.2 us                                                | 28.9 us: 1.08x faster                                                      |
| regex_dna                | 227 ms                                                 | 213 ms: 1.06x faster                                                       |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                       |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                       |
| telco                    | 7.27 ms                                                | 7.76 ms: 1.07x slower                                                      |
| coverage                 | 79.4 ms                                                | 91.8 ms: 1.16x slower                                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 5.03 ms: 1.39x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.53x slower                                                      |
| bench_mp_pool            | 24.0 ms                                                | 82.3 ms: 3.43x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                               |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250205-3.14.0a4+-c05e483/bm-20250205-linux-x86_64-iritkatriel-binary_subscr_to_op-3.14.0a4+-c05e483.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.454x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.26x