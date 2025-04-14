# Results vs. 3.10.4

- fork: mdboom
- ref: specialize_compact_i
- machine: linux-x86_64
- commit hash: fd72580
- commit date: 2025-01-28
- overall geometric mean: 1.356x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 265 ms: 1.31x faster                                                   |
| chameleon      | 9.68 ms                                                | 7.02 ms: 1.38x faster                                                  |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                 |
| html5lib       | 88.9 ms                                                | 64.7 ms: 1.37x faster                                                  |
| tornado_http   | 136 ms                                                 | 96.0 ms: 1.42x faster                                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 463 ms: 1.57x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 565 ms: 1.54x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 1.20 sec: 1.48x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 741 ms: 1.37x faster                                                   |
| Geometric mean          | (ref)                                                  | 1.49x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 93.3 ms: 1.65x faster                                                  |
| float          | 117 ms                                                 | 83.0 ms: 1.41x faster                                                  |
| pidigits       | 191 ms                                                 | 222 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                  | 1.26x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.41x faster                                                   |
| regex_v8       | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                  |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                   |
| regex_effbot   | 3.63 ms                                                | 3.70 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 309 us: 1.57x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                                   |
| tomli_loads          | 3.14 sec                                               | 2.12 sec: 1.48x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 86.0 ms: 1.16x faster                                                  |
| json_loads           | 31.2 us                                                | 28.4 us: 1.10x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 107 ms: 1.08x faster                                                   |
| xml_etree_parse      | 168 ms                                                 | 158 ms: 1.06x faster                                                   |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.6 ms: 1.16x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 9.00 ms: 1.52x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.14x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.2 ms: 1.49x faster                                                  |
| mako            | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                  |
| genshi_text     | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 50.8 ms: 1.30x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 115 us: 4.72x faster                                                   |
| generators               | 80.1 ms                                                | 29.3 ms: 2.74x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.33 ms: 2.38x faster                                                  |
| chaos                    | 115 ms                                                 | 59.5 ms: 1.94x faster                                                  |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                                   |
| pylint                   | 551 ms                                                 | 306 ms: 1.80x faster                                                   |
| logging_silent           | 190 ns                                                 | 105 ns: 1.80x faster                                                   |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.78x faster                                                   |
| scimark_monte_carlo      | 118 ms                                                 | 67.5 ms: 1.75x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                  |
| go                       | 240 ms                                                 | 139 ms: 1.73x faster                                                   |
| crypto_pyaes             | 128 ms                                                 | 74.3 ms: 1.72x faster                                                  |
| richards_super           | 94.7 ms                                                | 55.3 ms: 1.71x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.70x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.15 ms: 1.69x faster                                                  |
| nbody                    | 154 ms                                                 | 93.3 ms: 1.65x faster                                                  |
| richards                 | 79.3 ms                                                | 49.1 ms: 1.61x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.3 ms: 1.57x faster                                                  |
| async_tree_none          | 728 ms                                                 | 463 ms: 1.57x faster                                                   |
| pickle_pure_python       | 484 us                                                 | 309 us: 1.57x faster                                                   |
| pyflate                  | 716 ms                                                 | 458 ms: 1.56x faster                                                   |
| spectral_norm            | 170 ms                                                 | 110 ms: 1.54x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 565 ms: 1.54x faster                                                   |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                   |
| deepcopy_memo            | 58.5 us                                                | 38.6 us: 1.52x faster                                                  |
| django_template          | 48.2 ms                                                | 32.2 ms: 1.49x faster                                                  |
| mako                     | 16.3 ms                                                | 11.0 ms: 1.49x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                                   |
| tomli_loads              | 3.14 sec                                               | 2.12 sec: 1.48x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.48x faster                                                 |
| tornado_http             | 136 ms                                                 | 96.0 ms: 1.42x faster                                                  |
| logging_format           | 9.09 us                                                | 6.43 us: 1.41x faster                                                  |
| regex_compile            | 188 ms                                                 | 134 ms: 1.41x faster                                                   |
| float                    | 117 ms                                                 | 83.0 ms: 1.41x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.91 us: 1.41x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 735 ms: 1.38x faster                                                   |
| chameleon                | 9.68 ms                                                | 7.02 ms: 1.38x faster                                                  |
| genshi_text              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                  |
| html5lib                 | 88.9 ms                                                | 64.7 ms: 1.37x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 741 ms: 1.37x faster                                                   |
| deepcopy                 | 479 us                                                 | 351 us: 1.36x faster                                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.2 ms: 1.36x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                                  |
| thrift                   | 1.07 ms                                                | 794 us: 1.35x faster                                                   |
| fannkuch                 | 532 ms                                                 | 395 ms: 1.35x faster                                                   |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.34x faster                                                   |
| xml_etree_process        | 79.1 ms                                                | 58.9 ms: 1.34x faster                                                  |
| nqueens                  | 106 ms                                                 | 79.0 ms: 1.34x faster                                                  |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                   |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.33x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 3.16 us: 1.32x faster                                                  |
| 2to3                     | 348 ms                                                 | 265 ms: 1.31x faster                                                   |
| genshi_xml               | 66.0 ms                                                | 50.8 ms: 1.30x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 53.4 ms: 1.30x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.22 sec: 1.29x faster                                                 |
| sympy_str                | 346 ms                                                 | 271 ms: 1.28x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 66.8 ms: 1.26x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.13 ms: 1.26x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 137 ms: 1.26x faster                                                   |
| scimark_fft              | 466 ms                                                 | 374 ms: 1.25x faster                                                   |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                   |
| gunicorn                 | 1.53 ms                                                | 1.24 ms: 1.23x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 840 us: 1.17x faster                                                   |
| python_startup           | 14.6 ms                                                | 12.6 ms: 1.16x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 86.0 ms: 1.16x faster                                                  |
| pathlib                  | 20.5 ms                                                | 18.4 ms: 1.11x faster                                                  |
| json_loads               | 31.2 us                                                | 28.4 us: 1.10x faster                                                  |
| json                     | 5.69 ms                                                | 5.20 ms: 1.09x faster                                                  |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 107 ms: 1.08x faster                                                   |
| sqlite_synth             | 3.02 us                                                | 2.83 us: 1.07x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 26.1 ms: 1.06x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 158 ms: 1.06x faster                                                   |
| mdp                      | 2.85 sec                                               | 2.69 sec: 1.06x faster                                                 |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                   |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.00x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.70 ms: 1.02x slower                                                  |
| async_generators         | 444 ms                                                 | 456 ms: 1.03x slower                                                   |
| pidigits                 | 191 ms                                                 | 222 ms: 1.16x slower                                                   |
| telco                    | 7.27 ms                                                | 8.46 ms: 1.17x slower                                                  |
| coverage                 | 79.4 ms                                                | 94.2 ms: 1.19x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.72 ms: 1.30x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.42 ms: 1.49x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 9.00 ms: 1.52x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, djangocms, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250128-3.13.0a2+-fd72580/bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.356x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.24x