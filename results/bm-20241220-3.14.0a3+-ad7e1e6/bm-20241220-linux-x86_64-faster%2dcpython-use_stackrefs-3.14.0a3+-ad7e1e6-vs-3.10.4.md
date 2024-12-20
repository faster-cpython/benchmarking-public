# Results vs. 3.10.4

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: ad7e1e6
- commit date: 2024-12-20
- overall geometric mean: 1.412x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 257 ms: 1.35x faster                                                      |
| docutils       | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                    |
| html5lib       | 88.9 ms                                                | 63.7 ms: 1.39x faster                                                     |
| Geometric mean | (ref)                                                  | 1.33x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 629 ms: 2.81x faster                                                      |
| async_tree_none         | 728 ms                                                 | 270 ms: 2.70x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 342 ms: 2.55x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 496 ms: 2.05x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.51x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 100 ms: 1.53x faster                                                      |
| float          | 117 ms                                                 | 78.1 ms: 1.50x faster                                                     |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.33x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                      |
| regex_v8       | 27.8 ms                                                | 26.5 ms: 1.05x faster                                                     |
| regex_effbot   | 3.63 ms                                                | 3.54 ms: 1.02x faster                                                     |
| regex_dna      | 227 ms                                                 | 223 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.98 sec: 1.58x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 221 us: 1.49x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 331 us: 1.47x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 59.4 ms: 1.33x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.23x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.21x faster                                                      |
| json_loads           | 31.2 us                                                | 26.5 us: 1.18x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 84.7 ms: 1.17x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.31x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 33.0 ms: 1.46x faster                                                     |
| genshi_text     | 31.8 ms                                                | 22.3 ms: 1.42x faster                                                     |
| mako            | 16.3 ms                                                | 12.2 ms: 1.34x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 50.6 ms: 1.31x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.31x faster                                                      |
| generators               | 80.1 ms                                                | 28.3 ms: 2.83x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 629 ms: 2.81x faster                                                      |
| async_tree_none          | 728 ms                                                 | 270 ms: 2.70x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 342 ms: 2.55x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.34 ms: 2.37x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 496 ms: 2.05x faster                                                      |
| go                       | 240 ms                                                 | 117 ms: 2.04x faster                                                      |
| pylint                   | 551 ms                                                 | 280 ms: 1.97x faster                                                      |
| logging_silent           | 190 ns                                                 | 100 ns: 1.89x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 31.0 us: 1.89x faster                                                     |
| raytrace                 | 507 ms                                                 | 273 ms: 1.86x faster                                                      |
| richards_super           | 94.7 ms                                                | 51.1 ms: 1.85x faster                                                     |
| chaos                    | 115 ms                                                 | 62.6 ms: 1.84x faster                                                     |
| deepcopy                 | 479 us                                                 | 267 us: 1.79x faster                                                      |
| richards                 | 79.3 ms                                                | 44.5 ms: 1.78x faster                                                     |
| scimark_sor              | 220 ms                                                 | 124 ms: 1.76x faster                                                      |
| djangocms                | 38.4 us                                                | 22.1 us: 1.74x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 73.7 ms: 1.73x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 69.8 ms: 1.69x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                                     |
| comprehensions           | 28.8 us                                                | 17.5 us: 1.64x faster                                                     |
| hexiom                   | 10.4 ms                                                | 6.41 ms: 1.62x faster                                                     |
| spectral_norm            | 170 ms                                                 | 106 ms: 1.60x faster                                                      |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.98 sec: 1.58x faster                                                    |
| nbody                    | 154 ms                                                 | 100 ms: 1.53x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.76 us: 1.51x faster                                                     |
| pyflate                  | 716 ms                                                 | 475 ms: 1.51x faster                                                      |
| float                    | 117 ms                                                 | 78.1 ms: 1.50x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 221 us: 1.49x faster                                                      |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.48x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 331 us: 1.47x faster                                                      |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                      |
| django_template          | 48.2 ms                                                | 33.0 ms: 1.46x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.77 us: 1.44x faster                                                     |
| logging_format           | 9.09 us                                                | 6.33 us: 1.44x faster                                                     |
| genshi_text              | 31.8 ms                                                | 22.3 ms: 1.42x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.7 ms: 1.39x faster                                                     |
| html5lib                 | 88.9 ms                                                | 63.7 ms: 1.39x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                                    |
| thrift                   | 1.07 ms                                                | 776 us: 1.38x faster                                                      |
| 2to3                     | 348 ms                                                 | 257 ms: 1.35x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.35x faster                                                    |
| mako                     | 16.3 ms                                                | 12.2 ms: 1.34x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                                      |
| xml_etree_process        | 79.1 ms                                                | 59.4 ms: 1.33x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 767 ms: 1.33x faster                                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.90 ms: 1.32x faster                                                     |
| scimark_fft              | 466 ms                                                 | 353 ms: 1.32x faster                                                      |
| sympy_sum                | 196 ms                                                 | 149 ms: 1.32x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 50.6 ms: 1.31x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 64.7 ms: 1.30x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.30x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 53.5 ms: 1.29x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                                     |
| sympy_str                | 346 ms                                                 | 272 ms: 1.27x faster                                                      |
| nqueens                  | 106 ms                                                 | 83.5 ms: 1.27x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.64 sec: 1.25x faster                                                    |
| fannkuch                 | 532 ms                                                 | 427 ms: 1.24x faster                                                      |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.23x faster                                                     |
| sympy_expand             | 566 ms                                                 | 463 ms: 1.22x faster                                                      |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.22x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.21x faster                                                      |
| json_loads               | 31.2 us                                                | 26.5 us: 1.18x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 84.7 ms: 1.17x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.48 sec: 1.15x faster                                                    |
| json                     | 5.69 ms                                                | 4.99 ms: 1.14x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 873 us: 1.13x faster                                                      |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                     |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.11x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.81 us: 1.07x faster                                                     |
| regex_v8                 | 27.8 ms                                                | 26.5 ms: 1.05x faster                                                     |
| async_generators         | 444 ms                                                 | 429 ms: 1.04x faster                                                      |
| regex_effbot             | 3.63 ms                                                | 3.54 ms: 1.02x faster                                                     |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| regex_dna                | 227 ms                                                 | 223 ms: 1.02x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                      |
| coverage                 | 79.4 ms                                                | 83.8 ms: 1.05x slower                                                     |
| mypy2                    | 894 ms                                                 | 951 ms: 1.06x slower                                                      |
| telco                    | 7.27 ms                                                | 7.88 ms: 1.08x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 4.92 ms: 1.36x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.44 ms: 1.51x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 81.9 ms: 3.41x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                              |
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241220-3.14.0a3+-ad7e1e6/bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.412x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.27x