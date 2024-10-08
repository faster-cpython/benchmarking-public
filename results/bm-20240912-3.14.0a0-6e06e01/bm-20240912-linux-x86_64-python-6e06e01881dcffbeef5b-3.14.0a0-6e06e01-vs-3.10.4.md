# Results vs. 3.10.4

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: linux-x86_64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.41x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.31x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 253 ms: 1.38x faster                                                  |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                |
| html5lib       | 88.9 ms                                                | 62.4 ms: 1.42x faster                                                 |
| tornado_http   | 136 ms                                                 | 89.9 ms: 1.52x faster                                                 |
| Geometric mean | (ref)                                                  | 1.38x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 315 ms: 2.31x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 395 ms: 2.20x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 873 ms: 2.03x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 569 ms: 1.79x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.07x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 89.5 ms: 1.71x faster                                                 |
| float          | 117 ms                                                 | 76.7 ms: 1.53x faster                                                 |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.39x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 129 ms: 1.47x faster                                                  |
| regex_v8       | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                 |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                                  |
| tomli_loads          | 3.14 sec                                               | 2.04 sec: 1.54x faster                                                |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                 |
| xml_etree_process    | 79.1 ms                                                | 59.0 ms: 1.34x faster                                                 |
| xml_etree_generate   | 99.4 ms                                                | 85.4 ms: 1.16x faster                                                 |
| json_loads           | 31.2 us                                                | 27.0 us: 1.16x faster                                                 |
| xml_etree_iterparse  | 115 ms                                                 | 105 ms: 1.10x faster                                                  |
| xml_etree_parse      | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| pickle_list          | 5.08 us                                                | 4.87 us: 1.04x faster                                                 |
| unpickle_list        | 5.20 us                                                | 5.36 us: 1.03x slower                                                 |
| unpickle             | 14.4 us                                                | 14.9 us: 1.04x slower                                                 |
| pickle               | 10.7 us                                                | 11.4 us: 1.07x slower                                                 |
| pickle_dict          | 29.6 us                                                | 33.8 us: 1.14x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 6.99 ms: 1.18x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.7 ms: 1.47x faster                                                 |
| mako            | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                 |
| django_template | 48.2 ms                                                | 34.6 ms: 1.39x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 48.6 ms: 1.36x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 158 us: 3.44x faster                                                  |
| generators               | 80.1 ms                                                | 28.2 ms: 2.84x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.14 ms: 2.52x faster                                                 |
| async_tree_none          | 728 ms                                                 | 315 ms: 2.31x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 395 ms: 2.20x faster                                                  |
| go                       | 240 ms                                                 | 117 ms: 2.05x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 873 ms: 2.03x faster                                                  |
| chaos                    | 115 ms                                                 | 58.3 ms: 1.98x faster                                                 |
| deepcopy_memo            | 58.5 us                                                | 29.5 us: 1.98x faster                                                 |
| asyncio_tcp              | 922 ms                                                 | 471 ms: 1.96x faster                                                  |
| raytrace                 | 507 ms                                                 | 262 ms: 1.94x faster                                                  |
| logging_silent           | 190 ns                                                 | 99.9 ns: 1.90x faster                                                 |
| deepcopy                 | 479 us                                                 | 255 us: 1.88x faster                                                  |
| richards_super           | 94.7 ms                                                | 51.7 ms: 1.83x faster                                                 |
| scimark_sor              | 220 ms                                                 | 122 ms: 1.80x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 71.1 ms: 1.80x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 569 ms: 1.79x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 67.1 ms: 1.76x faster                                                 |
| pylint                   | 551 ms                                                 | 319 ms: 1.73x faster                                                  |
| richards                 | 79.3 ms                                                | 45.8 ms: 1.73x faster                                                 |
| nbody                    | 154 ms                                                 | 89.5 ms: 1.71x faster                                                 |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                                 |
| sqlglot_parse            | 2.17 ms                                                | 1.28 ms: 1.69x faster                                                 |
| hexiom                   | 10.4 ms                                                | 6.16 ms: 1.69x faster                                                 |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.63x faster                                                 |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                                  |
| deepcopy_reduce          | 4.17 us                                                | 2.63 us: 1.59x faster                                                 |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.04 sec: 1.54x faster                                                |
| float                    | 117 ms                                                 | 76.7 ms: 1.53x faster                                                 |
| tornado_http             | 136 ms                                                 | 89.9 ms: 1.52x faster                                                 |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                                 |
| logging_simple           | 8.30 us                                                | 5.49 us: 1.51x faster                                                 |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.51x faster                                                  |
| pyflate                  | 716 ms                                                 | 476 ms: 1.51x faster                                                  |
| logging_format           | 9.09 us                                                | 6.12 us: 1.48x faster                                                 |
| genshi_text              | 31.8 ms                                                | 21.7 ms: 1.47x faster                                                 |
| mako                     | 16.3 ms                                                | 11.1 ms: 1.47x faster                                                 |
| regex_compile            | 188 ms                                                 | 129 ms: 1.47x faster                                                  |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.78 sec: 1.44x faster                                                |
| pprint_pformat           | 2.10 sec                                               | 1.47 sec: 1.43x faster                                                |
| pprint_safe_repr         | 1.02 sec                                               | 714 ms: 1.43x faster                                                  |
| html5lib                 | 88.9 ms                                                | 62.4 ms: 1.42x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.60 ms: 1.41x faster                                                 |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.40x faster                                                |
| django_template          | 48.2 ms                                                | 34.6 ms: 1.39x faster                                                 |
| python_startup           | 14.6 ms                                                | 10.5 ms: 1.39x faster                                                 |
| 2to3                     | 348 ms                                                 | 253 ms: 1.38x faster                                                  |
| thrift                   | 1.07 ms                                                | 779 us: 1.38x faster                                                  |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                                 |
| genshi_xml               | 66.0 ms                                                | 48.6 ms: 1.36x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 59.0 ms: 1.34x faster                                                 |
| sympy_sum                | 196 ms                                                 | 147 ms: 1.34x faster                                                  |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.32x faster                                                  |
| sympy_integrate          | 25.8 ms                                                | 19.5 ms: 1.32x faster                                                 |
| fannkuch                 | 532 ms                                                 | 403 ms: 1.32x faster                                                  |
| nqueens                  | 106 ms                                                 | 80.4 ms: 1.32x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 64.5 ms: 1.31x faster                                                 |
| sqlglot_optimize         | 69.2 ms                                                | 53.2 ms: 1.30x faster                                                 |
| unpack_sequence          | 60.0 ns                                                | 46.3 ns: 1.30x faster                                                 |
| sympy_str                | 346 ms                                                 | 267 ms: 1.29x faster                                                  |
| pathlib                  | 20.5 ms                                                | 15.9 ms: 1.29x faster                                                 |
| scimark_fft              | 466 ms                                                 | 363 ms: 1.28x faster                                                  |
| bench_thread_pool        | 986 us                                                 | 787 us: 1.25x faster                                                  |
| sympy_expand             | 566 ms                                                 | 456 ms: 1.24x faster                                                  |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 85.4 ms: 1.16x faster                                                 |
| json_loads               | 31.2 us                                                | 27.0 us: 1.16x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 24.6 ms: 1.13x faster                                                 |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.11x faster                                                  |
| json                     | 5.69 ms                                                | 5.15 ms: 1.11x faster                                                 |
| xml_etree_iterparse      | 115 ms                                                 | 105 ms: 1.10x faster                                                  |
| xml_etree_parse          | 168 ms                                                 | 156 ms: 1.08x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 2.83 us: 1.07x faster                                                 |
| mdp                      | 2.85 sec                                               | 2.69 sec: 1.06x faster                                                |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                                  |
| pickle_list              | 5.08 us                                                | 4.87 us: 1.04x faster                                                 |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                  |
| async_generators         | 444 ms                                                 | 437 ms: 1.01x faster                                                  |
| unpickle_list            | 5.20 us                                                | 5.36 us: 1.03x slower                                                 |
| unpickle                 | 14.4 us                                                | 14.9 us: 1.04x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 1.73 ms: 1.07x slower                                                 |
| pickle                   | 10.7 us                                                | 11.4 us: 1.07x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 3.90 ms: 1.08x slower                                                 |
| coverage                 | 79.4 ms                                                | 85.7 ms: 1.08x slower                                                 |
| pickle_dict              | 29.6 us                                                | 33.8 us: 1.14x slower                                                 |
| telco                    | 7.27 ms                                                | 8.46 ms: 1.16x slower                                                 |
| python_startup_no_site   | 5.93 ms                                                | 6.99 ms: 1.18x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                          |

Benchmark hidden because not significant (3): bench_mp_pool, asyncio_websockets, regex_effbot
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-linux-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.35x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.31x

# Memory
- memory change: 1.11x