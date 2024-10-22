# Results vs. 3.10.4

- fork: brandtbucher
- ref: confidence
- machine: linux-x86_64
- commit hash: d2146e9
- commit date: 2024-09-06
- overall geometric mean: 1.38x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 276 ms: 1.26x faster                                              |
| docutils       | 3.30 sec                                               | 3.00 sec: 1.10x faster                                            |
| html5lib       | 88.9 ms                                                | 62.3 ms: 1.43x faster                                             |
| tornado_http   | 136 ms                                                 | 96.1 ms: 1.42x faster                                             |
| Geometric mean | (ref)                                                  | 1.29x faster                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 326 ms: 2.24x faster                                              |
| async_tree_memoization  | 870 ms                                                 | 396 ms: 2.20x faster                                              |
| async_tree_io           | 1.77 sec                                               | 929 ms: 1.90x faster                                              |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 568 ms: 1.79x faster                                              |
| Geometric mean          | (ref)                                                  | 2.02x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 81.2 ms: 1.89x faster                                             |
| float          | 117 ms                                                 | 70.7 ms: 1.66x faster                                             |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                              |
| Geometric mean | (ref)                                                  | 1.48x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 142 ms: 1.33x faster                                              |
| regex_v8       | 27.8 ms                                                | 24.0 ms: 1.16x faster                                             |
| regex_dna      | 227 ms                                                 | 210 ms: 1.08x faster                                              |
| regex_effbot   | 3.63 ms                                                | 3.50 ms: 1.04x faster                                             |
| Geometric mean | (ref)                                                  | 1.15x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.93 sec: 1.63x faster                                            |
| pickle_pure_python   | 484 us                                                 | 304 us: 1.59x faster                                              |
| unpickle_pure_python | 331 us                                                 | 213 us: 1.55x faster                                              |
| xml_etree_process    | 79.1 ms                                                | 55.1 ms: 1.44x faster                                             |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                             |
| xml_etree_generate   | 99.4 ms                                                | 78.3 ms: 1.27x faster                                             |
| xml_etree_iterparse  | 115 ms                                                 | 98.8 ms: 1.17x faster                                             |
| xml_etree_parse      | 168 ms                                                 | 148 ms: 1.14x faster                                              |
| json_loads           | 31.2 us                                                | 28.6 us: 1.09x faster                                             |
| unpickle             | 14.4 us                                                | 14.8 us: 1.03x slower                                             |
| unpickle_list        | 5.20 us                                                | 5.40 us: 1.04x slower                                             |
| pickle_list          | 5.08 us                                                | 5.29 us: 1.04x slower                                             |
| pickle               | 10.7 us                                                | 11.6 us: 1.09x slower                                             |
| pickle_dict          | 29.6 us                                                | 34.1 us: 1.15x slower                                             |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.7 ms: 1.37x faster                                             |
| python_startup_no_site | 5.93 ms                                                | 7.16 ms: 1.21x slower                                             |
| Geometric mean         | (ref)                                                  | 1.06x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.79 ms: 1.67x faster                                             |
| django_template | 48.2 ms                                                | 35.5 ms: 1.36x faster                                             |
| genshi_text     | 31.8 ms                                                | 24.4 ms: 1.30x faster                                             |
| genshi_xml      | 66.0 ms                                                | 58.7 ms: 1.12x faster                                             |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 164 us: 3.32x faster                                              |
| deltablue                | 7.91 ms                                                | 3.20 ms: 2.47x faster                                             |
| generators               | 80.1 ms                                                | 33.2 ms: 2.41x faster                                             |
| async_tree_none          | 728 ms                                                 | 326 ms: 2.24x faster                                              |
| richards_super           | 94.7 ms                                                | 42.9 ms: 2.21x faster                                             |
| async_tree_memoization   | 870 ms                                                 | 396 ms: 2.20x faster                                              |
| deepcopy_memo            | 58.5 us                                                | 27.0 us: 2.16x faster                                             |
| richards                 | 79.3 ms                                                | 38.7 ms: 2.05x faster                                             |
| chaos                    | 115 ms                                                 | 58.3 ms: 1.98x faster                                             |
| crypto_pyaes             | 128 ms                                                 | 66.4 ms: 1.93x faster                                             |
| async_tree_io            | 1.77 sec                                               | 929 ms: 1.90x faster                                              |
| scimark_sor              | 220 ms                                                 | 116 ms: 1.90x faster                                              |
| asyncio_tcp              | 922 ms                                                 | 486 ms: 1.90x faster                                              |
| nbody                    | 154 ms                                                 | 81.2 ms: 1.89x faster                                             |
| scimark_monte_carlo      | 118 ms                                                 | 62.9 ms: 1.88x faster                                             |
| logging_silent           | 190 ns                                                 | 101 ns: 1.88x faster                                              |
| raytrace                 | 507 ms                                                 | 275 ms: 1.85x faster                                              |
| go                       | 240 ms                                                 | 131 ms: 1.83x faster                                              |
| deepcopy                 | 479 us                                                 | 267 us: 1.80x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 568 ms: 1.79x faster                                              |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                             |
| pyflate                  | 716 ms                                                 | 424 ms: 1.69x faster                                              |
| mako                     | 16.3 ms                                                | 9.79 ms: 1.67x faster                                             |
| spectral_norm            | 170 ms                                                 | 103 ms: 1.66x faster                                              |
| float                    | 117 ms                                                 | 70.7 ms: 1.66x faster                                             |
| tomli_loads              | 3.14 sec                                               | 1.93 sec: 1.63x faster                                            |
| sqlglot_parse            | 2.17 ms                                                | 1.33 ms: 1.63x faster                                             |
| scimark_lu               | 176 ms                                                 | 110 ms: 1.60x faster                                              |
| pickle_pure_python       | 484 us                                                 | 304 us: 1.59x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 213 us: 1.55x faster                                              |
| deepcopy_reduce          | 4.17 us                                                | 2.70 us: 1.55x faster                                             |
| coroutines               | 35.1 ms                                                | 22.7 ms: 1.54x faster                                             |
| sqlglot_transpile        | 2.57 ms                                                | 1.68 ms: 1.53x faster                                             |
| hexiom                   | 10.4 ms                                                | 6.84 ms: 1.52x faster                                             |
| logging_simple           | 8.30 us                                                | 5.52 us: 1.51x faster                                             |
| scimark_fft              | 466 ms                                                 | 312 ms: 1.49x faster                                              |
| logging_format           | 9.09 us                                                | 6.12 us: 1.49x faster                                             |
| pylint                   | 551 ms                                                 | 373 ms: 1.48x faster                                              |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.43 ms: 1.46x faster                                             |
| pprint_safe_repr         | 1.02 sec                                               | 700 ms: 1.45x faster                                              |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.45x faster                                            |
| xml_etree_process        | 79.1 ms                                                | 55.1 ms: 1.44x faster                                             |
| fannkuch                 | 532 ms                                                 | 372 ms: 1.43x faster                                              |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.80 sec: 1.43x faster                                            |
| html5lib                 | 88.9 ms                                                | 62.3 ms: 1.43x faster                                             |
| tornado_http             | 136 ms                                                 | 96.1 ms: 1.42x faster                                             |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                             |
| python_startup           | 14.6 ms                                                | 10.7 ms: 1.37x faster                                             |
| thrift                   | 1.07 ms                                                | 787 us: 1.36x faster                                              |
| django_template          | 48.2 ms                                                | 35.5 ms: 1.36x faster                                             |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.34x faster                                            |
| regex_compile            | 188 ms                                                 | 142 ms: 1.33x faster                                              |
| genshi_text              | 31.8 ms                                                | 24.4 ms: 1.30x faster                                             |
| pathlib                  | 20.5 ms                                                | 16.0 ms: 1.28x faster                                             |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                              |
| xml_etree_generate       | 99.4 ms                                                | 78.3 ms: 1.27x faster                                             |
| 2to3                     | 348 ms                                                 | 276 ms: 1.26x faster                                              |
| nqueens                  | 106 ms                                                 | 85.1 ms: 1.24x faster                                             |
| dulwich_log              | 84.3 ms                                                | 69.4 ms: 1.22x faster                                             |
| sqlglot_optimize         | 69.2 ms                                                | 58.3 ms: 1.19x faster                                             |
| bench_thread_pool        | 986 us                                                 | 839 us: 1.18x faster                                              |
| xml_etree_iterparse      | 115 ms                                                 | 98.8 ms: 1.17x faster                                             |
| regex_v8                 | 27.8 ms                                                | 24.0 ms: 1.16x faster                                             |
| sympy_str                | 346 ms                                                 | 302 ms: 1.14x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 148 ms: 1.14x faster                                              |
| sympy_integrate          | 25.8 ms                                                | 22.8 ms: 1.13x faster                                             |
| sympy_sum                | 196 ms                                                 | 174 ms: 1.13x faster                                              |
| genshi_xml               | 66.0 ms                                                | 58.7 ms: 1.12x faster                                             |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                              |
| sympy_expand             | 566 ms                                                 | 511 ms: 1.11x faster                                              |
| docutils                 | 3.30 sec                                               | 3.00 sec: 1.10x faster                                            |
| json_loads               | 31.2 us                                                | 28.6 us: 1.09x faster                                             |
| sqlite_synth             | 3.02 us                                                | 2.77 us: 1.09x faster                                             |
| regex_dna                | 227 ms                                                 | 210 ms: 1.08x faster                                              |
| json                     | 5.69 ms                                                | 5.35 ms: 1.06x faster                                             |
| mdp                      | 2.85 sec                                               | 2.73 sec: 1.04x faster                                            |
| regex_effbot             | 3.63 ms                                                | 3.50 ms: 1.04x faster                                             |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                              |
| asyncio_websockets       | 559 ms                                                 | 555 ms: 1.01x faster                                              |
| unpickle                 | 14.4 us                                                | 14.8 us: 1.03x slower                                             |
| async_generators         | 444 ms                                                 | 459 ms: 1.03x slower                                              |
| unpickle_list            | 5.20 us                                                | 5.40 us: 1.04x slower                                             |
| gc_traversal             | 3.62 ms                                                | 3.77 ms: 1.04x slower                                             |
| pickle_list              | 5.08 us                                                | 5.29 us: 1.04x slower                                             |
| telco                    | 7.27 ms                                                | 7.83 ms: 1.08x slower                                             |
| pickle                   | 10.7 us                                                | 11.6 us: 1.09x slower                                             |
| coverage                 | 79.4 ms                                                | 86.8 ms: 1.09x slower                                             |
| create_gc_cycles         | 1.62 ms                                                | 1.77 ms: 1.09x slower                                             |
| pickle_dict              | 29.6 us                                                | 34.1 us: 1.15x slower                                             |
| python_startup_no_site   | 5.93 ms                                                | 7.16 ms: 1.21x slower                                             |
| unpack_sequence          | 60.0 ns                                                | 109 ns: 1.81x slower                                              |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240906-3.14.0a0-d2146e9-JIT/bm-20240906-linux-x86_64-brandtbucher-confidence-3.14.0a0-d2146e9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.22x