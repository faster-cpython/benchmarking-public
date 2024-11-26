# Results vs. 3.10.4

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-x86_64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.087x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.07x slower
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 423 ms: 1.21x slower                                                        |
| docutils       | 3.41 sec                                                     | 3.38 sec: 1.01x faster                                                      |
| html5lib       | 94.6 ms                                                      | 107 ms: 1.13x slower                                                        |
| tornado_http   | 157 ms                                                       | 169 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 940 ms: 1.70x faster                                                        |
| async_tree_none         | 692 ms                                                       | 416 ms: 1.66x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 515 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 675 ms: 1.39x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.58x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| float          | 111 ms                                                       | 140 ms: 1.26x slower                                                        |
| nbody          | 134 ms                                                       | 194 ms: 1.45x slower                                                        |
| Geometric mean | (ref)                                                        | 1.19x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 236 ms: 1.11x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 27.0 ms: 1.01x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.40 ms: 1.10x slower                                                       |
| regex_compile  | 190 ms                                                       | 223 ms: 1.18x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 160 ms                                                       | 140 ms: 1.14x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 105 ms: 1.05x faster                                                        |
| json_loads           | 30.3 us                                                      | 29.0 us: 1.05x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 14.0 ms: 1.04x faster                                                       |
| pickle               | 9.89 us                                                      | 10.4 us: 1.05x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 32.2 us: 1.09x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.50 us: 1.09x slower                                                       |
| tomli_loads          | 2.92 sec                                                     | 3.31 sec: 1.13x slower                                                      |
| unpickle_list        | 4.65 us                                                      | 5.29 us: 1.14x slower                                                       |
| xml_etree_process    | 75.9 ms                                                      | 91.9 ms: 1.21x slower                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 113 ms: 1.22x slower                                                        |
| unpickle             | 13.5 us                                                      | 16.8 us: 1.25x slower                                                       |
| unpickle_pure_python | 312 us                                                       | 396 us: 1.27x slower                                                        |
| pickle_pure_python   | 455 us                                                       | 585 us: 1.29x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.10x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 17.5 ms: 1.52x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.56x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 63.3 ms                                                      | 80.5 ms: 1.27x slower                                                       |
| django_template | 50.2 ms                                                      | 66.9 ms: 1.33x slower                                                       |
| genshi_text     | 31.4 ms                                                      | 42.6 ms: 1.36x slower                                                       |
| mako            | 14.7 ms                                                      | 21.5 ms: 1.46x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.35x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 261 us: 2.05x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 457 ms: 1.70x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 940 ms: 1.70x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.86 sec: 1.67x faster                                                      |
| async_tree_none          | 692 ms                                                       | 416 ms: 1.66x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 515 ms: 1.59x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 675 ms: 1.39x faster                                                        |
| generators               | 57.3 ms                                                      | 41.4 ms: 1.39x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.83 ms: 1.32x faster                                                       |
| pylint                   | 566 ms                                                       | 436 ms: 1.30x faster                                                        |
| gc_traversal             | 3.42 ms                                                      | 2.81 ms: 1.22x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 140 ms: 1.14x faster                                                        |
| regex_dna                | 261 ms                                                       | 236 ms: 1.11x faster                                                        |
| deepcopy                 | 468 us                                                       | 424 us: 1.10x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 19.6 ms: 1.09x faster                                                       |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| coroutines               | 30.3 ms                                                      | 28.0 ms: 1.08x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 105 ms: 1.05x faster                                                        |
| json_loads               | 30.3 us                                                      | 29.0 us: 1.05x faster                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.70 ms: 1.04x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 14.0 ms: 1.04x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 48.4 us: 1.03x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.38 sec: 1.01x faster                                                      |
| regex_v8                 | 27.2 ms                                                      | 27.0 ms: 1.01x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 120 ms: 1.01x slower                                                        |
| json                     | 5.86 ms                                                      | 5.93 ms: 1.01x slower                                                       |
| pycparser                | 1.67 sec                                                     | 1.74 sec: 1.04x slower                                                      |
| pyflate                  | 733 ms                                                       | 767 ms: 1.05x slower                                                        |
| pickle                   | 9.89 us                                                      | 10.4 us: 1.05x slower                                                       |
| scimark_fft              | 361 ms                                                       | 388 ms: 1.07x slower                                                        |
| richards_super           | 90.6 ms                                                      | 97.4 ms: 1.07x slower                                                       |
| tornado_http             | 157 ms                                                       | 169 ms: 1.08x slower                                                        |
| richards                 | 75.1 ms                                                      | 81.4 ms: 1.08x slower                                                       |
| mdp                      | 3.01 sec                                                     | 3.26 sec: 1.08x slower                                                      |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.52 ms: 1.09x slower                                                       |
| deltablue                | 7.50 ms                                                      | 8.17 ms: 1.09x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 32.2 us: 1.09x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.50 us: 1.09x slower                                                       |
| comprehensions           | 26.7 us                                                      | 29.3 us: 1.10x slower                                                       |
| dulwich_log              | 81.1 ms                                                      | 89.2 ms: 1.10x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.40 ms: 1.10x slower                                                       |
| nqueens                  | 115 ms                                                       | 128 ms: 1.11x slower                                                        |
| logging_silent           | 167 ns                                                       | 187 ns: 1.12x slower                                                        |
| chaos                    | 109 ms                                                       | 122 ms: 1.13x slower                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 4.53 us: 1.13x slower                                                       |
| html5lib                 | 94.6 ms                                                      | 107 ms: 1.13x slower                                                        |
| tomli_loads              | 2.92 sec                                                     | 3.31 sec: 1.13x slower                                                      |
| unpickle_list            | 4.65 us                                                      | 5.29 us: 1.14x slower                                                       |
| sympy_integrate          | 28.2 ms                                                      | 32.1 ms: 1.14x slower                                                       |
| go                       | 262 ms                                                       | 301 ms: 1.15x slower                                                        |
| thrift                   | 1.18 ms                                                      | 1.36 ms: 1.15x slower                                                       |
| async_generators         | 421 ms                                                       | 488 ms: 1.16x slower                                                        |
| regex_compile            | 190 ms                                                       | 223 ms: 1.18x slower                                                        |
| spectral_norm            | 139 ms                                                       | 164 ms: 1.18x slower                                                        |
| meteor_contest           | 138 ms                                                       | 166 ms: 1.20x slower                                                        |
| 2to3                     | 350 ms                                                       | 423 ms: 1.21x slower                                                        |
| xml_etree_process        | 75.9 ms                                                      | 91.9 ms: 1.21x slower                                                       |
| hexiom                   | 9.42 ms                                                      | 11.5 ms: 1.22x slower                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 131 ms: 1.22x slower                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 113 ms: 1.22x slower                                                        |
| raytrace                 | 489 ms                                                       | 605 ms: 1.24x slower                                                        |
| sympy_str                | 360 ms                                                       | 447 ms: 1.24x slower                                                        |
| unpickle                 | 13.5 us                                                      | 16.8 us: 1.25x slower                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 3.35 ms: 1.25x slower                                                       |
| sqlglot_normalize        | 144 ms                                                       | 180 ms: 1.25x slower                                                        |
| float                    | 111 ms                                                       | 140 ms: 1.26x slower                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 2.83 ms: 1.26x slower                                                       |
| unpickle_pure_python     | 312 us                                                       | 396 us: 1.27x slower                                                        |
| genshi_xml               | 63.3 ms                                                      | 80.5 ms: 1.27x slower                                                       |
| fannkuch                 | 483 ms                                                       | 619 ms: 1.28x slower                                                        |
| logging_format           | 9.64 us                                                      | 12.4 us: 1.28x slower                                                       |
| pickle_pure_python       | 455 us                                                       | 585 us: 1.29x slower                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 1.35 sec: 1.29x slower                                                      |
| sqlglot_optimize         | 70.1 ms                                                      | 90.5 ms: 1.29x slower                                                       |
| logging_simple           | 8.88 us                                                      | 11.5 us: 1.30x slower                                                       |
| scimark_lu               | 167 ms                                                       | 217 ms: 1.30x slower                                                        |
| pprint_pformat           | 2.15 sec                                                     | 2.81 sec: 1.30x slower                                                      |
| django_template          | 50.2 ms                                                      | 66.9 ms: 1.33x slower                                                       |
| sympy_sum                | 193 ms                                                       | 259 ms: 1.34x slower                                                        |
| sympy_expand             | 600 ms                                                       | 807 ms: 1.34x slower                                                        |
| genshi_text              | 31.4 ms                                                      | 42.6 ms: 1.36x slower                                                       |
| scimark_sor              | 180 ms                                                       | 258 ms: 1.43x slower                                                        |
| telco                    | 7.23 ms                                                      | 10.4 ms: 1.44x slower                                                       |
| nbody                    | 134 ms                                                       | 194 ms: 1.45x slower                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.66 ms: 1.45x slower                                                       |
| mako                     | 14.7 ms                                                      | 21.5 ms: 1.46x slower                                                       |
| python_startup           | 11.5 ms                                                      | 17.5 ms: 1.52x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                       |
| coverage                 | 63.3 ms                                                      | 109 ms: 1.72x slower                                                        |
| unpack_sequence          | 59.9 ns                                                      | 130 ns: 2.17x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.09x slower                                                                |

Benchmark hidden because not significant (1): sqlite_synth
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240920-3.14.0a0-342e654-NOGIL/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.087x slower
# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 1.30x