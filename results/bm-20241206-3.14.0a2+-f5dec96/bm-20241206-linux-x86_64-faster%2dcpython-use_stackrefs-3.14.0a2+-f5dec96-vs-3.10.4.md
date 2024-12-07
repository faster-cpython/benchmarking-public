# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: f5dec96
- commit date: 2024-12-06
- overall geometric mean: 1.423x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.36x faster                                                      |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                    |
| html5lib       | 88.9 ms                                                | 63.0 ms: 1.41x faster                                                     |
| Geometric mean | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 605 ms: 2.92x faster                                                      |
| async_tree_none         | 728 ms                                                 | 274 ms: 2.66x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 347 ms: 2.51x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 501 ms: 2.03x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.51x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 97.1 ms: 1.58x faster                                                     |
| float          | 117 ms                                                 | 78.8 ms: 1.49x faster                                                     |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.33x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.49x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.35 ms: 1.09x faster                                                     |
| regex_v8       | 27.8 ms                                                | 26.4 ms: 1.05x faster                                                     |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                  | 1.15x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                      |
| tomli_loads          | 3.14 sec                                               | 2.10 sec: 1.49x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 326 us: 1.48x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.24x faster                                                     |
| json_loads           | 31.2 us                                                | 26.2 us: 1.19x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 84.7 ms: 1.17x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 99.2 ms: 1.16x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                     |
| genshi_text     | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                     |
| mako            | 16.3 ms                                                | 11.8 ms: 1.38x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.27x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 605 ms: 2.92x faster                                                      |
| generators               | 80.1 ms                                                | 29.1 ms: 2.75x faster                                                     |
| async_tree_none          | 728 ms                                                 | 274 ms: 2.66x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 347 ms: 2.51x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.25 ms: 2.44x faster                                                     |
| go                       | 240 ms                                                 | 117 ms: 2.05x faster                                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 501 ms: 2.03x faster                                                      |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 30.0 us: 1.95x faster                                                     |
| logging_silent           | 190 ns                                                 | 97.5 ns: 1.95x faster                                                     |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                                      |
| chaos                    | 115 ms                                                 | 61.4 ms: 1.88x faster                                                     |
| richards_super           | 94.7 ms                                                | 51.9 ms: 1.83x faster                                                     |
| deepcopy                 | 479 us                                                 | 263 us: 1.82x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 72.8 ms: 1.76x faster                                                     |
| richards                 | 79.3 ms                                                | 45.7 ms: 1.74x faster                                                     |
| djangocms                | 38.4 us                                                | 22.3 us: 1.72x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 68.8 ms: 1.72x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.19 ms: 1.68x faster                                                     |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                                     |
| scimark_sor              | 220 ms                                                 | 132 ms: 1.67x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                                     |
| nbody                    | 154 ms                                                 | 97.1 ms: 1.58x faster                                                     |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                      |
| django_template          | 48.2 ms                                                | 31.9 ms: 1.51x faster                                                     |
| pyflate                  | 716 ms                                                 | 476 ms: 1.50x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.79 us: 1.50x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 2.10 sec: 1.49x faster                                                    |
| regex_compile            | 188 ms                                                 | 127 ms: 1.49x faster                                                      |
| float                    | 117 ms                                                 | 78.8 ms: 1.49x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 326 us: 1.48x faster                                                      |
| spectral_norm            | 170 ms                                                 | 117 ms: 1.46x faster                                                      |
| logging_simple           | 8.30 us                                                | 5.71 us: 1.45x faster                                                     |
| logging_format           | 9.09 us                                                | 6.25 us: 1.45x faster                                                     |
| genshi_text              | 31.8 ms                                                | 22.1 ms: 1.44x faster                                                     |
| coroutines               | 35.1 ms                                                | 24.4 ms: 1.44x faster                                                     |
| html5lib                 | 88.9 ms                                                | 63.0 ms: 1.41x faster                                                     |
| mako                     | 16.3 ms                                                | 11.8 ms: 1.38x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                    |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.37x faster                                                    |
| 2to3                     | 348 ms                                                 | 255 ms: 1.36x faster                                                      |
| thrift                   | 1.07 ms                                                | 785 us: 1.36x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 58.6 ms: 1.35x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 755 ms: 1.35x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 49.6 ms: 1.33x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.33x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.32x faster                                                      |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 65.1 ms: 1.30x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 53.7 ms: 1.29x faster                                                     |
| sympy_str                | 346 ms                                                 | 271 ms: 1.27x faster                                                      |
| scimark_fft              | 466 ms                                                 | 367 ms: 1.27x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                    |
| fannkuch                 | 532 ms                                                 | 423 ms: 1.26x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.19 ms: 1.25x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                     |
| nqueens                  | 106 ms                                                 | 85.6 ms: 1.24x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.24x faster                                                     |
| sympy_expand             | 566 ms                                                 | 459 ms: 1.23x faster                                                      |
| json_loads               | 31.2 us                                                | 26.2 us: 1.19x faster                                                     |
| json                     | 5.69 ms                                                | 4.83 ms: 1.18x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 84.7 ms: 1.17x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 99.2 ms: 1.16x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 855 us: 1.15x faster                                                      |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                     |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                      |
| mdp                      | 2.85 sec                                               | 2.62 sec: 1.09x faster                                                    |
| regex_effbot             | 3.63 ms                                                | 3.35 ms: 1.09x faster                                                     |
| sqlite_synth             | 3.02 us                                                | 2.86 us: 1.06x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 26.4 ms: 1.05x faster                                                     |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                                      |
| async_generators         | 444 ms                                                 | 429 ms: 1.04x faster                                                      |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                      |
| coverage                 | 79.4 ms                                                | 83.2 ms: 1.05x slower                                                     |
| telco                    | 7.27 ms                                                | 7.81 ms: 1.07x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 4.57 ms: 1.26x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.27 ms: 1.40x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 79.1 ms: 3.29x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.40x faster                                                              |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241206-3.14.0a2+-f5dec96/bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-f5dec96.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.423x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.26x