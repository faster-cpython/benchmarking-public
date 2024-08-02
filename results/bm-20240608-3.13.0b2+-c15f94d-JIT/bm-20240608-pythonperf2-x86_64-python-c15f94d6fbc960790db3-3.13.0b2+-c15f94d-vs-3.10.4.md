# Results vs. 3.10.4

- fork: python
- ref: c15f94d6fbc960790db3
- machine: linux-x86_64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.26x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 306 ms: 1.15x faster                                                         |
| chameleon      | 9.44 ms                                                      | 7.67 ms: 1.23x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.13 sec: 1.09x faster                                                       |
| html5lib       | 94.6 ms                                                      | 73.9 ms: 1.28x faster                                                        |
| tornado_http   | 157 ms                                                       | 122 ms: 1.28x faster                                                         |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 376 ms: 1.84x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 447 ms: 1.83x faster                                                         |
| async_tree_io           | 1.60 sec                                                     | 883 ms: 1.81x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 627 ms: 1.49x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.74x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 84.0 ms: 1.60x faster                                                        |
| float          | 111 ms                                                       | 73.3 ms: 1.52x faster                                                        |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.38x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 140 ms: 1.36x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                        |
| regex_dna      | 261 ms                                                       | 251 ms: 1.04x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.62 ms: 1.17x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 316 us: 1.44x faster                                                         |
| unpickle_pure_python | 312 us                                                       | 221 us: 1.41x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.09 sec: 1.40x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 58.4 ms: 1.30x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.7 us: 1.23x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 82.9 ms: 1.11x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 100 ms: 1.10x faster                                                         |
| unpickle_list        | 4.65 us                                                      | 4.70 us: 1.01x slower                                                        |
| pickle               | 9.89 us                                                      | 10.9 us: 1.10x slower                                                        |
| unpickle             | 13.5 us                                                      | 14.8 us: 1.10x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.54 us: 1.10x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 34.0 us: 1.15x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.8 ms: 1.20x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 9.44 ms: 1.29x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.24x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.15 ms: 1.61x faster                                                        |
| django_template | 50.2 ms                                                      | 41.9 ms: 1.20x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 28.0 ms: 1.12x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 62.4 ms: 1.01x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.22x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 182 us: 2.94x faster                                                         |
| asyncio_tcp              | 779 ms                                                       | 380 ms: 2.05x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.74 ms: 2.00x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                       |
| async_tree_none          | 692 ms                                                       | 376 ms: 1.84x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 447 ms: 1.83x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 883 ms: 1.81x faster                                                         |
| richards_super           | 90.6 ms                                                      | 52.4 ms: 1.73x faster                                                        |
| spectral_norm            | 139 ms                                                       | 81.6 ms: 1.70x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 71.1 ms: 1.68x faster                                                        |
| generators               | 57.3 ms                                                      | 34.3 ms: 1.67x faster                                                        |
| richards                 | 75.1 ms                                                      | 45.4 ms: 1.65x faster                                                        |
| chaos                    | 109 ms                                                       | 65.6 ms: 1.65x faster                                                        |
| raytrace                 | 489 ms                                                       | 298 ms: 1.64x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 66.3 ms: 1.62x faster                                                        |
| mako                     | 14.7 ms                                                      | 9.15 ms: 1.61x faster                                                        |
| nbody                    | 134 ms                                                       | 84.0 ms: 1.60x faster                                                        |
| go                       | 262 ms                                                       | 164 ms: 1.60x faster                                                         |
| pyflate                  | 733 ms                                                       | 463 ms: 1.58x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.58x faster                                                        |
| float                    | 111 ms                                                       | 73.3 ms: 1.52x faster                                                        |
| pylint                   | 566 ms                                                       | 376 ms: 1.51x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 627 ms: 1.49x faster                                                         |
| comprehensions           | 26.7 us                                                      | 18.1 us: 1.48x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.82 ms: 1.47x faster                                                        |
| scimark_lu               | 167 ms                                                       | 114 ms: 1.47x faster                                                         |
| pickle_pure_python       | 455 us                                                       | 316 us: 1.44x faster                                                         |
| hexiom                   | 9.42 ms                                                      | 6.65 ms: 1.42x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 221 us: 1.41x faster                                                         |
| fannkuch                 | 483 ms                                                       | 343 ms: 1.41x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.09 sec: 1.40x faster                                                       |
| logging_silent           | 167 ns                                                       | 120 ns: 1.39x faster                                                         |
| coroutines               | 30.3 ms                                                      | 21.8 ms: 1.39x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.41 us: 1.38x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.02 us: 1.37x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                        |
| regex_compile            | 190 ms                                                       | 140 ms: 1.36x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 36.9 us: 1.35x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.77 ms: 1.34x faster                                                        |
| scimark_sor              | 180 ms                                                       | 138 ms: 1.31x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.31x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 58.4 ms: 1.30x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 814 ms: 1.29x faster                                                         |
| thrift                   | 1.18 ms                                                      | 915 us: 1.29x faster                                                         |
| tornado_http             | 157 ms                                                       | 122 ms: 1.28x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 73.9 ms: 1.28x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.02 ms: 1.26x faster                                                        |
| chameleon                | 9.44 ms                                                      | 7.67 ms: 1.23x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 65.9 ms: 1.23x faster                                                        |
| json_loads               | 30.3 us                                                      | 24.7 us: 1.23x faster                                                        |
| scimark_fft              | 361 ms                                                       | 295 ms: 1.23x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 17.6 ms: 1.21x faster                                                        |
| django_template          | 50.2 ms                                                      | 41.9 ms: 1.20x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 954 us: 1.20x faster                                                         |
| nqueens                  | 115 ms                                                       | 96.9 ms: 1.19x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.56 sec: 1.17x faster                                                       |
| dask                     | 472 ms                                                       | 403 ms: 1.17x faster                                                         |
| sympy_sum                | 193 ms                                                       | 167 ms: 1.16x faster                                                         |
| sympy_str                | 360 ms                                                       | 312 ms: 1.16x faster                                                         |
| 2to3                     | 350 ms                                                       | 306 ms: 1.15x faster                                                         |
| sympy_expand             | 600 ms                                                       | 529 ms: 1.14x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 28.0 ms: 1.12x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 128 ms: 1.12x faster                                                         |
| deepcopy                 | 468 us                                                       | 418 us: 1.12x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                         |
| async_generators         | 421 ms                                                       | 378 ms: 1.11x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 63.0 ms: 1.11x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 82.9 ms: 1.11x faster                                                        |
| json                     | 5.86 ms                                                      | 5.33 ms: 1.10x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 100 ms: 1.10x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 25.7 ms: 1.10x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.13 sec: 1.09x faster                                                       |
| mypy2                    | 933 ms                                                       | 855 ms: 1.09x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 3.68 us: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.79 us: 1.07x faster                                                        |
| meteor_contest           | 138 ms                                                       | 131 ms: 1.06x faster                                                         |
| regex_dna                | 261 ms                                                       | 251 ms: 1.04x faster                                                         |
| aiohttp                  | 1.19 ms                                                      | 1.17 ms: 1.02x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 62.4 ms: 1.01x faster                                                        |
| unpickle_list            | 4.65 us                                                      | 4.70 us: 1.01x slower                                                        |
| pickle                   | 9.89 us                                                      | 10.9 us: 1.10x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 1.94 ms: 1.10x slower                                                        |
| unpickle                 | 13.5 us                                                      | 14.8 us: 1.10x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.54 us: 1.10x slower                                                        |
| flaskblogging            | 4.39 ms                                                      | 4.90 ms: 1.12x slower                                                        |
| telco                    | 7.23 ms                                                      | 8.19 ms: 1.13x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 34.0 us: 1.15x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.62 ms: 1.17x slower                                                        |
| python_startup           | 11.5 ms                                                      | 13.8 ms: 1.20x slower                                                        |
| coverage                 | 63.3 ms                                                      | 80.5 ms: 1.27x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.44 ms: 1.29x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 4.44 ms: 1.30x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, gunicorn
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.23x