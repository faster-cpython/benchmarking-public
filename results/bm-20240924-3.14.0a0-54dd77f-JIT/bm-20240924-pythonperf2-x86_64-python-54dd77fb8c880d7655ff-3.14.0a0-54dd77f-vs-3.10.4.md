# Results vs. 3.10.4

- fork: python
- ref: 54dd77fb8c880d7655ff
- machine: linux-x86_64
- commit hash: 54dd77f
- commit date: 2024-09-24
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 312 ms: 1.12x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.18 sec: 1.07x faster                                                      |
| html5lib       | 94.6 ms                                                      | 71.4 ms: 1.33x faster                                                       |
| tornado_http   | 157 ms                                                       | 122 ms: 1.28x faster                                                        |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 325 ms: 2.12x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 408 ms: 2.01x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 806 ms: 1.98x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 578 ms: 1.62x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.92x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 83.8 ms: 1.60x faster                                                       |
| float          | 111 ms                                                       | 73.6 ms: 1.51x faster                                                       |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.38x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 148 ms: 1.28x faster                                                        |
| regex_dna      | 261 ms                                                       | 234 ms: 1.12x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 216 us: 1.44x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 325 us: 1.40x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.11 sec: 1.38x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 56.4 ms: 1.35x faster                                                       |
| json_loads           | 30.3 us                                                      | 24.2 us: 1.26x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 80.2 ms: 1.15x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 98.2 ms: 1.13x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| pickle               | 9.89 us                                                      | 10.6 us: 1.07x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 32.2 us: 1.09x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.54 us: 1.10x slower                                                       |
| unpickle             | 13.5 us                                                      | 14.9 us: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.17x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.00 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.16 ms: 1.60x faster                                                       |
| django_template | 50.2 ms                                                      | 42.4 ms: 1.19x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 29.5 ms: 1.07x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 68.6 ms: 1.08x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.17x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 183 us: 2.94x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.17 ms: 2.36x faster                                                       |
| async_tree_none          | 692 ms                                                       | 325 ms: 2.12x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 380 ms: 2.05x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 408 ms: 2.01x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 806 ms: 1.98x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| deepcopy_memo            | 49.8 us                                                      | 26.9 us: 1.85x faster                                                       |
| go                       | 262 ms                                                       | 148 ms: 1.76x faster                                                        |
| richards_super           | 90.6 ms                                                      | 51.6 ms: 1.76x faster                                                       |
| scimark_sor              | 180 ms                                                       | 104 ms: 1.73x faster                                                        |
| spectral_norm            | 139 ms                                                       | 81.4 ms: 1.71x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 69.9 ms: 1.70x faster                                                       |
| scimark_lu               | 167 ms                                                       | 98.4 ms: 1.70x faster                                                       |
| richards                 | 75.1 ms                                                      | 44.6 ms: 1.68x faster                                                       |
| pyflate                  | 733 ms                                                       | 445 ms: 1.65x faster                                                        |
| chaos                    | 109 ms                                                       | 66.9 ms: 1.62x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 578 ms: 1.62x faster                                                        |
| logging_silent           | 167 ns                                                       | 104 ns: 1.61x faster                                                        |
| mako                     | 14.7 ms                                                      | 9.16 ms: 1.60x faster                                                       |
| nbody                    | 134 ms                                                       | 83.8 ms: 1.60x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 68.5 ms: 1.57x faster                                                       |
| deepcopy                 | 468 us                                                       | 298 us: 1.57x faster                                                        |
| generators               | 57.3 ms                                                      | 37.3 ms: 1.54x faster                                                       |
| float                    | 111 ms                                                       | 73.6 ms: 1.51x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.49 ms: 1.51x faster                                                       |
| raytrace                 | 489 ms                                                       | 332 ms: 1.47x faster                                                        |
| comprehensions           | 26.7 us                                                      | 18.2 us: 1.47x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 216 us: 1.44x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.3 ms: 1.43x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 325 us: 1.40x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.11 sec: 1.38x faster                                                      |
| sqlglot_transpile        | 2.68 ms                                                      | 1.95 ms: 1.38x faster                                                       |
| pylint                   | 566 ms                                                       | 411 ms: 1.38x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.6 ms: 1.37x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.92 us: 1.37x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.95 ms: 1.35x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 56.4 ms: 1.35x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.35x faster                                                       |
| fannkuch                 | 483 ms                                                       | 360 ms: 1.34x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.67 us: 1.33x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.26 us: 1.33x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 71.4 ms: 1.33x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 792 ms: 1.33x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.30x faster                                                      |
| pycparser                | 1.67 sec                                                     | 1.29 sec: 1.30x faster                                                      |
| thrift                   | 1.18 ms                                                      | 915 us: 1.29x faster                                                        |
| tornado_http             | 157 ms                                                       | 122 ms: 1.28x faster                                                        |
| regex_compile            | 190 ms                                                       | 148 ms: 1.28x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.01 ms: 1.27x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 64.3 ms: 1.26x faster                                                       |
| scimark_fft              | 361 ms                                                       | 287 ms: 1.26x faster                                                        |
| json_loads               | 30.3 us                                                      | 24.2 us: 1.26x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 5.08 ms: 1.25x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 927 us: 1.23x faster                                                        |
| django_template          | 50.2 ms                                                      | 42.4 ms: 1.19x faster                                                       |
| nqueens                  | 115 ms                                                       | 98.2 ms: 1.17x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.60 sec: 1.16x faster                                                      |
| sympy_str                | 360 ms                                                       | 313 ms: 1.15x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 80.2 ms: 1.15x faster                                                       |
| sympy_sum                | 193 ms                                                       | 170 ms: 1.14x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 98.2 ms: 1.13x faster                                                       |
| 2to3                     | 350 ms                                                       | 312 ms: 1.12x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.66 us: 1.12x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 128 ms: 1.12x faster                                                        |
| regex_dna                | 261 ms                                                       | 234 ms: 1.12x faster                                                        |
| sympy_expand             | 600 ms                                                       | 537 ms: 1.12x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| json                     | 5.86 ms                                                      | 5.33 ms: 1.10x faster                                                       |
| async_generators         | 421 ms                                                       | 387 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.18 sec: 1.07x faster                                                      |
| meteor_contest           | 138 ms                                                       | 129 ms: 1.07x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 65.6 ms: 1.07x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 29.5 ms: 1.07x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 26.5 ms: 1.06x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 25.8 ms: 1.05x faster                                                       |
| pickle                   | 9.89 us                                                      | 10.6 us: 1.07x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.91 ms: 1.08x slower                                                       |
| genshi_xml               | 63.3 ms                                                      | 68.6 ms: 1.08x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 32.2 us: 1.09x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.54 us: 1.10x slower                                                       |
| unpickle                 | 13.5 us                                                      | 14.9 us: 1.10x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.20 ms: 1.14x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.17x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.00 ms: 1.23x slower                                                       |
| coverage                 | 63.3 ms                                                      | 79.8 ms: 1.26x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.42 ms: 1.29x slower                                                       |
| unpack_sequence          | 59.9 ns                                                      | 87.7 ns: 1.46x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.29x faster                                                                |

Benchmark hidden because not significant (2): unpickle_list, asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240924-3.14.0a0-54dd77f-JIT/bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.22x