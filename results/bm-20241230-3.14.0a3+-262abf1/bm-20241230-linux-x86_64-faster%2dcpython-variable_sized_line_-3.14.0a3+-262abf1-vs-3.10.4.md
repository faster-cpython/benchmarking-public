# Results vs. 3.10.4

- fork: faster-cpython
- ref: variable_sized_line_
- machine: linux-x86_64
- commit hash: 262abf1
- commit date: 2024-12-30
- overall geometric mean: 1.428x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241230-linux-x86_64-faster%2dcpython-variable_sized_line_-3.14.0a3+-262abf1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.36x faster                                                             |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                           |
| html5lib       | 88.9 ms                                                | 62.6 ms: 1.42x faster                                                            |
| Geometric mean | (ref)                                                  | 1.35x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241230-linux-x86_64-faster%2dcpython-variable_sized_line_-3.14.0a3+-262abf1 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 619 ms: 2.86x faster                                                             |
| async_tree_none         | 728 ms                                                 | 268 ms: 2.72x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 337 ms: 2.58x faster                                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 500 ms: 2.03x faster                                                             |
| Geometric mean          | (ref)                                                  | 2.53x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241230-linux-x86_64-faster%2dcpython-variable_sized_line_-3.14.0a3+-262abf1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 93.2 ms: 1.65x faster                                                            |
| float          | 117 ms                                                 | 77.9 ms: 1.50x faster                                                            |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241230-linux-x86_64-faster%2dcpython-variable_sized_line_-3.14.0a3+-262abf1 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                             |
| regex_effbot   | 3.63 ms                                                | 3.27 ms: 1.11x faster                                                            |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                            |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                  | 1.16x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241230-linux-x86_64-faster%2dcpython-variable_sized_line_-3.14.0a3+-262abf1 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.99 sec: 1.58x faster                                                           |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                             |
| pickle_pure_python   | 484 us                                                 | 327 us: 1.48x faster                                                             |
| xml_etree_process    | 79.1 ms                                                | 59.0 ms: 1.34x faster                                                            |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                            |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.21x faster                                                             |
| xml_etree_iterparse  | 115 ms                                                 | 97.6 ms: 1.18x faster                                                            |
| json_loads           | 31.2 us                                                | 26.6 us: 1.17x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 84.8 ms: 1.17x faster                                                            |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241230-linux-x86_64-faster%2dcpython-variable_sized_line_-3.14.0a3+-262abf1 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                            |
| python_startup_no_site | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241230-linux-x86_64-faster%2dcpython-variable_sized_line_-3.14.0a3+-262abf1 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.7 ms: 1.52x faster                                                            |
| genshi_text     | 31.8 ms                                                | 22.4 ms: 1.42x faster                                                            |
| mako            | 16.3 ms                                                | 11.8 ms: 1.39x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241230-linux-x86_64-faster%2dcpython-variable_sized_line_-3.14.0a3+-262abf1 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.35x faster                                                             |
| async_tree_io            | 1.77 sec                                               | 619 ms: 2.86x faster                                                             |
| generators               | 80.1 ms                                                | 28.6 ms: 2.80x faster                                                            |
| async_tree_none          | 728 ms                                                 | 268 ms: 2.72x faster                                                             |
| async_tree_memoization   | 870 ms                                                 | 337 ms: 2.58x faster                                                             |
| deltablue                | 7.91 ms                                                | 3.34 ms: 2.37x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 500 ms: 2.03x faster                                                             |
| go                       | 240 ms                                                 | 119 ms: 2.01x faster                                                             |
| pylint                   | 551 ms                                                 | 278 ms: 1.98x faster                                                             |
| chaos                    | 115 ms                                                 | 61.4 ms: 1.88x faster                                                            |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                                             |
| deepcopy_memo            | 58.5 us                                                | 31.4 us: 1.86x faster                                                            |
| richards_super           | 94.7 ms                                                | 51.1 ms: 1.85x faster                                                            |
| raytrace                 | 507 ms                                                 | 275 ms: 1.84x faster                                                             |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.79x faster                                                             |
| richards                 | 79.3 ms                                                | 44.3 ms: 1.79x faster                                                            |
| crypto_pyaes             | 128 ms                                                 | 72.0 ms: 1.77x faster                                                            |
| djangocms                | 38.4 us                                                | 22.1 us: 1.74x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 68.1 ms: 1.74x faster                                                            |
| logging_silent           | 190 ns                                                 | 109 ns: 1.73x faster                                                             |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                            |
| nbody                    | 154 ms                                                 | 93.2 ms: 1.65x faster                                                            |
| hexiom                   | 10.4 ms                                                | 6.36 ms: 1.64x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                            |
| spectral_norm            | 170 ms                                                 | 107 ms: 1.59x faster                                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.63 us: 1.58x faster                                                            |
| tomli_loads              | 3.14 sec                                               | 1.99 sec: 1.58x faster                                                           |
| django_template          | 48.2 ms                                                | 31.7 ms: 1.52x faster                                                            |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                             |
| pyflate                  | 716 ms                                                 | 474 ms: 1.51x faster                                                             |
| float                    | 117 ms                                                 | 77.9 ms: 1.50x faster                                                            |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                             |
| coroutines               | 35.1 ms                                                | 23.7 ms: 1.48x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 327 us: 1.48x faster                                                             |
| logging_format           | 9.09 us                                                | 6.18 us: 1.47x faster                                                            |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                             |
| logging_simple           | 8.30 us                                                | 5.67 us: 1.46x faster                                                            |
| genshi_text              | 31.8 ms                                                | 22.4 ms: 1.42x faster                                                            |
| html5lib                 | 88.9 ms                                                | 62.6 ms: 1.42x faster                                                            |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.6 ms: 1.41x faster                                                            |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                           |
| mako                     | 16.3 ms                                                | 11.8 ms: 1.39x faster                                                            |
| thrift                   | 1.07 ms                                                | 774 us: 1.38x faster                                                             |
| pprint_safe_repr         | 1.02 sec                                               | 736 ms: 1.38x faster                                                             |
| sqlglot_normalize        | 143 ms                                                 | 104 ms: 1.38x faster                                                             |
| 2to3                     | 348 ms                                                 | 255 ms: 1.36x faster                                                             |
| xml_etree_process        | 79.1 ms                                                | 59.0 ms: 1.34x faster                                                            |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                           |
| nqueens                  | 106 ms                                                 | 79.7 ms: 1.33x faster                                                            |
| genshi_xml               | 66.0 ms                                                | 49.8 ms: 1.33x faster                                                            |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                             |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                                             |
| scimark_fft              | 466 ms                                                 | 353 ms: 1.32x faster                                                             |
| dulwich_log              | 84.3 ms                                                | 64.2 ms: 1.31x faster                                                            |
| sqlglot_optimize         | 69.2 ms                                                | 52.7 ms: 1.31x faster                                                            |
| fannkuch                 | 532 ms                                                 | 408 ms: 1.30x faster                                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.98 ms: 1.30x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                                            |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                                             |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                                           |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                                            |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                                             |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.23x faster                                                            |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.21x faster                                                             |
| xml_etree_iterparse      | 115 ms                                                 | 97.6 ms: 1.18x faster                                                            |
| json_loads               | 31.2 us                                                | 26.6 us: 1.17x faster                                                            |
| xml_etree_generate       | 99.4 ms                                                | 84.8 ms: 1.17x faster                                                            |
| json                     | 5.69 ms                                                | 4.98 ms: 1.14x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 866 us: 1.14x faster                                                             |
| mdp                      | 2.85 sec                                               | 2.51 sec: 1.14x faster                                                           |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                            |
| regex_effbot             | 3.63 ms                                                | 3.27 ms: 1.11x faster                                                            |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                             |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.09x faster                                                            |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                                            |
| async_generators         | 444 ms                                                 | 420 ms: 1.06x faster                                                             |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                                             |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                             |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                             |
| coverage                 | 79.4 ms                                                | 83.3 ms: 1.05x slower                                                            |
| mypy2                    | 894 ms                                                 | 952 ms: 1.06x slower                                                             |
| telco                    | 7.27 ms                                                | 7.84 ms: 1.08x slower                                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.06 ms: 1.19x slower                                                            |
| gc_traversal             | 3.62 ms                                                | 4.62 ms: 1.27x slower                                                            |
| create_gc_cycles         | 1.62 ms                                                | 2.45 ms: 1.51x slower                                                            |
| bench_mp_pool            | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                                     |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241230-3.14.0a3+-262abf1/bm-20241230-linux-x86_64-faster%2dcpython-variable_sized_line_-3.14.0a3+-262abf1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.428x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.27x