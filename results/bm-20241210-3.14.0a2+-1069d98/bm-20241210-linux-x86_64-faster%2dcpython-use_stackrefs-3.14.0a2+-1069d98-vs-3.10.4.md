# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: 1069d98
- commit date: 2024-12-10
- overall geometric mean: 1.408x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.36x faster                                                      |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                    |
| html5lib       | 88.9 ms                                                | 63.1 ms: 1.41x faster                                                     |
| Geometric mean | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 639 ms: 2.77x faster                                                      |
| async_tree_none         | 728 ms                                                 | 275 ms: 2.65x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 345 ms: 2.52x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 500 ms: 2.03x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.48x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 99.3 ms: 1.55x faster                                                     |
| float          | 117 ms                                                 | 79.3 ms: 1.48x faster                                                     |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.32x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.40 ms: 1.07x faster                                                     |
| regex_v8       | 27.8 ms                                                | 26.9 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.13x faster                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                                      |
| tomli_loads          | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 326 us: 1.49x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 59.5 ms: 1.33x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.24x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.22x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 98.6 ms: 1.17x faster                                                     |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 85.8 ms: 1.16x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.6 ms: 1.48x faster                                                     |
| genshi_text     | 31.8 ms                                                | 22.2 ms: 1.44x faster                                                     |
| mako            | 16.3 ms                                                | 11.9 ms: 1.37x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 51.1 ms: 1.29x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                                      |
| generators               | 80.1 ms                                                | 28.1 ms: 2.85x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 639 ms: 2.77x faster                                                      |
| async_tree_none          | 728 ms                                                 | 275 ms: 2.65x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 345 ms: 2.52x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.27 ms: 2.42x faster                                                     |
| go                       | 240 ms                                                 | 117 ms: 2.05x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 500 ms: 2.03x faster                                                      |
| pylint                   | 551 ms                                                 | 281 ms: 1.96x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 30.4 us: 1.92x faster                                                     |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                      |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                                      |
| chaos                    | 115 ms                                                 | 62.0 ms: 1.86x faster                                                     |
| deepcopy                 | 479 us                                                 | 262 us: 1.83x faster                                                      |
| richards_super           | 94.7 ms                                                | 52.7 ms: 1.80x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 72.5 ms: 1.76x faster                                                     |
| djangocms                | 38.4 us                                                | 22.2 us: 1.73x faster                                                     |
| richards                 | 79.3 ms                                                | 46.0 ms: 1.72x faster                                                     |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.72x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 69.0 ms: 1.71x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.18 ms: 1.68x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                                     |
| comprehensions           | 28.8 us                                                | 17.4 us: 1.65x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                                     |
| nbody                    | 154 ms                                                 | 99.3 ms: 1.55x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.72 us: 1.53x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                                      |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                      |
| tomli_loads              | 3.14 sec                                               | 2.09 sec: 1.50x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.58 us: 1.49x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 326 us: 1.49x faster                                                      |
| pyflate                  | 716 ms                                                 | 481 ms: 1.49x faster                                                      |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                                     |
| django_template          | 48.2 ms                                                | 32.6 ms: 1.48x faster                                                     |
| float                    | 117 ms                                                 | 79.3 ms: 1.48x faster                                                     |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                                      |
| spectral_norm            | 170 ms                                                 | 116 ms: 1.47x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.9 ms: 1.47x faster                                                     |
| genshi_text              | 31.8 ms                                                | 22.2 ms: 1.44x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.5 ms: 1.41x faster                                                     |
| html5lib                 | 88.9 ms                                                | 63.1 ms: 1.41x faster                                                     |
| thrift                   | 1.07 ms                                                | 782 us: 1.37x faster                                                      |
| mako                     | 16.3 ms                                                | 11.9 ms: 1.37x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.36x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 750 ms: 1.36x faster                                                      |
| 2to3                     | 348 ms                                                 | 257 ms: 1.36x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.33x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 59.5 ms: 1.33x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.33x faster                                                      |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.31x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.00 ms: 1.29x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 51.1 ms: 1.29x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 65.5 ms: 1.29x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 53.8 ms: 1.29x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 20.1 ms: 1.28x faster                                                     |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                                      |
| scimark_fft              | 466 ms                                                 | 368 ms: 1.27x faster                                                      |
| fannkuch                 | 532 ms                                                 | 424 ms: 1.25x faster                                                      |
| nqueens                  | 106 ms                                                 | 84.6 ms: 1.25x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                    |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.24x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.6 ms: 1.23x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.22x faster                                                      |
| sympy_expand             | 566 ms                                                 | 465 ms: 1.22x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 98.6 ms: 1.17x faster                                                     |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 85.8 ms: 1.16x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 863 us: 1.14x faster                                                      |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                     |
| json                     | 5.69 ms                                                | 5.07 ms: 1.12x faster                                                     |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.40 ms: 1.07x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.71 sec: 1.05x faster                                                    |
| async_generators         | 444 ms                                                 | 426 ms: 1.04x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.92 us: 1.03x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 26.9 ms: 1.03x faster                                                     |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.00x faster                                                      |
| coverage                 | 79.4 ms                                                | 83.1 ms: 1.05x slower                                                     |
| mypy2                    | 894 ms                                                 | 952 ms: 1.06x slower                                                      |
| telco                    | 7.27 ms                                                | 7.87 ms: 1.08x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.02 ms: 1.18x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 5.03 ms: 1.39x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 81.4 ms: 3.39x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                              |

Benchmark hidden because not significant (1): regex_dna
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241210-3.14.0a2+-1069d98/bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.408x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.27x