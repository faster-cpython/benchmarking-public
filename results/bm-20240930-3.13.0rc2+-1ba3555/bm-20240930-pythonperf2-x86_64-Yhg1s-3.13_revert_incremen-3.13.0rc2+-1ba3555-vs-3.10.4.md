# Results vs. 3.10.4

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: linux-x86_64
- commit hash: 1ba3555
- commit date: 2024-09-30
- overall geometric mean: 1.291x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 289 ms: 1.21x faster                                                         |
| chameleon      | 9.44 ms                                                      | 7.42 ms: 1.27x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.81 sec: 1.21x faster                                                       |
| html5lib       | 94.6 ms                                                      | 72.7 ms: 1.30x faster                                                        |
| tornado_http   | 157 ms                                                       | 119 ms: 1.31x faster                                                         |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 847 ms: 1.89x faster                                                         |
| async_tree_none         | 692 ms                                                       | 378 ms: 1.83x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 457 ms: 1.79x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 606 ms: 1.55x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.76x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 87.0 ms: 1.54x faster                                                        |
| float          | 111 ms                                                       | 81.9 ms: 1.36x faster                                                        |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 142 ms: 1.33x faster                                                         |
| regex_dna      | 261 ms                                                       | 242 ms: 1.08x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 214 us: 1.46x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 318 us: 1.43x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 11.0 ms: 1.33x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.28 sec: 1.28x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 59.6 ms: 1.27x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.4 us: 1.25x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 100.0 ms: 1.11x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 146 ms: 1.10x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 85.3 ms: 1.08x faster                                                        |
| unpickle_list        | 4.65 us                                                      | 4.73 us: 1.02x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 31.0 us: 1.05x slower                                                        |
| pickle               | 9.89 us                                                      | 10.6 us: 1.07x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.46 us: 1.08x slower                                                        |
| unpickle             | 13.5 us                                                      | 15.2 us: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 8.95 ms: 1.22x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                        |
| django_template | 50.2 ms                                                      | 38.9 ms: 1.29x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 25.4 ms: 1.24x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 55.2 ms: 1.15x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 171 us: 3.14x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.35 ms: 2.24x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 380 ms: 2.05x faster                                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 847 ms: 1.89x faster                                                         |
| async_tree_none          | 692 ms                                                       | 378 ms: 1.83x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 457 ms: 1.79x faster                                                         |
| chaos                    | 109 ms                                                       | 62.2 ms: 1.75x faster                                                        |
| raytrace                 | 489 ms                                                       | 280 ms: 1.74x faster                                                         |
| generators               | 57.3 ms                                                      | 33.1 ms: 1.73x faster                                                        |
| scimark_lu               | 167 ms                                                       | 97.7 ms: 1.71x faster                                                        |
| logging_silent           | 167 ns                                                       | 98.5 ns: 1.70x faster                                                        |
| pylint                   | 566 ms                                                       | 347 ms: 1.63x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 66.8 ms: 1.61x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.39 ms: 1.61x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 75.3 ms: 1.58x faster                                                        |
| go                       | 262 ms                                                       | 166 ms: 1.58x faster                                                         |
| comprehensions           | 26.7 us                                                      | 17.2 us: 1.56x faster                                                        |
| richards_super           | 90.6 ms                                                      | 58.4 ms: 1.55x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 606 ms: 1.55x faster                                                         |
| nbody                    | 134 ms                                                       | 87.0 ms: 1.54x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.77 ms: 1.51x faster                                                        |
| pyflate                  | 733 ms                                                       | 494 ms: 1.48x faster                                                         |
| hexiom                   | 9.42 ms                                                      | 6.37 ms: 1.48x faster                                                        |
| coroutines               | 30.3 ms                                                      | 20.8 ms: 1.46x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 214 us: 1.46x faster                                                         |
| richards                 | 75.1 ms                                                      | 51.9 ms: 1.45x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 318 us: 1.43x faster                                                         |
| spectral_norm            | 139 ms                                                       | 98.3 ms: 1.42x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.5 ms: 1.40x faster                                                        |
| scimark_sor              | 180 ms                                                       | 131 ms: 1.37x faster                                                         |
| logging_simple           | 8.88 us                                                      | 6.52 us: 1.36x faster                                                        |
| float                    | 111 ms                                                       | 81.9 ms: 1.36x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.72 ms: 1.35x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.18 us: 1.34x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                       |
| regex_compile            | 190 ms                                                       | 142 ms: 1.33x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 11.0 ms: 1.33x faster                                                        |
| tornado_http             | 157 ms                                                       | 119 ms: 1.31x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 72.7 ms: 1.30x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.29x faster                                                       |
| django_template          | 50.2 ms                                                      | 38.9 ms: 1.29x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 38.6 us: 1.29x faster                                                        |
| thrift                   | 1.18 ms                                                      | 914 us: 1.29x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.28 sec: 1.28x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 820 ms: 1.28x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 59.6 ms: 1.27x faster                                                        |
| chameleon                | 9.44 ms                                                      | 7.42 ms: 1.27x faster                                                        |
| nqueens                  | 115 ms                                                       | 90.6 ms: 1.27x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 903 us: 1.26x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 65.0 ms: 1.25x faster                                                        |
| sympy_sum                | 193 ms                                                       | 155 ms: 1.25x faster                                                         |
| json_loads               | 30.3 us                                                      | 24.4 us: 1.25x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 25.4 ms: 1.24x faster                                                        |
| fannkuch                 | 483 ms                                                       | 390 ms: 1.24x faster                                                         |
| dask                     | 472 ms                                                       | 382 ms: 1.23x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.81 sec: 1.21x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.19 ms: 1.21x faster                                                        |
| 2to3                     | 350 ms                                                       | 289 ms: 1.21x faster                                                         |
| sympy_str                | 360 ms                                                       | 298 ms: 1.21x faster                                                         |
| deepcopy                 | 468 us                                                       | 388 us: 1.21x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 23.4 ms: 1.21x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 49.8 ns: 1.20x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 17.8 ms: 1.20x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 121 ms: 1.19x faster                                                         |
| sympy_expand             | 600 ms                                                       | 507 ms: 1.18x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.55 sec: 1.18x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 60.3 ms: 1.16x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.45 us: 1.16x faster                                                        |
| scimark_fft              | 361 ms                                                       | 314 ms: 1.15x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 55.2 ms: 1.15x faster                                                        |
| async_generators         | 421 ms                                                       | 368 ms: 1.14x faster                                                         |
| json                     | 5.86 ms                                                      | 5.25 ms: 1.12x faster                                                        |
| gunicorn                 | 1.16 ms                                                      | 1.04 ms: 1.12x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 100.0 ms: 1.11x faster                                                       |
| aiohttp                  | 1.19 ms                                                      | 1.08 ms: 1.10x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 146 ms: 1.10x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 85.3 ms: 1.08x faster                                                        |
| regex_dna                | 261 ms                                                       | 242 ms: 1.08x faster                                                         |
| meteor_contest           | 138 ms                                                       | 129 ms: 1.07x faster                                                         |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.80 us: 1.07x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                        |
| unpickle_list            | 4.65 us                                                      | 4.73 us: 1.02x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 1.83 ms: 1.04x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 31.0 us: 1.05x slower                                                        |
| flaskblogging            | 4.39 ms                                                      | 4.62 ms: 1.05x slower                                                        |
| pickle                   | 9.89 us                                                      | 10.6 us: 1.07x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.46 us: 1.08x slower                                                        |
| mypy2                    | 933 ms                                                       | 1.05 sec: 1.12x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.2 us: 1.13x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                        |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                        |
| telco                    | 7.23 ms                                                      | 8.53 ms: 1.18x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 4.16 ms: 1.22x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.95 ms: 1.22x slower                                                        |
| coverage                 | 63.3 ms                                                      | 78.6 ms: 1.24x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240930-3.13.0rc2+-1ba3555/bm-20240930-pythonperf2-x86_64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.291x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.12x