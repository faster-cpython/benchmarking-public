# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_stackrefs_single
- machine: linux-x86_64
- commit hash: 916faf4
- commit date: 2025-03-07
- overall geometric mean: 1.439x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                             |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                           |
| html5lib       | 88.9 ms                                                | 61.6 ms: 1.44x faster                                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 616 ms: 2.87x faster                                                             |
| async_tree_none         | 728 ms                                                 | 267 ms: 2.73x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 331 ms: 2.63x faster                                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 489 ms: 2.08x faster                                                             |
| Geometric mean          | (ref)                                                  | 2.56x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.0 ms: 1.67x faster                                                            |
| nbody          | 154 ms                                                 | 98.1 ms: 1.56x faster                                                            |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                  | 1.38x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.50x faster                                                             |
| regex_v8       | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                            |
| regex_effbot   | 3.63 ms                                                | 3.50 ms: 1.04x faster                                                            |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                           |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                             |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                             |
| xml_etree_process    | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                            |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 83.8 ms: 1.19x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 100.0 ms: 1.15x faster                                                           |
| xml_etree_parse      | 168 ms                                                 | 150 ms: 1.12x faster                                                             |
| json_loads           | 31.2 us                                                | 29.9 us: 1.05x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.12x faster                                                            |
| python_startup_no_site | 5.93 ms                                                | 7.19 ms: 1.21x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.8 ms: 1.52x faster                                                            |
| genshi_text     | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                            |
| mako            | 16.3 ms                                                | 11.8 ms: 1.39x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.35x faster                                                             |
| async_tree_io            | 1.77 sec                                               | 616 ms: 2.87x faster                                                             |
| generators               | 80.1 ms                                                | 28.2 ms: 2.84x faster                                                            |
| async_tree_none          | 728 ms                                                 | 267 ms: 2.73x faster                                                             |
| async_tree_memoization   | 870 ms                                                 | 331 ms: 2.63x faster                                                             |
| deltablue                | 7.91 ms                                                | 3.12 ms: 2.54x faster                                                            |
| go                       | 240 ms                                                 | 114 ms: 2.11x faster                                                             |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 489 ms: 2.08x faster                                                             |
| deepcopy_memo            | 58.5 us                                                | 29.0 us: 2.02x faster                                                            |
| logging_silent           | 190 ns                                                 | 95.0 ns: 2.00x faster                                                            |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                                             |
| chaos                    | 115 ms                                                 | 59.7 ms: 1.93x faster                                                            |
| richards_super           | 94.7 ms                                                | 49.5 ms: 1.91x faster                                                            |
| raytrace                 | 507 ms                                                 | 269 ms: 1.88x faster                                                             |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                             |
| deepcopy                 | 479 us                                                 | 259 us: 1.85x faster                                                             |
| richards                 | 79.3 ms                                                | 43.2 ms: 1.84x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 67.8 ms: 1.74x faster                                                            |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                            |
| spectral_norm            | 170 ms                                                 | 98.8 ms: 1.72x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.70x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 75.4 ms: 1.70x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.15 ms: 1.69x faster                                                            |
| float                    | 117 ms                                                 | 70.0 ms: 1.67x faster                                                            |
| pyflate                  | 716 ms                                                 | 436 ms: 1.64x faster                                                             |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                           |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                            |
| nbody                    | 154 ms                                                 | 98.1 ms: 1.56x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                             |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                             |
| django_template          | 48.2 ms                                                | 31.8 ms: 1.52x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.51x faster                                                            |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                             |
| genshi_text              | 31.8 ms                                                | 21.2 ms: 1.50x faster                                                            |
| regex_compile            | 188 ms                                                 | 126 ms: 1.50x faster                                                             |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                            |
| coroutines               | 35.1 ms                                                | 24.1 ms: 1.46x faster                                                            |
| html5lib                 | 88.9 ms                                                | 61.6 ms: 1.44x faster                                                            |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                           |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.5 ms: 1.42x faster                                                            |
| pprint_safe_repr         | 1.02 sec                                               | 728 ms: 1.40x faster                                                             |
| thrift                   | 1.07 ms                                                | 770 us: 1.39x faster                                                             |
| mako                     | 16.3 ms                                                | 11.8 ms: 1.39x faster                                                            |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                             |
| sqlglot_normalize        | 143 ms                                                 | 105 ms: 1.36x faster                                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.76 ms: 1.36x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                            |
| scimark_fft              | 466 ms                                                 | 347 ms: 1.34x faster                                                             |
| genshi_xml               | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                            |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.33x faster                                                             |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.32x faster                                                           |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                             |
| sqlglot_optimize         | 69.2 ms                                                | 52.6 ms: 1.31x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 19.8 ms: 1.30x faster                                                            |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                                             |
| dulwich_log              | 84.3 ms                                                | 65.3 ms: 1.29x faster                                                            |
| fannkuch                 | 532 ms                                                 | 412 ms: 1.29x faster                                                             |
| nqueens                  | 106 ms                                                 | 83.8 ms: 1.26x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                           |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                            |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                                             |
| pathlib                  | 20.5 ms                                                | 17.1 ms: 1.20x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 83.8 ms: 1.19x faster                                                            |
| mdp                      | 2.85 sec                                               | 2.46 sec: 1.16x faster                                                           |
| xml_etree_iterparse      | 115 ms                                                 | 100.0 ms: 1.15x faster                                                           |
| bench_thread_pool        | 986 us                                                 | 871 us: 1.13x faster                                                             |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                             |
| xml_etree_parse          | 168 ms                                                 | 150 ms: 1.12x faster                                                             |
| async_generators         | 444 ms                                                 | 396 ms: 1.12x faster                                                             |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.12x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 25.0 ms: 1.11x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                                            |
| json                     | 5.69 ms                                                | 5.35 ms: 1.06x faster                                                            |
| json_loads               | 31.2 us                                                | 29.9 us: 1.05x faster                                                            |
| regex_effbot             | 3.63 ms                                                | 3.50 ms: 1.04x faster                                                            |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                             |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                             |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                                             |
| telco                    | 7.27 ms                                                | 7.82 ms: 1.08x slower                                                            |
| coverage                 | 79.4 ms                                                | 92.5 ms: 1.16x slower                                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.19 ms: 1.21x slower                                                            |
| gc_traversal             | 3.62 ms                                                | 4.87 ms: 1.34x slower                                                            |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                            |
| bench_mp_pool            | 24.0 ms                                                | 82.2 ms: 3.42x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                                     |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250307-3.14.0a5+-916faf4/bm-20250307-linux-x86_64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.439x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.27x