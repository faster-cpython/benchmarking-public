# Results vs. 3.10.4

- fork: mdboom
- ref: specialize_compact_i
- machine: linux-x86_64
- commit hash: f366df0
- commit date: 2025-01-29
- overall geometric mean: 1.452x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 253 ms: 1.38x faster                                                   |
| docutils       | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                 |
| html5lib       | 88.9 ms                                                | 60.7 ms: 1.46x faster                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 620 ms: 2.85x faster                                                   |
| async_tree_none         | 728 ms                                                 | 263 ms: 2.77x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 321 ms: 2.71x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 487 ms: 2.09x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.59x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.9 ms: 1.65x faster                                                  |
| nbody          | 154 ms                                                 | 93.2 ms: 1.65x faster                                                  |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.41x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.50x faster                                                   |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.34 ms: 1.09x faster                                                  |
| regex_dna      | 227 ms                                                 | 209 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 58.4 ms: 1.36x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.8 ms: 1.21x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 97.4 ms: 1.19x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 83.9 ms: 1.18x faster                                                  |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.0 ms: 1.50x faster                                                  |
| genshi_text     | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                  |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 49.1 ms: 1.35x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 156 us: 3.48x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 620 ms: 2.85x faster                                                   |
| generators               | 80.1 ms                                                | 28.3 ms: 2.83x faster                                                  |
| async_tree_none          | 728 ms                                                 | 263 ms: 2.77x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 321 ms: 2.71x faster                                                   |
| deltablue                | 7.91 ms                                                | 3.28 ms: 2.41x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 487 ms: 2.09x faster                                                   |
| go                       | 240 ms                                                 | 117 ms: 2.05x faster                                                   |
| pylint                   | 551 ms                                                 | 272 ms: 2.03x faster                                                   |
| chaos                    | 115 ms                                                 | 59.0 ms: 1.96x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 30.8 us: 1.90x faster                                                  |
| deepcopy                 | 479 us                                                 | 255 us: 1.88x faster                                                   |
| richards_super           | 94.7 ms                                                | 50.8 ms: 1.87x faster                                                  |
| raytrace                 | 507 ms                                                 | 274 ms: 1.85x faster                                                   |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 69.9 ms: 1.83x faster                                                  |
| richards                 | 79.3 ms                                                | 44.2 ms: 1.79x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 66.3 ms: 1.78x faster                                                  |
| spectral_norm            | 170 ms                                                 | 95.9 ms: 1.77x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.75x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                  |
| logging_silent           | 190 ns                                                 | 113 ns: 1.68x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.29 ms: 1.65x faster                                                  |
| float                    | 117 ms                                                 | 70.9 ms: 1.65x faster                                                  |
| nbody                    | 154 ms                                                 | 93.2 ms: 1.65x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.96 sec: 1.60x faster                                                 |
| pyflate                  | 716 ms                                                 | 450 ms: 1.59x faster                                                   |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.45 us: 1.52x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                                   |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.51x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                   |
| logging_format           | 9.09 us                                                | 6.04 us: 1.50x faster                                                  |
| regex_compile            | 188 ms                                                 | 125 ms: 1.50x faster                                                   |
| django_template          | 48.2 ms                                                | 32.0 ms: 1.50x faster                                                  |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.48x faster                                                  |
| genshi_text              | 31.8 ms                                                | 21.5 ms: 1.48x faster                                                  |
| html5lib                 | 88.9 ms                                                | 60.7 ms: 1.46x faster                                                  |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                  |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.4 ms: 1.43x faster                                                  |
| thrift                   | 1.07 ms                                                | 759 us: 1.41x faster                                                   |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.62 ms: 1.40x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 731 ms: 1.39x faster                                                   |
| scimark_fft              | 466 ms                                                 | 335 ms: 1.39x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 103 ms: 1.38x faster                                                   |
| 2to3                     | 348 ms                                                 | 253 ms: 1.38x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 58.4 ms: 1.36x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                 |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.35x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 49.1 ms: 1.35x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.34x faster                                                   |
| sqlglot_optimize         | 69.2 ms                                                | 52.0 ms: 1.33x faster                                                  |
| fannkuch                 | 532 ms                                                 | 401 ms: 1.33x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 63.9 ms: 1.32x faster                                                  |
| nqueens                  | 106 ms                                                 | 80.5 ms: 1.31x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.31x faster                                                  |
| sympy_str                | 346 ms                                                 | 265 ms: 1.30x faster                                                   |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.30x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                 |
| sympy_expand             | 566 ms                                                 | 449 ms: 1.26x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.8 ms: 1.21x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 97.4 ms: 1.19x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 83.9 ms: 1.18x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.45 sec: 1.16x faster                                                 |
| async_generators         | 444 ms                                                 | 384 ms: 1.15x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 858 us: 1.15x faster                                                   |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                  |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                   |
| json                     | 5.69 ms                                                | 5.14 ms: 1.11x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                  |
| regex_effbot             | 3.63 ms                                                | 3.34 ms: 1.09x faster                                                  |
| regex_dna                | 227 ms                                                 | 209 ms: 1.08x faster                                                   |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                                  |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                   |
| telco                    | 7.27 ms                                                | 7.78 ms: 1.07x slower                                                  |
| coverage                 | 79.4 ms                                                | 90.7 ms: 1.14x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 5.03 ms: 1.39x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.53x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 80.9 ms: 3.37x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                           |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250129-3.14.0a4+-f366df0/bm-20250129-linux-x86_64-mdboom-specialize_compact_i-3.14.0a4+-f366df0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.452x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.26x