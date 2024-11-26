# Results vs. 3.10.4

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: linux-x86_64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.423x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 276 ms: 1.26x faster                                                  |
| docutils       | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                |
| html5lib       | 88.9 ms                                                | 64.5 ms: 1.38x faster                                                 |
| tornado_http   | 136 ms                                                 | 94.6 ms: 1.44x faster                                                 |
| Geometric mean | (ref)                                                  | 1.29x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 321 ms: 2.27x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 401 ms: 2.17x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 857 ms: 2.06x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 575 ms: 1.77x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.06x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 80.2 ms: 1.91x faster                                                 |
| float          | 117 ms                                                 | 70.0 ms: 1.67x faster                                                 |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.49x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 141 ms: 1.33x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.12x faster                                                 |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 3.80 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                |
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 55.6 ms: 1.42x faster                                                 |
| json_dumps           | 14.2 ms                                                | 10.1 ms: 1.40x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 78.7 ms: 1.26x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 97.9 ms: 1.18x faster                                                 |
| json_loads           | 31.2 us                                                | 26.7 us: 1.17x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 145 ms: 1.16x faster                                                  |
| unpickle             | 14.4 us                                                | 14.6 us: 1.01x slower                                                 |
| pickle_list          | 5.08 us                                                | 5.17 us: 1.02x slower                                                 |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                                 |
| pickle_dict          | 29.6 us                                                | 34.5 us: 1.17x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.88 ms: 1.65x faster                                                 |
| django_template | 48.2 ms                                                | 35.3 ms: 1.36x faster                                                 |
| genshi_text     | 31.8 ms                                                | 25.4 ms: 1.25x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 60.0 ms: 1.10x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 166 us: 3.28x faster                                                  |
| deltablue                | 7.91 ms                                                | 3.21 ms: 2.47x faster                                                 |
| generators               | 80.1 ms                                                | 32.8 ms: 2.44x faster                                                 |
| async_tree_none          | 728 ms                                                 | 321 ms: 2.27x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 401 ms: 2.17x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 27.2 us: 2.15x faster                                                 |
| richards_super           | 94.7 ms                                                | 45.6 ms: 2.08x faster                                                 |
| async_tree_io            | 1.77 sec                                               | 857 ms: 2.06x faster                                                  |
| chaos                    | 115 ms                                                 | 58.0 ms: 1.99x faster                                                 |
| richards                 | 79.3 ms                                                | 39.9 ms: 1.99x faster                                                 |
| crypto_pyaes             | 128 ms                                                 | 65.8 ms: 1.94x faster                                                 |
| nbody                    | 154 ms                                                 | 80.2 ms: 1.91x faster                                                 |
| scimark_monte_carlo      | 118 ms                                                 | 63.0 ms: 1.88x faster                                                 |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.88x faster                                                  |
| deepcopy                 | 479 us                                                 | 258 us: 1.86x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 498 ms: 1.85x faster                                                  |
| go                       | 240 ms                                                 | 131 ms: 1.84x faster                                                  |
| logging_silent           | 190 ns                                                 | 104 ns: 1.82x faster                                                  |
| raytrace                 | 507 ms                                                 | 281 ms: 1.81x faster                                                  |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 575 ms: 1.77x faster                                                  |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                                 |
| spectral_norm            | 170 ms                                                 | 98.4 ms: 1.73x faster                                                 |
| float                    | 117 ms                                                 | 70.0 ms: 1.67x faster                                                 |
| mako                     | 16.3 ms                                                | 9.88 ms: 1.65x faster                                                 |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                                |
| sqlglot_parse            | 2.17 ms                                                | 1.35 ms: 1.61x faster                                                 |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.60x faster                                                  |
| pyflate                  | 716 ms                                                 | 448 ms: 1.60x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.68 us: 1.56x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.21 ms: 1.54x faster                                                 |
| coroutines               | 35.1 ms                                                | 22.9 ms: 1.53x faster                                                 |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                  |
| sqlglot_transpile        | 2.57 ms                                                | 1.69 ms: 1.52x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.86 ms: 1.51x faster                                                 |
| scimark_fft              | 466 ms                                                 | 308 ms: 1.51x faster                                                  |
| pylint                   | 551 ms                                                 | 375 ms: 1.47x faster                                                  |
| logging_format           | 9.09 us                                                | 6.24 us: 1.46x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.75 us: 1.44x faster                                                 |
| tornado_http             | 136 ms                                                 | 94.6 ms: 1.44x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 55.6 ms: 1.42x faster                                                 |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.81 sec: 1.42x faster                                                |
| fannkuch                 | 532 ms                                                 | 375 ms: 1.42x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.1 ms: 1.40x faster                                                 |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.38x faster                                                 |
| html5lib                 | 88.9 ms                                                | 64.5 ms: 1.38x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.15 sec: 1.37x faster                                                |
| django_template          | 48.2 ms                                                | 35.3 ms: 1.36x faster                                                 |
| pprint_safe_repr         | 1.02 sec                                               | 748 ms: 1.36x faster                                                  |
| thrift                   | 1.07 ms                                                | 790 us: 1.36x faster                                                  |
| regex_compile            | 188 ms                                                 | 141 ms: 1.33x faster                                                  |
| pprint_pformat           | 2.10 sec                                               | 1.60 sec: 1.32x faster                                                |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.28x faster                                                 |
| xml_etree_generate       | 99.4 ms                                                | 78.7 ms: 1.26x faster                                                 |
| sqlglot_normalize        | 143 ms                                                 | 113 ms: 1.26x faster                                                  |
| 2to3                     | 348 ms                                                 | 276 ms: 1.26x faster                                                  |
| genshi_text              | 31.8 ms                                                | 25.4 ms: 1.25x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 67.8 ms: 1.24x faster                                                 |
| nqueens                  | 106 ms                                                 | 85.5 ms: 1.24x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 58.2 ms: 1.19x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 97.9 ms: 1.18x faster                                                 |
| bench_thread_pool        | 986 us                                                 | 839 us: 1.18x faster                                                  |
| json_loads               | 31.2 us                                                | 26.7 us: 1.17x faster                                                 |
| xml_etree_parse          | 168 ms                                                 | 145 ms: 1.16x faster                                                  |
| sympy_str                | 346 ms                                                 | 299 ms: 1.16x faster                                                  |
| json                     | 5.69 ms                                                | 4.94 ms: 1.15x faster                                                 |
| sympy_sum                | 196 ms                                                 | 173 ms: 1.14x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.12x faster                                                 |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                                  |
| sympy_expand             | 566 ms                                                 | 506 ms: 1.12x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.96 sec: 1.11x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.74 us: 1.10x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 60.0 ms: 1.10x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.66 sec: 1.07x faster                                                |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                  |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                                  |
| unpickle                 | 14.4 us                                                | 14.6 us: 1.01x slower                                                 |
| pickle_list              | 5.08 us                                                | 5.17 us: 1.02x slower                                                 |
| async_generators         | 444 ms                                                 | 461 ms: 1.04x slower                                                  |
| regex_effbot             | 3.63 ms                                                | 3.80 ms: 1.05x slower                                                 |
| coverage                 | 79.4 ms                                                | 85.2 ms: 1.07x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.07x slower                                                 |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 3.94 ms: 1.09x slower                                                 |
| telco                    | 7.27 ms                                                | 8.05 ms: 1.11x slower                                                 |
| pickle_dict              | 29.6 us                                                | 34.5 us: 1.17x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 7.07 ms: 1.19x slower                                                 |
| unpack_sequence          | 60.0 ns                                                | 112 ns: 1.87x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                          |

Benchmark hidden because not significant (2): unpickle_list, bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240912-3.14.0a0-6e06e01-JIT/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.423x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.21x