# Results vs. 3.10.4

- fork: python
- ref: c15f94d6fbc960790db3
- machine: linux-x86_64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.10x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 345 ms: 1.01x faster                                                         |
| chameleon      | 9.44 ms                                                      | 8.61 ms: 1.10x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.47 sec: 1.02x slower                                                       |
| html5lib       | 94.6 ms                                                      | 88.0 ms: 1.08x faster                                                        |
| tornado_http   | 157 ms                                                       | 129 ms: 1.21x faster                                                         |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 398 ms: 1.74x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 475 ms: 1.72x faster                                                         |
| async_tree_io           | 1.60 sec                                                     | 943 ms: 1.69x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 654 ms: 1.43x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.64x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 96.2 ms: 1.16x faster                                                        |
| nbody          | 134 ms                                                       | 125 ms: 1.07x faster                                                         |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 27.2 ms                                                      | 26.0 ms: 1.05x faster                                                        |
| regex_dna      | 261 ms                                                       | 255 ms: 1.03x faster                                                         |
| regex_compile  | 190 ms                                                       | 216 ms: 1.14x slower                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 14.5 ms                                                      | 11.3 ms: 1.29x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.4 us: 1.24x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.11x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 68.8 ms: 1.10x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 434 us: 1.05x faster                                                         |
| unpickle_pure_python | 312 us                                                       | 307 us: 1.02x faster                                                         |
| unpickle_list        | 4.65 us                                                      | 4.73 us: 1.02x slower                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 113 ms: 1.02x slower                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 97.0 ms: 1.05x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 31.3 us: 1.06x slower                                                        |
| pickle               | 9.89 us                                                      | 10.5 us: 1.06x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.56 us: 1.11x slower                                                        |
| unpickle             | 13.5 us                                                      | 15.0 us: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.2 ms: 1.15x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 8.91 ms: 1.22x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.18x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 45.5 ms: 1.10x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 33.0 ms: 1.05x slower                                                        |
| genshi_xml      | 63.3 ms                                                      | 67.7 ms: 1.07x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 197 us: 2.72x faster                                                         |
| asyncio_tcp              | 779 ms                                                       | 388 ms: 2.01x faster                                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.60 sec: 1.94x faster                                                       |
| async_tree_none          | 692 ms                                                       | 398 ms: 1.74x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 475 ms: 1.72x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 943 ms: 1.69x faster                                                         |
| generators               | 57.3 ms                                                      | 34.1 ms: 1.68x faster                                                        |
| deltablue                | 7.50 ms                                                      | 4.54 ms: 1.65x faster                                                        |
| raytrace                 | 489 ms                                                       | 338 ms: 1.45x faster                                                         |
| pylint                   | 566 ms                                                       | 394 ms: 1.44x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 654 ms: 1.43x faster                                                         |
| chaos                    | 109 ms                                                       | 80.7 ms: 1.34x faster                                                        |
| coroutines               | 30.3 ms                                                      | 22.8 ms: 1.33x faster                                                        |
| richards_super           | 90.6 ms                                                      | 68.3 ms: 1.33x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.39 us: 1.30x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.82 us: 1.30x faster                                                        |
| thrift                   | 1.18 ms                                                      | 906 us: 1.30x faster                                                         |
| go                       | 262 ms                                                       | 202 ms: 1.30x faster                                                         |
| crypto_pyaes             | 119 ms                                                       | 92.4 ms: 1.29x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.3 ms: 1.29x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.74 ms: 1.28x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.97 ms: 1.28x faster                                                        |
| json_loads               | 30.3 us                                                      | 24.4 us: 1.24x faster                                                        |
| richards                 | 75.1 ms                                                      | 61.2 ms: 1.23x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 2.20 ms: 1.22x faster                                                        |
| tornado_http             | 157 ms                                                       | 129 ms: 1.21x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 18.3 ms: 1.17x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.45 sec: 1.16x faster                                                       |
| float                    | 111 ms                                                       | 96.2 ms: 1.16x faster                                                        |
| scimark_lu               | 167 ms                                                       | 145 ms: 1.15x faster                                                         |
| pyflate                  | 733 ms                                                       | 637 ms: 1.15x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 1.02 ms: 1.11x faster                                                        |
| scimark_sor              | 180 ms                                                       | 163 ms: 1.11x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.11x faster                                                         |
| dask                     | 472 ms                                                       | 427 ms: 1.11x faster                                                         |
| django_template          | 50.2 ms                                                      | 45.5 ms: 1.10x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 68.8 ms: 1.10x faster                                                        |
| chameleon                | 9.44 ms                                                      | 8.61 ms: 1.10x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.77 sec: 1.09x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 99.7 ms: 1.08x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 88.0 ms: 1.08x faster                                                        |
| nbody                    | 134 ms                                                       | 125 ms: 1.07x faster                                                         |
| json                     | 5.86 ms                                                      | 5.48 ms: 1.07x faster                                                        |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| async_generators         | 421 ms                                                       | 395 ms: 1.07x faster                                                         |
| logging_silent           | 167 ns                                                       | 157 ns: 1.07x faster                                                         |
| pickle_pure_python       | 455 us                                                       | 434 us: 1.05x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 26.0 ms: 1.05x faster                                                        |
| mypy2                    | 933 ms                                                       | 897 ms: 1.04x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 78.3 ms: 1.04x faster                                                        |
| regex_dna                | 261 ms                                                       | 255 ms: 1.03x faster                                                         |
| sympy_sum                | 193 ms                                                       | 189 ms: 1.02x faster                                                         |
| sqlglot_normalize        | 144 ms                                                       | 141 ms: 1.02x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 2.11 sec: 1.02x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 307 us: 1.02x faster                                                         |
| 2to3                     | 350 ms                                                       | 345 ms: 1.01x faster                                                         |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 1.04 sec: 1.01x faster                                                       |
| fannkuch                 | 483 ms                                                       | 479 ms: 1.01x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 28.1 ms: 1.00x faster                                                        |
| aiohttp                  | 1.19 ms                                                      | 1.19 ms: 1.01x slower                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 70.7 ms: 1.01x slower                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 4.07 us: 1.01x slower                                                        |
| deepcopy                 | 468 us                                                       | 475 us: 1.02x slower                                                         |
| nqueens                  | 115 ms                                                       | 117 ms: 1.02x slower                                                         |
| docutils                 | 3.41 sec                                                     | 3.47 sec: 1.02x slower                                                       |
| unpickle_list            | 4.65 us                                                      | 4.73 us: 1.02x slower                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 113 ms: 1.02x slower                                                         |
| sympy_str                | 360 ms                                                       | 371 ms: 1.03x slower                                                         |
| meteor_contest           | 138 ms                                                       | 143 ms: 1.03x slower                                                         |
| comprehensions           | 26.7 us                                                      | 27.6 us: 1.04x slower                                                        |
| sympy_expand             | 600 ms                                                       | 628 ms: 1.05x slower                                                         |
| genshi_text              | 31.4 ms                                                      | 33.0 ms: 1.05x slower                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 97.0 ms: 1.05x slower                                                        |
| spectral_norm            | 139 ms                                                       | 147 ms: 1.06x slower                                                         |
| pickle_dict              | 29.5 us                                                      | 31.3 us: 1.06x slower                                                        |
| pickle                   | 9.89 us                                                      | 10.5 us: 1.06x slower                                                        |
| genshi_xml               | 63.3 ms                                                      | 67.7 ms: 1.07x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.56 us: 1.11x slower                                                        |
| unpickle                 | 13.5 us                                                      | 15.0 us: 1.11x slower                                                        |
| hexiom                   | 9.42 ms                                                      | 10.6 ms: 1.13x slower                                                        |
| flaskblogging            | 4.39 ms                                                      | 4.96 ms: 1.13x slower                                                        |
| regex_compile            | 190 ms                                                       | 216 ms: 1.14x slower                                                         |
| python_startup           | 11.5 ms                                                      | 13.2 ms: 1.15x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                        |
| deepcopy_memo            | 49.8 us                                                      | 57.7 us: 1.16x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.06 ms: 1.17x slower                                                        |
| scimark_fft              | 361 ms                                                       | 433 ms: 1.20x slower                                                         |
| python_startup_no_site   | 7.33 ms                                                      | 8.91 ms: 1.22x slower                                                        |
| telco                    | 7.23 ms                                                      | 9.41 ms: 1.30x slower                                                        |
| coverage                 | 63.3 ms                                                      | 83.4 ms: 1.32x slower                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 6.80 ms: 1.34x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 4.72 ms: 1.38x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.10x faster                                                                 |

Benchmark hidden because not significant (4): sqlite_synth, mako, tomli_loads, gunicorn
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240608-3.13.0b2+-c15f94d-PYTHON_UOPS/bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.14x