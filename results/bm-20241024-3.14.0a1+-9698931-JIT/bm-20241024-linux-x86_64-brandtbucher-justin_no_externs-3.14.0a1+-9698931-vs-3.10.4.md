# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.267x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 301 ms: 1.16x faster                                                      |
| docutils       | 3.30 sec                                               | 3.01 sec: 1.10x faster                                                    |
| html5lib       | 88.9 ms                                                | 68.6 ms: 1.30x faster                                                     |
| tornado_http   | 136 ms                                                 | 96.7 ms: 1.41x faster                                                     |
| Geometric mean | (ref)                                                  | 1.23x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 352 ms: 2.07x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 433 ms: 2.01x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 880 ms: 2.01x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 589 ms: 1.73x faster                                                      |
| Geometric mean          | (ref)                                                  | 1.95x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 102 ms: 1.50x faster                                                      |
| float          | 117 ms                                                 | 83.5 ms: 1.40x faster                                                     |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.29x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 154 ms: 1.23x faster                                                      |
| regex_v8       | 27.8 ms                                                | 25.9 ms: 1.07x faster                                                     |
| regex_dna      | 227 ms                                                 | 213 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.18 sec: 1.44x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 349 us: 1.39x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 248 us: 1.33x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 63.7 ms: 1.24x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                     |
| json_loads           | 31.2 us                                                | 27.0 us: 1.16x faster                                                     |
| xml_etree_parse      | 168 ms                                                 | 152 ms: 1.10x faster                                                      |
| xml_etree_generate   | 99.4 ms                                                | 90.4 ms: 1.10x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.22x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.8 ms: 1.23x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 12.1 ms: 1.35x faster                                                     |
| django_template | 48.2 ms                                                | 39.2 ms: 1.23x faster                                                     |
| genshi_text     | 31.8 ms                                                | 27.6 ms: 1.15x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 64.5 ms: 1.02x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.18x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 183 us: 2.97x faster                                                      |
| async_tree_none          | 728 ms                                                 | 352 ms: 2.07x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.93 ms: 2.02x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 433 ms: 2.01x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 880 ms: 2.01x faster                                                      |
| generators               | 80.1 ms                                                | 41.6 ms: 1.93x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 589 ms: 1.73x faster                                                      |
| deepcopy_memo            | 58.5 us                                                | 35.3 us: 1.66x faster                                                     |
| pylint                   | 551 ms                                                 | 337 ms: 1.64x faster                                                      |
| chaos                    | 115 ms                                                 | 72.9 ms: 1.58x faster                                                     |
| logging_silent           | 190 ns                                                 | 122 ns: 1.56x faster                                                      |
| deepcopy                 | 479 us                                                 | 309 us: 1.55x faster                                                      |
| raytrace                 | 507 ms                                                 | 327 ms: 1.55x faster                                                      |
| richards_super           | 94.7 ms                                                | 61.5 ms: 1.54x faster                                                     |
| crypto_pyaes             | 128 ms                                                 | 84.6 ms: 1.51x faster                                                     |
| coroutines               | 35.1 ms                                                | 23.3 ms: 1.50x faster                                                     |
| nbody                    | 154 ms                                                 | 102 ms: 1.50x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.47 ms: 1.48x faster                                                     |
| scimark_monte_carlo      | 118 ms                                                 | 80.7 ms: 1.47x faster                                                     |
| scimark_sor              | 220 ms                                                 | 151 ms: 1.46x faster                                                      |
| go                       | 240 ms                                                 | 165 ms: 1.45x faster                                                      |
| logging_format           | 9.09 us                                                | 6.27 us: 1.45x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 2.18 sec: 1.44x faster                                                    |
| logging_simple           | 8.30 us                                                | 5.77 us: 1.44x faster                                                     |
| scimark_lu               | 176 ms                                                 | 123 ms: 1.44x faster                                                      |
| tornado_http             | 136 ms                                                 | 96.7 ms: 1.41x faster                                                     |
| float                    | 117 ms                                                 | 83.5 ms: 1.40x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.84 ms: 1.40x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 349 us: 1.39x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 3.07 us: 1.36x faster                                                     |
| pyflate                  | 716 ms                                                 | 531 ms: 1.35x faster                                                      |
| mako                     | 16.3 ms                                                | 12.1 ms: 1.35x faster                                                     |
| richards                 | 79.3 ms                                                | 59.1 ms: 1.34x faster                                                     |
| thrift                   | 1.07 ms                                                | 801 us: 1.34x faster                                                      |
| unpickle_pure_python     | 331 us                                                 | 248 us: 1.33x faster                                                      |
| comprehensions           | 28.8 us                                                | 22.0 us: 1.31x faster                                                     |
| html5lib                 | 88.9 ms                                                | 68.6 ms: 1.30x faster                                                     |
| sqlalchemy_imperative    | 23.3 ms                                                | 18.1 ms: 1.29x faster                                                     |
| spectral_norm            | 170 ms                                                 | 135 ms: 1.26x faster                                                      |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 63.7 ms: 1.24x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.23 ms: 1.24x faster                                                     |
| python_startup           | 14.6 ms                                                | 11.8 ms: 1.23x faster                                                     |
| django_template          | 48.2 ms                                                | 39.2 ms: 1.23x faster                                                     |
| regex_compile            | 188 ms                                                 | 154 ms: 1.23x faster                                                      |
| dulwich_log              | 84.3 ms                                                | 68.9 ms: 1.22x faster                                                     |
| pycparser                | 1.58 sec                                               | 1.29 sec: 1.22x faster                                                    |
| scimark_fft              | 466 ms                                                 | 382 ms: 1.22x faster                                                      |
| json_dumps               | 14.2 ms                                                | 11.7 ms: 1.21x faster                                                     |
| hexiom                   | 10.4 ms                                                | 8.79 ms: 1.18x faster                                                     |
| pprint_safe_repr         | 1.02 sec                                               | 870 ms: 1.17x faster                                                      |
| pprint_pformat           | 2.10 sec                                               | 1.81 sec: 1.16x faster                                                    |
| 2to3                     | 348 ms                                                 | 301 ms: 1.16x faster                                                      |
| json_loads               | 31.2 us                                                | 27.0 us: 1.16x faster                                                     |
| genshi_text              | 31.8 ms                                                | 27.6 ms: 1.15x faster                                                     |
| sqlglot_normalize        | 143 ms                                                 | 125 ms: 1.15x faster                                                      |
| sqlalchemy_declarative   | 172 ms                                                 | 151 ms: 1.14x faster                                                      |
| json                     | 5.69 ms                                                | 5.15 ms: 1.11x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 152 ms: 1.10x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 90.4 ms: 1.10x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                      |
| docutils                 | 3.30 sec                                               | 3.01 sec: 1.10x faster                                                    |
| fannkuch                 | 532 ms                                                 | 486 ms: 1.09x faster                                                      |
| sympy_str                | 346 ms                                                 | 321 ms: 1.08x faster                                                      |
| sympy_expand             | 566 ms                                                 | 525 ms: 1.08x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 25.9 ms: 1.07x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.66 sec: 1.07x faster                                                    |
| bench_thread_pool        | 986 us                                                 | 921 us: 1.07x faster                                                      |
| sympy_sum                | 196 ms                                                 | 184 ms: 1.07x faster                                                      |
| regex_dna                | 227 ms                                                 | 213 ms: 1.06x faster                                                      |
| sqlglot_optimize         | 69.2 ms                                                | 65.7 ms: 1.05x faster                                                     |
| genshi_xml               | 66.0 ms                                                | 64.5 ms: 1.02x faster                                                     |
| sympy_integrate          | 25.8 ms                                                | 25.2 ms: 1.02x faster                                                     |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                      |
| meteor_contest           | 120 ms                                                 | 122 ms: 1.02x slower                                                      |
| async_generators         | 444 ms                                                 | 464 ms: 1.05x slower                                                      |
| coverage                 | 79.4 ms                                                | 84.6 ms: 1.06x slower                                                     |
| telco                    | 7.27 ms                                                | 8.42 ms: 1.16x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 4.70 ms: 1.30x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.69 ms: 1.66x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 84.6 ms: 3.52x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.24x faster                                                              |

Benchmark hidden because not significant (2): regex_effbot, nqueens
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241024-3.14.0a1+-9698931-JIT/bm-20241024-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.267x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: 1.33x