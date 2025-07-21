# Results vs. 3.10.4

- fork: python
- ref: 800d37feca2e0ea33439
- machine: linux-x86_64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.332x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.25x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.88 sec: 1.19x faster                                                      |
| html5lib       | 94.6 ms                                                      | 66.3 ms: 1.43x faster                                                       |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 612 ms: 2.61x faster                                                        |
| async_tree_none         | 692 ms                                                       | 267 ms: 2.59x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 323 ms: 2.53x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 494 ms: 1.90x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.39x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 71.2 ms: 1.56x faster                                                       |
| nbody          | 134 ms                                                       | 93.0 ms: 1.44x faster                                                       |
| pidigits       | 271 ms                                                       | 256 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 131 ms: 1.45x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 23.6 ms: 1.15x faster                                                       |
| regex_dna      | 261 ms                                                       | 227 ms: 1.15x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.14x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 205 us: 1.53x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.00 sec: 1.46x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 325 us: 1.40x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 57.2 ms: 1.33x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                       |
| json_loads           | 30.3 us                                                      | 26.3 us: 1.15x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.14x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 97.5 ms: 1.13x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 81.9 ms: 1.13x faster                                                       |
| unpickle_list        | 4.65 us                                                      | 5.02 us: 1.08x slower                                                       |
| unpickle             | 13.5 us                                                      | 14.8 us: 1.10x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.99 us: 1.21x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 36.5 us: 1.24x slower                                                       |
| pickle               | 9.89 us                                                      | 12.5 us: 1.27x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.10x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.68 ms: 1.18x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.2 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.25x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 36.1 ms: 1.39x faster                                                       |
| mako            | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.5 ms: 1.34x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 53.4 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.32x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 166 us: 3.23x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 612 ms: 2.61x faster                                                        |
| async_tree_none          | 692 ms                                                       | 267 ms: 2.59x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 323 ms: 2.53x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.17 ms: 2.36x faster                                                       |
| mdp                      | 3.01 sec                                                     | 1.27 sec: 2.36x faster                                                      |
| go                       | 262 ms                                                       | 116 ms: 2.25x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 368 ms: 2.12x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.59 sec: 1.95x faster                                                      |
| generators               | 57.3 ms                                                      | 29.4 ms: 1.95x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 494 ms: 1.90x faster                                                        |
| chaos                    | 109 ms                                                       | 58.4 ms: 1.86x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 27.2 us: 1.83x faster                                                       |
| logging_silent           | 167 ns                                                       | 93.9 ns: 1.78x faster                                                       |
| pyflate                  | 733 ms                                                       | 412 ms: 1.78x faster                                                        |
| pylint                   | 566 ms                                                       | 318 ms: 1.78x faster                                                        |
| richards_super           | 90.6 ms                                                      | 50.9 ms: 1.78x faster                                                       |
| raytrace                 | 489 ms                                                       | 278 ms: 1.76x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 61.2 ms: 1.76x faster                                                       |
| scimark_lu               | 167 ms                                                       | 95.2 ms: 1.75x faster                                                       |
| deepcopy                 | 468 us                                                       | 268 us: 1.75x faster                                                        |
| scimark_sor              | 180 ms                                                       | 103 ms: 1.74x faster                                                        |
| richards                 | 75.1 ms                                                      | 45.1 ms: 1.66x faster                                                       |
| comprehensions           | 26.7 us                                                      | 16.1 us: 1.66x faster                                                       |
| spectral_norm            | 139 ms                                                       | 86.3 ms: 1.61x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 5.86 ms: 1.61x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 76.2 ms: 1.56x faster                                                       |
| float                    | 111 ms                                                       | 71.2 ms: 1.56x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 205 us: 1.53x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.02 us: 1.47x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.62 us: 1.46x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.00 sec: 1.46x faster                                                      |
| regex_compile            | 190 ms                                                       | 131 ms: 1.45x faster                                                        |
| nbody                    | 134 ms                                                       | 93.0 ms: 1.44x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 66.3 ms: 1.43x faster                                                       |
| thrift                   | 1.18 ms                                                      | 826 us: 1.42x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 42.3 ns: 1.42x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.52 sec: 1.41x faster                                                      |
| pickle_pure_python       | 455 us                                                       | 325 us: 1.40x faster                                                        |
| django_template          | 50.2 ms                                                      | 36.1 ms: 1.39x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 754 ms: 1.39x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 58.3 ms: 1.39x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.91 us: 1.38x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.1 ms: 1.37x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                       |
| fannkuch                 | 483 ms                                                       | 360 ms: 1.34x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 23.5 ms: 1.34x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 57.2 ms: 1.33x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.31x faster                                                      |
| sympy_sum                | 193 ms                                                       | 149 ms: 1.30x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 21.9 ms: 1.28x faster                                                       |
| sympy_str                | 360 ms                                                       | 283 ms: 1.27x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.9 ms: 1.27x faster                                                       |
| nqueens                  | 115 ms                                                       | 91.8 ms: 1.25x faster                                                       |
| 2to3                     | 350 ms                                                       | 281 ms: 1.25x faster                                                        |
| sympy_expand             | 600 ms                                                       | 481 ms: 1.25x faster                                                        |
| scimark_fft              | 361 ms                                                       | 303 ms: 1.19x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 961 us: 1.19x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.88 sec: 1.19x faster                                                      |
| genshi_xml               | 63.3 ms                                                      | 53.4 ms: 1.18x faster                                                       |
| json_loads               | 30.3 us                                                      | 26.3 us: 1.15x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 23.6 ms: 1.15x faster                                                       |
| regex_dna                | 261 ms                                                       | 227 ms: 1.15x faster                                                        |
| meteor_contest           | 138 ms                                                       | 120 ms: 1.15x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 141 ms: 1.14x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 97.5 ms: 1.13x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 81.9 ms: 1.13x faster                                                       |
| json                     | 5.86 ms                                                      | 5.39 ms: 1.09x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.75 ms: 1.07x faster                                                       |
| pidigits                 | 271 ms                                                       | 256 ms: 1.06x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.84 us: 1.05x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 380 ms: 1.03x faster                                                        |
| async_generators         | 421 ms                                                       | 424 ms: 1.01x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 5.02 us: 1.08x slower                                                       |
| unpickle                 | 13.5 us                                                      | 14.8 us: 1.10x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.68 ms: 1.18x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.99 us: 1.21x slower                                                       |
| coverage                 | 63.3 ms                                                      | 77.7 ms: 1.23x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 36.5 us: 1.24x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.5 us: 1.27x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.2 ms: 1.32x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.90 ms: 1.64x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.25 ms: 1.83x slower                                                       |
| telco                    | 7.23 ms                                                      | 160 ms: 22.08x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 2.38 sec: 373.82x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250719-3.15.0a0-800d37f/bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.332x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.38x