# Results vs. 3.10.4

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: 696d3fd
- commit date: 2025-03-30
- overall geometric mean: 1.380x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 2.63x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 272 ms: 1.28x faster                                          |
| docutils       | 3.30 sec                                               | 2.77 sec: 1.19x faster                                        |
| html5lib       | 88.9 ms                                                | 64.5 ms: 1.38x faster                                         |
| Geometric mean | (ref)                                                  | 1.28x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 625 ms: 2.83x faster                                          |
| async_tree_none         | 728 ms                                                 | 267 ms: 2.73x faster                                          |
| async_tree_memoization  | 870 ms                                                 | 328 ms: 2.65x faster                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 494 ms: 2.06x faster                                          |
| Geometric mean          | (ref)                                                  | 2.55x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 117 ms                                                 | 81.0 ms: 1.45x faster                                         |
| nbody          | 154 ms                                                 | 107 ms: 1.43x faster                                          |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                  | 1.28x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 137 ms: 1.37x faster                                          |
| regex_v8       | 27.8 ms                                                | 23.2 ms: 1.20x faster                                         |
| regex_effbot   | 3.63 ms                                                | 3.26 ms: 1.11x faster                                         |
| regex_dna      | 227 ms                                                 | 209 ms: 1.08x faster                                          |
| Geometric mean | (ref)                                                  | 1.19x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.85 sec: 1.70x faster                                        |
| pickle_pure_python   | 484 us                                                 | 342 us: 1.42x faster                                          |
| unpickle_pure_python | 331 us                                                 | 236 us: 1.40x faster                                          |
| xml_etree_process    | 79.1 ms                                                | 59.1 ms: 1.34x faster                                         |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                         |
| xml_etree_parse      | 168 ms                                                 | 141 ms: 1.19x faster                                          |
| xml_etree_generate   | 99.4 ms                                                | 84.5 ms: 1.18x faster                                         |
| xml_etree_iterparse  | 115 ms                                                 | 99.1 ms: 1.17x faster                                         |
| json_loads           | 31.2 us                                                | 29.8 us: 1.05x faster                                         |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                         |
| python_startup_no_site | 5.93 ms                                                | 8.22 ms: 1.39x slower                                         |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 22.1 ms: 1.44x faster                                         |
| django_template | 48.2 ms                                                | 33.5 ms: 1.44x faster                                         |
| mako            | 16.3 ms                                                | 11.6 ms: 1.40x faster                                         |
| genshi_xml      | 66.0 ms                                                | 52.1 ms: 1.27x faster                                         |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 181 us: 3.01x faster                                          |
| async_tree_io            | 1.77 sec                                               | 625 ms: 2.83x faster                                          |
| async_tree_none          | 728 ms                                                 | 267 ms: 2.73x faster                                          |
| generators               | 80.1 ms                                                | 29.7 ms: 2.70x faster                                         |
| async_tree_memoization   | 870 ms                                                 | 328 ms: 2.65x faster                                          |
| deltablue                | 7.91 ms                                                | 3.58 ms: 2.21x faster                                         |
| mdp                      | 2.85 sec                                               | 1.33 sec: 2.15x faster                                        |
| richards_super           | 94.7 ms                                                | 45.8 ms: 2.07x faster                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 494 ms: 2.06x faster                                          |
| richards                 | 79.3 ms                                                | 40.4 ms: 1.96x faster                                         |
| pylint                   | 551 ms                                                 | 290 ms: 1.90x faster                                          |
| deepcopy_memo            | 58.5 us                                                | 30.8 us: 1.90x faster                                         |
| chaos                    | 115 ms                                                 | 61.3 ms: 1.88x faster                                         |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                          |
| deepcopy                 | 479 us                                                 | 274 us: 1.75x faster                                          |
| raytrace                 | 507 ms                                                 | 291 ms: 1.74x faster                                          |
| tomli_loads              | 3.14 sec                                               | 1.85 sec: 1.70x faster                                        |
| scimark_sor              | 220 ms                                                 | 134 ms: 1.63x faster                                          |
| scimark_monte_carlo      | 118 ms                                                 | 72.6 ms: 1.63x faster                                         |
| go                       | 240 ms                                                 | 150 ms: 1.60x faster                                          |
| coroutines               | 35.1 ms                                                | 21.9 ms: 1.60x faster                                         |
| pyflate                  | 716 ms                                                 | 478 ms: 1.50x faster                                          |
| float                    | 117 ms                                                 | 81.0 ms: 1.45x faster                                         |
| crypto_pyaes             | 128 ms                                                 | 88.5 ms: 1.44x faster                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.89 us: 1.44x faster                                         |
| genshi_text              | 31.8 ms                                                | 22.1 ms: 1.44x faster                                         |
| django_template          | 48.2 ms                                                | 33.5 ms: 1.44x faster                                         |
| nbody                    | 154 ms                                                 | 107 ms: 1.43x faster                                          |
| logging_format           | 9.09 us                                                | 6.40 us: 1.42x faster                                         |
| logging_simple           | 8.30 us                                                | 5.85 us: 1.42x faster                                         |
| pickle_pure_python       | 484 us                                                 | 342 us: 1.42x faster                                          |
| mako                     | 16.3 ms                                                | 11.6 ms: 1.40x faster                                         |
| hexiom                   | 10.4 ms                                                | 7.41 ms: 1.40x faster                                         |
| unpickle_pure_python     | 331 us                                                 | 236 us: 1.40x faster                                          |
| comprehensions           | 28.8 us                                                | 20.5 us: 1.40x faster                                         |
| scimark_lu               | 176 ms                                                 | 126 ms: 1.40x faster                                          |
| html5lib                 | 88.9 ms                                                | 64.5 ms: 1.38x faster                                         |
| regex_compile            | 188 ms                                                 | 137 ms: 1.37x faster                                          |
| dulwich_log              | 84.3 ms                                                | 62.2 ms: 1.36x faster                                         |
| spectral_norm            | 170 ms                                                 | 127 ms: 1.34x faster                                          |
| xml_etree_process        | 79.1 ms                                                | 59.1 ms: 1.34x faster                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.7 ms: 1.32x faster                                         |
| 2to3                     | 348 ms                                                 | 272 ms: 1.28x faster                                          |
| genshi_xml               | 66.0 ms                                                | 52.1 ms: 1.27x faster                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 136 ms: 1.26x faster                                          |
| pycparser                | 1.58 sec                                               | 1.25 sec: 1.26x faster                                        |
| sympy_sum                | 196 ms                                                 | 156 ms: 1.26x faster                                          |
| pprint_safe_repr         | 1.02 sec                                               | 817 ms: 1.25x faster                                          |
| sympy_integrate          | 25.8 ms                                                | 20.7 ms: 1.25x faster                                         |
| pprint_pformat           | 2.10 sec                                               | 1.71 sec: 1.23x faster                                        |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                         |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.22x faster                                         |
| sympy_str                | 346 ms                                                 | 286 ms: 1.21x faster                                          |
| regex_v8                 | 27.8 ms                                                | 23.2 ms: 1.20x faster                                         |
| scimark_fft              | 466 ms                                                 | 390 ms: 1.20x faster                                          |
| xml_etree_parse          | 168 ms                                                 | 141 ms: 1.19x faster                                          |
| docutils                 | 3.30 sec                                               | 2.77 sec: 1.19x faster                                        |
| fannkuch                 | 532 ms                                                 | 448 ms: 1.19x faster                                          |
| nqueens                  | 106 ms                                                 | 89.7 ms: 1.18x faster                                         |
| xml_etree_generate       | 99.4 ms                                                | 84.5 ms: 1.18x faster                                         |
| xml_etree_iterparse      | 115 ms                                                 | 99.1 ms: 1.17x faster                                         |
| sympy_expand             | 566 ms                                                 | 498 ms: 1.14x faster                                          |
| regex_effbot             | 3.63 ms                                                | 3.26 ms: 1.11x faster                                         |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                         |
| bench_thread_pool        | 986 us                                                 | 899 us: 1.10x faster                                          |
| regex_dna                | 227 ms                                                 | 209 ms: 1.08x faster                                          |
| json                     | 5.69 ms                                                | 5.30 ms: 1.07x faster                                         |
| sqlite_synth             | 3.02 us                                                | 2.83 us: 1.07x faster                                         |
| async_generators         | 444 ms                                                 | 418 ms: 1.06x faster                                          |
| meteor_contest           | 120 ms                                                 | 114 ms: 1.05x faster                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.18 ms: 1.05x faster                                         |
| json_loads               | 31.2 us                                                | 29.8 us: 1.05x faster                                         |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                          |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                          |
| coverage                 | 79.4 ms                                                | 86.1 ms: 1.08x slower                                         |
| telco                    | 7.27 ms                                                | 8.19 ms: 1.13x slower                                         |
| gc_traversal             | 3.62 ms                                                | 4.82 ms: 1.33x slower                                         |
| python_startup_no_site   | 5.93 ms                                                | 8.22 ms: 1.39x slower                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.53x slower                                         |
| bench_mp_pool            | 24.0 ms                                                | 84.3 ms: 3.51x slower                                         |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                  |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250330-3.14.0a6+-696d3fd-JIT/bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.380x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 2.63x