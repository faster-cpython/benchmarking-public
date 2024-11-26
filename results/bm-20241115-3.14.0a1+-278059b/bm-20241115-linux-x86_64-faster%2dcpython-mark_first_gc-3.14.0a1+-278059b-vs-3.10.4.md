# Results vs. 3.10.4

- fork: faster-cpython
- ref: mark_first_gc
- machine: linux-x86_64
- commit hash: 278059b
- commit date: 2024-11-15
- overall geometric mean: 1.430x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 263 ms: 1.33x faster                                                      |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                                    |
| html5lib       | 88.9 ms                                                | 67.5 ms: 1.32x faster                                                     |
| Geometric mean | (ref)                                                  | 1.29x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 643 ms: 2.75x faster                                                      |
| async_tree_none         | 728 ms                                                 | 283 ms: 2.57x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 358 ms: 2.43x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 514 ms: 1.98x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.41x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 96.5 ms: 1.59x faster                                                     |
| float          | 117 ms                                                 | 84.2 ms: 1.39x faster                                                     |
| pidigits       | 191 ms                                                 | 192 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.30x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.44x faster                                                      |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                     |
| regex_dna      | 227 ms                                                 | 221 ms: 1.03x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.86 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                  | 1.12x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 221 us: 1.50x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 324 us: 1.49x faster                                                      |
| tomli_loads          | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                    |
| xml_etree_process    | 79.1 ms                                                | 61.9 ms: 1.28x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                     |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 87.9 ms: 1.13x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 155 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 117 ms: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.25x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.4 ms: 1.18x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 6.72 ms: 1.13x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.9 ms: 1.46x faster                                                     |
| genshi_text     | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                     |
| mako            | 16.3 ms                                                | 11.6 ms: 1.41x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 51.4 ms: 1.29x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 161 us: 3.37x faster                                                      |
| generators               | 80.1 ms                                                | 27.9 ms: 2.87x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 643 ms: 2.75x faster                                                      |
| async_tree_none          | 728 ms                                                 | 283 ms: 2.57x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 358 ms: 2.43x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.42 ms: 2.32x faster                                                     |
| pylint                   | 551 ms                                                 | 277 ms: 1.99x faster                                                      |
| go                       | 240 ms                                                 | 121 ms: 1.99x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 514 ms: 1.98x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 30.8 us: 1.90x faster                                                     |
| chaos                    | 115 ms                                                 | 61.5 ms: 1.88x faster                                                     |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                                      |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                      |
| richards_super           | 94.7 ms                                                | 53.2 ms: 1.78x faster                                                     |
| logging_silent           | 190 ns                                                 | 109 ns: 1.74x faster                                                      |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.72x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 68.6 ms: 1.72x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 74.6 ms: 1.71x faster                                                     |
| djangocms                | 38.4 us                                                | 22.5 us: 1.71x faster                                                     |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.71x faster                                                     |
| richards                 | 79.3 ms                                                | 46.8 ms: 1.69x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.65x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.37 ms: 1.63x faster                                                     |
| nbody                    | 154 ms                                                 | 96.5 ms: 1.59x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.59x faster                                                     |
| gc_traversal             | 3.62 ms                                                | 2.29 ms: 1.59x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                     |
| pyflate                  | 716 ms                                                 | 472 ms: 1.52x faster                                                      |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 221 us: 1.50x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 324 us: 1.49x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.57 us: 1.49x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                    |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.47x faster                                                     |
| django_template          | 48.2 ms                                                | 32.9 ms: 1.46x faster                                                     |
| logging_format           | 9.09 us                                                | 6.23 us: 1.46x faster                                                     |
| spectral_norm            | 170 ms                                                 | 117 ms: 1.46x faster                                                      |
| regex_compile            | 188 ms                                                 | 130 ms: 1.44x faster                                                      |
| genshi_text              | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                                    |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.5 ms: 1.42x faster                                                     |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.41x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.40x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 728 ms: 1.40x faster                                                      |
| float                    | 117 ms                                                 | 84.2 ms: 1.39x faster                                                     |
| thrift                   | 1.07 ms                                                | 776 us: 1.38x faster                                                      |
| sqlalchemy_declarative   | 172 ms                                                 | 128 ms: 1.34x faster                                                      |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                      |
| 2to3                     | 348 ms                                                 | 263 ms: 1.33x faster                                                      |
| html5lib                 | 88.9 ms                                                | 67.5 ms: 1.32x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.32x faster                                                      |
| nqueens                  | 106 ms                                                 | 80.8 ms: 1.31x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.98 ms: 1.30x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 65.1 ms: 1.29x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.29x faster                                                     |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 51.4 ms: 1.29x faster                                                     |
| fannkuch                 | 532 ms                                                 | 415 ms: 1.28x faster                                                      |
| scimark_fft              | 466 ms                                                 | 364 ms: 1.28x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 61.9 ms: 1.28x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 54.3 ms: 1.27x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.27x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.27x faster                                                     |
| sympy_expand             | 566 ms                                                 | 454 ms: 1.25x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                                    |
| python_startup           | 14.6 ms                                                | 12.4 ms: 1.18x faster                                                     |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 851 us: 1.16x faster                                                      |
| json                     | 5.69 ms                                                | 4.92 ms: 1.16x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.51 sec: 1.14x faster                                                    |
| xml_etree_generate       | 99.4 ms                                                | 87.9 ms: 1.13x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                                     |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                      |
| xml_etree_parse          | 168 ms                                                 | 155 ms: 1.09x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.88 us: 1.05x faster                                                     |
| regex_dna                | 227 ms                                                 | 221 ms: 1.03x faster                                                      |
| async_generators         | 444 ms                                                 | 433 ms: 1.02x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                      |
| pidigits                 | 191 ms                                                 | 192 ms: 1.01x slower                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 117 ms: 1.01x slower                                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.67 ms: 1.03x slower                                                     |
| regex_effbot             | 3.63 ms                                                | 3.86 ms: 1.06x slower                                                     |
| telco                    | 7.27 ms                                                | 7.83 ms: 1.08x slower                                                     |
| coverage                 | 79.4 ms                                                | 88.1 ms: 1.11x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 6.72 ms: 1.13x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 83.5 ms: 3.48x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                              |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241115-3.14.0a1+-278059b/bm-20241115-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-278059b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.430x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.24x