# Results vs. 3.10.4

- fork: mdboom
- ref: fast_tuple_dealloc
- machine: linux-x86_64
- commit hash: 661a2b8
- commit date: 2025-04-15
- overall geometric mean: 1.445x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 262 ms: 1.33x faster                                                 |
| docutils       | 3.30 sec                                               | 3.21 sec: 1.03x faster                                               |
| html5lib       | 88.9 ms                                                | 60.5 ms: 1.47x faster                                                |
| Geometric mean | (ref)                                                  | 1.26x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 611 ms: 2.89x faster                                                 |
| async_tree_none         | 728 ms                                                 | 258 ms: 2.83x faster                                                 |
| async_tree_memoization  | 870 ms                                                 | 310 ms: 2.81x faster                                                 |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                                 |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 117 ms                                                 | 69.1 ms: 1.70x faster                                                |
| nbody          | 154 ms                                                 | 94.6 ms: 1.62x faster                                                |
| pidigits       | 191 ms                                                 | 198 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.38x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                                 |
| regex_v8       | 27.8 ms                                                | 22.7 ms: 1.22x faster                                                |
| regex_effbot   | 3.63 ms                                                | 3.15 ms: 1.15x faster                                                |
| regex_dna      | 227 ms                                                 | 203 ms: 1.12x faster                                                 |
| Geometric mean | (ref)                                                  | 1.24x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.59x faster                                               |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                 |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 84.4 ms: 1.18x faster                                                |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                                |
| json_dumps           | 14.2 ms                                                | 12.1 ms: 1.17x faster                                                |
| json_loads           | 31.2 us                                                | 29.5 us: 1.06x faster                                                |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.3 ms: 1.10x faster                                                |
| python_startup_no_site | 5.93 ms                                                | 8.24 ms: 1.39x slower                                                |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.3 ms: 1.54x faster                                                |
| genshi_text     | 31.8 ms                                                | 21.0 ms: 1.51x faster                                                |
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                |
| genshi_xml      | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 169 us: 3.23x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 611 ms: 2.89x faster                                                 |
| async_tree_none          | 728 ms                                                 | 258 ms: 2.83x faster                                                 |
| async_tree_memoization   | 870 ms                                                 | 310 ms: 2.81x faster                                                 |
| generators               | 80.1 ms                                                | 29.5 ms: 2.72x faster                                                |
| deltablue                | 7.91 ms                                                | 3.37 ms: 2.35x faster                                                |
| mdp                      | 2.85 sec                                               | 1.25 sec: 2.27x faster                                               |
| go                       | 240 ms                                                 | 114 ms: 2.11x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                                 |
| chaos                    | 115 ms                                                 | 56.6 ms: 2.04x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                                |
| pylint                   | 551 ms                                                 | 280 ms: 1.97x faster                                                 |
| logging_silent           | 190 ns                                                 | 98.2 ns: 1.93x faster                                                |
| raytrace                 | 507 ms                                                 | 264 ms: 1.92x faster                                                 |
| richards_super           | 94.7 ms                                                | 49.4 ms: 1.92x faster                                                |
| deepcopy                 | 479 us                                                 | 254 us: 1.89x faster                                                 |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.85x faster                                                 |
| richards                 | 79.3 ms                                                | 43.6 ms: 1.82x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 68.2 ms: 1.73x faster                                                |
| crypto_pyaes             | 128 ms                                                 | 73.9 ms: 1.73x faster                                                |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                |
| float                    | 117 ms                                                 | 69.1 ms: 1.70x faster                                                |
| hexiom                   | 10.4 ms                                                | 6.32 ms: 1.64x faster                                                |
| nbody                    | 154 ms                                                 | 94.6 ms: 1.62x faster                                                |
| pyflate                  | 716 ms                                                 | 447 ms: 1.60x faster                                                 |
| spectral_norm            | 170 ms                                                 | 106 ms: 1.60x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.59x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                |
| django_template          | 48.2 ms                                                | 31.3 ms: 1.54x faster                                                |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                 |
| genshi_text              | 31.8 ms                                                | 21.0 ms: 1.51x faster                                                |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                                 |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.49x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.60 us: 1.48x faster                                                |
| html5lib                 | 88.9 ms                                                | 60.5 ms: 1.47x faster                                                |
| logging_format           | 9.09 us                                                | 6.25 us: 1.45x faster                                                |
| coroutines               | 35.1 ms                                                | 24.2 ms: 1.45x faster                                                |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 719 ms: 1.42x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 59.7 ms: 1.41x faster                                                |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                               |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.1 ms: 1.37x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 19.3 ms: 1.34x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.86 ms: 1.33x faster                                                |
| 2to3                     | 348 ms                                                 | 262 ms: 1.33x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                |
| nqueens                  | 106 ms                                                 | 81.1 ms: 1.30x faster                                                |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                 |
| scimark_fft              | 466 ms                                                 | 358 ms: 1.30x faster                                                 |
| sympy_str                | 346 ms                                                 | 271 ms: 1.27x faster                                                 |
| sqlalchemy_declarative   | 172 ms                                                 | 137 ms: 1.26x faster                                                 |
| fannkuch                 | 532 ms                                                 | 425 ms: 1.25x faster                                                 |
| sympy_expand             | 566 ms                                                 | 463 ms: 1.22x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 22.7 ms: 1.22x faster                                                |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.22x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 84.4 ms: 1.18x faster                                                |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                                |
| json_dumps               | 14.2 ms                                                | 12.1 ms: 1.17x faster                                                |
| regex_effbot             | 3.63 ms                                                | 3.15 ms: 1.15x faster                                                |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                 |
| regex_dna                | 227 ms                                                 | 203 ms: 1.12x faster                                                 |
| async_generators         | 444 ms                                                 | 401 ms: 1.11x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 892 us: 1.11x faster                                                 |
| python_startup           | 14.6 ms                                                | 13.3 ms: 1.10x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.84 us: 1.07x faster                                                |
| json                     | 5.69 ms                                                | 5.36 ms: 1.06x faster                                                |
| json_loads               | 31.2 us                                                | 29.5 us: 1.06x faster                                                |
| docutils                 | 3.30 sec                                               | 3.21 sec: 1.03x faster                                               |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                 |
| pidigits                 | 191 ms                                                 | 198 ms: 1.04x slower                                                 |
| telco                    | 7.27 ms                                                | 7.86 ms: 1.08x slower                                                |
| coverage                 | 79.4 ms                                                | 88.4 ms: 1.11x slower                                                |
| python_startup_no_site   | 5.93 ms                                                | 8.24 ms: 1.39x slower                                                |
| gc_traversal             | 3.62 ms                                                | 5.11 ms: 1.41x slower                                                |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                                |
| bench_mp_pool            | 24.0 ms                                                | 82.1 ms: 3.42x slower                                                |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                         |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250415-3.14.0a7+-661a2b8/bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.445x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.36x