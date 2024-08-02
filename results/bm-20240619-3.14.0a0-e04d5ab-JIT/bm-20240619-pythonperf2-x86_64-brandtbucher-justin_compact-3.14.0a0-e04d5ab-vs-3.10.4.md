# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_compact
- machine: linux-x86_64
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 307 ms: 1.14x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.13 sec: 1.09x faster                                                      |
| html5lib       | 94.6 ms                                                      | 73.9 ms: 1.28x faster                                                       |
| tornado_http   | 157 ms                                                       | 123 ms: 1.27x faster                                                        |
| Geometric mean | (ref)                                                        | 1.19x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 380 ms: 1.82x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 913 ms: 1.75x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 476 ms: 1.72x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 628 ms: 1.49x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.69x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 84.7 ms: 1.58x faster                                                       |
| float          | 111 ms                                                       | 74.6 ms: 1.49x faster                                                       |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.37x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 137 ms: 1.38x faster                                                        |
| regex_dna      | 261 ms                                                       | 242 ms: 1.08x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.48 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 312 us: 1.46x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 222 us: 1.41x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.15 sec: 1.36x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 58.3 ms: 1.30x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.20x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 142 ms: 1.13x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 82.4 ms: 1.12x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 99.7 ms: 1.11x faster                                                       |
| unpickle_list        | 4.65 us                                                      | 4.91 us: 1.06x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 32.1 us: 1.09x slower                                                       |
| pickle               | 9.89 us                                                      | 10.8 us: 1.09x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.53 us: 1.10x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.5 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.8 ms: 1.20x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.47 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.25x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.24 ms: 1.59x faster                                                       |
| django_template | 50.2 ms                                                      | 40.9 ms: 1.23x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 27.6 ms: 1.14x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 64.9 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.21x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 186 us: 2.89x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 378 ms: 2.06x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.69 ms: 2.03x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| async_tree_none          | 692 ms                                                       | 380 ms: 1.82x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 28.3 us: 1.76x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 913 ms: 1.75x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 476 ms: 1.72x faster                                                        |
| richards_super           | 90.6 ms                                                      | 53.1 ms: 1.71x faster                                                       |
| spectral_norm            | 139 ms                                                       | 81.9 ms: 1.70x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 70.2 ms: 1.70x faster                                                       |
| generators               | 57.3 ms                                                      | 34.0 ms: 1.68x faster                                                       |
| raytrace                 | 489 ms                                                       | 296 ms: 1.65x faster                                                        |
| chaos                    | 109 ms                                                       | 65.9 ms: 1.65x faster                                                       |
| pyflate                  | 733 ms                                                       | 447 ms: 1.64x faster                                                        |
| richards                 | 75.1 ms                                                      | 45.8 ms: 1.64x faster                                                       |
| logging_silent           | 167 ns                                                       | 102 ns: 1.63x faster                                                        |
| go                       | 262 ms                                                       | 162 ms: 1.62x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 66.4 ms: 1.62x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.24 ms: 1.59x faster                                                       |
| nbody                    | 134 ms                                                       | 84.7 ms: 1.58x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.42 ms: 1.58x faster                                                       |
| deepcopy                 | 468 us                                                       | 308 us: 1.52x faster                                                        |
| pylint                   | 566 ms                                                       | 379 ms: 1.49x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 628 ms: 1.49x faster                                                        |
| float                    | 111 ms                                                       | 74.6 ms: 1.49x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.81 ms: 1.48x faster                                                       |
| comprehensions           | 26.7 us                                                      | 18.1 us: 1.47x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 312 us: 1.46x faster                                                        |
| scimark_sor              | 180 ms                                                       | 127 ms: 1.41x faster                                                        |
| fannkuch                 | 483 ms                                                       | 342 ms: 1.41x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.68 ms: 1.41x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 222 us: 1.41x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.38 us: 1.39x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.9 ms: 1.39x faster                                                       |
| regex_compile            | 190 ms                                                       | 137 ms: 1.38x faster                                                        |
| scimark_lu               | 167 ms                                                       | 122 ms: 1.37x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.09 us: 1.36x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.15 sec: 1.36x faster                                                      |
| bench_mp_pool            | 6.37 ms                                                      | 4.78 ms: 1.33x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                                      |
| pathlib                  | 21.4 ms                                                      | 16.1 ms: 1.33x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 795 ms: 1.32x faster                                                        |
| thrift                   | 1.18 ms                                                      | 896 us: 1.31x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.08 us: 1.30x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 58.3 ms: 1.30x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 73.9 ms: 1.28x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 3.98 ms: 1.28x faster                                                       |
| tornado_http             | 157 ms                                                       | 123 ms: 1.27x faster                                                        |
| django_template          | 50.2 ms                                                      | 40.9 ms: 1.23x faster                                                       |
| scimark_fft              | 361 ms                                                       | 294 ms: 1.23x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 66.3 ms: 1.22x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.2 us: 1.20x faster                                                       |
| nqueens                  | 115 ms                                                       | 96.1 ms: 1.20x faster                                                       |
| dask                     | 472 ms                                                       | 404 ms: 1.17x faster                                                        |
| sympy_sum                | 193 ms                                                       | 165 ms: 1.17x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 983 us: 1.16x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.60 sec: 1.16x faster                                                      |
| sympy_str                | 360 ms                                                       | 314 ms: 1.15x faster                                                        |
| 2to3                     | 350 ms                                                       | 307 ms: 1.14x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 27.6 ms: 1.14x faster                                                       |
| sympy_expand             | 600 ms                                                       | 529 ms: 1.13x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 142 ms: 1.13x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 82.4 ms: 1.12x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 99.7 ms: 1.11x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 63.7 ms: 1.10x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 25.7 ms: 1.10x faster                                                       |
| docutils                 | 3.41 sec                                                     | 3.13 sec: 1.09x faster                                                      |
| async_generators         | 421 ms                                                       | 386 ms: 1.09x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 132 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| regex_dna                | 261 ms                                                       | 242 ms: 1.08x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.79 us: 1.07x faster                                                       |
| json                     | 5.86 ms                                                      | 5.51 ms: 1.06x faster                                                       |
| meteor_contest           | 138 ms                                                       | 131 ms: 1.06x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 64.9 ms: 1.03x slower                                                       |
| unpickle_list            | 4.65 us                                                      | 4.91 us: 1.06x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.91 ms: 1.09x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 32.1 us: 1.09x slower                                                       |
| pickle                   | 9.89 us                                                      | 10.8 us: 1.09x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.53 us: 1.10x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.06 ms: 1.12x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.48 ms: 1.13x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.5 us: 1.15x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.8 ms: 1.20x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.47 ms: 1.29x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.47 ms: 1.31x slower                                                       |
| coverage                 | 63.3 ms                                                      | 85.2 ms: 1.35x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.29x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240619-3.14.0a0-e04d5ab-JIT/bm-20240619-pythonperf2-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.22x