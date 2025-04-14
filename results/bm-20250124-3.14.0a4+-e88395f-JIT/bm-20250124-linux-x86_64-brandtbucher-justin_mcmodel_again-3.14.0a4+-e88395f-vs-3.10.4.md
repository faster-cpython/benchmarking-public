# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: linux-x86_64
- commit hash: e88395f
- commit date: 2025-01-24
- overall geometric mean: 1.441x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.70x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 259 ms: 1.35x faster                                                         |
| docutils       | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                       |
| html5lib       | 88.9 ms                                                | 63.2 ms: 1.40x faster                                                        |
| Geometric mean | (ref)                                                  | 1.33x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 614 ms: 2.88x faster                                                         |
| async_tree_none         | 728 ms                                                 | 274 ms: 2.66x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 340 ms: 2.56x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 505 ms: 2.01x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.51x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.4 ms: 1.91x faster                                                        |
| float          | 117 ms                                                 | 63.2 ms: 1.85x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                  | 1.54x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                         |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                        |
| regex_effbot   | 3.63 ms                                                | 3.32 ms: 1.09x faster                                                        |
| regex_dna      | 227 ms                                                 | 212 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 195 us: 1.69x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 309 us: 1.57x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 78.8 ms: 1.26x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                        |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                         |
| xml_etree_iterparse  | 115 ms                                                 | 96.0 ms: 1.20x faster                                                        |
| json_loads           | 31.2 us                                                | 35.0 us: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.33x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.19x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.0 ms: 1.62x faster                                                        |
| django_template | 48.2 ms                                                | 33.7 ms: 1.43x faster                                                        |
| genshi_text     | 31.8 ms                                                | 22.9 ms: 1.39x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 57.0 ms: 1.16x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 614 ms: 2.88x faster                                                         |
| async_tree_none          | 728 ms                                                 | 274 ms: 2.66x faster                                                         |
| async_tree_memoization   | 870 ms                                                 | 340 ms: 2.56x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.19 ms: 2.48x faster                                                        |
| generators               | 80.1 ms                                                | 35.8 ms: 2.24x faster                                                        |
| chaos                    | 115 ms                                                 | 56.9 ms: 2.03x faster                                                        |
| richards_super           | 94.7 ms                                                | 46.8 ms: 2.02x faster                                                        |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 505 ms: 2.01x faster                                                         |
| scimark_sor              | 220 ms                                                 | 113 ms: 1.94x faster                                                         |
| deepcopy_memo            | 58.5 us                                                | 30.2 us: 1.94x faster                                                        |
| richards                 | 79.3 ms                                                | 41.3 ms: 1.92x faster                                                        |
| pylint                   | 551 ms                                                 | 288 ms: 1.92x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 61.8 ms: 1.91x faster                                                        |
| nbody                    | 154 ms                                                 | 80.4 ms: 1.91x faster                                                        |
| crypto_pyaes             | 128 ms                                                 | 67.0 ms: 1.91x faster                                                        |
| go                       | 240 ms                                                 | 129 ms: 1.86x faster                                                         |
| float                    | 117 ms                                                 | 63.2 ms: 1.85x faster                                                        |
| raytrace                 | 507 ms                                                 | 278 ms: 1.82x faster                                                         |
| deepcopy                 | 479 us                                                 | 264 us: 1.81x faster                                                         |
| spectral_norm            | 170 ms                                                 | 96.1 ms: 1.77x faster                                                        |
| logging_silent           | 190 ns                                                 | 108 ns: 1.76x faster                                                         |
| sqlglot_parse            | 2.17 ms                                                | 1.25 ms: 1.73x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.85 sec: 1.70x faster                                                       |
| comprehensions           | 28.8 us                                                | 16.9 us: 1.70x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 195 us: 1.69x faster                                                         |
| pyflate                  | 716 ms                                                 | 433 ms: 1.65x faster                                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                        |
| mako                     | 16.3 ms                                                | 10.0 ms: 1.62x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 309 us: 1.57x faster                                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                        |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                         |
| scimark_fft              | 466 ms                                                 | 309 ms: 1.51x faster                                                         |
| logging_format           | 9.09 us                                                | 6.16 us: 1.47x faster                                                        |
| coroutines               | 35.1 ms                                                | 23.8 ms: 1.47x faster                                                        |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                         |
| hexiom                   | 10.4 ms                                                | 7.12 ms: 1.46x faster                                                        |
| logging_simple           | 8.30 us                                                | 5.72 us: 1.45x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 711 ms: 1.43x faster                                                         |
| django_template          | 48.2 ms                                                | 33.7 ms: 1.43x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 56.2 ms: 1.41x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.41x faster                                                       |
| html5lib                 | 88.9 ms                                                | 63.2 ms: 1.40x faster                                                        |
| thrift                   | 1.07 ms                                                | 769 us: 1.39x faster                                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                        |
| genshi_text              | 31.8 ms                                                | 22.9 ms: 1.39x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.66 ms: 1.39x faster                                                        |
| fannkuch                 | 532 ms                                                 | 384 ms: 1.38x faster                                                         |
| 2to3                     | 348 ms                                                 | 259 ms: 1.35x faster                                                         |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.32x faster                                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                                         |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                        |
| sympy_sum                | 196 ms                                                 | 155 ms: 1.27x faster                                                         |
| sqlglot_optimize         | 69.2 ms                                                | 54.7 ms: 1.26x faster                                                        |
| dulwich_log              | 84.3 ms                                                | 66.7 ms: 1.26x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 78.8 ms: 1.26x faster                                                        |
| sympy_integrate          | 25.8 ms                                                | 20.5 ms: 1.26x faster                                                        |
| json_dumps               | 14.2 ms                                                | 11.2 ms: 1.26x faster                                                        |
| sympy_str                | 346 ms                                                 | 279 ms: 1.24x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.67 sec: 1.23x faster                                                       |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                         |
| xml_etree_iterparse      | 115 ms                                                 | 96.0 ms: 1.20x faster                                                        |
| sympy_expand             | 566 ms                                                 | 472 ms: 1.20x faster                                                         |
| nqueens                  | 106 ms                                                 | 89.6 ms: 1.18x faster                                                        |
| genshi_xml               | 66.0 ms                                                | 57.0 ms: 1.16x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                        |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                        |
| sqlite_synth             | 3.02 us                                                | 2.70 us: 1.12x faster                                                        |
| mdp                      | 2.85 sec                                               | 2.56 sec: 1.11x faster                                                       |
| bench_thread_pool        | 986 us                                                 | 889 us: 1.11x faster                                                         |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                         |
| regex_effbot             | 3.63 ms                                                | 3.32 ms: 1.09x faster                                                        |
| async_generators         | 444 ms                                                 | 413 ms: 1.08x faster                                                         |
| regex_dna                | 227 ms                                                 | 212 ms: 1.07x faster                                                         |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                         |
| json                     | 5.69 ms                                                | 5.95 ms: 1.05x slower                                                        |
| telco                    | 7.27 ms                                                | 7.69 ms: 1.06x slower                                                        |
| json_loads               | 31.2 us                                                | 35.0 us: 1.12x slower                                                        |
| coverage                 | 79.4 ms                                                | 90.3 ms: 1.14x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.19x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 5.04 ms: 1.39x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 81.1 ms: 3.38x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                                 |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250124-3.14.0a4+-e88395f-JIT/bm-20250124-linux-x86_64-brandtbucher-justin_mcmodel_again-3.14.0a4+-e88395f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.441x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.70x