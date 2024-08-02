# Results vs. 3.10.4

- fork: brandtbucher
- ref: jump_to_top
- machine: linux-x86_64
- commit hash: 7bff512
- commit date: 2024-06-20
- overall geometric mean: 1.38x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 273 ms: 1.28x faster                                               |
| html5lib       | 88.9 ms                                                | 66.7 ms: 1.33x faster                                              |
| tornado_http   | 136 ms                                                 | 93.3 ms: 1.46x faster                                              |
| Geometric mean | (ref)                                                  | 1.36x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 366 ms: 1.99x faster                                               |
| async_tree_io           | 1.77 sec                                               | 929 ms: 1.90x faster                                               |
| async_tree_memoization  | 870 ms                                                 | 480 ms: 1.81x faster                                               |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 611 ms: 1.66x faster                                               |
| Geometric mean          | (ref)                                                  | 1.84x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 79.2 ms: 1.94x faster                                              |
| float          | 117 ms                                                 | 70.2 ms: 1.67x faster                                              |
| pidigits       | 191 ms                                                 | 185 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.49x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 135 ms: 1.40x faster                                               |
| regex_v8       | 27.8 ms                                                | 26.8 ms: 1.04x faster                                              |
| regex_effbot   | 3.63 ms                                                | 3.85 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                  | 1.08x faster                                                       |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 290 us: 1.67x faster                                               |
| tomli_loads          | 3.14 sec                                               | 1.91 sec: 1.64x faster                                             |
| unpickle_pure_python | 331 us                                                 | 218 us: 1.52x faster                                               |
| xml_etree_process    | 79.1 ms                                                | 57.6 ms: 1.37x faster                                              |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                              |
| xml_etree_generate   | 99.4 ms                                                | 80.4 ms: 1.24x faster                                              |
| xml_etree_iterparse  | 115 ms                                                 | 99.5 ms: 1.16x faster                                              |
| xml_etree_parse      | 168 ms                                                 | 147 ms: 1.14x faster                                               |
| json_loads           | 31.2 us                                                | 28.8 us: 1.09x faster                                              |
| unpickle_list        | 5.20 us                                                | 5.28 us: 1.02x slower                                              |
| pickle_list          | 5.08 us                                                | 5.31 us: 1.05x slower                                              |
| pickle               | 10.7 us                                                | 11.9 us: 1.12x slower                                              |
| pickle_dict          | 29.6 us                                                | 35.5 us: 1.20x slower                                              |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                       |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.8 ms: 1.35x faster                                              |
| python_startup_no_site | 5.93 ms                                                | 7.39 ms: 1.25x slower                                              |
| Geometric mean         | (ref)                                                  | 1.04x faster                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 16.3 ms                                                | 9.63 ms: 1.69x faster                                              |
| django_template | 48.2 ms                                                | 36.6 ms: 1.32x faster                                              |
| genshi_text     | 31.8 ms                                                | 24.5 ms: 1.30x faster                                              |
| genshi_xml      | 66.0 ms                                                | 56.5 ms: 1.17x faster                                              |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 167 us: 3.25x faster                                               |
| generators               | 80.1 ms                                                | 29.5 ms: 2.71x faster                                              |
| deltablue                | 7.91 ms                                                | 3.52 ms: 2.25x faster                                              |
| deepcopy_memo            | 58.5 us                                                | 28.6 us: 2.04x faster                                              |
| async_tree_none          | 728 ms                                                 | 366 ms: 1.99x faster                                               |
| richards_super           | 94.7 ms                                                | 48.0 ms: 1.97x faster                                              |
| chaos                    | 115 ms                                                 | 59.2 ms: 1.95x faster                                              |
| nbody                    | 154 ms                                                 | 79.2 ms: 1.94x faster                                              |
| scimark_monte_carlo      | 118 ms                                                 | 61.6 ms: 1.92x faster                                              |
| crypto_pyaes             | 128 ms                                                 | 67.0 ms: 1.91x faster                                              |
| async_tree_io            | 1.77 sec                                               | 929 ms: 1.90x faster                                               |
| richards                 | 79.3 ms                                                | 41.9 ms: 1.89x faster                                              |
| asyncio_tcp              | 922 ms                                                 | 490 ms: 1.88x faster                                               |
| raytrace                 | 507 ms                                                 | 271 ms: 1.87x faster                                               |
| async_tree_memoization   | 870 ms                                                 | 480 ms: 1.81x faster                                               |
| logging_silent           | 190 ns                                                 | 107 ns: 1.78x faster                                               |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                              |
| deepcopy                 | 479 us                                                 | 275 us: 1.74x faster                                               |
| mako                     | 16.3 ms                                                | 9.63 ms: 1.69x faster                                              |
| scimark_sor              | 220 ms                                                 | 131 ms: 1.68x faster                                               |
| sqlglot_parse            | 2.17 ms                                                | 1.29 ms: 1.68x faster                                              |
| pickle_pure_python       | 484 us                                                 | 290 us: 1.67x faster                                               |
| float                    | 117 ms                                                 | 70.2 ms: 1.67x faster                                              |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 611 ms: 1.66x faster                                               |
| go                       | 240 ms                                                 | 145 ms: 1.65x faster                                               |
| tomli_loads              | 3.14 sec                                               | 1.91 sec: 1.64x faster                                             |
| spectral_norm            | 170 ms                                                 | 104 ms: 1.63x faster                                               |
| pylint                   | 551 ms                                                 | 341 ms: 1.62x faster                                               |
| sqlglot_transpile        | 2.57 ms                                                | 1.61 ms: 1.60x faster                                              |
| pyflate                  | 716 ms                                                 | 447 ms: 1.60x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.51 ms: 1.60x faster                                              |
| logging_simple           | 8.30 us                                                | 5.46 us: 1.52x faster                                              |
| logging_format           | 9.09 us                                                | 5.99 us: 1.52x faster                                              |
| unpickle_pure_python     | 331 us                                                 | 218 us: 1.52x faster                                               |
| fannkuch                 | 532 ms                                                 | 353 ms: 1.51x faster                                               |
| deepcopy_reduce          | 4.17 us                                                | 2.83 us: 1.47x faster                                              |
| scimark_fft              | 466 ms                                                 | 317 ms: 1.47x faster                                               |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.41 ms: 1.47x faster                                              |
| tornado_http             | 136 ms                                                 | 93.3 ms: 1.46x faster                                              |
| coroutines               | 35.1 ms                                                | 24.2 ms: 1.45x faster                                              |
| pprint_safe_repr         | 1.02 sec                                               | 710 ms: 1.43x faster                                               |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.79 sec: 1.43x faster                                             |
| scimark_lu               | 176 ms                                                 | 123 ms: 1.43x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.48 sec: 1.42x faster                                             |
| regex_compile            | 188 ms                                                 | 135 ms: 1.40x faster                                               |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                             |
| xml_etree_process        | 79.1 ms                                                | 57.6 ms: 1.37x faster                                              |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                              |
| python_startup           | 14.6 ms                                                | 10.8 ms: 1.35x faster                                              |
| thrift                   | 1.07 ms                                                | 804 us: 1.33x faster                                               |
| html5lib                 | 88.9 ms                                                | 66.7 ms: 1.33x faster                                              |
| django_template          | 48.2 ms                                                | 36.6 ms: 1.32x faster                                              |
| genshi_text              | 31.8 ms                                                | 24.5 ms: 1.30x faster                                              |
| 2to3                     | 348 ms                                                 | 273 ms: 1.28x faster                                               |
| sqlglot_normalize        | 143 ms                                                 | 112 ms: 1.27x faster                                               |
| pathlib                  | 20.5 ms                                                | 16.1 ms: 1.27x faster                                              |
| dulwich_log              | 84.3 ms                                                | 67.1 ms: 1.26x faster                                              |
| sqlglot_optimize         | 69.2 ms                                                | 55.6 ms: 1.24x faster                                              |
| nqueens                  | 106 ms                                                 | 85.4 ms: 1.24x faster                                              |
| xml_etree_generate       | 99.4 ms                                                | 80.4 ms: 1.24x faster                                              |
| dask                     | 441 ms                                                 | 363 ms: 1.21x faster                                               |
| bench_thread_pool        | 986 us                                                 | 827 us: 1.19x faster                                               |
| sympy_sum                | 196 ms                                                 | 165 ms: 1.19x faster                                               |
| sympy_str                | 346 ms                                                 | 294 ms: 1.18x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 22.0 ms: 1.17x faster                                              |
| genshi_xml               | 66.0 ms                                                | 56.5 ms: 1.17x faster                                              |
| xml_etree_iterparse      | 115 ms                                                 | 99.5 ms: 1.16x faster                                              |
| xml_etree_parse          | 168 ms                                                 | 147 ms: 1.14x faster                                               |
| sympy_expand             | 566 ms                                                 | 499 ms: 1.13x faster                                               |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.13x faster                                             |
| meteor_contest           | 120 ms                                                 | 107 ms: 1.12x faster                                               |
| json_loads               | 31.2 us                                                | 28.8 us: 1.09x faster                                              |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                              |
| json                     | 5.69 ms                                                | 5.29 ms: 1.08x faster                                              |
| regex_v8                 | 27.8 ms                                                | 26.8 ms: 1.04x faster                                              |
| pidigits                 | 191 ms                                                 | 185 ms: 1.03x faster                                               |
| gc_traversal             | 3.62 ms                                                | 3.59 ms: 1.01x faster                                              |
| asyncio_websockets       | 559 ms                                                 | 556 ms: 1.01x faster                                               |
| unpickle_list            | 5.20 us                                                | 5.28 us: 1.02x slower                                              |
| async_generators         | 444 ms                                                 | 462 ms: 1.04x slower                                               |
| pickle_list              | 5.08 us                                                | 5.31 us: 1.05x slower                                              |
| regex_effbot             | 3.63 ms                                                | 3.85 ms: 1.06x slower                                              |
| create_gc_cycles         | 1.62 ms                                                | 1.74 ms: 1.08x slower                                              |
| telco                    | 7.27 ms                                                | 7.87 ms: 1.08x slower                                              |
| pickle                   | 10.7 us                                                | 11.9 us: 1.12x slower                                              |
| coverage                 | 79.4 ms                                                | 94.1 ms: 1.18x slower                                              |
| pickle_dict              | 29.6 us                                                | 35.5 us: 1.20x slower                                              |
| python_startup_no_site   | 5.93 ms                                                | 7.39 ms: 1.25x slower                                              |
| Geometric mean           | (ref)                                                  | 1.38x faster                                                       |

Benchmark hidden because not significant (3): bench_mp_pool, regex_dna, unpickle
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, djangocms, docutils, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (5) of results/bm-20240620-3.14.0a0-7bff512-JIT/bm-20240620-linux-x86_64-brandtbucher-jump_to_top-3.14.0a0-7bff512.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.21x