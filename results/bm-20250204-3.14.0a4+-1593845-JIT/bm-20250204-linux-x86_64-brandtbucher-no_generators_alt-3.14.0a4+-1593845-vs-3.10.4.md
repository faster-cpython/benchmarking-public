# Results vs. 3.10.4

- fork: brandtbucher
- ref: no_generators_alt
- machine: linux-x86_64
- commit hash: 1593845
- commit date: 2025-02-04
- overall geometric mean: 1.437x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 261 ms: 1.33x faster                                                      |
| docutils       | 3.30 sec                                               | 2.69 sec: 1.22x faster                                                    |
| html5lib       | 88.9 ms                                                | 63.5 ms: 1.40x faster                                                     |
| Geometric mean | (ref)                                                  | 1.32x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 628 ms: 2.81x faster                                                      |
| async_tree_none         | 728 ms                                                 | 269 ms: 2.70x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 329 ms: 2.64x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 499 ms: 2.04x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.53x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 117 ms                                                 | 67.6 ms: 1.73x faster                                                     |
| nbody          | 154 ms                                                 | 90.0 ms: 1.71x faster                                                     |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.45x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.46x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 2.98 ms: 1.22x faster                                                     |
| regex_dna      | 227 ms                                                 | 194 ms: 1.17x faster                                                      |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                     |
| Geometric mean | (ref)                                                  | 1.24x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.82 sec: 1.72x faster                                                    |
| unpickle_pure_python | 331 us                                                 | 201 us: 1.65x faster                                                      |
| pickle_pure_python   | 484 us                                                 | 319 us: 1.52x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 56.4 ms: 1.40x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 79.3 ms: 1.25x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 95.2 ms: 1.21x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 139 ms: 1.21x faster                                                      |
| json_loads           | 31.2 us                                                | 28.7 us: 1.09x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.00 ms: 1.63x faster                                                    |
| django_template | 48.2 ms                                                | 33.1 ms: 1.46x faster                                                     |
| genshi_text     | 31.8 ms                                                | 24.0 ms: 1.32x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 62.1 ms: 1.06x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 163 us: 3.34x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 628 ms: 2.81x faster                                                      |
| generators               | 80.1 ms                                                | 29.6 ms: 2.71x faster                                                     |
| async_tree_none          | 728 ms                                                 | 269 ms: 2.70x faster                                                      |
| async_tree_memoization   | 870 ms                                                 | 329 ms: 2.64x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.52 ms: 2.25x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 499 ms: 2.04x faster                                                      |
| chaos                    | 115 ms                                                 | 59.3 ms: 1.95x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 30.2 us: 1.93x faster                                                     |
| pylint                   | 551 ms                                                 | 286 ms: 1.93x faster                                                      |
| scimark_sor              | 220 ms                                                 | 115 ms: 1.91x faster                                                      |
| go                       | 240 ms                                                 | 126 ms: 1.91x faster                                                      |
| richards_super           | 94.7 ms                                                | 50.2 ms: 1.89x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 63.3 ms: 1.87x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 70.1 ms: 1.82x faster                                                     |
| spectral_norm            | 170 ms                                                 | 93.4 ms: 1.82x faster                                                     |
| richards                 | 79.3 ms                                                | 44.2 ms: 1.79x faster                                                     |
| deepcopy                 | 479 us                                                 | 271 us: 1.77x faster                                                      |
| raytrace                 | 507 ms                                                 | 290 ms: 1.75x faster                                                      |
| float                    | 117 ms                                                 | 67.6 ms: 1.73x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 1.82 sec: 1.72x faster                                                    |
| logging_silent           | 190 ns                                                 | 111 ns: 1.71x faster                                                      |
| nbody                    | 154 ms                                                 | 90.0 ms: 1.71x faster                                                     |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                     |
| comprehensions           | 28.8 us                                                | 17.2 us: 1.68x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 201 us: 1.65x faster                                                      |
| mako                     | 16.3 ms                                                | 10.00 ms: 1.63x faster                                                    |
| sqlglot_transpile        | 2.57 ms                                                | 1.60 ms: 1.61x faster                                                     |
| pyflate                  | 716 ms                                                 | 460 ms: 1.56x faster                                                      |
| pickle_pure_python       | 484 us                                                 | 319 us: 1.52x faster                                                      |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.77 us: 1.51x faster                                                     |
| scimark_fft              | 466 ms                                                 | 310 ms: 1.50x faster                                                      |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.60 us: 1.48x faster                                                     |
| coroutines               | 35.1 ms                                                | 23.7 ms: 1.48x faster                                                     |
| regex_compile            | 188 ms                                                 | 129 ms: 1.46x faster                                                      |
| django_template          | 48.2 ms                                                | 33.1 ms: 1.46x faster                                                     |
| hexiom                   | 10.4 ms                                                | 7.39 ms: 1.41x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.50 sec: 1.40x faster                                                    |
| xml_etree_process        | 79.1 ms                                                | 56.4 ms: 1.40x faster                                                     |
| html5lib                 | 88.9 ms                                                | 63.5 ms: 1.40x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.63 ms: 1.40x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.8 ms: 1.39x faster                                                     |
| thrift                   | 1.07 ms                                                | 773 us: 1.39x faster                                                      |
| pprint_safe_repr         | 1.02 sec                                               | 740 ms: 1.37x faster                                                      |
| fannkuch                 | 532 ms                                                 | 391 ms: 1.36x faster                                                      |
| 2to3                     | 348 ms                                                 | 261 ms: 1.33x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.33x faster                                                      |
| genshi_text              | 31.8 ms                                                | 24.0 ms: 1.32x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.31x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.22 sec: 1.29x faster                                                    |
| sqlglot_optimize         | 69.2 ms                                                | 54.0 ms: 1.28x faster                                                     |
| sympy_sum                | 196 ms                                                 | 154 ms: 1.28x faster                                                      |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 20.4 ms: 1.26x faster                                                     |
| xml_etree_generate       | 99.4 ms                                                | 79.3 ms: 1.25x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.25x faster                                                     |
| sympy_str                | 346 ms                                                 | 278 ms: 1.24x faster                                                      |
| docutils                 | 3.30 sec                                               | 2.69 sec: 1.22x faster                                                    |
| dulwich_log              | 84.3 ms                                                | 69.2 ms: 1.22x faster                                                     |
| regex_effbot             | 3.63 ms                                                | 2.98 ms: 1.22x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 95.2 ms: 1.21x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 139 ms: 1.21x faster                                                      |
| sympy_expand             | 566 ms                                                 | 469 ms: 1.21x faster                                                      |
| nqueens                  | 106 ms                                                 | 88.7 ms: 1.19x faster                                                     |
| regex_dna                | 227 ms                                                 | 194 ms: 1.17x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                                     |
| python_startup           | 14.6 ms                                                | 12.9 ms: 1.13x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.55 sec: 1.12x faster                                                    |
| json                     | 5.69 ms                                                | 5.13 ms: 1.11x faster                                                     |
| bench_thread_pool        | 986 us                                                 | 894 us: 1.10x faster                                                      |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                                      |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.10x faster                                                     |
| json_loads               | 31.2 us                                                | 28.7 us: 1.09x faster                                                     |
| async_generators         | 444 ms                                                 | 413 ms: 1.07x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 62.1 ms: 1.06x faster                                                     |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                      |
| telco                    | 7.27 ms                                                | 7.59 ms: 1.04x slower                                                     |
| coverage                 | 79.4 ms                                                | 89.6 ms: 1.13x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 4.94 ms: 1.36x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 81.2 ms: 3.38x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                              |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250204-3.14.0a4+-1593845-JIT/bm-20250204-linux-x86_64-brandtbucher-no_generators_alt-3.14.0a4+-1593845.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.437x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.28x