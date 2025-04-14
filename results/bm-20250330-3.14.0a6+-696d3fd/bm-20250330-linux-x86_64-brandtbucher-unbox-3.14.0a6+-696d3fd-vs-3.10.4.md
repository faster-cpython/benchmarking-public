# Results vs. 3.10.4

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: 696d3fd
- commit date: 2025-03-30
- overall geometric mean: 1.403x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 2.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 262 ms: 1.33x faster                                          |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                        |
| html5lib       | 88.9 ms                                                | 64.2 ms: 1.38x faster                                         |
| Geometric mean | (ref)                                                  | 1.32x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 603 ms: 2.93x faster                                          |
| async_tree_none         | 728 ms                                                 | 255 ms: 2.86x faster                                          |
| async_tree_memoization  | 870 ms                                                 | 316 ms: 2.75x faster                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 493 ms: 2.06x faster                                          |
| Geometric mean          | (ref)                                                  | 2.63x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 111 ms: 1.38x faster                                          |
| float          | 117 ms                                                 | 85.4 ms: 1.37x faster                                         |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                  | 1.24x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 134 ms: 1.40x faster                                          |
| regex_v8       | 27.8 ms                                                | 23.3 ms: 1.19x faster                                         |
| regex_effbot   | 3.63 ms                                                | 3.32 ms: 1.09x faster                                         |
| regex_dna      | 227 ms                                                 | 220 ms: 1.03x faster                                          |
| Geometric mean | (ref)                                                  | 1.17x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.89 sec: 1.66x faster                                        |
| pickle_pure_python   | 484 us                                                 | 330 us: 1.47x faster                                          |
| unpickle_pure_python | 331 us                                                 | 228 us: 1.45x faster                                          |
| xml_etree_process    | 79.1 ms                                                | 60.7 ms: 1.30x faster                                         |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                         |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.18x faster                                          |
| xml_etree_iterparse  | 115 ms                                                 | 100 ms: 1.15x faster                                          |
| xml_etree_generate   | 99.4 ms                                                | 87.2 ms: 1.14x faster                                         |
| json_loads           | 31.2 us                                                | 29.7 us: 1.05x faster                                         |
| Geometric mean       | (ref)                                                  | 1.28x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                         |
| python_startup_no_site | 5.93 ms                                                | 8.18 ms: 1.38x slower                                         |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 32.7 ms: 1.47x faster                                         |
| genshi_text     | 31.8 ms                                                | 21.8 ms: 1.46x faster                                         |
| mako            | 16.3 ms                                                | 11.9 ms: 1.37x faster                                         |
| genshi_xml      | 66.0 ms                                                | 50.3 ms: 1.31x faster                                         |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.29x faster                                          |
| async_tree_io            | 1.77 sec                                               | 603 ms: 2.93x faster                                          |
| async_tree_none          | 728 ms                                                 | 255 ms: 2.86x faster                                          |
| async_tree_memoization   | 870 ms                                                 | 316 ms: 2.75x faster                                          |
| generators               | 80.1 ms                                                | 29.7 ms: 2.69x faster                                         |
| mdp                      | 2.85 sec                                               | 1.29 sec: 2.21x faster                                        |
| deltablue                | 7.91 ms                                                | 3.65 ms: 2.17x faster                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 493 ms: 2.06x faster                                          |
| go                       | 240 ms                                                 | 122 ms: 1.96x faster                                          |
| pylint                   | 551 ms                                                 | 282 ms: 1.96x faster                                          |
| deepcopy_memo            | 58.5 us                                                | 30.4 us: 1.92x faster                                         |
| chaos                    | 115 ms                                                 | 60.6 ms: 1.91x faster                                         |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                          |
| deepcopy                 | 479 us                                                 | 260 us: 1.84x faster                                          |
| richards_super           | 94.7 ms                                                | 51.8 ms: 1.83x faster                                         |
| raytrace                 | 507 ms                                                 | 283 ms: 1.79x faster                                          |
| richards                 | 79.3 ms                                                | 45.3 ms: 1.75x faster                                         |
| hexiom                   | 10.4 ms                                                | 6.13 ms: 1.70x faster                                         |
| scimark_monte_carlo      | 118 ms                                                 | 69.9 ms: 1.69x faster                                         |
| tomli_loads              | 3.14 sec                                               | 1.89 sec: 1.66x faster                                        |
| scimark_sor              | 220 ms                                                 | 134 ms: 1.64x faster                                          |
| comprehensions           | 28.8 us                                                | 17.6 us: 1.63x faster                                         |
| coroutines               | 35.1 ms                                                | 22.2 ms: 1.58x faster                                         |
| pyflate                  | 716 ms                                                 | 455 ms: 1.57x faster                                          |
| crypto_pyaes             | 128 ms                                                 | 82.9 ms: 1.54x faster                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.73 us: 1.53x faster                                         |
| django_template          | 48.2 ms                                                | 32.7 ms: 1.47x faster                                         |
| pickle_pure_python       | 484 us                                                 | 330 us: 1.47x faster                                          |
| logging_simple           | 8.30 us                                                | 5.66 us: 1.47x faster                                         |
| genshi_text              | 31.8 ms                                                | 21.8 ms: 1.46x faster                                         |
| logging_format           | 9.09 us                                                | 6.24 us: 1.46x faster                                         |
| unpickle_pure_python     | 331 us                                                 | 228 us: 1.45x faster                                          |
| dulwich_log              | 84.3 ms                                                | 60.1 ms: 1.40x faster                                         |
| regex_compile            | 188 ms                                                 | 134 ms: 1.40x faster                                          |
| scimark_lu               | 176 ms                                                 | 127 ms: 1.39x faster                                          |
| html5lib                 | 88.9 ms                                                | 64.2 ms: 1.38x faster                                         |
| nbody                    | 154 ms                                                 | 111 ms: 1.38x faster                                          |
| pprint_pformat           | 2.10 sec                                               | 1.53 sec: 1.38x faster                                        |
| mako                     | 16.3 ms                                                | 11.9 ms: 1.37x faster                                         |
| float                    | 117 ms                                                 | 85.4 ms: 1.37x faster                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.0 ms: 1.37x faster                                         |
| pprint_safe_repr         | 1.02 sec                                               | 747 ms: 1.36x faster                                          |
| spectral_norm            | 170 ms                                                 | 127 ms: 1.34x faster                                          |
| 2to3                     | 348 ms                                                 | 262 ms: 1.33x faster                                          |
| genshi_xml               | 66.0 ms                                                | 50.3 ms: 1.31x faster                                         |
| xml_etree_process        | 79.1 ms                                                | 60.7 ms: 1.30x faster                                         |
| pycparser                | 1.58 sec                                               | 1.21 sec: 1.30x faster                                        |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 133 ms: 1.30x faster                                          |
| sympy_sum                | 196 ms                                                 | 152 ms: 1.29x faster                                          |
| sympy_str                | 346 ms                                                 | 274 ms: 1.26x faster                                          |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                        |
| nqueens                  | 106 ms                                                 | 85.5 ms: 1.24x faster                                         |
| fannkuch                 | 532 ms                                                 | 431 ms: 1.23x faster                                          |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                         |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.22x faster                                         |
| sympy_expand             | 566 ms                                                 | 466 ms: 1.21x faster                                          |
| regex_v8                 | 27.8 ms                                                | 23.3 ms: 1.19x faster                                         |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.18x faster                                          |
| xml_etree_iterparse      | 115 ms                                                 | 100 ms: 1.15x faster                                          |
| xml_etree_generate       | 99.4 ms                                                | 87.2 ms: 1.14x faster                                         |
| bench_thread_pool        | 986 us                                                 | 884 us: 1.12x faster                                          |
| async_generators         | 444 ms                                                 | 400 ms: 1.11x faster                                          |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                         |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                          |
| regex_effbot             | 3.63 ms                                                | 3.32 ms: 1.09x faster                                         |
| json                     | 5.69 ms                                                | 5.29 ms: 1.08x faster                                         |
| sqlite_synth             | 3.02 us                                                | 2.82 us: 1.07x faster                                         |
| json_loads               | 31.2 us                                                | 29.7 us: 1.05x faster                                         |
| scimark_fft              | 466 ms                                                 | 450 ms: 1.04x faster                                          |
| regex_dna                | 227 ms                                                 | 220 ms: 1.03x faster                                          |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 6.30 ms: 1.03x faster                                         |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                          |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                          |
| coverage                 | 79.4 ms                                                | 86.1 ms: 1.08x slower                                         |
| telco                    | 7.27 ms                                                | 7.92 ms: 1.09x slower                                         |
| gc_traversal             | 3.62 ms                                                | 4.86 ms: 1.34x slower                                         |
| python_startup_no_site   | 5.93 ms                                                | 8.18 ms: 1.38x slower                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.51 ms: 1.55x slower                                         |
| bench_mp_pool            | 24.0 ms                                                | 83.7 ms: 3.49x slower                                         |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                  |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250330-3.14.0a6+-696d3fd/bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.403x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 2.38x