# Results vs. 3.10.4

- fork: faster-cpython
- ref: better_instrument_fo
- machine: linux-x86_64
- commit hash: 182c512
- commit date: 2024-12-31
- overall geometric mean: 1.438x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                                             |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                           |
| html5lib       | 88.9 ms                                                | 62.5 ms: 1.42x faster                                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 616 ms: 2.87x faster                                                             |
| async_tree_none         | 728 ms                                                 | 264 ms: 2.75x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 329 ms: 2.64x faster                                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 482 ms: 2.11x faster                                                             |
| Geometric mean          | (ref)                                                  | 2.58x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 95.9 ms: 1.60x faster                                                            |
| float          | 117 ms                                                 | 73.2 ms: 1.60x faster                                                            |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                  | 1.38x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.48x faster                                                             |
| regex_effbot   | 3.63 ms                                                | 3.28 ms: 1.11x faster                                                            |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                            |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                  | 1.16x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.01 sec: 1.57x faster                                                           |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                                             |
| pickle_pure_python   | 484 us                                                 | 320 us: 1.51x faster                                                             |
| xml_etree_process    | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                            |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 137 ms: 1.23x faster                                                             |
| xml_etree_iterparse  | 115 ms                                                 | 97.0 ms: 1.19x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 84.1 ms: 1.18x faster                                                            |
| json_loads           | 31.2 us                                                | 26.5 us: 1.18x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                            |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.0 ms: 1.51x faster                                                            |
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                            |
| genshi_text     | 31.8 ms                                                | 22.4 ms: 1.42x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 162 us: 3.36x faster                                                             |
| generators               | 80.1 ms                                                | 27.6 ms: 2.90x faster                                                            |
| async_tree_io            | 1.77 sec                                               | 616 ms: 2.87x faster                                                             |
| async_tree_none          | 728 ms                                                 | 264 ms: 2.75x faster                                                             |
| async_tree_memoization   | 870 ms                                                 | 329 ms: 2.64x faster                                                             |
| deltablue                | 7.91 ms                                                | 3.26 ms: 2.43x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 482 ms: 2.11x faster                                                             |
| go                       | 240 ms                                                 | 117 ms: 2.04x faster                                                             |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                                             |
| chaos                    | 115 ms                                                 | 60.5 ms: 1.91x faster                                                            |
| deepcopy_memo            | 58.5 us                                                | 30.7 us: 1.91x faster                                                            |
| richards_super           | 94.7 ms                                                | 50.5 ms: 1.87x faster                                                            |
| raytrace                 | 507 ms                                                 | 272 ms: 1.87x faster                                                             |
| deepcopy                 | 479 us                                                 | 258 us: 1.85x faster                                                             |
| richards                 | 79.3 ms                                                | 43.6 ms: 1.82x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 71.4 ms: 1.79x faster                                                            |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.78x faster                                                             |
| djangocms                | 38.4 us                                                | 21.7 us: 1.77x faster                                                            |
| logging_silent           | 190 ns                                                 | 108 ns: 1.76x faster                                                             |
| scimark_monte_carlo      | 118 ms                                                 | 67.7 ms: 1.75x faster                                                            |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.28 ms: 1.66x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                            |
| spectral_norm            | 170 ms                                                 | 105 ms: 1.61x faster                                                             |
| nbody                    | 154 ms                                                 | 95.9 ms: 1.60x faster                                                            |
| float                    | 117 ms                                                 | 73.2 ms: 1.60x faster                                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.65 us: 1.57x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 2.01 sec: 1.57x faster                                                           |
| pyflate                  | 716 ms                                                 | 459 ms: 1.56x faster                                                             |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                                             |
| pickle_pure_python       | 484 us                                                 | 320 us: 1.51x faster                                                             |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                            |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                             |
| django_template          | 48.2 ms                                                | 32.0 ms: 1.51x faster                                                            |
| logging_simple           | 8.30 us                                                | 5.61 us: 1.48x faster                                                            |
| logging_format           | 9.09 us                                                | 6.16 us: 1.48x faster                                                            |
| regex_compile            | 188 ms                                                 | 128 ms: 1.48x faster                                                             |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                            |
| html5lib                 | 88.9 ms                                                | 62.5 ms: 1.42x faster                                                            |
| genshi_text              | 31.8 ms                                                | 22.4 ms: 1.42x faster                                                            |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                           |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.5 ms: 1.42x faster                                                            |
| thrift                   | 1.07 ms                                                | 767 us: 1.40x faster                                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.64 ms: 1.40x faster                                                            |
| pprint_safe_repr         | 1.02 sec                                               | 733 ms: 1.39x faster                                                             |
| sqlglot_normalize        | 143 ms                                                 | 104 ms: 1.37x faster                                                             |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                                             |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                                           |
| xml_etree_process        | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                            |
| scimark_fft              | 466 ms                                                 | 346 ms: 1.34x faster                                                             |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.33x faster                                                             |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                             |
| genshi_xml               | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                            |
| dulwich_log              | 84.3 ms                                                | 64.1 ms: 1.32x faster                                                            |
| sqlglot_optimize         | 69.2 ms                                                | 52.7 ms: 1.31x faster                                                            |
| nqueens                  | 106 ms                                                 | 81.3 ms: 1.30x faster                                                            |
| fannkuch                 | 532 ms                                                 | 410 ms: 1.30x faster                                                             |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.29x faster                                                            |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                                             |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                            |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                           |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                            |
| sympy_expand             | 566 ms                                                 | 455 ms: 1.24x faster                                                             |
| xml_etree_parse          | 168 ms                                                 | 137 ms: 1.23x faster                                                             |
| xml_etree_iterparse      | 115 ms                                                 | 97.0 ms: 1.19x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 84.1 ms: 1.18x faster                                                            |
| json_loads               | 31.2 us                                                | 26.5 us: 1.18x faster                                                            |
| json                     | 5.69 ms                                                | 4.94 ms: 1.15x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 865 us: 1.14x faster                                                             |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                            |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                             |
| mdp                      | 2.85 sec                                               | 2.54 sec: 1.12x faster                                                           |
| regex_effbot             | 3.63 ms                                                | 3.28 ms: 1.11x faster                                                            |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                                            |
| async_generators         | 444 ms                                                 | 421 ms: 1.05x faster                                                             |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                             |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                             |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                             |
| coverage                 | 79.4 ms                                                | 83.4 ms: 1.05x slower                                                            |
| mypy2                    | 894 ms                                                 | 944 ms: 1.06x slower                                                             |
| telco                    | 7.27 ms                                                | 7.74 ms: 1.07x slower                                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                            |
| gc_traversal             | 3.62 ms                                                | 4.95 ms: 1.36x slower                                                            |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                                            |
| bench_mp_pool            | 24.0 ms                                                | 82.2 ms: 3.42x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                                     |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241231-3.14.0a3+-182c512/bm-20241231-linux-x86_64-faster%2dcpython-better_instrument_fo-3.14.0a3+-182c512.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.438x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.27x