# Results vs. 3.10.4

- fork: python
- ref: v3.13.0b2
- machine: linux-x86_64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 281 ms: 1.24x faster                                       |
| chameleon      | 9.68 ms                                                | 7.11 ms: 1.36x faster                                      |
| docutils       | 3.30 sec                                               | 2.99 sec: 1.10x faster                                     |
| html5lib       | 88.9 ms                                                | 69.1 ms: 1.29x faster                                      |
| tornado_http   | 136 ms                                                 | 96.9 ms: 1.41x faster                                      |
| Geometric mean | (ref)                                                  | 1.28x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 377 ms: 1.93x faster                                       |
| async_tree_memoization  | 870 ms                                                 | 456 ms: 1.91x faster                                       |
| async_tree_io           | 1.77 sec                                               | 932 ms: 1.90x faster                                       |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 612 ms: 1.66x faster                                       |
| Geometric mean          | (ref)                                                  | 1.85x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 154 ms                                                 | 83.5 ms: 1.84x faster                                      |
| float          | 117 ms                                                 | 73.0 ms: 1.60x faster                                      |
| pidigits       | 191 ms                                                 | 188 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                  | 1.44x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 138 ms: 1.36x faster                                       |
| regex_v8       | 27.8 ms                                                | 25.2 ms: 1.10x faster                                      |
| regex_dna      | 227 ms                                                 | 230 ms: 1.01x slower                                       |
| regex_effbot   | 3.63 ms                                                | 3.69 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 300 us: 1.62x faster                                       |
| tomli_loads          | 3.14 sec                                               | 1.95 sec: 1.61x faster                                     |
| unpickle_pure_python | 331 us                                                 | 222 us: 1.49x faster                                       |
| json_dumps           | 14.2 ms                                                | 10.3 ms: 1.37x faster                                      |
| xml_etree_process    | 79.1 ms                                                | 58.5 ms: 1.35x faster                                      |
| xml_etree_generate   | 99.4 ms                                                | 82.9 ms: 1.20x faster                                      |
| xml_etree_iterparse  | 115 ms                                                 | 102 ms: 1.13x faster                                       |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                       |
| json_loads           | 31.2 us                                                | 28.8 us: 1.08x faster                                      |
| unpickle_list        | 5.20 us                                                | 5.26 us: 1.01x slower                                      |
| unpickle             | 14.4 us                                                | 15.1 us: 1.05x slower                                      |
| pickle               | 10.7 us                                                | 11.9 us: 1.11x slower                                      |
| pickle_dict          | 29.6 us                                                | 34.8 us: 1.18x slower                                      |
| Geometric mean       | (ref)                                                  | 1.17x faster                                               |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 11.3 ms: 1.29x faster                                      |
| python_startup_no_site | 5.93 ms                                                | 7.62 ms: 1.29x slower                                      |
| Geometric mean         | (ref)                                                  | 1.00x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.83 ms: 1.66x faster                                      |
| django_template | 48.2 ms                                                | 36.4 ms: 1.32x faster                                      |
| genshi_text     | 31.8 ms                                                | 25.5 ms: 1.25x faster                                      |
| genshi_xml      | 66.0 ms                                                | 60.2 ms: 1.10x faster                                      |
| Geometric mean  | (ref)                                                  | 1.32x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 173 us: 3.15x faster                                       |
| generators               | 80.1 ms                                                | 33.5 ms: 2.39x faster                                      |
| deltablue                | 7.91 ms                                                | 3.70 ms: 2.14x faster                                      |
| chaos                    | 115 ms                                                 | 58.5 ms: 1.97x faster                                      |
| richards_super           | 94.7 ms                                                | 48.4 ms: 1.96x faster                                      |
| async_tree_none          | 728 ms                                                 | 377 ms: 1.93x faster                                       |
| async_tree_memoization   | 870 ms                                                 | 456 ms: 1.91x faster                                       |
| richards                 | 79.3 ms                                                | 41.7 ms: 1.90x faster                                      |
| async_tree_io            | 1.77 sec                                               | 932 ms: 1.90x faster                                       |
| scimark_monte_carlo      | 118 ms                                                 | 62.7 ms: 1.88x faster                                      |
| crypto_pyaes             | 128 ms                                                 | 68.0 ms: 1.88x faster                                      |
| nbody                    | 154 ms                                                 | 83.5 ms: 1.84x faster                                      |
| raytrace                 | 507 ms                                                 | 280 ms: 1.81x faster                                       |
| asyncio_tcp              | 922 ms                                                 | 522 ms: 1.77x faster                                       |
| logging_silent           | 190 ns                                                 | 108 ns: 1.76x faster                                       |
| comprehensions           | 28.8 us                                                | 16.7 us: 1.72x faster                                      |
| scimark_sor              | 220 ms                                                 | 128 ms: 1.71x faster                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.30 ms: 1.67x faster                                      |
| spectral_norm            | 170 ms                                                 | 102 ms: 1.66x faster                                       |
| mako                     | 16.3 ms                                                | 9.83 ms: 1.66x faster                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 612 ms: 1.66x faster                                       |
| pyflate                  | 716 ms                                                 | 436 ms: 1.64x faster                                       |
| pickle_pure_python       | 484 us                                                 | 300 us: 1.62x faster                                       |
| tomli_loads              | 3.14 sec                                               | 1.95 sec: 1.61x faster                                     |
| float                    | 117 ms                                                 | 73.0 ms: 1.60x faster                                      |
| go                       | 240 ms                                                 | 151 ms: 1.59x faster                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                      |
| deepcopy_memo            | 58.5 us                                                | 37.3 us: 1.57x faster                                      |
| pylint                   | 551 ms                                                 | 353 ms: 1.56x faster                                       |
| hexiom                   | 10.4 ms                                                | 6.67 ms: 1.56x faster                                      |
| coroutines               | 35.1 ms                                                | 22.6 ms: 1.55x faster                                      |
| unpickle_pure_python     | 331 us                                                 | 222 us: 1.49x faster                                       |
| fannkuch                 | 532 ms                                                 | 358 ms: 1.49x faster                                       |
| scimark_fft              | 466 ms                                                 | 317 ms: 1.47x faster                                       |
| logging_simple           | 8.30 us                                                | 5.70 us: 1.46x faster                                      |
| pprint_pformat           | 2.10 sec                                               | 1.45 sec: 1.45x faster                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.48 ms: 1.44x faster                                      |
| logging_format           | 9.09 us                                                | 6.30 us: 1.44x faster                                      |
| pprint_safe_repr         | 1.02 sec                                               | 715 ms: 1.42x faster                                       |
| tornado_http             | 136 ms                                                 | 96.9 ms: 1.41x faster                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.86 sec: 1.39x faster                                     |
| scimark_lu               | 176 ms                                                 | 127 ms: 1.38x faster                                       |
| json_dumps               | 14.2 ms                                                | 10.3 ms: 1.37x faster                                      |
| regex_compile            | 188 ms                                                 | 138 ms: 1.36x faster                                       |
| chameleon                | 9.68 ms                                                | 7.11 ms: 1.36x faster                                      |
| xml_etree_process        | 79.1 ms                                                | 58.5 ms: 1.35x faster                                      |
| pycparser                | 1.58 sec                                               | 1.17 sec: 1.35x faster                                     |
| django_template          | 48.2 ms                                                | 36.4 ms: 1.32x faster                                      |
| thrift                   | 1.07 ms                                                | 826 us: 1.30x faster                                       |
| python_startup           | 14.6 ms                                                | 11.3 ms: 1.29x faster                                      |
| html5lib                 | 88.9 ms                                                | 69.1 ms: 1.29x faster                                      |
| deepcopy                 | 479 us                                                 | 375 us: 1.28x faster                                       |
| deepcopy_reduce          | 4.17 us                                                | 3.30 us: 1.26x faster                                      |
| sqlglot_normalize        | 143 ms                                                 | 114 ms: 1.26x faster                                       |
| genshi_text              | 31.8 ms                                                | 25.5 ms: 1.25x faster                                      |
| 2to3                     | 348 ms                                                 | 281 ms: 1.24x faster                                       |
| nqueens                  | 106 ms                                                 | 86.5 ms: 1.22x faster                                      |
| sqlglot_optimize         | 69.2 ms                                                | 56.8 ms: 1.22x faster                                      |
| dulwich_log              | 84.3 ms                                                | 69.7 ms: 1.21x faster                                      |
| xml_etree_generate       | 99.4 ms                                                | 82.9 ms: 1.20x faster                                      |
| pathlib                  | 20.5 ms                                                | 17.4 ms: 1.17x faster                                      |
| djangocms                | 38.4 us                                                | 32.8 us: 1.17x faster                                      |
| dask                     | 441 ms                                                 | 377 ms: 1.17x faster                                       |
| aiohttp                  | 1.44 ms                                                | 1.25 ms: 1.15x faster                                      |
| sympy_str                | 346 ms                                                 | 302 ms: 1.15x faster                                       |
| sympy_integrate          | 25.8 ms                                                | 22.5 ms: 1.14x faster                                      |
| sympy_sum                | 196 ms                                                 | 172 ms: 1.14x faster                                       |
| gunicorn                 | 1.53 ms                                                | 1.34 ms: 1.14x faster                                      |
| bench_thread_pool        | 986 us                                                 | 867 us: 1.14x faster                                       |
| xml_etree_iterparse      | 115 ms                                                 | 102 ms: 1.13x faster                                       |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                       |
| sympy_expand             | 566 ms                                                 | 510 ms: 1.11x faster                                       |
| docutils                 | 3.30 sec                                               | 2.99 sec: 1.10x faster                                     |
| regex_v8                 | 27.8 ms                                                | 25.2 ms: 1.10x faster                                      |
| mypy2                    | 894 ms                                                 | 814 ms: 1.10x faster                                       |
| genshi_xml               | 66.0 ms                                                | 60.2 ms: 1.10x faster                                      |
| mdp                      | 2.85 sec                                               | 2.62 sec: 1.09x faster                                     |
| json_loads               | 31.2 us                                                | 28.8 us: 1.08x faster                                      |
| meteor_contest           | 120 ms                                                 | 111 ms: 1.08x faster                                       |
| json                     | 5.69 ms                                                | 5.34 ms: 1.07x faster                                      |
| sqlite_synth             | 3.02 us                                                | 2.88 us: 1.05x faster                                      |
| pidigits                 | 191 ms                                                 | 188 ms: 1.01x faster                                       |
| bench_mp_pool            | 24.0 ms                                                | 23.9 ms: 1.00x faster                                      |
| unpickle_list            | 5.20 us                                                | 5.26 us: 1.01x slower                                      |
| regex_dna                | 227 ms                                                 | 230 ms: 1.01x slower                                       |
| asyncio_websockets       | 559 ms                                                 | 567 ms: 1.01x slower                                       |
| regex_effbot             | 3.63 ms                                                | 3.69 ms: 1.02x slower                                      |
| async_generators         | 444 ms                                                 | 462 ms: 1.04x slower                                       |
| unpickle                 | 14.4 us                                                | 15.1 us: 1.05x slower                                      |
| gc_traversal             | 3.62 ms                                                | 3.88 ms: 1.07x slower                                      |
| flaskblogging            | 8.58 ms                                                | 9.27 ms: 1.08x slower                                      |
| pickle                   | 10.7 us                                                | 11.9 us: 1.11x slower                                      |
| telco                    | 7.27 ms                                                | 8.12 ms: 1.12x slower                                      |
| create_gc_cycles         | 1.62 ms                                                | 1.83 ms: 1.13x slower                                      |
| coverage                 | 79.4 ms                                                | 92.7 ms: 1.17x slower                                      |
| pickle_dict              | 29.6 us                                                | 34.8 us: 1.18x slower                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.62 ms: 1.29x slower                                      |
| Geometric mean           | (ref)                                                  | 1.33x faster                                               |

Benchmark hidden because not significant (1): pickle_list
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.21x