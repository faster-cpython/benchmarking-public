# Results vs. 3.10.4

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-x86_64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.321x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 310 ms: 1.13x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.16 sec: 1.08x faster                                                      |
| html5lib       | 94.6 ms                                                      | 70.3 ms: 1.35x faster                                                       |
| tornado_http   | 157 ms                                                       | 121 ms: 1.30x faster                                                        |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 320 ms: 2.16x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 401 ms: 2.04x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 801 ms: 1.99x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 574 ms: 1.63x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.95x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 81.1 ms: 1.65x faster                                                       |
| float          | 111 ms                                                       | 73.7 ms: 1.51x faster                                                       |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.39x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 147 ms: 1.30x faster                                                        |
| regex_dna      | 261 ms                                                       | 235 ms: 1.11x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.46 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 213 us: 1.46x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 328 us: 1.39x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.12 sec: 1.38x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 55.8 ms: 1.36x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 10.9 ms: 1.34x faster                                                       |
| json_loads           | 30.3 us                                                      | 24.7 us: 1.23x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 78.7 ms: 1.17x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 98.3 ms: 1.12x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| unpickle_list        | 4.65 us                                                      | 4.75 us: 1.02x slower                                                       |
| pickle               | 9.89 us                                                      | 10.8 us: 1.09x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.51 us: 1.09x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 32.4 us: 1.10x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.4 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 8.97 ms: 1.22x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.10 ms: 1.62x faster                                                       |
| django_template | 50.2 ms                                                      | 43.1 ms: 1.16x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 28.3 ms: 1.11x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 62.3 ms: 1.02x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.21x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 179 us: 2.99x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.19 ms: 2.35x faster                                                       |
| async_tree_none          | 692 ms                                                       | 320 ms: 2.16x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 376 ms: 2.07x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 401 ms: 2.04x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 801 ms: 1.99x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.60 sec: 1.94x faster                                                      |
| deepcopy_memo            | 49.8 us                                                      | 26.9 us: 1.85x faster                                                       |
| go                       | 262 ms                                                       | 151 ms: 1.73x faster                                                        |
| scimark_sor              | 180 ms                                                       | 104 ms: 1.73x faster                                                        |
| scimark_lu               | 167 ms                                                       | 96.5 ms: 1.73x faster                                                       |
| richards_super           | 90.6 ms                                                      | 52.9 ms: 1.71x faster                                                       |
| spectral_norm            | 139 ms                                                       | 82.3 ms: 1.69x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 70.6 ms: 1.69x faster                                                       |
| richards                 | 75.1 ms                                                      | 44.9 ms: 1.67x faster                                                       |
| nbody                    | 134 ms                                                       | 81.1 ms: 1.65x faster                                                       |
| logging_silent           | 167 ns                                                       | 102 ns: 1.65x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 574 ms: 1.63x faster                                                        |
| chaos                    | 109 ms                                                       | 66.6 ms: 1.63x faster                                                       |
| deepcopy                 | 468 us                                                       | 289 us: 1.62x faster                                                        |
| mako                     | 14.7 ms                                                      | 9.10 ms: 1.62x faster                                                       |
| pyflate                  | 733 ms                                                       | 465 ms: 1.58x faster                                                        |
| generators               | 57.3 ms                                                      | 36.9 ms: 1.55x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 69.2 ms: 1.55x faster                                                       |
| raytrace                 | 489 ms                                                       | 316 ms: 1.55x faster                                                        |
| float                    | 111 ms                                                       | 73.7 ms: 1.51x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.48 ms: 1.51x faster                                                       |
| comprehensions           | 26.7 us                                                      | 18.1 us: 1.48x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 213 us: 1.46x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.4 ms: 1.41x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.88 us: 1.39x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 328 us: 1.39x faster                                                        |
| pylint                   | 566 ms                                                       | 409 ms: 1.38x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.94 ms: 1.38x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.12 sec: 1.38x faster                                                      |
| xml_etree_process        | 75.9 ms                                                      | 55.8 ms: 1.36x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 15.7 ms: 1.36x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.54 us: 1.36x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.95 ms: 1.35x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.13 us: 1.35x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 70.3 ms: 1.35x faster                                                       |
| fannkuch                 | 483 ms                                                       | 361 ms: 1.34x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.9 ms: 1.34x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 789 ms: 1.33x faster                                                        |
| thrift                   | 1.18 ms                                                      | 896 us: 1.31x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.28 sec: 1.31x faster                                                      |
| regex_compile            | 190 ms                                                       | 147 ms: 1.30x faster                                                        |
| tornado_http             | 157 ms                                                       | 121 ms: 1.30x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 3.96 ms: 1.28x faster                                                       |
| scimark_fft              | 361 ms                                                       | 283 ms: 1.28x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 64.6 ms: 1.26x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 5.17 ms: 1.23x faster                                                       |
| json_loads               | 30.3 us                                                      | 24.7 us: 1.23x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 939 us: 1.22x faster                                                        |
| nqueens                  | 115 ms                                                       | 97.2 ms: 1.18x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 78.7 ms: 1.17x faster                                                       |
| sympy_str                | 360 ms                                                       | 309 ms: 1.17x faster                                                        |
| django_template          | 50.2 ms                                                      | 43.1 ms: 1.16x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.59 sec: 1.16x faster                                                      |
| sympy_sum                | 193 ms                                                       | 168 ms: 1.15x faster                                                        |
| sympy_expand             | 600 ms                                                       | 524 ms: 1.14x faster                                                        |
| 2to3                     | 350 ms                                                       | 310 ms: 1.13x faster                                                        |
| json                     | 5.86 ms                                                      | 5.20 ms: 1.13x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 98.3 ms: 1.12x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 129 ms: 1.12x faster                                                        |
| regex_dna                | 261 ms                                                       | 235 ms: 1.11x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 28.3 ms: 1.11x faster                                                       |
| async_generators         | 421 ms                                                       | 380 ms: 1.11x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.72 us: 1.10x faster                                                       |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.16 sec: 1.08x faster                                                      |
| regex_v8                 | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 26.3 ms: 1.07x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 65.6 ms: 1.07x faster                                                       |
| meteor_contest           | 138 ms                                                       | 131 ms: 1.06x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 62.3 ms: 1.02x faster                                                       |
| unpickle_list            | 4.65 us                                                      | 4.75 us: 1.02x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.91 ms: 1.08x slower                                                       |
| pickle                   | 9.89 us                                                      | 10.8 us: 1.09x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.51 us: 1.09x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 32.4 us: 1.10x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.05 ms: 1.11x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.46 ms: 1.12x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.4 us: 1.14x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.97 ms: 1.22x slower                                                       |
| coverage                 | 63.3 ms                                                      | 81.1 ms: 1.28x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.40 ms: 1.29x slower                                                       |
| unpack_sequence          | 59.9 ns                                                      | 91.8 ns: 1.53x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.30x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.321x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.22x