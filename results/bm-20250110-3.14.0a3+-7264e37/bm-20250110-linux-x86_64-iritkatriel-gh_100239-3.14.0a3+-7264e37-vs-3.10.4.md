# Results vs. 3.10.4

- fork: iritkatriel
- ref: gh_100239
- machine: linux-x86_64
- commit hash: 7264e37
- commit date: 2025-01-10
- overall geometric mean: 1.449x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.32x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 254 ms: 1.37x faster                                             |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                           |
| html5lib       | 88.9 ms                                                | 61.3 ms: 1.45x faster                                            |
| Geometric mean | (ref)                                                  | 1.36x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 604 ms: 2.93x faster                                             |
| async_tree_none         | 728 ms                                                 | 258 ms: 2.83x faster                                             |
| async_tree_memoization  | 870 ms                                                 | 325 ms: 2.68x faster                                             |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 483 ms: 2.10x faster                                             |
| Geometric mean          | (ref)                                                  | 2.61x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 94.2 ms: 1.63x faster                                            |
| float          | 117 ms                                                 | 71.9 ms: 1.63x faster                                            |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.40x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 128 ms: 1.47x faster                                             |
| regex_v8       | 27.8 ms                                                | 25.5 ms: 1.09x faster                                            |
| regex_effbot   | 3.63 ms                                                | 3.48 ms: 1.04x faster                                            |
| regex_dna      | 227 ms                                                 | 219 ms: 1.03x faster                                             |
| Geometric mean | (ref)                                                  | 1.15x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.64x faster                                           |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.52x faster                                             |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.51x faster                                             |
| xml_etree_process    | 79.1 ms                                                | 59.5 ms: 1.33x faster                                            |
| json_dumps           | 14.2 ms                                                | 11.4 ms: 1.24x faster                                            |
| xml_etree_parse      | 168 ms                                                 | 138 ms: 1.22x faster                                             |
| xml_etree_iterparse  | 115 ms                                                 | 97.5 ms: 1.18x faster                                            |
| json_loads           | 31.2 us                                                | 26.5 us: 1.18x faster                                            |
| xml_etree_generate   | 99.4 ms                                                | 85.3 ms: 1.17x faster                                            |
| Geometric mean       | (ref)                                                  | 1.32x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.8 ms: 1.14x faster                                            |
| python_startup_no_site | 5.93 ms                                                | 7.04 ms: 1.19x slower                                            |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.9 ms: 1.51x faster                                            |
| genshi_text     | 31.8 ms                                                | 22.2 ms: 1.43x faster                                            |
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                            |
| genshi_xml      | 66.0 ms                                                | 49.2 ms: 1.34x faster                                            |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.40x faster                                             |
| async_tree_io            | 1.77 sec                                               | 604 ms: 2.93x faster                                             |
| generators               | 80.1 ms                                                | 27.9 ms: 2.87x faster                                            |
| async_tree_none          | 728 ms                                                 | 258 ms: 2.83x faster                                             |
| async_tree_memoization   | 870 ms                                                 | 325 ms: 2.68x faster                                             |
| deltablue                | 7.91 ms                                                | 3.23 ms: 2.45x faster                                            |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 483 ms: 2.10x faster                                             |
| go                       | 240 ms                                                 | 115 ms: 2.09x faster                                             |
| chaos                    | 115 ms                                                 | 57.9 ms: 2.00x faster                                            |
| pylint                   | 551 ms                                                 | 277 ms: 1.99x faster                                             |
| raytrace                 | 507 ms                                                 | 270 ms: 1.88x faster                                             |
| deepcopy_memo            | 58.5 us                                                | 31.2 us: 1.87x faster                                            |
| richards_super           | 94.7 ms                                                | 50.8 ms: 1.87x faster                                            |
| deepcopy                 | 479 us                                                 | 261 us: 1.83x faster                                             |
| richards                 | 79.3 ms                                                | 44.2 ms: 1.79x faster                                            |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.78x faster                                             |
| crypto_pyaes             | 128 ms                                                 | 72.0 ms: 1.77x faster                                            |
| spectral_norm            | 170 ms                                                 | 96.3 ms: 1.76x faster                                            |
| logging_silent           | 190 ns                                                 | 109 ns: 1.75x faster                                             |
| scimark_monte_carlo      | 118 ms                                                 | 67.7 ms: 1.75x faster                                            |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.70x faster                                            |
| hexiom                   | 10.4 ms                                                | 6.23 ms: 1.67x faster                                            |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.64x faster                                           |
| pyflate                  | 716 ms                                                 | 437 ms: 1.64x faster                                             |
| nbody                    | 154 ms                                                 | 94.2 ms: 1.63x faster                                            |
| float                    | 117 ms                                                 | 71.9 ms: 1.63x faster                                            |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.62x faster                                            |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                            |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.52x faster                                             |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                             |
| django_template          | 48.2 ms                                                | 31.9 ms: 1.51x faster                                            |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.51x faster                                             |
| coroutines               | 35.1 ms                                                | 23.5 ms: 1.49x faster                                            |
| regex_compile            | 188 ms                                                 | 128 ms: 1.47x faster                                             |
| logging_simple           | 8.30 us                                                | 5.64 us: 1.47x faster                                            |
| logging_format           | 9.09 us                                                | 6.20 us: 1.47x faster                                            |
| html5lib                 | 88.9 ms                                                | 61.3 ms: 1.45x faster                                            |
| genshi_text              | 31.8 ms                                                | 22.2 ms: 1.43x faster                                            |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                            |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.5 ms: 1.42x faster                                            |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                           |
| pprint_safe_repr         | 1.02 sec                                               | 722 ms: 1.41x faster                                             |
| pycparser                | 1.58 sec                                               | 1.13 sec: 1.40x faster                                           |
| thrift                   | 1.07 ms                                                | 769 us: 1.39x faster                                             |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.66 ms: 1.39x faster                                            |
| sqlglot_normalize        | 143 ms                                                 | 104 ms: 1.38x faster                                             |
| 2to3                     | 348 ms                                                 | 254 ms: 1.37x faster                                             |
| genshi_xml               | 66.0 ms                                                | 49.2 ms: 1.34x faster                                            |
| scimark_fft              | 466 ms                                                 | 349 ms: 1.33x faster                                             |
| sqlalchemy_declarative   | 172 ms                                                 | 129 ms: 1.33x faster                                             |
| fannkuch                 | 532 ms                                                 | 399 ms: 1.33x faster                                             |
| nqueens                  | 106 ms                                                 | 79.4 ms: 1.33x faster                                            |
| xml_etree_process        | 79.1 ms                                                | 59.5 ms: 1.33x faster                                            |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                             |
| dulwich_log              | 84.3 ms                                                | 63.5 ms: 1.33x faster                                            |
| sqlglot_optimize         | 69.2 ms                                                | 52.7 ms: 1.31x faster                                            |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.29x faster                                            |
| sympy_str                | 346 ms                                                 | 269 ms: 1.29x faster                                             |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                           |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                            |
| json_dumps               | 14.2 ms                                                | 11.4 ms: 1.24x faster                                            |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                             |
| xml_etree_parse          | 168 ms                                                 | 138 ms: 1.22x faster                                             |
| xml_etree_iterparse      | 115 ms                                                 | 97.5 ms: 1.18x faster                                            |
| json_loads               | 31.2 us                                                | 26.5 us: 1.18x faster                                            |
| xml_etree_generate       | 99.4 ms                                                | 85.3 ms: 1.17x faster                                            |
| json                     | 5.69 ms                                                | 4.91 ms: 1.16x faster                                            |
| bench_thread_pool        | 986 us                                                 | 861 us: 1.15x faster                                             |
| python_startup           | 14.6 ms                                                | 12.8 ms: 1.14x faster                                            |
| mdp                      | 2.85 sec                                               | 2.51 sec: 1.14x faster                                           |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                             |
| regex_v8                 | 27.8 ms                                                | 25.5 ms: 1.09x faster                                            |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                            |
| async_generators         | 444 ms                                                 | 421 ms: 1.05x faster                                             |
| regex_effbot             | 3.63 ms                                                | 3.48 ms: 1.04x faster                                            |
| regex_dna                | 227 ms                                                 | 219 ms: 1.03x faster                                             |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                             |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                             |
| coverage                 | 79.4 ms                                                | 84.5 ms: 1.06x slower                                            |
| telco                    | 7.27 ms                                                | 7.77 ms: 1.07x slower                                            |
| python_startup_no_site   | 5.93 ms                                                | 7.04 ms: 1.19x slower                                            |
| gc_traversal             | 3.62 ms                                                | 4.85 ms: 1.34x slower                                            |
| create_gc_cycles         | 1.62 ms                                                | 2.46 ms: 1.52x slower                                            |
| bench_mp_pool            | 24.0 ms                                                | 81.6 ms: 3.40x slower                                            |
| Geometric mean           | (ref)                                                  | 1.42x faster                                                     |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250110-3.14.0a3+-7264e37/bm-20250110-linux-x86_64-iritkatriel-gh_100239-3.14.0a3+-7264e37.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.449x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.34x
- 99% likely to have a speedup of 1.32x

# Memory
- memory change: 1.26x