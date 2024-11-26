# Results vs. 3.10.4

- fork: faster-cpython
- ref: load_const_return_re
- machine: linux-x86_64
- commit hash: 2a3b1e2
- commit date: 2024-10-23
- overall geometric mean: 1.412x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                                             |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                           |
| html5lib       | 88.9 ms                                                | 63.4 ms: 1.40x faster                                                            |
| tornado_http   | 136 ms                                                 | 91.4 ms: 1.49x faster                                                            |
| Geometric mean | (ref)                                                  | 1.37x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 327 ms: 2.22x faster                                                             |
| async_tree_memoization  | 870 ms                                                 | 414 ms: 2.10x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 855 ms: 2.07x faster                                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 566 ms: 1.79x faster                                                             |
| Geometric mean          | (ref)                                                  | 2.04x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 95.8 ms: 1.60x faster                                                            |
| float          | 117 ms                                                 | 80.3 ms: 1.46x faster                                                            |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 131 ms: 1.44x faster                                                             |
| regex_v8       | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                            |
| regex_dna      | 227 ms                                                 | 214 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 315 us: 1.54x faster                                                             |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                             |
| tomli_loads          | 3.14 sec                                               | 2.12 sec: 1.48x faster                                                           |
| xml_etree_process    | 79.1 ms                                                | 60.1 ms: 1.32x faster                                                            |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.28x faster                                                            |
| json_loads           | 31.2 us                                                | 26.2 us: 1.19x faster                                                            |
| xml_etree_generate   | 99.4 ms                                                | 87.1 ms: 1.14x faster                                                            |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                                             |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                                             |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.8 ms: 1.24x faster                                                            |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                            |
| django_template | 48.2 ms                                                | 34.8 ms: 1.38x faster                                                            |
| genshi_text     | 31.8 ms                                                | 23.8 ms: 1.34x faster                                                            |
| genshi_xml      | 66.0 ms                                                | 52.5 ms: 1.26x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.35x faster                                                             |
| generators               | 80.1 ms                                                | 26.8 ms: 2.99x faster                                                            |
| deltablue                | 7.91 ms                                                | 3.26 ms: 2.43x faster                                                            |
| async_tree_none          | 728 ms                                                 | 327 ms: 2.22x faster                                                             |
| async_tree_memoization   | 870 ms                                                 | 414 ms: 2.10x faster                                                             |
| async_tree_io            | 1.77 sec                                               | 855 ms: 2.07x faster                                                             |
| go                       | 240 ms                                                 | 120 ms: 2.00x faster                                                             |
| logging_silent           | 190 ns                                                 | 98.3 ns: 1.93x faster                                                            |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                                             |
| deepcopy_memo            | 58.5 us                                                | 31.1 us: 1.88x faster                                                            |
| chaos                    | 115 ms                                                 | 62.6 ms: 1.84x faster                                                            |
| deepcopy                 | 479 us                                                 | 263 us: 1.82x faster                                                             |
| richards_super           | 94.7 ms                                                | 52.7 ms: 1.80x faster                                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 566 ms: 1.79x faster                                                             |
| crypto_pyaes             | 128 ms                                                 | 71.8 ms: 1.78x faster                                                            |
| pylint                   | 551 ms                                                 | 318 ms: 1.74x faster                                                             |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                            |
| richards                 | 79.3 ms                                                | 46.1 ms: 1.72x faster                                                            |
| scimark_monte_carlo      | 118 ms                                                 | 69.1 ms: 1.71x faster                                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                            |
| scimark_sor              | 220 ms                                                 | 132 ms: 1.67x faster                                                             |
| hexiom                   | 10.4 ms                                                | 6.28 ms: 1.65x faster                                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                            |
| nbody                    | 154 ms                                                 | 95.8 ms: 1.60x faster                                                            |
| pyflate                  | 716 ms                                                 | 459 ms: 1.56x faster                                                             |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                            |
| pickle_pure_python       | 484 us                                                 | 315 us: 1.54x faster                                                             |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                             |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.51x faster                                                            |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                                             |
| tornado_http             | 136 ms                                                 | 91.4 ms: 1.49x faster                                                            |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.49x faster                                                             |
| tomli_loads              | 3.14 sec                                               | 2.12 sec: 1.48x faster                                                           |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                                            |
| logging_format           | 9.09 us                                                | 6.18 us: 1.47x faster                                                            |
| float                    | 117 ms                                                 | 80.3 ms: 1.46x faster                                                            |
| regex_compile            | 188 ms                                                 | 131 ms: 1.44x faster                                                             |
| mako                     | 16.3 ms                                                | 11.4 ms: 1.43x faster                                                            |
| html5lib                 | 88.9 ms                                                | 63.4 ms: 1.40x faster                                                            |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                                           |
| thrift                   | 1.07 ms                                                | 773 us: 1.39x faster                                                             |
| django_template          | 48.2 ms                                                | 34.8 ms: 1.38x faster                                                            |
| pprint_safe_repr         | 1.02 sec                                               | 738 ms: 1.38x faster                                                             |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                           |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                                             |
| sqlglot_normalize        | 143 ms                                                 | 106 ms: 1.34x faster                                                             |
| genshi_text              | 31.8 ms                                                | 23.8 ms: 1.34x faster                                                            |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.33x faster                                                             |
| dulwich_log              | 84.3 ms                                                | 64.0 ms: 1.32x faster                                                            |
| xml_etree_process        | 79.1 ms                                                | 60.1 ms: 1.32x faster                                                            |
| nqueens                  | 106 ms                                                 | 80.6 ms: 1.31x faster                                                            |
| fannkuch                 | 532 ms                                                 | 405 ms: 1.31x faster                                                             |
| sqlglot_optimize         | 69.2 ms                                                | 53.3 ms: 1.30x faster                                                            |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.29x faster                                                            |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                                             |
| pathlib                  | 20.5 ms                                                | 15.8 ms: 1.29x faster                                                            |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.01 ms: 1.29x faster                                                            |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.28x faster                                                            |
| scimark_fft              | 466 ms                                                 | 365 ms: 1.27x faster                                                             |
| genshi_xml               | 66.0 ms                                                | 52.5 ms: 1.26x faster                                                            |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                                             |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                           |
| python_startup           | 14.6 ms                                                | 11.8 ms: 1.24x faster                                                            |
| json_loads               | 31.2 us                                                | 26.2 us: 1.19x faster                                                            |
| json                     | 5.69 ms                                                | 4.85 ms: 1.17x faster                                                            |
| bench_thread_pool        | 986 us                                                 | 842 us: 1.17x faster                                                             |
| xml_etree_generate       | 99.4 ms                                                | 87.1 ms: 1.14x faster                                                            |
| mdp                      | 2.85 sec                                               | 2.50 sec: 1.14x faster                                                           |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                             |
| regex_v8                 | 27.8 ms                                                | 25.3 ms: 1.10x faster                                                            |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                                             |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                                             |
| regex_dna                | 227 ms                                                 | 214 ms: 1.06x faster                                                             |
| async_generators         | 444 ms                                                 | 427 ms: 1.04x faster                                                             |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                             |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                             |
| coverage                 | 79.4 ms                                                | 84.4 ms: 1.06x slower                                                            |
| telco                    | 7.27 ms                                                | 8.02 ms: 1.10x slower                                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                                            |
| gc_traversal             | 3.62 ms                                                | 4.47 ms: 1.23x slower                                                            |
| create_gc_cycles         | 1.62 ms                                                | 2.67 ms: 1.65x slower                                                            |
| bench_mp_pool            | 24.0 ms                                                | 78.7 ms: 3.28x slower                                                            |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                                     |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241023-3.14.0a1+-2a3b1e2/bm-20241023-linux-x86_64-faster%2dcpython-load_const_return_re-3.14.0a1+-2a3b1e2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.412x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.25x