# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_reserved_fram
- machine: linux-x86_64
- commit hash: 735a0ce
- commit date: 2024-11-19
- overall geometric mean: 1.387x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 279 ms: 1.25x faster                                                         |
| docutils       | 3.30 sec                                               | 2.93 sec: 1.12x faster                                                       |
| html5lib       | 88.9 ms                                                | 65.7 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                  | 1.24x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 334 ms: 2.18x faster                                                         |
| async_tree_memoization  | 870 ms                                                 | 420 ms: 2.07x faster                                                         |
| async_tree_io           | 1.77 sec                                               | 864 ms: 2.05x faster                                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 584 ms: 1.74x faster                                                         |
| Geometric mean          | (ref)                                                  | 2.00x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 82.4 ms: 1.86x faster                                                        |
| float          | 117 ms                                                 | 76.6 ms: 1.53x faster                                                        |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                  | 1.43x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 139 ms: 1.36x faster                                                         |
| regex_v8       | 27.8 ms                                                | 25.4 ms: 1.10x faster                                                        |
| regex_dna      | 227 ms                                                 | 219 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.59x faster                                                       |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.51x faster                                                         |
| pickle_pure_python   | 484 us                                                 | 325 us: 1.49x faster                                                         |
| xml_etree_process    | 79.1 ms                                                | 55.7 ms: 1.42x faster                                                        |
| json_dumps           | 14.2 ms                                                | 11.1 ms: 1.28x faster                                                        |
| xml_etree_generate   | 99.4 ms                                                | 79.1 ms: 1.26x faster                                                        |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                                        |
| xml_etree_iterparse  | 115 ms                                                 | 101 ms: 1.14x faster                                                         |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                                         |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| python_startup_no_site | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                        |
| django_template | 48.2 ms                                                | 33.9 ms: 1.42x faster                                                        |
| genshi_text     | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                        |
| genshi_xml      | 66.0 ms                                                | 58.8 ms: 1.12x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 171 us: 3.19x faster                                                         |
| deltablue                | 7.91 ms                                                | 3.28 ms: 2.41x faster                                                        |
| generators               | 80.1 ms                                                | 35.9 ms: 2.23x faster                                                        |
| async_tree_none          | 728 ms                                                 | 334 ms: 2.18x faster                                                         |
| richards_super           | 94.7 ms                                                | 45.1 ms: 2.10x faster                                                        |
| async_tree_memoization   | 870 ms                                                 | 420 ms: 2.07x faster                                                         |
| async_tree_io            | 1.77 sec                                               | 864 ms: 2.05x faster                                                         |
| richards                 | 79.3 ms                                                | 39.1 ms: 2.02x faster                                                        |
| logging_silent           | 190 ns                                                 | 96.3 ns: 1.97x faster                                                        |
| deepcopy_memo            | 58.5 us                                                | 29.9 us: 1.96x faster                                                        |
| chaos                    | 115 ms                                                 | 59.6 ms: 1.94x faster                                                        |
| nbody                    | 154 ms                                                 | 82.4 ms: 1.86x faster                                                        |
| scimark_sor              | 220 ms                                                 | 118 ms: 1.86x faster                                                         |
| crypto_pyaes             | 128 ms                                                 | 68.9 ms: 1.85x faster                                                        |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                                         |
| scimark_monte_carlo      | 118 ms                                                 | 64.5 ms: 1.83x faster                                                        |
| go                       | 240 ms                                                 | 134 ms: 1.80x faster                                                         |
| deepcopy                 | 479 us                                                 | 272 us: 1.76x faster                                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 584 ms: 1.74x faster                                                         |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.64x faster                                                        |
| pyflate                  | 716 ms                                                 | 443 ms: 1.62x faster                                                         |
| djangocms                | 38.4 us                                                | 23.8 us: 1.61x faster                                                        |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.61x faster                                                        |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.59x faster                                                       |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                        |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.55x faster                                                        |
| float                    | 117 ms                                                 | 76.6 ms: 1.53x faster                                                        |
| scimark_lu               | 176 ms                                                 | 115 ms: 1.53x faster                                                         |
| sqlglot_transpile        | 2.57 ms                                                | 1.70 ms: 1.52x faster                                                        |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.51x faster                                                         |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                                        |
| pickle_pure_python       | 484 us                                                 | 325 us: 1.49x faster                                                         |
| hexiom                   | 10.4 ms                                                | 7.00 ms: 1.48x faster                                                        |
| logging_format           | 9.09 us                                                | 6.15 us: 1.48x faster                                                        |
| pylint                   | 551 ms                                                 | 376 ms: 1.47x faster                                                         |
| scimark_fft              | 466 ms                                                 | 322 ms: 1.44x faster                                                         |
| spectral_norm            | 170 ms                                                 | 118 ms: 1.44x faster                                                         |
| django_template          | 48.2 ms                                                | 33.9 ms: 1.42x faster                                                        |
| xml_etree_process        | 79.1 ms                                                | 55.7 ms: 1.42x faster                                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.65 ms: 1.39x faster                                                        |
| pprint_pformat           | 2.10 sec                                               | 1.52 sec: 1.39x faster                                                       |
| pprint_safe_repr         | 1.02 sec                                               | 743 ms: 1.37x faster                                                         |
| fannkuch                 | 532 ms                                                 | 390 ms: 1.36x faster                                                         |
| regex_compile            | 188 ms                                                 | 139 ms: 1.36x faster                                                         |
| html5lib                 | 88.9 ms                                                | 65.7 ms: 1.35x faster                                                        |
| thrift                   | 1.07 ms                                                | 795 us: 1.35x faster                                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.7 ms: 1.32x faster                                                        |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.31x faster                                                       |
| json_dumps               | 14.2 ms                                                | 11.1 ms: 1.28x faster                                                        |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                        |
| genshi_text              | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                        |
| xml_etree_generate       | 99.4 ms                                                | 79.1 ms: 1.26x faster                                                        |
| 2to3                     | 348 ms                                                 | 279 ms: 1.25x faster                                                         |
| dulwich_log              | 84.3 ms                                                | 67.8 ms: 1.24x faster                                                        |
| sqlglot_normalize        | 143 ms                                                 | 116 ms: 1.23x faster                                                         |
| nqueens                  | 106 ms                                                 | 87.9 ms: 1.20x faster                                                        |
| sqlalchemy_declarative   | 172 ms                                                 | 147 ms: 1.17x faster                                                         |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                                        |
| sqlglot_optimize         | 69.2 ms                                                | 60.4 ms: 1.14x faster                                                        |
| xml_etree_iterparse      | 115 ms                                                 | 101 ms: 1.14x faster                                                         |
| json                     | 5.69 ms                                                | 4.98 ms: 1.14x faster                                                        |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                                        |
| sympy_str                | 346 ms                                                 | 304 ms: 1.14x faster                                                         |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                                         |
| docutils                 | 3.30 sec                                               | 2.93 sec: 1.12x faster                                                       |
| genshi_xml               | 66.0 ms                                                | 58.8 ms: 1.12x faster                                                        |
| sympy_expand             | 566 ms                                                 | 504 ms: 1.12x faster                                                         |
| sympy_sum                | 196 ms                                                 | 175 ms: 1.12x faster                                                         |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                         |
| bench_thread_pool        | 986 us                                                 | 888 us: 1.11x faster                                                         |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.10x faster                                                       |
| sympy_integrate          | 25.8 ms                                                | 23.4 ms: 1.10x faster                                                        |
| regex_v8                 | 27.8 ms                                                | 25.4 ms: 1.10x faster                                                        |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                                        |
| regex_dna                | 227 ms                                                 | 219 ms: 1.04x faster                                                         |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                         |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                         |
| async_generators         | 444 ms                                                 | 454 ms: 1.02x slower                                                         |
| coverage                 | 79.4 ms                                                | 84.0 ms: 1.06x slower                                                        |
| telco                    | 7.27 ms                                                | 7.69 ms: 1.06x slower                                                        |
| python_startup_no_site   | 5.93 ms                                                | 7.11 ms: 1.20x slower                                                        |
| gc_traversal             | 3.62 ms                                                | 4.57 ms: 1.26x slower                                                        |
| create_gc_cycles         | 1.62 ms                                                | 2.69 ms: 1.66x slower                                                        |
| bench_mp_pool            | 24.0 ms                                                | 84.3 ms: 3.51x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.36x faster                                                                 |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20241119-3.14.0a1+-735a0ce-JIT/bm-20241119-linux-x86_64-brandtbucher-justin_reserved_fram-3.14.0a1+-735a0ce.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.387x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.34x