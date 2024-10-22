# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_call_kw
- machine: linux-x86_64
- commit hash: 6b9055c
- commit date: 2024-08-14
- overall geometric mean: 1.13x faster
- HPT reliability: 99.87%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 353 ms: 1.01x slower                                                                |
| docutils       | 3.41 sec                                                     | 3.54 sec: 1.04x slower                                                              |
| html5lib       | 94.6 ms                                                      | 85.2 ms: 1.11x faster                                                               |
| tornado_http   | 157 ms                                                       | 127 ms: 1.24x faster                                                                |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 348 ms: 1.99x faster                                                                |
| async_tree_io           | 1.60 sec                                                     | 853 ms: 1.87x faster                                                                |
| async_tree_memoization  | 819 ms                                                       | 443 ms: 1.85x faster                                                                |
| async_tree_cpu_io_mixed | 936 ms                                                       | 604 ms: 1.55x faster                                                                |
| Geometric mean          | (ref)                                                        | 1.81x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 93.8 ms: 1.18x faster                                                               |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                                |
| nbody          | 134 ms                                                       | 128 ms: 1.05x faster                                                                |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 240 ms: 1.09x faster                                                                |
| regex_v8       | 27.2 ms                                                      | 26.8 ms: 1.01x faster                                                               |
| regex_compile  | 190 ms                                                       | 208 ms: 1.10x slower                                                                |
| regex_effbot   | 3.09 ms                                                      | 3.57 ms: 1.16x slower                                                               |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| json_dumps           | 14.5 ms                                                      | 11.9 ms: 1.22x faster                                                               |
| json_loads           | 30.3 us                                                      | 25.6 us: 1.19x faster                                                               |
| unpickle_pure_python | 312 us                                                       | 272 us: 1.15x faster                                                                |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                                |
| pickle_pure_python   | 455 us                                                       | 410 us: 1.11x faster                                                                |
| xml_etree_process    | 75.9 ms                                                      | 70.0 ms: 1.08x faster                                                               |
| tomli_loads          | 2.92 sec                                                     | 2.87 sec: 1.02x faster                                                              |
| xml_etree_iterparse  | 110 ms                                                       | 116 ms: 1.05x slower                                                                |
| xml_etree_generate   | 92.3 ms                                                      | 101 ms: 1.09x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.08x faster                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                               |
| python_startup_no_site | 7.33 ms                                                      | 9.12 ms: 1.24x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 44.4 ms: 1.13x faster                                                               |
| genshi_text     | 31.4 ms                                                      | 30.8 ms: 1.02x faster                                                               |
| genshi_xml      | 63.3 ms                                                      | 65.7 ms: 1.04x slower                                                               |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                        |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 200 us: 2.68x faster                                                                |
| asyncio_tcp              | 779 ms                                                       | 388 ms: 2.01x faster                                                                |
| async_tree_none          | 692 ms                                                       | 348 ms: 1.99x faster                                                                |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.60 sec: 1.94x faster                                                              |
| async_tree_io            | 1.60 sec                                                     | 853 ms: 1.87x faster                                                                |
| async_tree_memoization   | 819 ms                                                       | 443 ms: 1.85x faster                                                                |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 604 ms: 1.55x faster                                                                |
| raytrace                 | 489 ms                                                       | 325 ms: 1.50x faster                                                                |
| deltablue                | 7.50 ms                                                      | 5.24 ms: 1.43x faster                                                               |
| pylint                   | 566 ms                                                       | 411 ms: 1.38x faster                                                                |
| chaos                    | 109 ms                                                       | 80.0 ms: 1.36x faster                                                               |
| coroutines               | 30.3 ms                                                      | 22.5 ms: 1.35x faster                                                               |
| logging_simple           | 8.88 us                                                      | 6.67 us: 1.33x faster                                                               |
| thrift                   | 1.18 ms                                                      | 886 us: 1.33x faster                                                                |
| logging_format           | 9.64 us                                                      | 7.27 us: 1.33x faster                                                               |
| scimark_lu               | 167 ms                                                       | 127 ms: 1.32x faster                                                                |
| deepcopy                 | 468 us                                                       | 355 us: 1.32x faster                                                                |
| go                       | 262 ms                                                       | 199 ms: 1.31x faster                                                                |
| sqlglot_parse            | 2.24 ms                                                      | 1.73 ms: 1.29x faster                                                               |
| bench_mp_pool            | 6.37 ms                                                      | 4.99 ms: 1.28x faster                                                               |
| pathlib                  | 21.4 ms                                                      | 16.8 ms: 1.27x faster                                                               |
| richards_super           | 90.6 ms                                                      | 71.2 ms: 1.27x faster                                                               |
| generators               | 57.3 ms                                                      | 45.3 ms: 1.27x faster                                                               |
| crypto_pyaes             | 119 ms                                                       | 95.2 ms: 1.25x faster                                                               |
| deepcopy_reduce          | 4.01 us                                                      | 3.23 us: 1.24x faster                                                               |
| tornado_http             | 157 ms                                                       | 127 ms: 1.24x faster                                                                |
| json_dumps               | 14.5 ms                                                      | 11.9 ms: 1.22x faster                                                               |
| sqlglot_transpile        | 2.68 ms                                                      | 2.21 ms: 1.21x faster                                                               |
| pyflate                  | 733 ms                                                       | 613 ms: 1.20x faster                                                                |
| json_loads               | 30.3 us                                                      | 25.6 us: 1.19x faster                                                               |
| float                    | 111 ms                                                       | 93.8 ms: 1.18x faster                                                               |
| richards                 | 75.1 ms                                                      | 63.6 ms: 1.18x faster                                                               |
| bench_thread_pool        | 1.14 ms                                                      | 982 us: 1.16x faster                                                                |
| unpickle_pure_python     | 312 us                                                       | 272 us: 1.15x faster                                                                |
| scimark_monte_carlo      | 107 ms                                                       | 93.7 ms: 1.15x faster                                                               |
| django_template          | 50.2 ms                                                      | 44.4 ms: 1.13x faster                                                               |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                                |
| html5lib                 | 94.6 ms                                                      | 85.2 ms: 1.11x faster                                                               |
| pickle_pure_python       | 455 us                                                       | 410 us: 1.11x faster                                                                |
| async_generators         | 421 ms                                                       | 385 ms: 1.09x faster                                                                |
| logging_silent           | 167 ns                                                       | 154 ns: 1.09x faster                                                                |
| regex_dna                | 261 ms                                                       | 240 ms: 1.09x faster                                                                |
| xml_etree_process        | 75.9 ms                                                      | 70.0 ms: 1.08x faster                                                               |
| pycparser                | 1.67 sec                                                     | 1.54 sec: 1.08x faster                                                              |
| mdp                      | 3.01 sec                                                     | 2.80 sec: 1.07x faster                                                              |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                                |
| nbody                    | 134 ms                                                       | 128 ms: 1.05x faster                                                                |
| deepcopy_memo            | 49.8 us                                                      | 47.5 us: 1.05x faster                                                               |
| pprint_pformat           | 2.15 sec                                                     | 2.11 sec: 1.02x faster                                                              |
| pprint_safe_repr         | 1.05 sec                                                     | 1.03 sec: 1.02x faster                                                              |
| genshi_text              | 31.4 ms                                                      | 30.8 ms: 1.02x faster                                                               |
| tomli_loads              | 2.92 sec                                                     | 2.87 sec: 1.02x faster                                                              |
| json                     | 5.86 ms                                                      | 5.78 ms: 1.01x faster                                                               |
| regex_v8                 | 27.2 ms                                                      | 26.8 ms: 1.01x faster                                                               |
| sqlglot_normalize        | 144 ms                                                       | 142 ms: 1.01x faster                                                                |
| sympy_sum                | 193 ms                                                       | 192 ms: 1.01x faster                                                                |
| 2to3                     | 350 ms                                                       | 353 ms: 1.01x slower                                                                |
| nqueens                  | 115 ms                                                       | 116 ms: 1.01x slower                                                                |
| sympy_integrate          | 28.2 ms                                                      | 28.5 ms: 1.01x slower                                                               |
| comprehensions           | 26.7 us                                                      | 27.2 us: 1.02x slower                                                               |
| asyncio_websockets       | 390 ms                                                       | 398 ms: 1.02x slower                                                                |
| fannkuch                 | 483 ms                                                       | 496 ms: 1.03x slower                                                                |
| sqlglot_optimize         | 70.1 ms                                                      | 72.5 ms: 1.03x slower                                                               |
| sympy_str                | 360 ms                                                       | 373 ms: 1.04x slower                                                                |
| docutils                 | 3.41 sec                                                     | 3.54 sec: 1.04x slower                                                              |
| genshi_xml               | 63.3 ms                                                      | 65.7 ms: 1.04x slower                                                               |
| sympy_expand             | 600 ms                                                       | 626 ms: 1.04x slower                                                                |
| xml_etree_iterparse      | 110 ms                                                       | 116 ms: 1.05x slower                                                                |
| meteor_contest           | 138 ms                                                       | 145 ms: 1.05x slower                                                                |
| xml_etree_generate       | 92.3 ms                                                      | 101 ms: 1.09x slower                                                                |
| regex_compile            | 190 ms                                                       | 208 ms: 1.10x slower                                                                |
| hexiom                   | 9.42 ms                                                      | 10.4 ms: 1.11x slower                                                               |
| spectral_norm            | 139 ms                                                       | 155 ms: 1.11x slower                                                                |
| create_gc_cycles         | 1.76 ms                                                      | 2.04 ms: 1.16x slower                                                               |
| regex_effbot             | 3.09 ms                                                      | 3.57 ms: 1.16x slower                                                               |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                               |
| scimark_fft              | 361 ms                                                       | 426 ms: 1.18x slower                                                                |
| telco                    | 7.23 ms                                                      | 8.95 ms: 1.24x slower                                                               |
| python_startup_no_site   | 7.33 ms                                                      | 9.12 ms: 1.24x slower                                                               |
| coverage                 | 63.3 ms                                                      | 80.0 ms: 1.26x slower                                                               |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 6.62 ms: 1.30x slower                                                               |
| gc_traversal             | 3.42 ms                                                      | 4.76 ms: 1.39x slower                                                               |
| Geometric mean           | (ref)                                                        | 1.13x faster                                                                        |

Benchmark hidden because not significant (2): mako, scimark_sor
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240814-3.14.0a0-6b9055c-PYTHON_UOPS/bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 99.87% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.15x