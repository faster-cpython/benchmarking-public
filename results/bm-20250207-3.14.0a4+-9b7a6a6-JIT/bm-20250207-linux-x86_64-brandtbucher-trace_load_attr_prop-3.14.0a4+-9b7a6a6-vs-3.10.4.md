# Results vs. 3.10.4

- fork: brandtbucher
- ref: trace_load_attr_prop
- machine: linux-x86_64
- commit hash: 9b7a6a6
- commit date: 2025-02-07
- overall geometric mean: 1.447x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4+-9b7a6a6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.34x faster                                                         |
| docutils       | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                       |
| html5lib       | 88.9 ms                                                | 62.2 ms: 1.43x faster                                                        |
| Geometric mean | (ref)                                                  | 1.33x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4+-9b7a6a6 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 626 ms: 2.83x faster                                                         |
| async_tree_none         | 728 ms                                                 | 270 ms: 2.70x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 329 ms: 2.64x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 492 ms: 2.07x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.54x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4+-9b7a6a6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.7 ms: 1.66x faster                                                        |
| nbody          | 154 ms                                                 | 96.5 ms: 1.59x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.39x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4+-9b7a6a6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 125 ms: 1.51x faster                                                         |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.24 ms: 1.12x faster                                                        |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                  | 1.20x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4+-9b7a6a6 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.84 sec: 1.71x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 200 us: 1.65x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 326 us: 1.49x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 55.0 ms: 1.44x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 78.7 ms: 1.26x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.21x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 96.1 ms: 1.20x faster                                                        |
| json_loads           | 31.2 us                                                | 29.1 us: 1.07x faster                                                        |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4+-9b7a6a6 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4+-9b7a6a6 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                        |
| django_template | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                        |
| genshi_text     | 31.8 ms                                                | 22.2 ms: 1.44x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 50.0 ms: 1.32x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4+-9b7a6a6 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 626 ms: 2.83x faster                                                         |
| generators               | 80.1 ms                                                | 28.7 ms: 2.79x faster                                                        |
| async_tree_none          | 728 ms                                                 | 270 ms: 2.70x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 329 ms: 2.64x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.26 ms: 2.43x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 492 ms: 2.07x faster                                                         |
| go                       | 240 ms                                                 | 118 ms: 2.03x faster                                                         |
| pylint                   | 551 ms                                                 | 279 ms: 1.98x faster                                                         |
| chaos                    | 115 ms                                                 | 59.1 ms: 1.95x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 30.4 us: 1.92x faster                                                        |
| richards_super           | 94.7 ms                                                | 49.8 ms: 1.90x faster                                                        |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                                         |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                         |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 70.5 ms: 1.81x faster                                                        |
| spectral_norm            | 170 ms                                                 | 93.9 ms: 1.81x faster                                                        |
| richards                 | 79.3 ms                                                | 43.8 ms: 1.81x faster                                                        |
| logging_silent           | 190 ns                                                 | 107 ns: 1.78x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 67.0 ms: 1.76x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.84 sec: 1.71x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                        |
| comprehensions           | 28.8 us                                                | 17.3 us: 1.66x faster                                                        |
| float                    | 117 ms                                                 | 70.7 ms: 1.66x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 200 us: 1.65x faster                                                         |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                                        |
| nbody                    | 154 ms                                                 | 96.5 ms: 1.59x faster                                                        |
| hexiom                   | 10.4 ms                                                | 6.70 ms: 1.55x faster                                                        |
| pyflate                  | 716 ms                                                 | 462 ms: 1.55x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                        |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                         |
| regex_compile            | 188 ms                                                 | 125 ms: 1.51x faster                                                         |
| django_template          | 48.2 ms                                                | 32.1 ms: 1.50x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.54 us: 1.50x faster                                                        |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.50x faster                                                        |
| scimark_fft              | 466 ms                                                 | 313 ms: 1.49x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 326 us: 1.49x faster                                                         |
| logging_format           | 9.09 us                                                | 6.16 us: 1.48x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 55.0 ms: 1.44x faster                                                        |
| genshi_text              | 31.8 ms                                                | 22.2 ms: 1.44x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.53 ms: 1.43x faster                                                        |
| html5lib                 | 88.9 ms                                                | 62.2 ms: 1.43x faster                                                        |
| thrift                   | 1.07 ms                                                | 756 us: 1.42x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                                       |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.7 ms: 1.40x faster                                                        |
| 2to3                     | 348 ms                                                 | 259 ms: 1.34x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                         |
| fannkuch                 | 532 ms                                                 | 397 ms: 1.34x faster                                                         |
| pprint_safe_repr         | 1.02 sec                                               | 761 ms: 1.34x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.58 sec: 1.33x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 50.0 ms: 1.32x faster                                                        |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                                         |
| sympy_sum                | 196 ms                                                 | 151 ms: 1.30x faster                                                         |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 53.7 ms: 1.29x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 20.1 ms: 1.28x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 66.2 ms: 1.27x faster                                                        |
| sympy_str                | 346 ms                                                 | 273 ms: 1.27x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 78.7 ms: 1.26x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.68 sec: 1.23x faster                                                       |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.21x faster                                                         |
| sympy_expand             | 566 ms                                                 | 467 ms: 1.21x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 96.1 ms: 1.20x faster                                                        |
| nqueens                  | 106 ms                                                 | 89.5 ms: 1.18x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                                        |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| regex_effbot             | 3.63 ms                                                | 3.24 ms: 1.12x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 886 us: 1.11x faster                                                         |
| sqlite_synth             | 3.02 us                                                | 2.72 us: 1.11x faster                                                        |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                         |
| async_generators         | 444 ms                                                 | 407 ms: 1.09x faster                                                         |
| json                     | 5.69 ms                                                | 5.27 ms: 1.08x faster                                                        |
| json_loads               | 31.2 us                                                | 29.1 us: 1.07x faster                                                        |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                         |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                         |
| telco                    | 7.27 ms                                                | 7.71 ms: 1.06x slower                                                        |
| coverage                 | 79.4 ms                                                | 91.3 ms: 1.15x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.76 ms: 1.31x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 80.8 ms: 3.37x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                 |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250207-3.14.0a4+-9b7a6a6-JIT/bm-20250207-linux-x86_64-brandtbucher-trace_load_attr_prop-3.14.0a4+-9b7a6a6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.447x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x