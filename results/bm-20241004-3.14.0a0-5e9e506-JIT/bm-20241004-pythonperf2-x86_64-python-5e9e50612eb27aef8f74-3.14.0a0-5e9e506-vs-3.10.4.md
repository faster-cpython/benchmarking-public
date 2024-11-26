# Results vs. 3.10.4

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: linux-x86_64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.288x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 318 ms: 1.10x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.27 sec: 1.04x faster                                                      |
| html5lib       | 94.6 ms                                                      | 71.5 ms: 1.32x faster                                                       |
| tornado_http   | 157 ms                                                       | 124 ms: 1.26x faster                                                        |
| Geometric mean | (ref)                                                        | 1.18x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 326 ms: 2.12x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 417 ms: 1.96x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 842 ms: 1.90x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 566 ms: 1.65x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.90x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 81.0 ms: 1.66x faster                                                       |
| float          | 111 ms                                                       | 77.5 ms: 1.43x faster                                                       |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.37x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 149 ms: 1.28x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                       |
| regex_dna      | 261 ms                                                       | 253 ms: 1.03x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 219 us: 1.42x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 334 us: 1.36x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.18 sec: 1.34x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 57.1 ms: 1.33x faster                                                       |
| json_loads           | 30.3 us                                                      | 23.5 us: 1.29x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 79.8 ms: 1.16x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.09x faster                                                        |
| pickle_dict          | 29.5 us                                                      | 30.7 us: 1.04x slower                                                       |
| pickle               | 9.89 us                                                      | 10.3 us: 1.04x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.31 us: 1.05x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.7 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.1 ms: 1.31x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.20 ms: 1.60x faster                                                       |
| django_template | 50.2 ms                                                      | 44.9 ms: 1.12x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 28.2 ms: 1.12x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 62.3 ms: 1.02x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.19x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 179 us: 3.00x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.23 ms: 2.32x faster                                                       |
| async_tree_none          | 692 ms                                                       | 326 ms: 2.12x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 377 ms: 2.07x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 417 ms: 1.96x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 842 ms: 1.90x faster                                                        |
| logging_silent           | 167 ns                                                       | 91.1 ns: 1.84x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 27.3 us: 1.83x faster                                                       |
| scimark_sor              | 180 ms                                                       | 102 ms: 1.76x faster                                                        |
| richards_super           | 90.6 ms                                                      | 52.5 ms: 1.72x faster                                                       |
| scimark_lu               | 167 ms                                                       | 97.2 ms: 1.72x faster                                                       |
| go                       | 262 ms                                                       | 153 ms: 1.71x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 71.2 ms: 1.67x faster                                                       |
| nbody                    | 134 ms                                                       | 81.0 ms: 1.66x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 566 ms: 1.65x faster                                                        |
| chaos                    | 109 ms                                                       | 65.7 ms: 1.65x faster                                                       |
| pyflate                  | 733 ms                                                       | 450 ms: 1.63x faster                                                        |
| richards                 | 75.1 ms                                                      | 46.5 ms: 1.62x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.20 ms: 1.60x faster                                                       |
| deepcopy                 | 468 us                                                       | 300 us: 1.56x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 69.1 ms: 1.55x faster                                                       |
| spectral_norm            | 139 ms                                                       | 90.6 ms: 1.54x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.50 ms: 1.49x faster                                                       |
| generators               | 57.3 ms                                                      | 38.8 ms: 1.48x faster                                                       |
| raytrace                 | 489 ms                                                       | 331 ms: 1.48x faster                                                        |
| float                    | 111 ms                                                       | 77.5 ms: 1.43x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.3 ms: 1.42x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 219 us: 1.42x faster                                                        |
| comprehensions           | 26.7 us                                                      | 19.3 us: 1.39x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 334 us: 1.36x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 15.7 ms: 1.36x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.98 ms: 1.36x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 780 ms: 1.35x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.18 sec: 1.34x faster                                                      |
| pprint_pformat           | 2.15 sec                                                     | 1.61 sec: 1.34x faster                                                      |
| deepcopy_reduce          | 4.01 us                                                      | 3.00 us: 1.34x faster                                                       |
| pylint                   | 566 ms                                                       | 425 ms: 1.33x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 57.1 ms: 1.33x faster                                                       |
| fannkuch                 | 483 ms                                                       | 364 ms: 1.33x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 71.5 ms: 1.32x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 7.12 ms: 1.32x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                                      |
| logging_simple           | 8.88 us                                                      | 6.76 us: 1.31x faster                                                       |
| json_loads               | 30.3 us                                                      | 23.5 us: 1.29x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.46 us: 1.29x faster                                                       |
| thrift                   | 1.18 ms                                                      | 910 us: 1.29x faster                                                        |
| scimark_fft              | 361 ms                                                       | 283 ms: 1.28x faster                                                        |
| regex_compile            | 190 ms                                                       | 149 ms: 1.28x faster                                                        |
| tornado_http             | 157 ms                                                       | 124 ms: 1.26x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.15 ms: 1.22x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 67.0 ms: 1.21x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 969 us: 1.18x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.59 sec: 1.16x faster                                                      |
| xml_etree_generate       | 92.3 ms                                                      | 79.8 ms: 1.16x faster                                                       |
| json                     | 5.86 ms                                                      | 5.16 ms: 1.14x faster                                                       |
| nqueens                  | 115 ms                                                       | 102 ms: 1.13x faster                                                        |
| sympy_expand             | 600 ms                                                       | 536 ms: 1.12x faster                                                        |
| django_template          | 50.2 ms                                                      | 44.9 ms: 1.12x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 28.2 ms: 1.12x faster                                                       |
| sympy_str                | 360 ms                                                       | 326 ms: 1.11x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.10x faster                                                        |
| 2to3                     | 350 ms                                                       | 318 ms: 1.10x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.72 us: 1.10x faster                                                       |
| async_generators         | 421 ms                                                       | 386 ms: 1.09x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 102 ms: 1.09x faster                                                        |
| sympy_sum                | 193 ms                                                       | 179 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 252 ms: 1.08x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 134 ms: 1.07x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                       |
| docutils                 | 3.41 sec                                                     | 3.27 sec: 1.04x faster                                                      |
| meteor_contest           | 138 ms                                                       | 134 ms: 1.03x faster                                                        |
| regex_dna                | 261 ms                                                       | 253 ms: 1.03x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 382 ms: 1.02x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 62.3 ms: 1.02x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 27.8 ms: 1.01x faster                                                       |
| pickle_dict              | 29.5 us                                                      | 30.7 us: 1.04x slower                                                       |
| pickle                   | 9.89 us                                                      | 10.3 us: 1.04x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.31 us: 1.05x slower                                                       |
| telco                    | 7.23 ms                                                      | 7.63 ms: 1.05x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.51 ms: 1.14x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.7 us: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                       |
| coverage                 | 63.3 ms                                                      | 78.8 ms: 1.25x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.1 ms: 1.31x slower                                                       |
| unpack_sequence          | 59.9 ns                                                      | 87.5 ns: 1.46x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.80 ms: 1.59x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 5.43 ms: 1.59x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 2.25 sec: 353.43x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.19x faster                                                                |

Benchmark hidden because not significant (2): sqlglot_optimize, unpickle_list
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-pythonperf2-x86_64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.288x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.34x