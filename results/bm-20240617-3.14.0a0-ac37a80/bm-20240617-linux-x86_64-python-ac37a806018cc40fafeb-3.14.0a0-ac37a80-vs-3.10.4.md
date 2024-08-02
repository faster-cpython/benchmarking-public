# Results vs. 3.10.4

- fork: python
- ref: ac37a806018cc40fafeb
- machine: linux-x86_64
- commit hash: ac37a80
- commit date: 2024-06-17
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 271 ms: 1.29x faster                                                  |
| docutils       | 3.30 sec                                               | 2.78 sec: 1.19x faster                                                |
| html5lib       | 88.9 ms                                                | 67.3 ms: 1.32x faster                                                 |
| tornado_http   | 136 ms                                                 | 93.8 ms: 1.45x faster                                                 |
| Geometric mean | (ref)                                                  | 1.31x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 375 ms: 1.94x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 466 ms: 1.87x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 976 ms: 1.81x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 630 ms: 1.61x faster                                                  |
| Geometric mean          | (ref)                                                  | 1.80x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.3 ms: 1.74x faster                                                 |
| float          | 117 ms                                                 | 78.1 ms: 1.50x faster                                                 |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.38x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 133 ms: 1.42x faster                                                  |
| regex_v8       | 27.8 ms                                                | 26.2 ms: 1.06x faster                                                 |
| regex_dna      | 227 ms                                                 | 227 ms: 1.00x slower                                                  |
| regex_effbot   | 3.63 ms                                                | 3.76 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 307 us: 1.58x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 219 us: 1.51x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 85.8 ms: 1.16x faster                                                 |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 107 ms: 1.08x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 160 ms: 1.05x faster                                                  |
| pickle_list          | 5.08 us                                                | 5.05 us: 1.01x faster                                                 |
| unpickle             | 14.4 us                                                | 15.1 us: 1.05x slower                                                 |
| unpickle_list        | 5.20 us                                                | 5.49 us: 1.06x slower                                                 |
| pickle               | 10.7 us                                                | 11.8 us: 1.11x slower                                                 |
| pickle_dict          | 29.6 us                                                | 34.7 us: 1.17x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.7 ms: 1.37x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                 |
| django_template | 48.2 ms                                                | 34.4 ms: 1.40x faster                                                 |
| genshi_text     | 31.8 ms                                                | 23.5 ms: 1.35x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 51.4 ms: 1.28x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                                  |
| generators               | 80.1 ms                                                | 29.2 ms: 2.74x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.26 ms: 2.43x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 29.7 us: 1.97x faster                                                 |
| async_tree_none          | 728 ms                                                 | 375 ms: 1.94x faster                                                  |
| raytrace                 | 507 ms                                                 | 266 ms: 1.90x faster                                                  |
| chaos                    | 115 ms                                                 | 60.9 ms: 1.90x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 488 ms: 1.89x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 466 ms: 1.87x faster                                                  |
| logging_silent           | 190 ns                                                 | 103 ns: 1.85x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 976 ms: 1.81x faster                                                  |
| deepcopy                 | 479 us                                                 | 266 us: 1.80x faster                                                  |
| pylint                   | 551 ms                                                 | 317 ms: 1.74x faster                                                  |
| nbody                    | 154 ms                                                 | 88.3 ms: 1.74x faster                                                 |
| richards_super           | 94.7 ms                                                | 55.1 ms: 1.72x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 74.5 ms: 1.72x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 69.0 ms: 1.71x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.16 ms: 1.69x faster                                                 |
| comprehensions           | 28.8 us                                                | 17.1 us: 1.69x faster                                                 |
| go                       | 240 ms                                                 | 146 ms: 1.65x faster                                                  |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                                 |
| scimark_sor              | 220 ms                                                 | 135 ms: 1.63x faster                                                  |
| richards                 | 79.3 ms                                                | 49.0 ms: 1.62x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 630 ms: 1.61x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.62 ms: 1.58x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 307 us: 1.58x faster                                                  |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                                 |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 219 us: 1.51x faster                                                  |
| float                    | 117 ms                                                 | 78.1 ms: 1.50x faster                                                 |
| spectral_norm            | 170 ms                                                 | 114 ms: 1.49x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.11 sec: 1.49x faster                                                |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                  |
| logging_simple           | 8.30 us                                                | 5.67 us: 1.46x faster                                                 |
| pyflate                  | 716 ms                                                 | 492 ms: 1.46x faster                                                  |
| tornado_http             | 136 ms                                                 | 93.8 ms: 1.45x faster                                                 |
| logging_format           | 9.09 us                                                | 6.31 us: 1.44x faster                                                 |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                                 |
| regex_compile            | 188 ms                                                 | 133 ms: 1.42x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.83 sec: 1.40x faster                                                |
| django_template          | 48.2 ms                                                | 34.4 ms: 1.40x faster                                                 |
| fannkuch                 | 532 ms                                                 | 389 ms: 1.37x faster                                                  |
| python_startup           | 14.6 ms                                                | 10.7 ms: 1.37x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.36x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 752 ms: 1.35x faster                                                  |
| genshi_text              | 31.8 ms                                                | 23.5 ms: 1.35x faster                                                 |
| thrift                   | 1.07 ms                                                | 796 us: 1.35x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.6 ms: 1.34x faster                                                 |
| nqueens                  | 106 ms                                                 | 79.5 ms: 1.33x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 59.8 ms: 1.32x faster                                                 |
| html5lib                 | 88.9 ms                                                | 67.3 ms: 1.32x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.20 sec: 1.32x faster                                                |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                                  |
| dulwich_log              | 84.3 ms                                                | 65.5 ms: 1.29x faster                                                 |
| 2to3                     | 348 ms                                                 | 271 ms: 1.29x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 51.4 ms: 1.28x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 20.3 ms: 1.27x faster                                                 |
| sympy_sum                | 196 ms                                                 | 156 ms: 1.26x faster                                                  |
| sqlglot_optimize         | 69.2 ms                                                | 54.8 ms: 1.26x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.13 ms: 1.26x faster                                                 |
| scimark_fft              | 466 ms                                                 | 372 ms: 1.25x faster                                                  |
| pathlib                  | 20.5 ms                                                | 16.3 ms: 1.25x faster                                                 |
| sympy_str                | 346 ms                                                 | 279 ms: 1.24x faster                                                  |
| sympy_expand             | 566 ms                                                 | 471 ms: 1.20x faster                                                  |
| dask                     | 441 ms                                                 | 367 ms: 1.20x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.78 sec: 1.19x faster                                                |
| bench_thread_pool        | 986 us                                                 | 834 us: 1.18x faster                                                  |
| xml_etree_generate       | 99.4 ms                                                | 85.8 ms: 1.16x faster                                                 |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                                  |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 107 ms: 1.08x faster                                                  |
| regex_v8                 | 27.8 ms                                                | 26.2 ms: 1.06x faster                                                 |
| json                     | 5.69 ms                                                | 5.39 ms: 1.06x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 160 ms: 1.05x faster                                                  |
| mdp                      | 2.85 sec                                               | 2.76 sec: 1.03x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.96 us: 1.02x faster                                                 |
| gc_traversal             | 3.62 ms                                                | 3.57 ms: 1.02x faster                                                 |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                                  |
| bench_mp_pool            | 24.0 ms                                                | 23.9 ms: 1.01x faster                                                 |
| pickle_list              | 5.08 us                                                | 5.05 us: 1.01x faster                                                 |
| regex_dna                | 227 ms                                                 | 227 ms: 1.00x slower                                                  |
| async_generators         | 444 ms                                                 | 446 ms: 1.00x slower                                                  |
| asyncio_websockets       | 559 ms                                                 | 566 ms: 1.01x slower                                                  |
| regex_effbot             | 3.63 ms                                                | 3.76 ms: 1.03x slower                                                 |
| unpickle                 | 14.4 us                                                | 15.1 us: 1.05x slower                                                 |
| unpickle_list            | 5.20 us                                                | 5.49 us: 1.06x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.08x slower                                                 |
| pickle                   | 10.7 us                                                | 11.8 us: 1.11x slower                                                 |
| telco                    | 7.27 ms                                                | 8.40 ms: 1.16x slower                                                 |
| pickle_dict              | 29.6 us                                                | 34.7 us: 1.17x slower                                                 |
| coverage                 | 79.4 ms                                                | 93.4 ms: 1.18x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.10 ms: 1.20x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.35x faster                                                          |
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240617-3.14.0a0-ac37a80/bm-20240617-linux-x86_64-python-ac37a806018cc40fafeb-3.14.0a0-ac37a80.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.11x