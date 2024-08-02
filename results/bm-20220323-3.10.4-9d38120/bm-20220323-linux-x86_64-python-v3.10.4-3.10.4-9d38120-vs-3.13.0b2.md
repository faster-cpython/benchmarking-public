# Results vs. 3.13.0b2

- fork: python
- ref: v3.10.4
- machine: linux-x86_64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.32x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x slower
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 348 ms: 1.27x slower                                   |
| chameleon      | 7.22 ms                                                    | 9.68 ms: 1.34x slower                                  |
| docutils       | 2.83 sec                                                   | 3.30 sec: 1.17x slower                                 |
| html5lib       | 67.2 ms                                                    | 88.9 ms: 1.32x slower                                  |
| tornado_http   | 94.6 ms                                                    | 136 ms: 1.44x slower                                   |
| Geometric mean | (ref)                                                      | 1.31x slower                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-------------------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_cpu_io_mixed | 611 ms                                                     | 1.02 sec: 1.66x slower                                 |
| async_tree_memoization  | 463 ms                                                     | 870 ms: 1.88x slower                                   |
| async_tree_io           | 939 ms                                                     | 1.77 sec: 1.88x slower                                 |
| async_tree_none         | 378 ms                                                     | 728 ms: 1.92x slower                                   |
| Geometric mean          | (ref)                                                      | 1.83x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 191 ms                                                     | 191 ms: 1.00x faster                                   |
| float          | 78.9 ms                                                    | 117 ms: 1.48x slower                                   |
| nbody          | 88.3 ms                                                    | 154 ms: 1.74x slower                                   |
| Geometric mean | (ref)                                                      | 1.37x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 227 ms: 1.02x slower                                   |
| regex_v8       | 25.1 ms                                                    | 27.8 ms: 1.11x slower                                  |
| regex_compile  | 137 ms                                                     | 188 ms: 1.38x slower                                   |
| Geometric mean | (ref)                                                      | 1.11x slower                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| pickle_dict          | 34.8 us                                                    | 29.6 us: 1.18x faster                                  |
| pickle               | 11.5 us                                                    | 10.7 us: 1.08x faster                                  |
| unpickle             | 15.1 us                                                    | 14.4 us: 1.05x faster                                  |
| unpickle_list        | 5.34 us                                                    | 5.20 us: 1.03x faster                                  |
| pickle_list          | 5.11 us                                                    | 5.08 us: 1.01x faster                                  |
| xml_etree_parse      | 162 ms                                                     | 168 ms: 1.04x slower                                   |
| xml_etree_iterparse  | 107 ms                                                     | 115 ms: 1.07x slower                                   |
| json_loads           | 28.9 us                                                    | 31.2 us: 1.08x slower                                  |
| xml_etree_generate   | 87.4 ms                                                    | 99.4 ms: 1.14x slower                                  |
| xml_etree_process    | 61.2 ms                                                    | 79.1 ms: 1.29x slower                                  |
| json_dumps           | 10.7 ms                                                    | 14.2 ms: 1.32x slower                                  |
| tomli_loads          | 2.12 sec                                                   | 3.14 sec: 1.48x slower                                 |
| unpickle_pure_python | 218 us                                                     | 331 us: 1.52x slower                                   |
| pickle_pure_python   | 305 us                                                     | 484 us: 1.59x slower                                   |
| Geometric mean       | (ref)                                                      | 1.14x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                    | 5.93 ms: 1.20x faster                                  |
| python_startup         | 10.8 ms                                                    | 14.6 ms: 1.36x slower                                  |
| Geometric mean         | (ref)                                                      | 1.06x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.6 ms                                                    | 66.0 ms: 1.28x slower                                  |
| genshi_text     | 23.7 ms                                                    | 31.8 ms: 1.34x slower                                  |
| django_template | 34.8 ms                                                    | 48.2 ms: 1.38x slower                                  |
| mako            | 11.2 ms                                                    | 16.3 ms: 1.45x slower                                  |
| Geometric mean  | (ref)                                                      | 1.36x slower                                           |

All benchmarks:
===============

