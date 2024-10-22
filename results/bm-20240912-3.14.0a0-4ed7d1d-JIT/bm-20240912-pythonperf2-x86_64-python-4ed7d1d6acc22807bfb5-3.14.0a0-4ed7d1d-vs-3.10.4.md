# Results vs. 3.10.4

- fork: python
- ref: 4ed7d1d6acc22807bfb5
- machine: linux-x86_64
- commit hash: 4ed7d1d
- commit date: 2024-09-12
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 309 ms: 1.13x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.15 sec: 1.08x faster                                                      |
| html5lib       | 94.6 ms                                                      | 71.1 ms: 1.33x faster                                                       |
| tornado_http   | 157 ms                                                       | 122 ms: 1.28x faster                                                        |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 323 ms: 2.14x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 404 ms: 2.03x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 812 ms: 1.97x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 576 ms: 1.62x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.93x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 81.8 ms: 1.64x faster                                                       |
| float          | 111 ms                                                       | 74.6 ms: 1.49x faster                                                       |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.38x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 147 ms: 1.29x faster                                                        |
| regex_dna      | 261 ms                                                       | 233 ms: 1.12x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.49 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 220 us: 1.42x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 326 us: 1.40x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.13 sec: 1.37x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 55.9 ms: 1.36x faster                                                       |
| json_loads           | 30.3 us                                                      | 23.9 us: 1.27x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 80.1 ms: 1.15x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 98.9 ms: 1.12x faster                                                       |
| pickle_list          | 4.12 us                                                      | 4.18 us: 1.02x slower                                                       |
| unpickle_list        | 4.65 us                                                      | 4.72 us: 1.02x slower                                                       |
| pickle               | 9.89 us                                                      | 10.4 us: 1.05x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.1 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.16x faster                                                                |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.00 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.23 ms: 1.59x faster                                                       |
| django_template | 50.2 ms                                                      | 42.8 ms: 1.17x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 29.5 ms: 1.06x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 66.0 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.18x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 181 us: 2.97x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.21 ms: 2.34x faster                                                       |
| async_tree_none          | 692 ms                                                       | 323 ms: 2.14x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 377 ms: 2.07x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 404 ms: 2.03x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 812 ms: 1.97x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| deepcopy_memo            | 49.8 us                                                      | 27.1 us: 1.84x faster                                                       |
| go                       | 262 ms                                                       | 149 ms: 1.75x faster                                                        |
| richards_super           | 90.6 ms                                                      | 52.1 ms: 1.74x faster                                                       |
| scimark_sor              | 180 ms                                                       | 105 ms: 1.72x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 69.3 ms: 1.72x faster                                                       |
| spectral_norm            | 139 ms                                                       | 81.6 ms: 1.71x faster                                                       |
| richards                 | 75.1 ms                                                      | 44.5 ms: 1.69x faster                                                       |
| scimark_lu               | 167 ms                                                       | 99.3 ms: 1.68x faster                                                       |
| logging_silent           | 167 ns                                                       | 100 ns: 1.67x faster                                                        |
| chaos                    | 109 ms                                                       | 65.7 ms: 1.65x faster                                                       |
| nbody                    | 134 ms                                                       | 81.8 ms: 1.64x faster                                                       |
| pyflate                  | 733 ms                                                       | 449 ms: 1.63x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 576 ms: 1.62x faster                                                        |
| deepcopy                 | 468 us                                                       | 289 us: 1.62x faster                                                        |
| mako                     | 14.7 ms                                                      | 9.23 ms: 1.59x faster                                                       |
| raytrace                 | 489 ms                                                       | 310 ms: 1.58x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 68.9 ms: 1.56x faster                                                       |
| generators               | 57.3 ms                                                      | 37.6 ms: 1.52x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.49 ms: 1.50x faster                                                       |
| float                    | 111 ms                                                       | 74.6 ms: 1.49x faster                                                       |
| comprehensions           | 26.7 us                                                      | 18.2 us: 1.46x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 220 us: 1.42x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.5 ms: 1.41x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 326 us: 1.40x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.94 ms: 1.38x faster                                                       |
| pylint                   | 566 ms                                                       | 410 ms: 1.38x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.92 us: 1.37x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.13 sec: 1.37x faster                                                      |
| json_dumps               | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 55.9 ms: 1.36x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.98 ms: 1.35x faster                                                       |
| fannkuch                 | 483 ms                                                       | 358 ms: 1.35x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.15 us: 1.35x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                      |
| logging_simple           | 8.88 us                                                      | 6.62 us: 1.34x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.0 ms: 1.34x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 71.1 ms: 1.33x faster                                                       |
| thrift                   | 1.18 ms                                                      | 885 us: 1.33x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 796 ms: 1.32x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.30x faster                                                      |
| regex_compile            | 190 ms                                                       | 147 ms: 1.29x faster                                                        |
| tornado_http             | 157 ms                                                       | 122 ms: 1.28x faster                                                        |
| json_loads               | 30.3 us                                                      | 23.9 us: 1.27x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 64.6 ms: 1.25x faster                                                       |
| scimark_fft              | 361 ms                                                       | 290 ms: 1.25x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.10 ms: 1.24x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 924 us: 1.24x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 5.25 ms: 1.21x faster                                                       |
| django_template          | 50.2 ms                                                      | 42.8 ms: 1.17x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.57 sec: 1.17x faster                                                      |
| nqueens                  | 115 ms                                                       | 99.1 ms: 1.16x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 80.1 ms: 1.15x faster                                                       |
| sympy_str                | 360 ms                                                       | 313 ms: 1.15x faster                                                        |
| sympy_sum                | 193 ms                                                       | 169 ms: 1.14x faster                                                        |
| json                     | 5.86 ms                                                      | 5.14 ms: 1.14x faster                                                       |
| 2to3                     | 350 ms                                                       | 309 ms: 1.13x faster                                                        |
| sympy_expand             | 600 ms                                                       | 533 ms: 1.13x faster                                                        |
| regex_dna                | 261 ms                                                       | 233 ms: 1.12x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 129 ms: 1.12x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 98.9 ms: 1.12x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.69 us: 1.11x faster                                                       |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.15 sec: 1.08x faster                                                      |
| async_generators         | 421 ms                                                       | 393 ms: 1.07x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 65.7 ms: 1.07x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 29.5 ms: 1.06x faster                                                       |
| meteor_contest           | 138 ms                                                       | 131 ms: 1.06x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 26.6 ms: 1.06x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 395 ms: 1.01x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.18 us: 1.02x slower                                                       |
| unpickle_list            | 4.65 us                                                      | 4.72 us: 1.02x slower                                                       |
| genshi_xml               | 63.3 ms                                                      | 66.0 ms: 1.04x slower                                                       |
| pickle                   | 9.89 us                                                      | 10.4 us: 1.05x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.94 ms: 1.10x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.1 us: 1.12x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.49 ms: 1.13x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.28 ms: 1.15x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.00 ms: 1.23x slower                                                       |
| coverage                 | 63.3 ms                                                      | 81.3 ms: 1.29x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.87 ms: 1.43x slower                                                       |
| unpack_sequence          | 59.9 ns                                                      | 89.4 ns: 1.49x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.30x faster                                                                |

Benchmark hidden because not significant (1): pickle_dict
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240912-3.14.0a0-4ed7d1d-JIT/bm-20240912-pythonperf2-x86_64-python-4ed7d1d6acc22807bfb5-3.14.0a0-4ed7d1d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.22x