# Results vs. 3.10.4

- fork: python
- ref: 33eeccf6d4f16e483b4c
- machine: linux-x86_64
- commit hash: 33eeccf
- commit date: 2024-09-17
- overall geometric mean: 1.38x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 276 ms: 1.26x faster                                                  |
| docutils       | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                |
| html5lib       | 88.9 ms                                                | 65.1 ms: 1.37x faster                                                 |
| tornado_http   | 136 ms                                                 | 94.4 ms: 1.44x faster                                                 |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 316 ms: 2.30x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 399 ms: 2.18x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 856 ms: 2.07x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 574 ms: 1.77x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.07x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.7 ms: 1.93x faster                                                 |
| float          | 117 ms                                                 | 69.9 ms: 1.68x faster                                                 |
| pidigits       | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.49x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 142 ms: 1.33x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                 |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.82 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                |
| pickle_pure_python   | 484 us                                                 | 307 us: 1.58x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 215 us: 1.54x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 54.1 ms: 1.46x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.1 ms: 1.40x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 77.8 ms: 1.28x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 98.2 ms: 1.18x faster                                                 |
| json_loads           | 31.2 us                                                | 26.9 us: 1.16x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 146 ms: 1.15x faster                                                  |
| unpickle             | 14.4 us                                                | 14.8 us: 1.03x slower                                                 |
| unpickle_list        | 5.20 us                                                | 5.40 us: 1.04x slower                                                 |
| pickle               | 10.7 us                                                | 11.4 us: 1.07x slower                                                 |
| pickle_dict          | 29.6 us                                                | 34.1 us: 1.15x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                 |
| django_template | 48.2 ms                                                | 36.1 ms: 1.33x faster                                                 |
| genshi_text     | 31.8 ms                                                | 25.5 ms: 1.25x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 59.6 ms: 1.11x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.21 ms: 2.46x faster                                                 |
| generators               | 80.1 ms                                                | 32.7 ms: 2.45x faster                                                 |
| async_tree_none          | 728 ms                                                 | 316 ms: 2.30x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 399 ms: 2.18x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 27.0 us: 2.17x faster                                                 |
| richards_super           | 94.7 ms                                                | 45.7 ms: 2.07x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 856 ms: 2.07x faster                                                  |
| richards                 | 79.3 ms                                                | 39.7 ms: 2.00x faster                                                 |
| chaos                    | 115 ms                                                 | 58.8 ms: 1.96x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 66.2 ms: 1.93x faster                                                 |
| nbody                    | 154 ms                                                 | 79.7 ms: 1.93x faster                                                 |
| scimark_sor              | 220 ms                                                 | 116 ms: 1.89x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 63.5 ms: 1.86x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 497 ms: 1.85x faster                                                  |
| go                       | 240 ms                                                 | 130 ms: 1.84x faster                                                  |
| raytrace                 | 507 ms                                                 | 276 ms: 1.84x faster                                                  |
| logging_silent           | 190 ns                                                 | 104 ns: 1.83x faster                                                  |
| deepcopy                 | 479 us                                                 | 263 us: 1.82x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 574 ms: 1.77x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                                 |
| float                    | 117 ms                                                 | 69.9 ms: 1.68x faster                                                 |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                                  |
| mako                     | 16.3 ms                                                | 10.0 ms: 1.63x faster                                                 |
| scimark_lu               | 176 ms                                                 | 109 ms: 1.62x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.34 ms: 1.61x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                                |
| pyflate                  | 716 ms                                                 | 448 ms: 1.60x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 307 us: 1.58x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.67 us: 1.56x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 215 us: 1.54x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.52x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.88 ms: 1.51x faster                                                 |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.57 us: 1.49x faster                                                 |
| logging_format           | 9.09 us                                                | 6.10 us: 1.49x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.49x faster                                                 |
| pylint                   | 551 ms                                                 | 372 ms: 1.48x faster                                                  |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.39 ms: 1.47x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 54.1 ms: 1.46x faster                                                 |
| tornado_http             | 136 ms                                                 | 94.4 ms: 1.44x faster                                                 |
| fannkuch                 | 532 ms                                                 | 373 ms: 1.43x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                |
| json_dumps               | 14.2 ms                                                | 10.1 ms: 1.40x faster                                                 |
| python_startup           | 14.6 ms                                                | 10.6 ms: 1.38x faster                                                 |
| thrift                   | 1.07 ms                                                | 781 us: 1.37x faster                                                  |
| html5lib                 | 88.9 ms                                                | 65.1 ms: 1.37x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 753 ms: 1.35x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.57 sec: 1.34x faster                                                |
| django_template          | 48.2 ms                                                | 36.1 ms: 1.33x faster                                                 |
| regex_compile            | 188 ms                                                 | 142 ms: 1.33x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 77.8 ms: 1.28x faster                                                 |
| pathlib                  | 20.5 ms                                                | 16.2 ms: 1.26x faster                                                 |
| 2to3                     | 348 ms                                                 | 276 ms: 1.26x faster                                                  |
| nqueens                  | 106 ms                                                 | 83.9 ms: 1.26x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                  |
| genshi_text              | 31.8 ms                                                | 25.5 ms: 1.25x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 67.6 ms: 1.25x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 58.0 ms: 1.19x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 837 us: 1.18x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 98.2 ms: 1.18x faster                                                 |
| json_loads               | 31.2 us                                                | 26.9 us: 1.16x faster                                                 |
| sympy_str                | 346 ms                                                 | 299 ms: 1.16x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 146 ms: 1.15x faster                                                  |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.14x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                                 |
| json                     | 5.69 ms                                                | 5.02 ms: 1.13x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                 |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                                  |
| sympy_expand             | 566 ms                                                 | 503 ms: 1.12x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                |
| genshi_xml               | 66.0 ms                                                | 59.6 ms: 1.11x faster                                                 |
| sqlite_synth             | 3.02 us                                                | 2.76 us: 1.10x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.66 sec: 1.07x faster                                                |
| pidigits                 | 191 ms                                                 | 186 ms: 1.03x faster                                                  |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.00x faster                                                  |
| async_generators         | 444 ms                                                 | 451 ms: 1.02x slower                                                  |
| unpickle                 | 14.4 us                                                | 14.8 us: 1.03x slower                                                 |
| unpickle_list            | 5.20 us                                                | 5.40 us: 1.04x slower                                                 |
| regex_effbot             | 3.63 ms                                                | 3.82 ms: 1.05x slower                                                 |
| pickle                   | 10.7 us                                                | 11.4 us: 1.07x slower                                                 |
| coverage                 | 79.4 ms                                                | 85.2 ms: 1.07x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 3.90 ms: 1.08x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.76 ms: 1.09x slower                                                 |
| telco                    | 7.27 ms                                                | 8.01 ms: 1.10x slower                                                 |
| pickle_dict              | 29.6 us                                                | 34.1 us: 1.15x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.09 ms: 1.20x slower                                                 |
| unpack_sequence          | 60.0 ns                                                | 112 ns: 1.87x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                          |

Benchmark hidden because not significant (2): bench_mp_pool, pickle_list
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240917-3.14.0a0-33eeccf-JIT/bm-20240917-linux-x86_64-python-33eeccf6d4f16e483b4c-3.14.0a0-33eeccf.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.20x