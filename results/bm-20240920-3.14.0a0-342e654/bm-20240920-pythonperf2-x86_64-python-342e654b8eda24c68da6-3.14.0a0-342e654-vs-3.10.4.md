# Results vs. 3.10.4

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-x86_64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.330x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 282 ms: 1.24x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| html5lib       | 94.6 ms                                                      | 72.4 ms: 1.31x faster                                                       |
| tornado_http   | 157 ms                                                       | 117 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 323 ms: 2.14x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 400 ms: 2.05x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 807 ms: 1.98x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 570 ms: 1.64x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.94x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 91.6 ms: 1.46x faster                                                       |
| float          | 111 ms                                                       | 78.2 ms: 1.42x faster                                                       |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 142 ms: 1.34x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                       |
| regex_dna      | 261 ms                                                       | 245 ms: 1.07x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.61 ms: 1.17x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 321 us: 1.42x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                       |
| unpickle_pure_python | 312 us                                                       | 229 us: 1.36x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 59.4 ms: 1.28x faster                                                       |
| json_loads           | 30.3 us                                                      | 24.6 us: 1.23x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.14x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.63 sec: 1.11x faster                                                      |
| xml_etree_iterparse  | 110 ms                                                       | 100 ms: 1.10x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 84.9 ms: 1.09x faster                                                       |
| unpickle_list        | 4.65 us                                                      | 4.69 us: 1.01x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 30.3 us: 1.03x slower                                                       |
| pickle               | 9.89 us                                                      | 10.2 us: 1.03x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.28 us: 1.04x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.1 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 8.94 ms: 1.22x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| django_template | 50.2 ms                                                      | 39.5 ms: 1.27x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 25.7 ms: 1.22x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 56.4 ms: 1.12x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.25x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 176 us: 3.05x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.42 ms: 2.19x faster                                                       |
| async_tree_none          | 692 ms                                                       | 323 ms: 2.14x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 372 ms: 2.09x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 400 ms: 2.05x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 807 ms: 1.98x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.57 sec: 1.97x faster                                                      |
| generators               | 57.3 ms                                                      | 29.6 ms: 1.94x faster                                                       |
| go                       | 262 ms                                                       | 139 ms: 1.88x faster                                                        |
| chaos                    | 109 ms                                                       | 63.4 ms: 1.71x faster                                                       |
| raytrace                 | 489 ms                                                       | 286 ms: 1.71x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.3 us: 1.70x faster                                                       |
| scimark_lu               | 167 ms                                                       | 99.0 ms: 1.68x faster                                                       |
| logging_silent           | 167 ns                                                       | 99.7 ns: 1.68x faster                                                       |
| deepcopy                 | 468 us                                                       | 284 us: 1.65x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 570 ms: 1.64x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 73.2 ms: 1.63x faster                                                       |
| pylint                   | 566 ms                                                       | 350 ms: 1.62x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 67.1 ms: 1.60x faster                                                       |
| richards_super           | 90.6 ms                                                      | 57.0 ms: 1.59x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.58x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.0 us: 1.57x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.16 ms: 1.53x faster                                                       |
| pyflate                  | 733 ms                                                       | 483 ms: 1.52x faster                                                        |
| scimark_sor              | 180 ms                                                       | 120 ms: 1.50x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.80 ms: 1.49x faster                                                       |
| richards                 | 75.1 ms                                                      | 50.9 ms: 1.47x faster                                                       |
| nbody                    | 134 ms                                                       | 91.6 ms: 1.46x faster                                                       |
| spectral_norm            | 139 ms                                                       | 96.7 ms: 1.44x faster                                                       |
| float                    | 111 ms                                                       | 78.2 ms: 1.42x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 321 us: 1.42x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.86 us: 1.40x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.38 us: 1.39x faster                                                       |
| thrift                   | 1.18 ms                                                      | 851 us: 1.38x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.98 us: 1.38x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.0 ms: 1.38x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.37x faster                                                      |
| json_dumps               | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 229 us: 1.36x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.7 ms: 1.36x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.69 ms: 1.36x faster                                                       |
| tornado_http             | 157 ms                                                       | 117 ms: 1.35x faster                                                        |
| regex_compile            | 190 ms                                                       | 142 ms: 1.34x faster                                                        |
| fannkuch                 | 483 ms                                                       | 361 ms: 1.34x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 857 us: 1.33x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.32x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 802 ms: 1.31x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 72.4 ms: 1.31x faster                                                       |
| nqueens                  | 115 ms                                                       | 89.1 ms: 1.29x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 59.4 ms: 1.28x faster                                                       |
| django_template          | 50.2 ms                                                      | 39.5 ms: 1.27x faster                                                       |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                        |
| 2to3                     | 350 ms                                                       | 282 ms: 1.24x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 116 ms: 1.24x faster                                                        |
| json_loads               | 30.3 us                                                      | 24.6 us: 1.23x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.12 ms: 1.23x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 25.7 ms: 1.22x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 23.0 ms: 1.22x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 66.4 ms: 1.22x faster                                                       |
| sympy_str                | 360 ms                                                       | 296 ms: 1.22x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 57.9 ms: 1.21x faster                                                       |
| sympy_expand             | 600 ms                                                       | 501 ms: 1.20x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.52 sec: 1.19x faster                                                      |
| scimark_fft              | 361 ms                                                       | 305 ms: 1.19x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| async_generators         | 421 ms                                                       | 359 ms: 1.17x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 52.6 ns: 1.14x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 141 ms: 1.14x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 56.4 ms: 1.12x faster                                                       |
| json                     | 5.86 ms                                                      | 5.26 ms: 1.11x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.63 sec: 1.11x faster                                                      |
| xml_etree_iterparse      | 110 ms                                                       | 100 ms: 1.10x faster                                                        |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 84.9 ms: 1.09x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.77 us: 1.08x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                       |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| regex_dna                | 261 ms                                                       | 245 ms: 1.07x faster                                                        |
| unpickle_list            | 4.65 us                                                      | 4.69 us: 1.01x slower                                                       |
| asyncio_websockets       | 390 ms                                                       | 397 ms: 1.02x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 30.3 us: 1.03x slower                                                       |
| pickle                   | 9.89 us                                                      | 10.2 us: 1.03x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.28 us: 1.04x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.1 us: 1.12x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.34 ms: 1.15x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.61 ms: 1.17x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.94 ms: 1.22x slower                                                       |
| coverage                 | 63.3 ms                                                      | 79.6 ms: 1.26x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.49 ms: 1.31x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.32x faster                                                                |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240920-3.14.0a0-342e654/bm-20240920-pythonperf2-x86_64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.330x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.13x