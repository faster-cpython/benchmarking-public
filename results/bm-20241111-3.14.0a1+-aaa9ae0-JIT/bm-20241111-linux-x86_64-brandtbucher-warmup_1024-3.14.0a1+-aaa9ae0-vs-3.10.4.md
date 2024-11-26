# Results vs. 3.10.4

- fork: brandtbucher
- ref: warmup_1024
- machine: linux-x86_64
- commit hash: aaa9ae0
- commit date: 2024-11-11
- overall geometric mean: 1.396x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 269 ms: 1.29x faster                                                |
| docutils       | 3.30 sec                                               | 2.88 sec: 1.14x faster                                              |
| html5lib       | 88.9 ms                                                | 66.8 ms: 1.33x faster                                               |
| Geometric mean | (ref)                                                  | 1.25x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 334 ms: 2.18x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 421 ms: 2.07x faster                                                |
| async_tree_io           | 1.77 sec                                               | 864 ms: 2.05x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 575 ms: 1.77x faster                                                |
| Geometric mean          | (ref)                                                  | 2.01x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 83.9 ms: 1.83x faster                                               |
| float          | 117 ms                                                 | 76.4 ms: 1.53x faster                                               |
| pidigits       | 191 ms                                                 | 186 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.42x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 136 ms: 1.39x faster                                                |
| regex_v8       | 27.8 ms                                                | 24.3 ms: 1.14x faster                                               |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                |
| regex_effbot   | 3.63 ms                                                | 3.53 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.14x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 331 us                                                 | 198 us: 1.67x faster                                                |
| tomli_loads          | 3.14 sec                                               | 1.94 sec: 1.62x faster                                              |
| pickle_pure_python   | 484 us                                                 | 322 us: 1.51x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 55.4 ms: 1.43x faster                                               |
| json_dumps           | 14.2 ms                                                | 10.9 ms: 1.30x faster                                               |
| xml_etree_generate   | 99.4 ms                                                | 78.9 ms: 1.26x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 99.3 ms: 1.16x faster                                               |
| json_loads           | 31.2 us                                                | 26.9 us: 1.16x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                                |
| Geometric mean       | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 12.7 ms: 1.15x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                               |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.1 ms: 1.62x faster                                               |
| genshi_text     | 31.8 ms                                                | 24.1 ms: 1.32x faster                                               |
| django_template | 48.2 ms                                                | 36.6 ms: 1.32x faster                                               |
| genshi_xml      | 66.0 ms                                                | 56.7 ms: 1.16x faster                                               |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.26x faster                                                |
| deltablue                | 7.91 ms                                                | 3.26 ms: 2.43x faster                                               |
| generators               | 80.1 ms                                                | 35.7 ms: 2.24x faster                                               |
| async_tree_none          | 728 ms                                                 | 334 ms: 2.18x faster                                                |
| richards                 | 79.3 ms                                                | 37.9 ms: 2.09x faster                                               |
| richards_super           | 94.7 ms                                                | 45.3 ms: 2.09x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 421 ms: 2.07x faster                                                |
| async_tree_io            | 1.77 sec                                               | 864 ms: 2.05x faster                                                |
| chaos                    | 115 ms                                                 | 58.7 ms: 1.97x faster                                               |
| deepcopy_memo            | 58.5 us                                                | 29.8 us: 1.96x faster                                               |
| logging_silent           | 190 ns                                                 | 98.8 ns: 1.92x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 67.8 ms: 1.88x faster                                               |
| go                       | 240 ms                                                 | 131 ms: 1.83x faster                                                |
| nbody                    | 154 ms                                                 | 83.9 ms: 1.83x faster                                               |
| scimark_sor              | 220 ms                                                 | 121 ms: 1.81x faster                                                |
| raytrace                 | 507 ms                                                 | 280 ms: 1.81x faster                                                |
| scimark_monte_carlo      | 118 ms                                                 | 66.2 ms: 1.78x faster                                               |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 575 ms: 1.77x faster                                                |
| deepcopy                 | 479 us                                                 | 272 us: 1.76x faster                                                |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.68x faster                                               |
| unpickle_pure_python     | 331 us                                                 | 198 us: 1.67x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                               |
| pyflate                  | 716 ms                                                 | 441 ms: 1.62x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.94 sec: 1.62x faster                                              |
| mako                     | 16.3 ms                                                | 10.1 ms: 1.62x faster                                               |
| pylint                   | 551 ms                                                 | 353 ms: 1.56x faster                                                |
| sqlglot_transpile        | 2.57 ms                                                | 1.65 ms: 1.56x faster                                               |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                               |
| float                    | 117 ms                                                 | 76.4 ms: 1.53x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 2.75 us: 1.52x faster                                               |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.51x faster                                                |
| pickle_pure_python       | 484 us                                                 | 322 us: 1.51x faster                                                |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.50x faster                                                |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                               |
| logging_simple           | 8.30 us                                                | 5.65 us: 1.47x faster                                               |
| scimark_fft              | 466 ms                                                 | 318 ms: 1.47x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                              |
| hexiom                   | 10.4 ms                                                | 7.27 ms: 1.43x faster                                               |
| xml_etree_process        | 79.1 ms                                                | 55.4 ms: 1.43x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 716 ms: 1.42x faster                                                |
| regex_compile            | 188 ms                                                 | 136 ms: 1.39x faster                                                |
| fannkuch                 | 532 ms                                                 | 385 ms: 1.38x faster                                                |
| thrift                   | 1.07 ms                                                | 786 us: 1.36x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.74 ms: 1.36x faster                                               |
| html5lib                 | 88.9 ms                                                | 66.8 ms: 1.33x faster                                               |
| pycparser                | 1.58 sec                                               | 1.19 sec: 1.33x faster                                              |
| genshi_text              | 31.8 ms                                                | 24.1 ms: 1.32x faster                                               |
| django_template          | 48.2 ms                                                | 36.6 ms: 1.32x faster                                               |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.8 ms: 1.31x faster                                               |
| json_dumps               | 14.2 ms                                                | 10.9 ms: 1.30x faster                                               |
| 2to3                     | 348 ms                                                 | 269 ms: 1.29x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 78.9 ms: 1.26x faster                                               |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.25x faster                                               |
| dulwich_log              | 84.3 ms                                                | 67.3 ms: 1.25x faster                                               |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.25x faster                                                |
| sqlalchemy_declarative   | 172 ms                                                 | 138 ms: 1.25x faster                                                |
| sqlglot_optimize         | 69.2 ms                                                | 57.0 ms: 1.21x faster                                               |
| nqueens                  | 106 ms                                                 | 87.6 ms: 1.21x faster                                               |
| genshi_xml               | 66.0 ms                                                | 56.7 ms: 1.16x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 99.3 ms: 1.16x faster                                               |
| json_loads               | 31.2 us                                                | 26.9 us: 1.16x faster                                               |
| sympy_str                | 346 ms                                                 | 298 ms: 1.16x faster                                                |
| json                     | 5.69 ms                                                | 4.92 ms: 1.16x faster                                               |
| sympy_sum                | 196 ms                                                 | 170 ms: 1.16x faster                                                |
| sympy_integrate          | 25.8 ms                                                | 22.3 ms: 1.16x faster                                               |
| python_startup           | 14.6 ms                                                | 12.7 ms: 1.15x faster                                               |
| regex_v8                 | 27.8 ms                                                | 24.3 ms: 1.14x faster                                               |
| docutils                 | 3.30 sec                                               | 2.88 sec: 1.14x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                                |
| sympy_expand             | 566 ms                                                 | 503 ms: 1.12x faster                                                |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                |
| bench_thread_pool        | 986 us                                                 | 882 us: 1.12x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.78 us: 1.09x faster                                               |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                |
| mdp                      | 2.85 sec                                               | 2.73 sec: 1.04x faster                                              |
| regex_effbot             | 3.63 ms                                                | 3.53 ms: 1.03x faster                                               |
| pidigits                 | 191 ms                                                 | 186 ms: 1.02x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                |
| async_generators         | 444 ms                                                 | 458 ms: 1.03x slower                                                |
| telco                    | 7.27 ms                                                | 7.61 ms: 1.05x slower                                               |
| coverage                 | 79.4 ms                                                | 83.4 ms: 1.05x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.56 ms: 1.26x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.69 ms: 1.66x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 79.3 ms: 3.30x slower                                               |
| Geometric mean           | (ref)                                                  | 1.37x faster                                                        |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241111-3.14.0a1+-aaa9ae0-JIT/bm-20241111-linux-x86_64-brandtbucher-warmup_1024-3.14.0a1+-aaa9ae0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.396x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.29x