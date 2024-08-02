# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a5
- machine: linux-x86_64
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 270 ms: 1.29x faster                                       |
| chameleon      | 9.68 ms                                                | 6.83 ms: 1.42x faster                                      |
| docutils       | 3.30 sec                                               | 2.66 sec: 1.24x faster                                     |
| html5lib       | 88.9 ms                                                | 67.4 ms: 1.32x faster                                      |
| tornado_http   | 136 ms                                                 | 98.6 ms: 1.38x faster                                      |
| Geometric mean | (ref)                                                  | 1.33x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 449 ms: 1.62x faster                                       |
| async_tree_memoization  | 870 ms                                                 | 581 ms: 1.50x faster                                       |
| async_tree_io           | 1.77 sec                                               | 1.22 sec: 1.45x faster                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 729 ms: 1.39x faster                                       |
| Geometric mean          | (ref)                                                  | 1.49x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 154 ms                                                 | 93.6 ms: 1.64x faster                                      |
| float          | 117 ms                                                 | 82.6 ms: 1.42x faster                                      |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                  | 1.33x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 133 ms: 1.42x faster                                       |
| regex_v8       | 27.8 ms                                                | 24.7 ms: 1.13x faster                                      |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                       |
| regex_effbot   | 3.63 ms                                                | 3.54 ms: 1.03x faster                                      |
| Geometric mean | (ref)                                                  | 1.15x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.60x faster                                       |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.53x faster                                       |
| tomli_loads          | 3.14 sec                                               | 2.16 sec: 1.45x faster                                     |
| xml_etree_process    | 79.1 ms                                                | 59.8 ms: 1.32x faster                                      |
| json_dumps           | 14.2 ms                                                | 10.8 ms: 1.32x faster                                      |
| xml_etree_generate   | 99.4 ms                                                | 87.3 ms: 1.14x faster                                      |
| json_loads           | 31.2 us                                                | 27.7 us: 1.13x faster                                      |
| xml_etree_iterparse  | 115 ms                                                 | 106 ms: 1.09x faster                                       |
| xml_etree_parse      | 168 ms                                                 | 159 ms: 1.05x faster                                       |
| unpickle_list        | 5.20 us                                                | 5.05 us: 1.03x faster                                      |
| pickle_list          | 5.08 us                                                | 5.01 us: 1.01x faster                                      |
| unpickle             | 14.4 us                                                | 15.1 us: 1.05x slower                                      |
| pickle               | 10.7 us                                                | 11.7 us: 1.09x slower                                      |
| pickle_dict          | 29.6 us                                                | 35.7 us: 1.21x slower                                      |
| Geometric mean       | (ref)                                                  | 1.15x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.4 ms: 1.40x faster                                      |
| python_startup_no_site | 5.93 ms                                                | 8.99 ms: 1.51x slower                                      |
| Geometric mean         | (ref)                                                  | 1.04x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.3 ms: 1.44x faster                                      |
| django_template | 48.2 ms                                                | 33.8 ms: 1.43x faster                                      |
| genshi_text     | 31.8 ms                                                | 23.0 ms: 1.39x faster                                      |
| genshi_xml      | 66.0 ms                                                | 52.0 ms: 1.27x faster                                      |
| Geometric mean  | (ref)                                                  | 1.38x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 112 us: 4.85x faster                                       |
| generators               | 80.1 ms                                                | 29.5 ms: 2.71x faster                                      |
| deltablue                | 7.91 ms                                                | 3.23 ms: 2.45x faster                                      |
| raytrace                 | 507 ms                                                 | 263 ms: 1.93x faster                                       |
| logging_silent           | 190 ns                                                 | 99.5 ns: 1.91x faster                                      |
| chaos                    | 115 ms                                                 | 60.9 ms: 1.90x faster                                      |
| asyncio_tcp              | 922 ms                                                 | 504 ms: 1.83x faster                                       |
| richards_super           | 94.7 ms                                                | 51.9 ms: 1.82x faster                                      |
| scimark_sor              | 220 ms                                                 | 123 ms: 1.79x faster                                       |
| pylint                   | 551 ms                                                 | 312 ms: 1.77x faster                                       |
| comprehensions           | 28.8 us                                                | 16.4 us: 1.75x faster                                      |
| crypto_pyaes             | 128 ms                                                 | 73.0 ms: 1.75x faster                                      |
| scimark_monte_carlo      | 118 ms                                                 | 67.9 ms: 1.74x faster                                      |
| go                       | 240 ms                                                 | 139 ms: 1.73x faster                                       |
| richards                 | 79.3 ms                                                | 45.9 ms: 1.73x faster                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.27 ms: 1.71x faster                                      |
| hexiom                   | 10.4 ms                                                | 6.13 ms: 1.69x faster                                      |
| nbody                    | 154 ms                                                 | 93.6 ms: 1.64x faster                                      |
| async_tree_none          | 728 ms                                                 | 449 ms: 1.62x faster                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.59 ms: 1.61x faster                                      |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.60x faster                                       |
| coroutines               | 35.1 ms                                                | 22.0 ms: 1.59x faster                                      |
| spectral_norm            | 170 ms                                                 | 108 ms: 1.57x faster                                       |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                       |
| deepcopy_memo            | 58.5 us                                                | 38.1 us: 1.53x faster                                      |
| pyflate                  | 716 ms                                                 | 469 ms: 1.53x faster                                       |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.53x faster                                       |
| async_tree_memoization   | 870 ms                                                 | 581 ms: 1.50x faster                                       |
| async_tree_io            | 1.77 sec                                               | 1.22 sec: 1.45x faster                                     |
| tomli_loads              | 3.14 sec                                               | 2.16 sec: 1.45x faster                                     |
| mako                     | 16.3 ms                                                | 11.3 ms: 1.44x faster                                      |
| django_template          | 48.2 ms                                                | 33.8 ms: 1.43x faster                                      |
| chameleon                | 9.68 ms                                                | 6.83 ms: 1.42x faster                                      |
| float                    | 117 ms                                                 | 82.6 ms: 1.42x faster                                      |
| logging_simple           | 8.30 us                                                | 5.85 us: 1.42x faster                                      |
| regex_compile            | 188 ms                                                 | 133 ms: 1.42x faster                                       |
| python_startup           | 14.6 ms                                                | 10.4 ms: 1.40x faster                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 729 ms: 1.39x faster                                       |
| logging_format           | 9.09 us                                                | 6.53 us: 1.39x faster                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.85 sec: 1.39x faster                                     |
| genshi_text              | 31.8 ms                                                | 23.0 ms: 1.39x faster                                      |
| deepcopy                 | 479 us                                                 | 346 us: 1.38x faster                                       |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.68 ms: 1.38x faster                                      |
| tornado_http             | 136 ms                                                 | 98.6 ms: 1.38x faster                                      |
| deepcopy_reduce          | 4.17 us                                                | 3.04 us: 1.37x faster                                      |
| thrift                   | 1.07 ms                                                | 790 us: 1.36x faster                                       |
| pprint_pformat           | 2.10 sec                                               | 1.55 sec: 1.35x faster                                     |
| pprint_safe_repr         | 1.02 sec                                               | 757 ms: 1.35x faster                                       |
| sqlglot_normalize        | 143 ms                                                 | 107 ms: 1.34x faster                                       |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                     |
| fannkuch                 | 532 ms                                                 | 400 ms: 1.33x faster                                       |
| xml_etree_process        | 79.1 ms                                                | 59.8 ms: 1.32x faster                                      |
| html5lib                 | 88.9 ms                                                | 67.4 ms: 1.32x faster                                      |
| json_dumps               | 14.2 ms                                                | 10.8 ms: 1.32x faster                                      |
| nqueens                  | 106 ms                                                 | 80.7 ms: 1.31x faster                                      |
| 2to3                     | 348 ms                                                 | 270 ms: 1.29x faster                                       |
| sympy_integrate          | 25.8 ms                                                | 20.0 ms: 1.29x faster                                      |
| scimark_fft              | 466 ms                                                 | 362 ms: 1.29x faster                                       |
| sqlglot_optimize         | 69.2 ms                                                | 53.9 ms: 1.28x faster                                      |
| sympy_sum                | 196 ms                                                 | 153 ms: 1.28x faster                                       |
| genshi_xml               | 66.0 ms                                                | 52.0 ms: 1.27x faster                                      |
| sympy_str                | 346 ms                                                 | 275 ms: 1.26x faster                                       |
| dulwich_log              | 84.3 ms                                                | 67.3 ms: 1.25x faster                                      |
| docutils                 | 3.30 sec                                               | 2.66 sec: 1.24x faster                                     |
| sympy_expand             | 566 ms                                                 | 466 ms: 1.21x faster                                       |
| aiohttp                  | 1.44 ms                                                | 1.19 ms: 1.21x faster                                      |
| djangocms                | 38.4 us                                                | 32.1 us: 1.20x faster                                      |
| dask                     | 441 ms                                                 | 370 ms: 1.19x faster                                       |
| gunicorn                 | 1.53 ms                                                | 1.29 ms: 1.19x faster                                      |
| bench_thread_pool        | 986 us                                                 | 842 us: 1.17x faster                                       |
| xml_etree_generate       | 99.4 ms                                                | 87.3 ms: 1.14x faster                                      |
| regex_v8                 | 27.8 ms                                                | 24.7 ms: 1.13x faster                                      |
| json_loads               | 31.2 us                                                | 27.7 us: 1.13x faster                                      |
| mdp                      | 2.85 sec                                               | 2.53 sec: 1.12x faster                                     |
| json                     | 5.69 ms                                                | 5.15 ms: 1.11x faster                                      |
| pathlib                  | 20.5 ms                                                | 18.5 ms: 1.10x faster                                      |
| meteor_contest           | 120 ms                                                 | 109 ms: 1.10x faster                                       |
| xml_etree_iterparse      | 115 ms                                                 | 106 ms: 1.09x faster                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.52 ms: 1.07x faster                                      |
| xml_etree_parse          | 168 ms                                                 | 159 ms: 1.05x faster                                       |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                       |
| sqlite_synth             | 3.02 us                                                | 2.89 us: 1.05x faster                                      |
| unpickle_list            | 5.20 us                                                | 5.05 us: 1.03x faster                                      |
| regex_effbot             | 3.63 ms                                                | 3.54 ms: 1.03x faster                                      |
| pickle_list              | 5.08 us                                                | 5.01 us: 1.01x faster                                      |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                       |
| bench_mp_pool            | 24.0 ms                                                | 23.9 ms: 1.01x faster                                      |
| asyncio_websockets       | 559 ms                                                 | 563 ms: 1.01x slower                                       |
| async_generators         | 444 ms                                                 | 449 ms: 1.01x slower                                       |
| flaskblogging            | 8.58 ms                                                | 8.82 ms: 1.03x slower                                      |
| gc_traversal             | 3.62 ms                                                | 3.78 ms: 1.04x slower                                      |
| unpickle                 | 14.4 us                                                | 15.1 us: 1.05x slower                                      |
| pickle                   | 10.7 us                                                | 11.7 us: 1.09x slower                                      |
| telco                    | 7.27 ms                                                | 8.60 ms: 1.18x slower                                      |
| coverage                 | 79.4 ms                                                | 95.6 ms: 1.20x slower                                      |
| pickle_dict              | 29.6 us                                                | 35.7 us: 1.21x slower                                      |
| python_startup_no_site   | 5.93 ms                                                | 8.99 ms: 1.51x slower                                      |
| Geometric mean           | (ref)                                                  | 1.34x faster                                               |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240312-3.13.0a5-076d169/bm-20240312-linux-x86_64-python-v3.13.0a5-3.13.0a5-076d169.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.08x