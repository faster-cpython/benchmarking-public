# Results vs. 3.10.4

- fork: brandtbucher
- ref: jump_backoff
- machine: linux-x86_64
- commit hash: 2e7a174
- commit date: 2024-11-13
- overall geometric mean: 1.274x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 297 ms: 1.18x faster                                                       |
| docutils       | 3.41 sec                                                     | 3.14 sec: 1.09x faster                                                     |
| html5lib       | 94.6 ms                                                      | 72.0 ms: 1.32x faster                                                      |
| Geometric mean | (ref)                                                        | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 340 ms: 2.03x faster                                                       |
| async_tree_memoization  | 819 ms                                                       | 416 ms: 1.97x faster                                                       |
| async_tree_io           | 1.60 sec                                                     | 857 ms: 1.86x faster                                                       |
| async_tree_cpu_io_mixed | 936 ms                                                       | 584 ms: 1.60x faster                                                       |
| Geometric mean          | (ref)                                                        | 1.86x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 87.7 ms: 1.53x faster                                                      |
| float          | 111 ms                                                       | 80.1 ms: 1.39x faster                                                      |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                        | 1.32x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 142 ms: 1.34x faster                                                       |
| regex_v8       | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                      |
| regex_dna      | 261 ms                                                       | 249 ms: 1.05x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                        | 1.07x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 197 us: 1.58x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.14 sec: 1.36x faster                                                     |
| pickle_pure_python   | 455 us                                                       | 334 us: 1.36x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 59.1 ms: 1.29x faster                                                      |
| json_loads           | 30.3 us                                                      | 25.3 us: 1.20x faster                                                      |
| xml_etree_generate   | 92.3 ms                                                      | 83.1 ms: 1.11x faster                                                      |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.08x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 152 ms: 1.06x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                      |
| python_startup         | 11.5 ms                                                      | 15.9 ms: 1.38x slower                                                      |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.49 ms: 1.55x faster                                                      |
| django_template | 50.2 ms                                                      | 42.7 ms: 1.18x faster                                                      |
| genshi_text     | 31.4 ms                                                      | 27.6 ms: 1.14x faster                                                      |
| genshi_xml      | 63.3 ms                                                      | 60.7 ms: 1.04x faster                                                      |
| Geometric mean  | (ref)                                                        | 1.21x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 180 us: 2.98x faster                                                       |
| deltablue                | 7.50 ms                                                      | 3.28 ms: 2.29x faster                                                      |
| async_tree_none          | 692 ms                                                       | 340 ms: 2.03x faster                                                       |
| async_tree_memoization   | 819 ms                                                       | 416 ms: 1.97x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 857 ms: 1.86x faster                                                       |
| richards_super           | 90.6 ms                                                      | 48.7 ms: 1.86x faster                                                      |
| logging_silent           | 167 ns                                                       | 95.1 ns: 1.76x faster                                                      |
| richards                 | 75.1 ms                                                      | 43.2 ms: 1.74x faster                                                      |
| scimark_lu               | 167 ms                                                       | 97.0 ms: 1.72x faster                                                      |
| go                       | 262 ms                                                       | 153 ms: 1.71x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 30.2 us: 1.65x faster                                                      |
| scimark_sor              | 180 ms                                                       | 111 ms: 1.63x faster                                                       |
| chaos                    | 109 ms                                                       | 66.7 ms: 1.63x faster                                                      |
| crypto_pyaes             | 119 ms                                                       | 73.6 ms: 1.62x faster                                                      |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 584 ms: 1.60x faster                                                       |
| pyflate                  | 733 ms                                                       | 463 ms: 1.58x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 197 us: 1.58x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 69.0 ms: 1.56x faster                                                      |
| mako                     | 14.7 ms                                                      | 9.49 ms: 1.55x faster                                                      |
| nbody                    | 134 ms                                                       | 87.7 ms: 1.53x faster                                                      |
| pylint                   | 566 ms                                                       | 377 ms: 1.50x faster                                                       |
| raytrace                 | 489 ms                                                       | 327 ms: 1.49x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.51 ms: 1.49x faster                                                      |
| deepcopy                 | 468 us                                                       | 318 us: 1.47x faster                                                       |
| generators               | 57.3 ms                                                      | 39.9 ms: 1.44x faster                                                      |
| coroutines               | 30.3 ms                                                      | 21.2 ms: 1.43x faster                                                      |
| spectral_norm            | 139 ms                                                       | 98.5 ms: 1.41x faster                                                      |
| sqlglot_transpile        | 2.68 ms                                                      | 1.92 ms: 1.40x faster                                                      |
| float                    | 111 ms                                                       | 80.1 ms: 1.39x faster                                                      |
| tomli_loads              | 2.92 sec                                                     | 2.14 sec: 1.36x faster                                                     |
| pickle_pure_python       | 455 us                                                       | 334 us: 1.36x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.53 us: 1.36x faster                                                      |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                     |
| comprehensions           | 26.7 us                                                      | 19.9 us: 1.34x faster                                                      |
| regex_compile            | 190 ms                                                       | 142 ms: 1.34x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.27 us: 1.33x faster                                                      |
| html5lib                 | 94.6 ms                                                      | 72.0 ms: 1.32x faster                                                      |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.31x faster                                                     |
| pathlib                  | 21.4 ms                                                      | 16.5 ms: 1.30x faster                                                      |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                      |
| hexiom                   | 9.42 ms                                                      | 7.27 ms: 1.30x faster                                                      |
| sqlalchemy_declarative   | 190 ms                                                       | 147 ms: 1.29x faster                                                       |
| thrift                   | 1.18 ms                                                      | 914 us: 1.29x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 59.1 ms: 1.29x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 817 ms: 1.29x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.13 us: 1.28x faster                                                      |
| fannkuch                 | 483 ms                                                       | 394 ms: 1.23x faster                                                       |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.7 ms: 1.21x faster                                                      |
| json_loads               | 30.3 us                                                      | 25.3 us: 1.20x faster                                                      |
| dulwich_log              | 81.1 ms                                                      | 68.0 ms: 1.19x faster                                                      |
| sympy_sum                | 193 ms                                                       | 163 ms: 1.18x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 966 us: 1.18x faster                                                       |
| 2to3                     | 350 ms                                                       | 297 ms: 1.18x faster                                                       |
| django_template          | 50.2 ms                                                      | 42.7 ms: 1.18x faster                                                      |
| scimark_fft              | 361 ms                                                       | 308 ms: 1.17x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.58 sec: 1.17x faster                                                     |
| genshi_text              | 31.4 ms                                                      | 27.6 ms: 1.14x faster                                                      |
| json                     | 5.86 ms                                                      | 5.17 ms: 1.14x faster                                                      |
| sympy_integrate          | 28.2 ms                                                      | 24.9 ms: 1.13x faster                                                      |
| sympy_str                | 360 ms                                                       | 319 ms: 1.13x faster                                                       |
| nqueens                  | 115 ms                                                       | 102 ms: 1.12x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 83.1 ms: 1.11x faster                                                      |
| sqlglot_normalize        | 144 ms                                                       | 130 ms: 1.11x faster                                                       |
| sympy_expand             | 600 ms                                                       | 545 ms: 1.10x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 64.0 ms: 1.10x faster                                                      |
| docutils                 | 3.41 sec                                                     | 3.14 sec: 1.09x faster                                                     |
| xml_etree_iterparse      | 110 ms                                                       | 102 ms: 1.08x faster                                                       |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.78 ms: 1.06x faster                                                      |
| regex_v8                 | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                      |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                      |
| xml_etree_parse          | 160 ms                                                       | 152 ms: 1.06x faster                                                       |
| regex_dna                | 261 ms                                                       | 249 ms: 1.05x faster                                                       |
| meteor_contest           | 138 ms                                                       | 132 ms: 1.05x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 60.7 ms: 1.04x faster                                                      |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                       |
| telco                    | 7.23 ms                                                      | 7.62 ms: 1.05x slower                                                      |
| async_generators         | 421 ms                                                       | 482 ms: 1.15x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                      |
| python_startup_no_site   | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                      |
| coverage                 | 63.3 ms                                                      | 80.4 ms: 1.27x slower                                                      |
| python_startup           | 11.5 ms                                                      | 15.9 ms: 1.38x slower                                                      |
| create_gc_cycles         | 1.76 ms                                                      | 2.90 ms: 1.65x slower                                                      |
| gc_traversal             | 3.42 ms                                                      | 6.10 ms: 1.79x slower                                                      |
| bench_mp_pool            | 6.37 ms                                                      | 1.60 sec: 250.78x slower                                                   |
| Geometric mean           | (ref)                                                        | 1.19x faster                                                               |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241113-3.14.0a1+-2e7a174-JIT/bm-20241113-pythonperf2-x86_64-brandtbucher-jump_backoff-3.14.0a1+-2e7a174.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.274x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.30x