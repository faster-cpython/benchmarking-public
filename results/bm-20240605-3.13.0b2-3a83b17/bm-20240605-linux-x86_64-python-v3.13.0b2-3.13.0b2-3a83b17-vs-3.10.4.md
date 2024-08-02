# Results vs. 3.10.4

- fork: python
- ref: v3.13.0b2
- machine: linux-x86_64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.32x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 274 ms: 1.27x faster                                       |
| chameleon      | 9.68 ms                                                | 7.22 ms: 1.34x faster                                      |
| docutils       | 3.30 sec                                               | 2.83 sec: 1.17x faster                                     |
| html5lib       | 88.9 ms                                                | 67.2 ms: 1.32x faster                                      |
| tornado_http   | 136 ms                                                 | 94.6 ms: 1.44x faster                                      |
| Geometric mean | (ref)                                                  | 1.31x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 378 ms: 1.92x faster                                       |
| async_tree_io           | 1.77 sec                                               | 939 ms: 1.88x faster                                       |
| async_tree_memoization  | 870 ms                                                 | 463 ms: 1.88x faster                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 611 ms: 1.66x faster                                       |
| Geometric mean          | (ref)                                                  | 1.83x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 154 ms                                                 | 88.3 ms: 1.74x faster                                      |
| float          | 117 ms                                                 | 78.9 ms: 1.48x faster                                      |
| pidigits       | 191 ms                                                 | 191 ms: 1.00x slower                                       |
| Geometric mean | (ref)                                                  | 1.37x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 137 ms: 1.38x faster                                       |
| regex_v8       | 27.8 ms                                                | 25.1 ms: 1.11x faster                                      |
| regex_dna      | 227 ms                                                 | 221 ms: 1.02x faster                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 305 us: 1.59x faster                                       |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                       |
| tomli_loads          | 3.14 sec                                               | 2.12 sec: 1.48x faster                                     |
| json_dumps           | 14.2 ms                                                | 10.7 ms: 1.32x faster                                      |
| xml_etree_process    | 79.1 ms                                                | 61.2 ms: 1.29x faster                                      |
| xml_etree_generate   | 99.4 ms                                                | 87.4 ms: 1.14x faster                                      |
| json_loads           | 31.2 us                                                | 28.9 us: 1.08x faster                                      |
| xml_etree_iterparse  | 115 ms                                                 | 107 ms: 1.07x faster                                       |
| xml_etree_parse      | 168 ms                                                 | 162 ms: 1.04x faster                                       |
| pickle_list          | 5.08 us                                                | 5.11 us: 1.01x slower                                      |
| unpickle_list        | 5.20 us                                                | 5.34 us: 1.03x slower                                      |
| unpickle             | 14.4 us                                                | 15.1 us: 1.05x slower                                      |
| pickle               | 10.7 us                                                | 11.5 us: 1.08x slower                                      |
| pickle_dict          | 29.6 us                                                | 34.8 us: 1.18x slower                                      |
| Geometric mean       | (ref)                                                  | 1.14x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.8 ms: 1.36x faster                                      |
| python_startup_no_site | 5.93 ms                                                | 7.11 ms: 1.20x slower                                      |
| Geometric mean         | (ref)                                                  | 1.06x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.2 ms: 1.45x faster                                      |
| django_template | 48.2 ms                                                | 34.8 ms: 1.38x faster                                      |
| genshi_text     | 31.8 ms                                                | 23.7 ms: 1.34x faster                                      |
| genshi_xml      | 66.0 ms                                                | 51.6 ms: 1.28x faster                                      |
| Geometric mean  | (ref)                                                  | 1.36x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.30x faster                                       |
| generators               | 80.1 ms                                                | 29.6 ms: 2.70x faster                                      |
| deltablue                | 7.91 ms                                                | 3.25 ms: 2.43x faster                                      |
| async_tree_none          | 728 ms                                                 | 378 ms: 1.92x faster                                       |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                       |
| async_tree_io            | 1.77 sec                                               | 939 ms: 1.88x faster                                       |
| chaos                    | 115 ms                                                 | 61.3 ms: 1.88x faster                                      |
| async_tree_memoization   | 870 ms                                                 | 463 ms: 1.88x faster                                       |
| asyncio_tcp              | 922 ms                                                 | 508 ms: 1.81x faster                                       |
| logging_silent           | 190 ns                                                 | 105 ns: 1.81x faster                                       |
| nbody                    | 154 ms                                                 | 88.3 ms: 1.74x faster                                      |
| pylint                   | 551 ms                                                 | 317 ms: 1.74x faster                                       |
| comprehensions           | 28.8 us                                                | 16.6 us: 1.73x faster                                      |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.72x faster                                       |
| scimark_monte_carlo      | 118 ms                                                 | 69.2 ms: 1.71x faster                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 611 ms: 1.66x faster                                       |
| go                       | 240 ms                                                 | 145 ms: 1.66x faster                                       |
| hexiom                   | 10.4 ms                                                | 6.30 ms: 1.65x faster                                      |
| richards_super           | 94.7 ms                                                | 57.4 ms: 1.65x faster                                      |
| crypto_pyaes             | 128 ms                                                 | 77.5 ms: 1.65x faster                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.32 ms: 1.64x faster                                      |
| pickle_pure_python       | 484 us                                                 | 305 us: 1.59x faster                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.57x faster                                      |
| richards                 | 79.3 ms                                                | 50.9 ms: 1.56x faster                                      |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                       |
| coroutines               | 35.1 ms                                                | 23.2 ms: 1.51x faster                                      |
| float                    | 117 ms                                                 | 78.9 ms: 1.48x faster                                      |
| tomli_loads              | 3.14 sec                                               | 2.12 sec: 1.48x faster                                     |
| pyflate                  | 716 ms                                                 | 484 ms: 1.48x faster                                       |
| deepcopy_memo            | 58.5 us                                                | 39.7 us: 1.47x faster                                      |
| spectral_norm            | 170 ms                                                 | 116 ms: 1.46x faster                                       |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.45x faster                                      |
| scimark_lu               | 176 ms                                                 | 122 ms: 1.45x faster                                       |
| logging_simple           | 8.30 us                                                | 5.74 us: 1.45x faster                                      |
| tornado_http             | 136 ms                                                 | 94.6 ms: 1.44x faster                                      |
| logging_format           | 9.09 us                                                | 6.47 us: 1.40x faster                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.84 sec: 1.40x faster                                     |
| django_template          | 48.2 ms                                                | 34.8 ms: 1.38x faster                                      |
| regex_compile            | 188 ms                                                 | 137 ms: 1.38x faster                                       |
| pycparser                | 1.58 sec                                               | 1.16 sec: 1.36x faster                                     |
| python_startup           | 14.6 ms                                                | 10.8 ms: 1.36x faster                                      |
| pprint_pformat           | 2.10 sec                                               | 1.56 sec: 1.35x faster                                     |
| genshi_text              | 31.8 ms                                                | 23.7 ms: 1.34x faster                                      |
| pprint_safe_repr         | 1.02 sec                                               | 758 ms: 1.34x faster                                       |
| chameleon                | 9.68 ms                                                | 7.22 ms: 1.34x faster                                      |
| fannkuch                 | 532 ms                                                 | 402 ms: 1.32x faster                                       |
| html5lib                 | 88.9 ms                                                | 67.2 ms: 1.32x faster                                      |
| json_dumps               | 14.2 ms                                                | 10.7 ms: 1.32x faster                                      |
| deepcopy                 | 479 us                                                 | 367 us: 1.30x faster                                       |
| thrift                   | 1.07 ms                                                | 823 us: 1.30x faster                                       |
| nqueens                  | 106 ms                                                 | 81.4 ms: 1.30x faster                                      |
| sqlglot_normalize        | 143 ms                                                 | 110 ms: 1.30x faster                                       |
| xml_etree_process        | 79.1 ms                                                | 61.2 ms: 1.29x faster                                      |
| genshi_xml               | 66.0 ms                                                | 51.6 ms: 1.28x faster                                      |
| 2to3                     | 348 ms                                                 | 274 ms: 1.27x faster                                       |
| sympy_sum                | 196 ms                                                 | 156 ms: 1.26x faster                                       |
| sympy_integrate          | 25.8 ms                                                | 20.5 ms: 1.26x faster                                      |
| dulwich_log              | 84.3 ms                                                | 67.2 ms: 1.26x faster                                      |
| sqlglot_optimize         | 69.2 ms                                                | 55.5 ms: 1.25x faster                                      |
| deepcopy_reduce          | 4.17 us                                                | 3.35 us: 1.25x faster                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.27 ms: 1.23x faster                                      |
| sympy_str                | 346 ms                                                 | 282 ms: 1.22x faster                                       |
| djangocms                | 38.4 us                                                | 31.5 us: 1.22x faster                                      |
| aiohttp                  | 1.44 ms                                                | 1.18 ms: 1.22x faster                                      |
| mypy2                    | 894 ms                                                 | 742 ms: 1.21x faster                                       |
| gunicorn                 | 1.53 ms                                                | 1.28 ms: 1.20x faster                                      |
| sympy_expand             | 566 ms                                                 | 473 ms: 1.20x faster                                       |
| dask                     | 441 ms                                                 | 369 ms: 1.19x faster                                       |
| scimark_fft              | 466 ms                                                 | 392 ms: 1.19x faster                                       |
| bench_thread_pool        | 986 us                                                 | 834 us: 1.18x faster                                       |
| pathlib                  | 20.5 ms                                                | 17.3 ms: 1.18x faster                                      |
| docutils                 | 3.30 sec                                               | 2.83 sec: 1.17x faster                                     |
| xml_etree_generate       | 99.4 ms                                                | 87.4 ms: 1.14x faster                                      |
| regex_v8                 | 27.8 ms                                                | 25.1 ms: 1.11x faster                                      |
| meteor_contest           | 120 ms                                                 | 110 ms: 1.09x faster                                       |
| json_loads               | 31.2 us                                                | 28.9 us: 1.08x faster                                      |
| xml_etree_iterparse      | 115 ms                                                 | 107 ms: 1.07x faster                                       |
| json                     | 5.69 ms                                                | 5.31 ms: 1.07x faster                                      |
| xml_etree_parse          | 168 ms                                                 | 162 ms: 1.04x faster                                       |
| regex_dna                | 227 ms                                                 | 221 ms: 1.02x faster                                       |
| mdp                      | 2.85 sec                                               | 2.79 sec: 1.02x faster                                     |
| sqlite_synth             | 3.02 us                                                | 2.99 us: 1.01x faster                                      |
| bench_mp_pool            | 24.0 ms                                                | 23.9 ms: 1.01x faster                                      |
| async_generators         | 444 ms                                                 | 442 ms: 1.00x faster                                       |
| pidigits                 | 191 ms                                                 | 191 ms: 1.00x slower                                       |
| pickle_list              | 5.08 us                                                | 5.11 us: 1.01x slower                                      |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.01x slower                                       |
| unpickle_list            | 5.20 us                                                | 5.34 us: 1.03x slower                                      |
| flaskblogging            | 8.58 ms                                                | 9.01 ms: 1.05x slower                                      |
| unpickle                 | 14.4 us                                                | 15.1 us: 1.05x slower                                      |
| pickle                   | 10.7 us                                                | 11.5 us: 1.08x slower                                      |
| gc_traversal             | 3.62 ms                                                | 3.98 ms: 1.10x slower                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.82 ms: 1.12x slower                                      |
| telco                    | 7.27 ms                                                | 8.41 ms: 1.16x slower                                      |
| coverage                 | 79.4 ms                                                | 93.1 ms: 1.17x slower                                      |
| pickle_dict              | 29.6 us                                                | 34.8 us: 1.18x slower                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.11 ms: 1.20x slower                                      |
| Geometric mean           | (ref)                                                  | 1.32x faster                                               |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.12x