| Benchmark                | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:----------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site   | 7.11 ms                                                    | 5.93 ms: 1.20x faster                                  |
| pickle_dict              | 34.8 us                                                    | 29.6 us: 1.18x faster                                  |
| coverage                 | 93.1 ms                                                    | 79.4 ms: 1.17x faster                                  |
| telco                    | 8.41 ms                                                    | 7.27 ms: 1.16x faster                                  |
| create_gc_cycles         | 1.82 ms                                                    | 1.62 ms: 1.12x faster                                  |
| gc_traversal             | 3.98 ms                                                    | 3.62 ms: 1.10x faster                                  |
| pickle                   | 11.5 us                                                    | 10.7 us: 1.08x faster                                  |
| unpickle                 | 15.1 us                                                    | 14.4 us: 1.05x faster                                  |
| flaskblogging            | 9.01 ms                                                    | 8.58 ms: 1.05x faster                                  |
| unpickle_list            | 5.34 us                                                    | 5.20 us: 1.03x faster                                  |
| asyncio_websockets       | 567 ms                                                     | 559 ms: 1.01x faster                                   |
| pickle_list              | 5.11 us                                                    | 5.08 us: 1.01x faster                                  |
| pidigits                 | 191 ms                                                     | 191 ms: 1.00x faster                                   |
| async_generators         | 442 ms                                                     | 444 ms: 1.00x slower                                   |
| bench_mp_pool            | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                  |
| sqlite_synth             | 2.99 us                                                    | 3.02 us: 1.01x slower                                  |
| mdp                      | 2.79 sec                                                   | 2.85 sec: 1.02x slower                                 |
| regex_dna                | 221 ms                                                     | 227 ms: 1.02x slower                                   |
| xml_etree_parse          | 162 ms                                                     | 168 ms: 1.04x slower                                   |
| json                     | 5.31 ms                                                    | 5.69 ms: 1.07x slower                                  |
| xml_etree_iterparse      | 107 ms                                                     | 115 ms: 1.07x slower                                   |
| json_loads               | 28.9 us                                                    | 31.2 us: 1.08x slower                                  |
| meteor_contest           | 110 ms                                                     | 120 ms: 1.09x slower                                   |
| regex_v8                 | 25.1 ms                                                    | 27.8 ms: 1.11x slower                                  |
| xml_etree_generate       | 87.4 ms                                                    | 99.4 ms: 1.14x slower                                  |
| docutils                 | 2.83 sec                                                   | 3.30 sec: 1.17x slower                                 |
| pathlib                  | 17.3 ms                                                    | 20.5 ms: 1.18x slower                                  |
| bench_thread_pool        | 834 us                                                     | 986 us: 1.18x slower                                   |
| scimark_fft              | 392 ms                                                     | 466 ms: 1.19x slower                                   |
| dask                     | 369 ms                                                     | 441 ms: 1.19x slower                                   |
| sympy_expand             | 473 ms                                                     | 566 ms: 1.20x slower                                   |
| gunicorn                 | 1.28 ms                                                    | 1.53 ms: 1.20x slower                                  |
| mypy2                    | 742 ms                                                     | 894 ms: 1.21x slower                                   |
| aiohttp                  | 1.18 ms                                                    | 1.44 ms: 1.22x slower                                  |
| djangocms                | 31.5 us                                                    | 38.4 us: 1.22x slower                                  |
| sympy_str                | 282 ms                                                     | 346 ms: 1.22x slower                                   |
| scimark_sparse_mat_mult  | 5.27 ms                                                    | 6.47 ms: 1.23x slower                                  |
| deepcopy_reduce          | 3.35 us                                                    | 4.17 us: 1.25x slower                                  |
| sqlglot_optimize         | 55.5 ms                                                    | 69.2 ms: 1.25x slower                                  |
| dulwich_log              | 67.2 ms                                                    | 84.3 ms: 1.26x slower                                  |
| sympy_integrate          | 20.5 ms                                                    | 25.8 ms: 1.26x slower                                  |
| sympy_sum                | 156 ms                                                     | 196 ms: 1.26x slower                                   |
| 2to3                     | 274 ms                                                     | 348 ms: 1.27x slower                                   |
| genshi_xml               | 51.6 ms                                                    | 66.0 ms: 1.28x slower                                  |
| xml_etree_process        | 61.2 ms                                                    | 79.1 ms: 1.29x slower                                  |
| sqlglot_normalize        | 110 ms                                                     | 143 ms: 1.30x slower                                   |
| nqueens                  | 81.4 ms                                                    | 106 ms: 1.30x slower                                   |
| thrift                   | 823 us                                                     | 1.07 ms: 1.30x slower                                  |
| deepcopy                 | 367 us                                                     | 479 us: 1.30x slower                                   |
| json_dumps               | 10.7 ms                                                    | 14.2 ms: 1.32x slower                                  |
| html5lib                 | 67.2 ms                                                    | 88.9 ms: 1.32x slower                                  |
| fannkuch                 | 402 ms                                                     | 532 ms: 1.32x slower                                   |
| chameleon                | 7.22 ms                                                    | 9.68 ms: 1.34x slower                                  |
| pprint_safe_repr         | 758 ms                                                     | 1.02 sec: 1.34x slower                                 |
| genshi_text              | 23.7 ms                                                    | 31.8 ms: 1.34x slower                                  |
| pprint_pformat           | 1.56 sec                                                   | 2.10 sec: 1.35x slower                                 |
| python_startup           | 10.8 ms                                                    | 14.6 ms: 1.36x slower                                  |
| pycparser                | 1.16 sec                                                   | 1.58 sec: 1.36x slower                                 |
| regex_compile            | 137 ms                                                     | 188 ms: 1.38x slower                                   |
| django_template          | 34.8 ms                                                    | 48.2 ms: 1.38x slower                                  |
| asyncio_tcp_ssl          | 1.84 sec                                                   | 2.57 sec: 1.40x slower                                 |
| logging_format           | 6.47 us                                                    | 9.09 us: 1.40x slower                                  |
| tornado_http             | 94.6 ms                                                    | 136 ms: 1.44x slower                                   |
| logging_simple           | 5.74 us                                                    | 8.30 us: 1.45x slower                                  |
| scimark_lu               | 122 ms                                                     | 176 ms: 1.45x slower                                   |
| mako                     | 11.2 ms                                                    | 16.3 ms: 1.45x slower                                  |
| spectral_norm            | 116 ms                                                     | 170 ms: 1.46x slower                                   |
| deepcopy_memo            | 39.7 us                                                    | 58.5 us: 1.47x slower                                  |
| pyflate                  | 484 ms                                                     | 716 ms: 1.48x slower                                   |
| tomli_loads              | 2.12 sec                                                   | 3.14 sec: 1.48x slower                                 |
| float                    | 78.9 ms                                                    | 117 ms: 1.48x slower                                   |
| coroutines               | 23.2 ms                                                    | 35.1 ms: 1.51x slower                                  |
| unpickle_pure_python     | 218 us                                                     | 331 us: 1.52x slower                                   |
| richards                 | 50.9 ms                                                    | 79.3 ms: 1.56x slower                                  |
| sqlglot_transpile        | 1.63 ms                                                    | 2.57 ms: 1.57x slower                                  |
| pickle_pure_python       | 305 us                                                     | 484 us: 1.59x slower                                   |
| sqlglot_parse            | 1.32 ms                                                    | 2.17 ms: 1.64x slower                                  |
| crypto_pyaes             | 77.5 ms                                                    | 128 ms: 1.65x slower                                   |
| richards_super           | 57.4 ms                                                    | 94.7 ms: 1.65x slower                                  |
| hexiom                   | 6.30 ms                                                    | 10.4 ms: 1.65x slower                                  |
| go                       | 145 ms                                                     | 240 ms: 1.66x slower                                   |
| async_tree_cpu_io_mixed  | 611 ms                                                     | 1.02 sec: 1.66x slower                                 |
| scimark_monte_carlo      | 69.2 ms                                                    | 118 ms: 1.71x slower                                   |
| scimark_sor              | 127 ms                                                     | 220 ms: 1.72x slower                                   |
| comprehensions           | 16.6 us                                                    | 28.8 us: 1.73x slower                                  |
| pylint                   | 317 ms                                                     | 551 ms: 1.74x slower                                   |
| nbody                    | 88.3 ms                                                    | 154 ms: 1.74x slower                                   |
| logging_silent           | 105 ns                                                     | 190 ns: 1.81x slower                                   |
| asyncio_tcp              | 508 ms                                                     | 922 ms: 1.81x slower                                   |
| async_tree_memoization   | 463 ms                                                     | 870 ms: 1.88x slower                                   |
| chaos                    | 61.3 ms                                                    | 115 ms: 1.88x slower                                   |
| async_tree_io            | 939 ms                                                     | 1.77 sec: 1.88x slower                                 |
| raytrace                 | 267 ms                                                     | 507 ms: 1.90x slower                                   |
| async_tree_none          | 378 ms                                                     | 728 ms: 1.92x slower                                   |
| deltablue                | 3.25 ms                                                    | 7.91 ms: 2.43x slower                                  |
| generators               | 29.6 ms                                                    | 80.1 ms: 2.70x slower                                  |
| typing_runtime_protocols | 165 us                                                     | 544 us: 3.30x slower                                   |
| Geometric mean           | (ref)                                                      | 1.32x slower                                           |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.27x
- 95% likely to have a slowdown of 1.26x
- 99% likely to have a slowdown of 1.24x

# Memory
- memory change: 0.91x