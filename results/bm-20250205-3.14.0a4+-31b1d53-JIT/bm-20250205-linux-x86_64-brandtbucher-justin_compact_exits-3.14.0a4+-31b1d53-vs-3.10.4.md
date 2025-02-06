# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_compact_exits
- machine: linux-x86_64
- commit hash: 31b1d53
- commit date: 2025-02-05
- overall geometric mean: 1.446x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                                         |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                       |
| html5lib       | 88.9 ms                                                | 61.4 ms: 1.45x faster                                                        |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 626 ms: 2.82x faster                                                         |
| async_tree_none         | 728 ms                                                 | 269 ms: 2.70x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 331 ms: 2.63x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 501 ms: 2.03x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.53x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 67.6 ms: 1.73x faster                                                        |
| nbody          | 154 ms                                                 | 94.8 ms: 1.62x faster                                                        |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.42x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.46x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.12 ms: 1.16x faster                                                        |
| regex_v8       | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                        |
| regex_dna      | 227 ms                                                 | 210 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                  | 1.20x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.81 sec: 1.73x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 194 us: 1.70x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 318 us: 1.52x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 57.0 ms: 1.39x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 79.6 ms: 1.25x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 137 ms: 1.22x faster                                                         |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 95.7 ms: 1.21x faster                                                        |
| json_loads           | 31.2 us                                                | 29.0 us: 1.07x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                        |
| django_template | 48.2 ms                                                | 32.8 ms: 1.47x faster                                                        |
| genshi_text     | 31.8 ms                                                | 23.2 ms: 1.37x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 56.7 ms: 1.17x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.39x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 626 ms: 2.82x faster                                                         |
| async_tree_none          | 728 ms                                                 | 269 ms: 2.70x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 331 ms: 2.63x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.40 ms: 2.33x faster                                                        |
| generators               | 80.1 ms                                                | 36.2 ms: 2.21x faster                                                        |
| richards_super           | 94.7 ms                                                | 46.1 ms: 2.05x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 501 ms: 2.03x faster                                                         |
| pylint                   | 551 ms                                                 | 277 ms: 1.99x faster                                                         |
| richards                 | 79.3 ms                                                | 39.9 ms: 1.98x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 29.9 us: 1.95x faster                                                        |
| chaos                    | 115 ms                                                 | 59.4 ms: 1.95x faster                                                        |
| scimark_sor              | 220 ms                                                 | 113 ms: 1.94x faster                                                         |
| go                       | 240 ms                                                 | 125 ms: 1.93x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 63.0 ms: 1.88x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 70.0 ms: 1.83x faster                                                        |
| deepcopy                 | 479 us                                                 | 269 us: 1.78x faster                                                         |
| raytrace                 | 507 ms                                                 | 286 ms: 1.77x faster                                                         |
| tomli_loads              | 3.14 sec                                               | 1.81 sec: 1.73x faster                                                       |
| spectral_norm            | 170 ms                                                 | 98.0 ms: 1.73x faster                                                        |
| float                    | 117 ms                                                 | 67.6 ms: 1.73x faster                                                        |
| logging_silent           | 190 ns                                                 | 110 ns: 1.73x faster                                                         |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.73x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.26 ms: 1.72x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 194 us: 1.70x faster                                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.57 ms: 1.64x faster                                                        |
| nbody                    | 154 ms                                                 | 94.8 ms: 1.62x faster                                                        |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.62x faster                                                        |
| pyflate                  | 716 ms                                                 | 448 ms: 1.60x faster                                                         |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 318 us: 1.52x faster                                                         |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.50x faster                                                        |
| coroutines               | 35.1 ms                                                | 23.4 ms: 1.50x faster                                                        |
| logging_format           | 9.09 us                                                | 6.12 us: 1.49x faster                                                        |
| django_template          | 48.2 ms                                                | 32.8 ms: 1.47x faster                                                        |
| scimark_fft              | 466 ms                                                 | 318 ms: 1.47x faster                                                         |
| regex_compile            | 188 ms                                                 | 130 ms: 1.46x faster                                                         |
| html5lib                 | 88.9 ms                                                | 61.4 ms: 1.45x faster                                                        |
| hexiom                   | 10.4 ms                                                | 7.28 ms: 1.43x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.56 ms: 1.42x faster                                                        |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.6 ms: 1.40x faster                                                        |
| thrift                   | 1.07 ms                                                | 765 us: 1.40x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 57.0 ms: 1.39x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.39x faster                                                       |
| fannkuch                 | 532 ms                                                 | 386 ms: 1.38x faster                                                         |
| genshi_text              | 31.8 ms                                                | 23.2 ms: 1.37x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.37x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 746 ms: 1.36x faster                                                         |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.33x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                                         |
| sqlglot_optimize         | 69.2 ms                                                | 53.1 ms: 1.30x faster                                                        |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                         |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.28x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 20.1 ms: 1.28x faster                                                        |
| sympy_str                | 346 ms                                                 | 271 ms: 1.28x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 66.8 ms: 1.26x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 79.6 ms: 1.25x faster                                                        |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 137 ms: 1.22x faster                                                         |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 95.7 ms: 1.21x faster                                                        |
| nqueens                  | 106 ms                                                 | 90.7 ms: 1.17x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 56.7 ms: 1.17x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.12 ms: 1.16x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 24.3 ms: 1.14x faster                                                        |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 891 us: 1.11x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.10x faster                                                        |
| json                     | 5.69 ms                                                | 5.18 ms: 1.10x faster                                                        |
| async_generators         | 444 ms                                                 | 406 ms: 1.09x faster                                                         |
| regex_dna                | 227 ms                                                 | 210 ms: 1.08x faster                                                         |
| json_loads               | 31.2 us                                                | 29.0 us: 1.07x faster                                                        |
| meteor_contest           | 120 ms                                                 | 112 ms: 1.07x faster                                                         |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                         |
| telco                    | 7.27 ms                                                | 7.49 ms: 1.03x slower                                                        |
| coverage                 | 79.4 ms                                                | 89.8 ms: 1.13x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.79 ms: 1.32x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 80.5 ms: 3.35x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                 |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250205-3.14.0a4+-31b1d53-JIT/bm-20250205-linux-x86_64-brandtbucher-justin_compact_exits-3.14.0a4+-31b1d53.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.446x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x