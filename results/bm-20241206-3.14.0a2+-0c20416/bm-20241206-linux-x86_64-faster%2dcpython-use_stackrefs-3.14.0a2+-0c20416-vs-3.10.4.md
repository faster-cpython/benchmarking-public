# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: 0c20416
- commit date: 2024-12-06
- overall geometric mean: 1.416x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 256 ms: 1.36x faster                                                      |
| docutils       | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                    |
| html5lib       | 88.9 ms                                                | 65.2 ms: 1.36x faster                                                     |
| Geometric mean | (ref)                                                  | 1.33x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 605 ms: 2.92x faster                                                      |
| async_tree_none         | 728 ms                                                 | 274 ms: 2.66x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 346 ms: 2.51x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 500 ms: 2.03x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.51x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 98.4 ms: 1.56x faster                                                     |
| float          | 117 ms                                                 | 78.4 ms: 1.49x faster                                                     |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.33x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 130 ms: 1.45x faster                                                      |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                     |
| regex_effbot   | 3.63 ms                                                | 3.50 ms: 1.04x faster                                                     |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.14x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 217 us: 1.53x faster                                                      |
| tomli_loads          | 3.14 sec                                               | 2.10 sec: 1.50x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 331 us: 1.46x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                     |
| json_loads           | 31.2 us                                                | 26.0 us: 1.20x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 84.5 ms: 1.18x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 143 ms: 1.17x faster                                                      |
| xml_etree_iterparse  | 115 ms                                                 | 99.4 ms: 1.16x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.03 ms: 1.18x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.0 ms: 1.50x faster                                                     |
| genshi_text     | 31.8 ms                                                | 22.5 ms: 1.41x faster                                                     |
| mako            | 16.3 ms                                                | 11.7 ms: 1.40x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 50.7 ms: 1.30x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.31x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 605 ms: 2.92x faster                                                      |
| generators               | 80.1 ms                                                | 28.8 ms: 2.78x faster                                                     |
| async_tree_none          | 728 ms                                                 | 274 ms: 2.66x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 346 ms: 2.51x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.28 ms: 2.41x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 500 ms: 2.03x faster                                                      |
| go                       | 240 ms                                                 | 118 ms: 2.03x faster                                                      |
| pylint                   | 551 ms                                                 | 276 ms: 2.00x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 30.6 us: 1.91x faster                                                     |
| raytrace                 | 507 ms                                                 | 269 ms: 1.88x faster                                                      |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                                      |
| chaos                    | 115 ms                                                 | 62.4 ms: 1.85x faster                                                     |
| richards_super           | 94.7 ms                                                | 51.8 ms: 1.83x faster                                                     |
| deepcopy                 | 479 us                                                 | 268 us: 1.79x faster                                                      |
| djangocms                | 38.4 us                                                | 22.0 us: 1.75x faster                                                     |
| richards                 | 79.3 ms                                                | 45.6 ms: 1.74x faster                                                     |
| scimark_sor              | 220 ms                                                 | 126 ms: 1.74x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 74.0 ms: 1.73x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 69.8 ms: 1.69x faster                                                     |
| comprehensions           | 28.8 us                                                | 17.3 us: 1.67x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.65x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.36 ms: 1.63x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                                     |
| nbody                    | 154 ms                                                 | 98.4 ms: 1.56x faster                                                     |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.53x faster                                                      |
| django_template          | 48.2 ms                                                | 32.0 ms: 1.50x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 2.10 sec: 1.50x faster                                                    |
| float                    | 117 ms                                                 | 78.4 ms: 1.49x faster                                                     |
| deepcopy_reduce          | 4.17 us                                                | 2.81 us: 1.49x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 331 us: 1.46x faster                                                      |
| pyflate                  | 716 ms                                                 | 492 ms: 1.46x faster                                                      |
| regex_compile            | 188 ms                                                 | 130 ms: 1.45x faster                                                      |
| logging_format           | 9.09 us                                                | 6.27 us: 1.45x faster                                                     |
| spectral_norm            | 170 ms                                                 | 118 ms: 1.44x faster                                                      |
| coroutines               | 35.1 ms                                                | 24.5 ms: 1.43x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.11 sec: 1.42x faster                                                    |
| genshi_text              | 31.8 ms                                                | 22.5 ms: 1.41x faster                                                     |
| mako                     | 16.3 ms                                                | 11.7 ms: 1.40x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                                     |
| thrift                   | 1.07 ms                                                | 778 us: 1.38x faster                                                      |
| html5lib                 | 88.9 ms                                                | 65.2 ms: 1.36x faster                                                     |
| 2to3                     | 348 ms                                                 | 256 ms: 1.36x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 58.7 ms: 1.35x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 769 ms: 1.32x faster                                                      |
| sqlalchemy_declarative   | 172 ms                                                 | 130 ms: 1.32x faster                                                      |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 109 ms: 1.31x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 50.7 ms: 1.30x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 65.3 ms: 1.29x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 54.2 ms: 1.28x faster                                                     |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.61 sec: 1.26x faster                                                    |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.13 ms: 1.26x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                     |
| nqueens                  | 106 ms                                                 | 84.9 ms: 1.25x faster                                                     |
| fannkuch                 | 532 ms                                                 | 429 ms: 1.24x faster                                                      |
| scimark_fft              | 466 ms                                                 | 379 ms: 1.23x faster                                                      |
| sympy_expand             | 566 ms                                                 | 462 ms: 1.22x faster                                                      |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                                     |
| json_loads               | 31.2 us                                                | 26.0 us: 1.20x faster                                                     |
| json                     | 5.69 ms                                                | 4.81 ms: 1.18x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 84.5 ms: 1.18x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 143 ms: 1.17x faster                                                      |
| xml_etree_iterparse      | 115 ms                                                 | 99.4 ms: 1.16x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 857 us: 1.15x faster                                                      |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                     |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.72 sec: 1.05x faster                                                    |
| sqlite_synth             | 3.02 us                                                | 2.90 us: 1.04x faster                                                     |
| regex_effbot             | 3.63 ms                                                | 3.50 ms: 1.04x faster                                                     |
| async_generators         | 444 ms                                                 | 428 ms: 1.04x faster                                                      |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                                      |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                                      |
| coverage                 | 79.4 ms                                                | 84.0 ms: 1.06x slower                                                     |
| telco                    | 7.27 ms                                                | 7.86 ms: 1.08x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.03 ms: 1.18x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 4.61 ms: 1.27x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.24 ms: 1.38x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 78.7 ms: 3.28x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                              |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241206-3.14.0a2+-0c20416/bm-20241206-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-0c20416.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.416x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.26x