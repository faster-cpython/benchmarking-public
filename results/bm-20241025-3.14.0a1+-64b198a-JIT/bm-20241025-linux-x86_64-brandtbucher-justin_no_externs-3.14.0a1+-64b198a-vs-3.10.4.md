# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.349x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 286 ms: 1.22x faster                                                      |
| docutils       | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                    |
| html5lib       | 88.9 ms                                                | 67.5 ms: 1.32x faster                                                     |
| tornado_http   | 136 ms                                                 | 96.4 ms: 1.41x faster                                                     |
| Geometric mean | (ref)                                                  | 1.26x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 339 ms: 2.15x faster                                                      |
| async_tree_memoization  | 870 ms                                                 | 419 ms: 2.07x faster                                                      |
| async_tree_io           | 1.77 sec                                               | 858 ms: 2.06x faster                                                      |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 580 ms: 1.75x faster                                                      |
| Geometric mean          | (ref)                                                  | 2.00x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 87.6 ms: 1.75x faster                                                     |
| float          | 117 ms                                                 | 78.6 ms: 1.49x faster                                                     |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.39x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 142 ms: 1.33x faster                                                      |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.13x faster                                                     |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                                      |
| regex_effbot   | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.01 sec: 1.56x faster                                                    |
| pickle_pure_python   | 484 us                                                 | 326 us: 1.49x faster                                                      |
| unpickle_pure_python | 331 us                                                 | 226 us: 1.46x faster                                                      |
| xml_etree_process    | 79.1 ms                                                | 58.0 ms: 1.37x faster                                                     |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.24x faster                                                     |
| xml_etree_generate   | 99.4 ms                                                | 82.4 ms: 1.21x faster                                                     |
| json_loads           | 31.2 us                                                | 27.1 us: 1.15x faster                                                     |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.14x faster                                                      |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.13x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.8 ms: 1.23x faster                                                     |
| python_startup_no_site | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.8 ms: 1.51x faster                                                     |
| django_template | 48.2 ms                                                | 36.6 ms: 1.32x faster                                                     |
| genshi_text     | 31.8 ms                                                | 26.5 ms: 1.20x faster                                                     |
| genshi_xml      | 66.0 ms                                                | 62.9 ms: 1.05x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.26x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 173 us: 3.14x faster                                                      |
| deltablue                | 7.91 ms                                                | 3.44 ms: 2.30x faster                                                     |
| async_tree_none          | 728 ms                                                 | 339 ms: 2.15x faster                                                      |
| generators               | 80.1 ms                                                | 37.6 ms: 2.13x faster                                                     |
| async_tree_memoization   | 870 ms                                                 | 419 ms: 2.07x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 858 ms: 2.06x faster                                                      |
| richards_super           | 94.7 ms                                                | 49.7 ms: 1.91x faster                                                     |
| deepcopy_memo            | 58.5 us                                                | 31.3 us: 1.87x faster                                                     |
| chaos                    | 115 ms                                                 | 63.2 ms: 1.83x faster                                                     |
| nbody                    | 154 ms                                                 | 87.6 ms: 1.75x faster                                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 580 ms: 1.75x faster                                                      |
| crypto_pyaes             | 128 ms                                                 | 73.0 ms: 1.75x faster                                                     |
| richards                 | 79.3 ms                                                | 45.3 ms: 1.75x faster                                                     |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.73x faster                                                      |
| go                       | 240 ms                                                 | 140 ms: 1.72x faster                                                      |
| raytrace                 | 507 ms                                                 | 297 ms: 1.71x faster                                                      |
| logging_silent           | 190 ns                                                 | 111 ns: 1.70x faster                                                      |
| scimark_monte_carlo      | 118 ms                                                 | 69.6 ms: 1.70x faster                                                     |
| deepcopy                 | 479 us                                                 | 283 us: 1.70x faster                                                      |
| pylint                   | 551 ms                                                 | 329 ms: 1.68x faster                                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.36 ms: 1.59x faster                                                     |
| tomli_loads              | 3.14 sec                                               | 2.01 sec: 1.56x faster                                                    |
| comprehensions           | 28.8 us                                                | 18.8 us: 1.53x faster                                                     |
| scimark_lu               | 176 ms                                                 | 116 ms: 1.52x faster                                                      |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                     |
| mako                     | 16.3 ms                                                | 10.8 ms: 1.51x faster                                                     |
| sqlglot_transpile        | 2.57 ms                                                | 1.72 ms: 1.50x faster                                                     |
| pyflate                  | 716 ms                                                 | 480 ms: 1.49x faster                                                      |
| float                    | 117 ms                                                 | 78.6 ms: 1.49x faster                                                     |
| pickle_pure_python       | 484 us                                                 | 326 us: 1.49x faster                                                      |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                                     |
| logging_simple           | 8.30 us                                                | 5.60 us: 1.48x faster                                                     |
| unpickle_pure_python     | 331 us                                                 | 226 us: 1.46x faster                                                      |
| deepcopy_reduce          | 4.17 us                                                | 2.88 us: 1.45x faster                                                     |
| tornado_http             | 136 ms                                                 | 96.4 ms: 1.41x faster                                                     |
| scimark_fft              | 466 ms                                                 | 336 ms: 1.39x faster                                                      |
| spectral_norm            | 170 ms                                                 | 123 ms: 1.38x faster                                                      |
| hexiom                   | 10.4 ms                                                | 7.60 ms: 1.37x faster                                                     |
| xml_etree_process        | 79.1 ms                                                | 58.0 ms: 1.37x faster                                                     |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                                    |
| thrift                   | 1.07 ms                                                | 796 us: 1.35x faster                                                      |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                                    |
| pprint_safe_repr         | 1.02 sec                                               | 766 ms: 1.33x faster                                                      |
| regex_compile            | 188 ms                                                 | 142 ms: 1.33x faster                                                      |
| html5lib                 | 88.9 ms                                                | 67.5 ms: 1.32x faster                                                     |
| django_template          | 48.2 ms                                                | 36.6 ms: 1.32x faster                                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.96 ms: 1.31x faster                                                     |
| fannkuch                 | 532 ms                                                 | 409 ms: 1.30x faster                                                      |
| sqlalchemy_imperative    | 23.3 ms                                                | 18.2 ms: 1.28x faster                                                     |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                                     |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.24x faster                                                     |
| python_startup           | 14.6 ms                                                | 11.8 ms: 1.23x faster                                                     |
| dulwich_log              | 84.3 ms                                                | 68.5 ms: 1.23x faster                                                     |
| 2to3                     | 348 ms                                                 | 286 ms: 1.22x faster                                                      |
| sqlglot_normalize        | 143 ms                                                 | 118 ms: 1.21x faster                                                      |
| xml_etree_generate       | 99.4 ms                                                | 82.4 ms: 1.21x faster                                                     |
| genshi_text              | 31.8 ms                                                | 26.5 ms: 1.20x faster                                                     |
| sqlalchemy_declarative   | 172 ms                                                 | 148 ms: 1.16x faster                                                      |
| json_loads               | 31.2 us                                                | 27.1 us: 1.15x faster                                                     |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.14x faster                                                      |
| nqueens                  | 106 ms                                                 | 93.2 ms: 1.14x faster                                                     |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.13x faster                                                      |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.13x faster                                                     |
| sqlglot_optimize         | 69.2 ms                                                | 61.6 ms: 1.12x faster                                                     |
| json                     | 5.69 ms                                                | 5.11 ms: 1.11x faster                                                     |
| docutils                 | 3.30 sec                                               | 2.97 sec: 1.11x faster                                                    |
| sympy_str                | 346 ms                                                 | 312 ms: 1.11x faster                                                      |
| bench_thread_pool        | 986 us                                                 | 893 us: 1.10x faster                                                      |
| sympy_expand             | 566 ms                                                 | 516 ms: 1.10x faster                                                      |
| sympy_sum                | 196 ms                                                 | 180 ms: 1.09x faster                                                      |
| sympy_integrate          | 25.8 ms                                                | 24.0 ms: 1.08x faster                                                     |
| meteor_contest           | 120 ms                                                 | 113 ms: 1.06x faster                                                      |
| genshi_xml               | 66.0 ms                                                | 62.9 ms: 1.05x faster                                                     |
| mdp                      | 2.85 sec                                               | 2.75 sec: 1.04x faster                                                    |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                      |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                                      |
| asyncio_websockets       | 559 ms                                                 | 554 ms: 1.01x faster                                                      |
| async_generators         | 444 ms                                                 | 458 ms: 1.03x slower                                                      |
| regex_effbot             | 3.63 ms                                                | 3.77 ms: 1.04x slower                                                     |
| coverage                 | 79.4 ms                                                | 83.8 ms: 1.06x slower                                                     |
| telco                    | 7.27 ms                                                | 8.04 ms: 1.11x slower                                                     |
| python_startup_no_site   | 5.93 ms                                                | 7.08 ms: 1.19x slower                                                     |
| gc_traversal             | 3.62 ms                                                | 4.75 ms: 1.31x slower                                                     |
| create_gc_cycles         | 1.62 ms                                                | 2.68 ms: 1.65x slower                                                     |
| bench_mp_pool            | 24.0 ms                                                | 84.7 ms: 3.53x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.32x faster                                                              |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241025-3.14.0a1+-64b198a-JIT/bm-20241025-linux-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.349x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.33x