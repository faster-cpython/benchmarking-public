# Results vs. 3.10.4

- fork: faster-cpython
- ref: tos_caching_1
- machine: linux-x86_64
- commit hash: 5bbc96e
- commit date: 2025-04-08
- overall geometric mean: 1.501x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 245 ms: 1.42x faster                                                      |
| docutils       | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                    |
| html5lib       | 88.9 ms                                                | 58.5 ms: 1.52x faster                                                     |
| Geometric mean | (ref)                                                  | 1.40x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 605 ms: 2.92x faster                                                      |
| async_tree_none         | 728 ms                                                 | 257 ms: 2.83x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 309 ms: 2.81x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 488 ms: 2.08x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.64x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.1 ms: 1.87x faster                                                     |
| float          | 117 ms                                                 | 66.9 ms: 1.75x faster                                                     |
| pidigits       | 191 ms                                                 | 202 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                  | 1.46x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                                      |
| regex_v8       | 27.8 ms                                                | 22.3 ms: 1.25x faster                                                     |
| regex_effbot   | 3.63 ms                                                | 3.06 ms: 1.19x faster                                                     |
| regex_dna      | 227 ms                                                 | 191 ms: 1.18x faster                                                      |
| Geometric mean | (ref)                                                  | 1.27x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.84 sec: 1.71x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 309 us: 1.57x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 220 us: 1.50x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 60.7 ms: 1.30x faster                                                     |
| json_dumps           | 14.2 ms                                                | 12.3 ms: 1.15x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 87.9 ms: 1.13x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 103 ms: 1.12x faster                                                      |
| json_loads           | 31.2 us                                                | 28.3 us: 1.10x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 162 ms: 1.04x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.27x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 8.12 ms: 1.37x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.0 ms: 1.52x faster                                                     |
| django_template | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                     |
| mako            | 16.3 ms                                                | 11.6 ms: 1.40x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 47.4 ms: 1.39x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 157 us: 3.47x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 605 ms: 2.92x faster                                                      |
| generators               | 80.1 ms                                                | 28.0 ms: 2.86x faster                                                     |
| async_tree_none          | 728 ms                                                 | 257 ms: 2.83x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 309 ms: 2.81x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.01 ms: 2.63x faster                                                     |
| mdp                      | 2.85 sec                                               | 1.21 sec: 2.35x faster                                                    |
| go                       | 240 ms                                                 | 108 ms: 2.22x faster                                                      |
| logging_silent           | 190 ns                                                 | 88.7 ns: 2.14x faster                                                     |
| chaos                    | 115 ms                                                 | 54.6 ms: 2.12x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 488 ms: 2.08x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 58.6 ms: 2.02x faster                                                     |
| raytrace                 | 507 ms                                                 | 252 ms: 2.02x faster                                                      |
| scimark_sor              | 220 ms                                                 | 109 ms: 2.01x faster                                                      |
| richards_super           | 94.7 ms                                                | 47.0 ms: 2.01x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 29.1 us: 2.01x faster                                                     |
| pylint                   | 551 ms                                                 | 274 ms: 2.01x faster                                                      |
| deepcopy                 | 479 us                                                 | 247 us: 1.94x faster                                                      |
| richards                 | 79.3 ms                                                | 41.1 ms: 1.93x faster                                                     |
| nbody                    | 154 ms                                                 | 82.1 ms: 1.87x faster                                                     |
| comprehensions           | 28.8 us                                                | 15.6 us: 1.85x faster                                                     |
| spectral_norm            | 170 ms                                                 | 93.5 ms: 1.82x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 71.7 ms: 1.78x faster                                                     |
| hexiom                   | 10.4 ms                                                | 5.86 ms: 1.77x faster                                                     |
| pyflate                  | 716 ms                                                 | 407 ms: 1.76x faster                                                      |
| float                    | 117 ms                                                 | 66.9 ms: 1.75x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.84 sec: 1.71x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 3.81 ms: 1.70x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.57 us: 1.62x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 309 us: 1.57x faster                                                      |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                      |
| scimark_fft              | 466 ms                                                 | 303 ms: 1.54x faster                                                      |
| genshi_text              | 31.8 ms                                                | 21.0 ms: 1.52x faster                                                     |
| html5lib                 | 88.9 ms                                                | 58.5 ms: 1.52x faster                                                     |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                     |
| django_template          | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 220 us: 1.50x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.53 us: 1.50x faster                                                     |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                                      |
| logging_format           | 9.09 us                                                | 6.11 us: 1.49x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 58.2 ms: 1.45x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.09 sec: 1.44x faster                                                    |
| 2to3                     | 348 ms                                                 | 245 ms: 1.42x faster                                                      |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.5 ms: 1.41x faster                                                     |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.40x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 47.4 ms: 1.39x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 18.6 ms: 1.39x faster                                                     |
| pathlib                  | 20.5 ms                                                | 15.1 ms: 1.36x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                                    |
| sympy_sum                | 196 ms                                                 | 146 ms: 1.35x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 758 ms: 1.34x faster                                                      |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.34x faster                                                      |
| nqueens                  | 106 ms                                                 | 78.8 ms: 1.34x faster                                                     |
| fannkuch                 | 532 ms                                                 | 396 ms: 1.34x faster                                                      |
| sympy_str                | 346 ms                                                 | 265 ms: 1.31x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 60.7 ms: 1.30x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.58 sec: 1.28x faster                                                    |
| regex_v8                 | 27.8 ms                                                | 22.3 ms: 1.25x faster                                                     |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.06 ms: 1.19x faster                                                     |
| regex_dna                | 227 ms                                                 | 191 ms: 1.18x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 848 us: 1.16x faster                                                      |
| json_dumps               | 14.2 ms                                                | 12.3 ms: 1.15x faster                                                     |
| async_generators         | 444 ms                                                 | 386 ms: 1.15x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.66 us: 1.14x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 87.9 ms: 1.13x faster                                                     |
| python_startup           | 14.6 ms                                                | 13.0 ms: 1.12x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 103 ms: 1.12x faster                                                      |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                      |
| json_loads               | 31.2 us                                                | 28.3 us: 1.10x faster                                                     |
| json                     | 5.69 ms                                                | 5.24 ms: 1.09x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 162 ms: 1.04x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                      |
| telco                    | 7.27 ms                                                | 7.38 ms: 1.02x slower                                                     |
| coverage                 | 79.4 ms                                                | 82.1 ms: 1.03x slower                                                     |
| pidigits                 | 191 ms                                                 | 202 ms: 1.06x slower                                                      |
| gc_traversal             | 3.62 ms                                                | 4.94 ms: 1.36x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 8.12 ms: 1.37x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.51 ms: 1.55x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 80.9 ms: 3.37x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.47x faster                                                              |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250408-3.14.0a6+-5bbc96e-CLANG/bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.501x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.39x
- 95% likely to have a speedup of 1.37x
- 99% likely to have a speedup of 1.35x

# Memory
- memory change: 1.28x