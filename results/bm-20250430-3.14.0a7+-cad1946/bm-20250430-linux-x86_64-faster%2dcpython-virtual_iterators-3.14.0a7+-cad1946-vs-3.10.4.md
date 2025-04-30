# Results vs. 3.10.4

- fork: faster-cpython
- ref: virtual_iterators
- machine: linux-x86_64
- commit hash: cad1946
- commit date: 2025-04-30
- overall geometric mean: 1.452x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 252 ms: 1.38x faster                                                          |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                        |
| html5lib       | 88.9 ms                                                | 60.9 ms: 1.46x faster                                                         |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 598 ms: 2.96x faster                                                          |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                          |
| async_tree_memoization  | 870 ms                                                 | 316 ms: 2.75x faster                                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 495 ms: 2.05x faster                                                          |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.4 ms: 1.66x faster                                                         |
| nbody          | 154 ms                                                 | 98.8 ms: 1.55x faster                                                         |
| pidigits       | 191 ms                                                 | 190 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                                          |
| regex_v8       | 27.8 ms                                                | 22.3 ms: 1.24x faster                                                         |
| regex_effbot   | 3.63 ms                                                | 3.10 ms: 1.17x faster                                                         |
| regex_dna      | 227 ms                                                 | 205 ms: 1.11x faster                                                          |
| Geometric mean | (ref)                                                  | 1.24x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.01 sec: 1.56x faster                                                        |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                          |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                          |
| xml_etree_process    | 79.1 ms                                                | 59.7 ms: 1.33x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                                          |
| json_dumps           | 14.2 ms                                                | 12.1 ms: 1.17x faster                                                         |
| xml_etree_generate   | 99.4 ms                                                | 85.5 ms: 1.16x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 99.3 ms: 1.16x faster                                                         |
| json_loads           | 31.2 us                                                | 30.4 us: 1.03x faster                                                         |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                         |
| python_startup_no_site | 5.93 ms                                                | 6.92 ms: 1.17x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.0 ms: 1.52x faster                                                         |
| django_template | 48.2 ms                                                | 32.0 ms: 1.50x faster                                                         |
| mako            | 16.3 ms                                                | 11.7 ms: 1.40x faster                                                         |
| genshi_xml      | 66.0 ms                                                | 49.2 ms: 1.34x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.37x faster                                                          |
| async_tree_io            | 1.77 sec                                               | 598 ms: 2.96x faster                                                          |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                          |
| async_tree_memoization   | 870 ms                                                 | 316 ms: 2.75x faster                                                          |
| generators               | 80.1 ms                                                | 29.4 ms: 2.72x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.36 ms: 2.35x faster                                                         |
| mdp                      | 2.85 sec                                               | 1.22 sec: 2.34x faster                                                        |
| go                       | 240 ms                                                 | 110 ms: 2.19x faster                                                          |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 495 ms: 2.05x faster                                                          |
| deepcopy_memo            | 58.5 us                                                | 28.9 us: 2.02x faster                                                         |
| chaos                    | 115 ms                                                 | 59.6 ms: 1.94x faster                                                         |
| logging_silent           | 190 ns                                                 | 98.3 ns: 1.93x faster                                                         |
| richards_super           | 94.7 ms                                                | 49.9 ms: 1.90x faster                                                         |
| raytrace                 | 507 ms                                                 | 268 ms: 1.89x faster                                                          |
| deepcopy                 | 479 us                                                 | 256 us: 1.87x faster                                                          |
| scimark_sor              | 220 ms                                                 | 119 ms: 1.84x faster                                                          |
| richards                 | 79.3 ms                                                | 43.1 ms: 1.84x faster                                                         |
| comprehensions           | 28.8 us                                                | 16.2 us: 1.78x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 68.0 ms: 1.74x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 75.1 ms: 1.70x faster                                                         |
| hexiom                   | 10.4 ms                                                | 6.14 ms: 1.69x faster                                                         |
| float                    | 117 ms                                                 | 70.4 ms: 1.66x faster                                                         |
| pyflate                  | 716 ms                                                 | 457 ms: 1.57x faster                                                          |
| tomli_loads              | 3.14 sec                                               | 2.01 sec: 1.56x faster                                                        |
| spectral_norm            | 170 ms                                                 | 109 ms: 1.56x faster                                                          |
| nbody                    | 154 ms                                                 | 98.8 ms: 1.55x faster                                                         |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                          |
| genshi_text              | 31.8 ms                                                | 21.0 ms: 1.52x faster                                                         |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                          |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                          |
| django_template          | 48.2 ms                                                | 32.0 ms: 1.50x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.78 us: 1.50x faster                                                         |
| logging_simple           | 8.30 us                                                | 5.57 us: 1.49x faster                                                         |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                                          |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                                         |
| html5lib                 | 88.9 ms                                                | 60.9 ms: 1.46x faster                                                         |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 715 ms: 1.42x faster                                                          |
| coroutines               | 35.1 ms                                                | 24.8 ms: 1.42x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 59.7 ms: 1.41x faster                                                         |
| mako                     | 16.3 ms                                                | 11.7 ms: 1.40x faster                                                         |
| 2to3                     | 348 ms                                                 | 252 ms: 1.38x faster                                                          |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.1 ms: 1.36x faster                                                         |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 49.2 ms: 1.34x faster                                                         |
| xml_etree_process        | 79.1 ms                                                | 59.7 ms: 1.33x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                                          |
| nqueens                  | 106 ms                                                 | 81.7 ms: 1.30x faster                                                         |
| fannkuch                 | 532 ms                                                 | 418 ms: 1.27x faster                                                          |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                        |
| scimark_fft              | 466 ms                                                 | 372 ms: 1.25x faster                                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.18 ms: 1.25x faster                                                         |
| regex_v8                 | 27.8 ms                                                | 22.3 ms: 1.24x faster                                                         |
| pathlib                  | 20.5 ms                                                | 17.1 ms: 1.19x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                                          |
| json_dumps               | 14.2 ms                                                | 12.1 ms: 1.17x faster                                                         |
| regex_effbot             | 3.63 ms                                                | 3.10 ms: 1.17x faster                                                         |
| xml_etree_generate       | 99.4 ms                                                | 85.5 ms: 1.16x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 99.3 ms: 1.16x faster                                                         |
| meteor_contest           | 120 ms                                                 | 105 ms: 1.13x faster                                                          |
| bench_thread_pool        | 986 us                                                 | 885 us: 1.11x faster                                                          |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                                         |
| regex_dna                | 227 ms                                                 | 205 ms: 1.11x faster                                                          |
| async_generators         | 444 ms                                                 | 410 ms: 1.08x faster                                                          |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.05x faster                                                         |
| json                     | 5.69 ms                                                | 5.49 ms: 1.04x faster                                                         |
| json_loads               | 31.2 us                                                | 30.4 us: 1.03x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 551 ms: 1.01x faster                                                          |
| pidigits                 | 191 ms                                                 | 190 ms: 1.00x faster                                                          |
| telco                    | 7.27 ms                                                | 7.93 ms: 1.09x slower                                                         |
| python_startup_no_site   | 5.93 ms                                                | 6.92 ms: 1.17x slower                                                         |
| coverage                 | 79.4 ms                                                | 93.2 ms: 1.17x slower                                                         |
| gc_traversal             | 3.62 ms                                                | 4.82 ms: 1.33x slower                                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.48 ms: 1.53x slower                                                         |
| bench_mp_pool            | 24.0 ms                                                | 82.5 ms: 3.43x slower                                                         |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                                  |
Ignored benchmarks (26) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (23) of results/bm-20250430-3.14.0a7+-cad1946/bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946.json: async_tree_cpu_io_mixed_tg, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.452x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.37x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.28x