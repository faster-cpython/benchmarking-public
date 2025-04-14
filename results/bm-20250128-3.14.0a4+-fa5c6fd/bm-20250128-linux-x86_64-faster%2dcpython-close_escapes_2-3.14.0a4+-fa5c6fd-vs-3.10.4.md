# Results vs. 3.10.4

- fork: faster-cpython
- ref: close_escapes_2
- machine: linux-x86_64
- commit hash: fa5c6fd
- commit date: 2025-01-28
- overall geometric mean: 1.453x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                        |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                      |
| html5lib       | 88.9 ms                                                | 61.1 ms: 1.45x faster                                                       |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 615 ms: 2.88x faster                                                        |
| async_tree_none         | 728 ms                                                 | 262 ms: 2.78x faster                                                        |
| async_tree_memoization  | 870 ms                                                 | 321 ms: 2.71x faster                                                        |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 495 ms: 2.05x faster                                                        |
| Geometric mean          | (ref)                                                  | 2.58x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 70.4 ms: 1.66x faster                                                       |
| nbody          | 154 ms                                                 | 92.8 ms: 1.65x faster                                                       |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                  | 1.41x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 126 ms: 1.49x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.34 ms: 1.09x faster                                                       |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                       |
| regex_dna      | 227 ms                                                 | 211 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                  | 1.17x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                        |
| pickle_pure_python   | 484 us                                                 | 321 us: 1.51x faster                                                        |
| xml_etree_process    | 79.1 ms                                                | 60.1 ms: 1.32x faster                                                       |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.22x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                       |
| xml_etree_iterparse  | 115 ms                                                 | 97.9 ms: 1.18x faster                                                       |
| xml_etree_generate   | 99.4 ms                                                | 85.3 ms: 1.17x faster                                                       |
| json_loads           | 31.2 us                                                | 29.0 us: 1.08x faster                                                       |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                       |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.7 ms: 1.52x faster                                                       |
| genshi_text     | 31.8 ms                                                | 21.3 ms: 1.49x faster                                                       |
| mako            | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                       |
| genshi_xml      | 66.0 ms                                                | 49.0 ms: 1.35x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.45x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.40x faster                                                        |
| generators               | 80.1 ms                                                | 27.6 ms: 2.91x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 615 ms: 2.88x faster                                                        |
| async_tree_none          | 728 ms                                                 | 262 ms: 2.78x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 321 ms: 2.71x faster                                                        |
| deltablue                | 7.91 ms                                                | 3.21 ms: 2.46x faster                                                       |
| go                       | 240 ms                                                 | 116 ms: 2.07x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 495 ms: 2.05x faster                                                        |
| pylint                   | 551 ms                                                 | 274 ms: 2.01x faster                                                        |
| chaos                    | 115 ms                                                 | 58.1 ms: 1.99x faster                                                       |
| deepcopy_memo            | 58.5 us                                                | 30.4 us: 1.92x faster                                                       |
| richards_super           | 94.7 ms                                                | 49.6 ms: 1.91x faster                                                       |
| deepcopy                 | 479 us                                                 | 254 us: 1.89x faster                                                        |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                        |
| logging_silent           | 190 ns                                                 | 103 ns: 1.84x faster                                                        |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                                        |
| richards                 | 79.3 ms                                                | 43.5 ms: 1.82x faster                                                       |
| crypto_pyaes             | 128 ms                                                 | 71.7 ms: 1.78x faster                                                       |
| scimark_monte_carlo      | 118 ms                                                 | 66.6 ms: 1.78x faster                                                       |
| spectral_norm            | 170 ms                                                 | 96.5 ms: 1.76x faster                                                       |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.26 ms: 1.73x faster                                                       |
| hexiom                   | 10.4 ms                                                | 6.12 ms: 1.70x faster                                                       |
| float                    | 117 ms                                                 | 70.4 ms: 1.66x faster                                                       |
| nbody                    | 154 ms                                                 | 92.8 ms: 1.65x faster                                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.56 ms: 1.65x faster                                                       |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                                      |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.54x faster                                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                                       |
| pyflate                  | 716 ms                                                 | 466 ms: 1.54x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                        |
| django_template          | 48.2 ms                                                | 31.7 ms: 1.52x faster                                                       |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                       |
| logging_simple           | 8.30 us                                                | 5.50 us: 1.51x faster                                                       |
| pickle_pure_python       | 484 us                                                 | 321 us: 1.51x faster                                                        |
| logging_format           | 9.09 us                                                | 6.04 us: 1.51x faster                                                       |
| regex_compile            | 188 ms                                                 | 126 ms: 1.49x faster                                                        |
| genshi_text              | 31.8 ms                                                | 21.3 ms: 1.49x faster                                                       |
| html5lib                 | 88.9 ms                                                | 61.1 ms: 1.45x faster                                                       |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.45x faster                                                       |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.4 ms: 1.42x faster                                                       |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                      |
| thrift                   | 1.07 ms                                                | 759 us: 1.41x faster                                                        |
| pprint_safe_repr         | 1.02 sec                                               | 726 ms: 1.40x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.62 ms: 1.40x faster                                                       |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 104 ms: 1.37x faster                                                        |
| scimark_fft              | 466 ms                                                 | 340 ms: 1.37x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 49.0 ms: 1.35x faster                                                       |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.34x faster                                                      |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                        |
| fannkuch                 | 532 ms                                                 | 398 ms: 1.34x faster                                                        |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.33x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 63.7 ms: 1.32x faster                                                       |
| nqueens                  | 106 ms                                                 | 80.3 ms: 1.32x faster                                                       |
| xml_etree_process        | 79.1 ms                                                | 60.1 ms: 1.32x faster                                                       |
| sqlglot_optimize         | 69.2 ms                                                | 52.6 ms: 1.32x faster                                                       |
| sympy_integrate          | 25.8 ms                                                | 19.7 ms: 1.31x faster                                                       |
| pathlib                  | 20.5 ms                                                | 15.7 ms: 1.30x faster                                                       |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                                        |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                                      |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                                        |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.22x faster                                                        |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                       |
| xml_etree_iterparse      | 115 ms                                                 | 97.9 ms: 1.18x faster                                                       |
| xml_etree_generate       | 99.4 ms                                                | 85.3 ms: 1.17x faster                                                       |
| async_generators         | 444 ms                                                 | 381 ms: 1.16x faster                                                        |
| bench_thread_pool        | 986 us                                                 | 861 us: 1.14x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.49 sec: 1.14x faster                                                      |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                       |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                        |
| json                     | 5.69 ms                                                | 5.12 ms: 1.11x faster                                                       |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                                       |
| regex_effbot             | 3.63 ms                                                | 3.34 ms: 1.09x faster                                                       |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                       |
| json_loads               | 31.2 us                                                | 29.0 us: 1.08x faster                                                       |
| regex_dna                | 227 ms                                                 | 211 ms: 1.08x faster                                                        |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                        |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                        |
| telco                    | 7.27 ms                                                | 7.86 ms: 1.08x slower                                                       |
| coverage                 | 79.4 ms                                                | 91.5 ms: 1.15x slower                                                       |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                                       |
| gc_traversal             | 3.62 ms                                                | 4.88 ms: 1.35x slower                                                       |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                       |
| bench_mp_pool            | 24.0 ms                                                | 81.2 ms: 3.38x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.43x faster                                                                |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250128-3.14.0a4+-fa5c6fd/bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.453x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.26x