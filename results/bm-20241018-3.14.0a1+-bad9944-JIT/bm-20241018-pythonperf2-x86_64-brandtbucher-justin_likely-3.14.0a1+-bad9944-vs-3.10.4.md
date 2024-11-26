# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_likely
- machine: linux-x86_64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.284x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 314 ms: 1.11x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.21 sec: 1.06x faster                                                      |
| html5lib       | 94.6 ms                                                      | 70.7 ms: 1.34x faster                                                       |
| tornado_http   | 157 ms                                                       | 123 ms: 1.28x faster                                                        |
| Geometric mean | (ref)                                                        | 1.19x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 332 ms: 2.08x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 412 ms: 1.99x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 836 ms: 1.91x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 577 ms: 1.62x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.89x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 83.3 ms: 1.61x faster                                                       |
| float          | 111 ms                                                       | 79.3 ms: 1.40x faster                                                       |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 152 ms: 1.25x faster                                                        |
| regex_dna      | 261 ms                                                       | 247 ms: 1.06x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.9 ms: 1.01x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 226 us: 1.38x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.15 sec: 1.36x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 337 us: 1.35x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 58.6 ms: 1.30x faster                                                       |
| json_loads           | 30.3 us                                                      | 24.3 us: 1.25x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 82.0 ms: 1.13x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 100.0 ms: 1.11x faster                                                      |
| pickle_dict          | 29.5 us                                                      | 31.7 us: 1.07x slower                                                       |
| pickle               | 9.89 us                                                      | 10.7 us: 1.08x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.60 us: 1.12x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.4 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.98 ms: 1.23x slower                                                       |
| python_startup         | 11.5 ms                                                      | 14.9 ms: 1.30x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.39 ms: 1.57x faster                                                       |
| django_template | 50.2 ms                                                      | 43.9 ms: 1.14x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 28.3 ms: 1.11x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 65.1 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.18x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 178 us: 3.01x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.31 ms: 2.27x faster                                                       |
| async_tree_none          | 692 ms                                                       | 332 ms: 2.08x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 378 ms: 2.06x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 412 ms: 1.99x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.59 sec: 1.96x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 836 ms: 1.91x faster                                                        |
| richards_super           | 90.6 ms                                                      | 48.9 ms: 1.85x faster                                                       |
| logging_silent           | 167 ns                                                       | 90.8 ns: 1.84x faster                                                       |
| scimark_lu               | 167 ms                                                       | 93.9 ms: 1.78x faster                                                       |
| scimark_sor              | 180 ms                                                       | 103 ms: 1.75x faster                                                        |
| go                       | 262 ms                                                       | 151 ms: 1.73x faster                                                        |
| richards                 | 75.1 ms                                                      | 43.7 ms: 1.72x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 29.9 us: 1.67x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 71.5 ms: 1.67x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 577 ms: 1.62x faster                                                        |
| chaos                    | 109 ms                                                       | 67.0 ms: 1.62x faster                                                       |
| nbody                    | 134 ms                                                       | 83.3 ms: 1.61x faster                                                       |
| raytrace                 | 489 ms                                                       | 307 ms: 1.59x faster                                                        |
| pyflate                  | 733 ms                                                       | 467 ms: 1.57x faster                                                        |
| mako                     | 14.7 ms                                                      | 9.39 ms: 1.57x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 69.6 ms: 1.54x faster                                                       |
| spectral_norm            | 139 ms                                                       | 92.8 ms: 1.50x faster                                                       |
| generators               | 57.3 ms                                                      | 38.3 ms: 1.50x faster                                                       |
| deepcopy                 | 468 us                                                       | 313 us: 1.50x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.52 ms: 1.47x faster                                                       |
| comprehensions           | 26.7 us                                                      | 18.9 us: 1.41x faster                                                       |
| float                    | 111 ms                                                       | 79.3 ms: 1.40x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.8 ms: 1.39x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 226 us: 1.38x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.15 sec: 1.36x faster                                                      |
| pickle_pure_python       | 455 us                                                       | 337 us: 1.35x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.14 us: 1.35x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.34x faster                                                       |
| pylint                   | 566 ms                                                       | 422 ms: 1.34x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.63 us: 1.34x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 70.7 ms: 1.34x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 2.01 ms: 1.34x faster                                                       |
| fannkuch                 | 483 ms                                                       | 364 ms: 1.33x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                                      |
| hexiom                   | 9.42 ms                                                      | 7.16 ms: 1.31x faster                                                       |
| thrift                   | 1.18 ms                                                      | 899 us: 1.31x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.31x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 807 ms: 1.30x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 58.6 ms: 1.30x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.11 us: 1.29x faster                                                       |
| tornado_http             | 157 ms                                                       | 123 ms: 1.28x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 64.4 ms: 1.26x faster                                                       |
| regex_compile            | 190 ms                                                       | 152 ms: 1.25x faster                                                        |
| json_loads               | 30.3 us                                                      | 24.3 us: 1.25x faster                                                       |
| scimark_fft              | 361 ms                                                       | 291 ms: 1.24x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 952 us: 1.20x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.60 sec: 1.15x faster                                                      |
| json                     | 5.86 ms                                                      | 5.10 ms: 1.15x faster                                                       |
| django_template          | 50.2 ms                                                      | 43.9 ms: 1.14x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.47 ms: 1.14x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 82.0 ms: 1.13x faster                                                       |
| sympy_expand             | 600 ms                                                       | 534 ms: 1.12x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                                        |
| nqueens                  | 115 ms                                                       | 103 ms: 1.11x faster                                                        |
| 2to3                     | 350 ms                                                       | 314 ms: 1.11x faster                                                        |
| sympy_str                | 360 ms                                                       | 324 ms: 1.11x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 28.3 ms: 1.11x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 100.0 ms: 1.11x faster                                                      |
| sympy_sum                | 193 ms                                                       | 176 ms: 1.09x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.74 us: 1.09x faster                                                       |
| async_generators         | 421 ms                                                       | 388 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 134 ms: 1.07x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.21 sec: 1.06x faster                                                      |
| regex_dna                | 261 ms                                                       | 247 ms: 1.06x faster                                                        |
| meteor_contest           | 138 ms                                                       | 131 ms: 1.05x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 381 ms: 1.02x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 27.6 ms: 1.02x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 26.9 ms: 1.01x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 65.1 ms: 1.03x slower                                                       |
| telco                    | 7.23 ms                                                      | 7.73 ms: 1.07x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 31.7 us: 1.07x slower                                                       |
| pickle                   | 9.89 us                                                      | 10.7 us: 1.08x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.60 us: 1.12x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.4 us: 1.14x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.98 ms: 1.23x slower                                                       |
| python_startup           | 11.5 ms                                                      | 14.9 ms: 1.30x slower                                                       |
| coverage                 | 63.3 ms                                                      | 82.9 ms: 1.31x slower                                                       |
| unpack_sequence          | 59.9 ns                                                      | 91.3 ns: 1.52x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 5.21 ms: 1.53x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.89 ms: 1.64x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 3.16 sec: 496.10x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.18x faster                                                                |

Benchmark hidden because not significant (2): sqlglot_optimize, unpickle_list
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-pythonperf2-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.284x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.34x