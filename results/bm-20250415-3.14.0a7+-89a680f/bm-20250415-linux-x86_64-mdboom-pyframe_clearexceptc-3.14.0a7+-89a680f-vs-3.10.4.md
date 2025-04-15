# Results vs. 3.10.4

- fork: mdboom
- ref: pyframe_clearexceptc
- machine: linux-x86_64
- commit hash: 89a680f
- commit date: 2025-04-15
- overall geometric mean: 1.461x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 251 ms: 1.39x faster                                                   |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                 |
| html5lib       | 88.9 ms                                                | 61.3 ms: 1.45x faster                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 613 ms: 2.89x faster                                                   |
| async_tree_none         | 728 ms                                                 | 258 ms: 2.82x faster                                                   |
| async_tree_memoization  | 870 ms                                                 | 310 ms: 2.81x faster                                                   |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 484 ms: 2.10x faster                                                   |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 117 ms                                                 | 67.0 ms: 1.75x faster                                                  |
| nbody          | 154 ms                                                 | 95.2 ms: 1.61x faster                                                  |
| pidigits       | 191 ms                                                 | 194 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.40x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.50x faster                                                   |
| regex_v8       | 27.8 ms                                                | 23.2 ms: 1.20x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.28 ms: 1.11x faster                                                  |
| regex_dna      | 227 ms                                                 | 209 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                  | 1.21x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                 |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                   |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                   |
| xml_etree_process    | 79.1 ms                                                | 59.2 ms: 1.34x faster                                                  |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                                  |
| xml_etree_generate   | 99.4 ms                                                | 85.0 ms: 1.17x faster                                                  |
| json_loads           | 31.2 us                                                | 30.2 us: 1.03x faster                                                  |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                  |
| python_startup_no_site | 5.93 ms                                                | 8.21 ms: 1.38x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 20.9 ms: 1.53x faster                                                  |
| django_template | 48.2 ms                                                | 31.6 ms: 1.52x faster                                                  |
| mako            | 16.3 ms                                                | 11.2 ms: 1.45x faster                                                  |
| genshi_xml      | 66.0 ms                                                | 48.8 ms: 1.35x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 613 ms: 2.89x faster                                                   |
| async_tree_none          | 728 ms                                                 | 258 ms: 2.82x faster                                                   |
| async_tree_memoization   | 870 ms                                                 | 310 ms: 2.81x faster                                                   |
| generators               | 80.1 ms                                                | 29.9 ms: 2.68x faster                                                  |
| mdp                      | 2.85 sec                                               | 1.21 sec: 2.35x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.38 ms: 2.34x faster                                                  |
| go                       | 240 ms                                                 | 112 ms: 2.14x faster                                                   |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 484 ms: 2.10x faster                                                   |
| chaos                    | 115 ms                                                 | 56.2 ms: 2.05x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 28.6 us: 2.04x faster                                                  |
| pylint                   | 551 ms                                                 | 279 ms: 1.98x faster                                                   |
| logging_silent           | 190 ns                                                 | 96.6 ns: 1.96x faster                                                  |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                                   |
| richards_super           | 94.7 ms                                                | 49.4 ms: 1.92x faster                                                  |
| deepcopy                 | 479 us                                                 | 254 us: 1.89x faster                                                   |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                   |
| richards                 | 79.3 ms                                                | 42.9 ms: 1.85x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 66.3 ms: 1.78x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 72.4 ms: 1.76x faster                                                  |
| float                    | 117 ms                                                 | 67.0 ms: 1.75x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                  |
| pyflate                  | 716 ms                                                 | 428 ms: 1.68x faster                                                   |
| hexiom                   | 10.4 ms                                                | 6.27 ms: 1.66x faster                                                  |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.65x faster                                                   |
| nbody                    | 154 ms                                                 | 95.2 ms: 1.61x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.59x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                  |
| genshi_text              | 31.8 ms                                                | 20.9 ms: 1.53x faster                                                  |
| django_template          | 48.2 ms                                                | 31.6 ms: 1.52x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                   |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                   |
| logging_simple           | 8.30 us                                                | 5.50 us: 1.51x faster                                                  |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                   |
| regex_compile            | 188 ms                                                 | 125 ms: 1.50x faster                                                   |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                  |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.45x faster                                                  |
| html5lib                 | 88.9 ms                                                | 61.3 ms: 1.45x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                 |
| coroutines               | 35.1 ms                                                | 24.4 ms: 1.44x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 715 ms: 1.42x faster                                                   |
| dulwich_log              | 84.3 ms                                                | 59.8 ms: 1.41x faster                                                  |
| 2to3                     | 348 ms                                                 | 251 ms: 1.39x faster                                                   |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.71 ms: 1.37x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 48.8 ms: 1.35x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.2 ms: 1.34x faster                                                  |
| xml_etree_process        | 79.1 ms                                                | 59.2 ms: 1.34x faster                                                  |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                   |
| nqueens                  | 106 ms                                                 | 80.3 ms: 1.32x faster                                                  |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.30x faster                                                   |
| scimark_fft              | 466 ms                                                 | 359 ms: 1.30x faster                                                   |
| fannkuch                 | 532 ms                                                 | 411 ms: 1.29x faster                                                   |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                                   |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                 |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                                   |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.22x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 23.2 ms: 1.20x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                   |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 85.0 ms: 1.17x faster                                                  |
| async_generators         | 444 ms                                                 | 388 ms: 1.14x faster                                                   |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.14x faster                                                   |
| bench_thread_pool        | 986 us                                                 | 883 us: 1.12x faster                                                   |
| regex_effbot             | 3.63 ms                                                | 3.28 ms: 1.11x faster                                                  |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.10x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                                  |
| regex_dna                | 227 ms                                                 | 209 ms: 1.08x faster                                                   |
| json                     | 5.69 ms                                                | 5.41 ms: 1.05x faster                                                  |
| json_loads               | 31.2 us                                                | 30.2 us: 1.03x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                   |
| pidigits                 | 191 ms                                                 | 194 ms: 1.02x slower                                                   |
| telco                    | 7.27 ms                                                | 7.67 ms: 1.06x slower                                                  |
| coverage                 | 79.4 ms                                                | 89.2 ms: 1.12x slower                                                  |
| gc_traversal             | 3.62 ms                                                | 4.82 ms: 1.33x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 8.21 ms: 1.38x slower                                                  |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                  |
| bench_mp_pool            | 24.0 ms                                                | 82.0 ms: 3.41x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                           |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250415-3.14.0a7+-89a680f/bm-20250415-linux-x86_64-mdboom-pyframe_clearexceptc-3.14.0a7+-89a680f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.461x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.35x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.27x