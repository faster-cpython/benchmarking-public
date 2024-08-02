# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 269 ms: 1.29x faster                                       |
| chameleon      | 9.68 ms                                                | 6.85 ms: 1.41x faster                                      |
| docutils       | 3.30 sec                                               | 2.65 sec: 1.24x faster                                     |
| html5lib       | 88.9 ms                                                | 67.4 ms: 1.32x faster                                      |
| tornado_http   | 136 ms                                                 | 97.1 ms: 1.40x faster                                      |
| Geometric mean | (ref)                                                  | 1.33x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 444 ms: 1.64x faster                                       |
| async_tree_memoization  | 870 ms                                                 | 571 ms: 1.52x faster                                       |
| async_tree_io           | 1.77 sec                                               | 1.20 sec: 1.47x faster                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 718 ms: 1.41x faster                                       |
| Geometric mean          | (ref)                                                  | 1.51x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 154 ms                                                 | 92.1 ms: 1.67x faster                                      |
| float          | 117 ms                                                 | 83.1 ms: 1.41x faster                                      |
| pidigits       | 191 ms                                                 | 189 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                  | 1.33x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 132 ms: 1.43x faster                                       |
| regex_v8       | 27.8 ms                                                | 24.4 ms: 1.14x faster                                      |
| regex_dna      | 227 ms                                                 | 224 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                  | 1.13x faster                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 302 us: 1.61x faster                                       |
| unpickle_pure_python | 331 us                                                 | 217 us: 1.53x faster                                       |
| tomli_loads          | 3.14 sec                                               | 2.20 sec: 1.43x faster                                     |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.36x faster                                      |
| xml_etree_process    | 79.1 ms                                                | 59.3 ms: 1.33x faster                                      |
| xml_etree_generate   | 99.4 ms                                                | 86.9 ms: 1.14x faster                                      |
| json_loads           | 31.2 us                                                | 27.9 us: 1.12x faster                                      |
| xml_etree_iterparse  | 115 ms                                                 | 107 ms: 1.08x faster                                       |
| xml_etree_parse      | 168 ms                                                 | 160 ms: 1.05x faster                                       |
| unpickle_list        | 5.20 us                                                | 5.09 us: 1.02x faster                                      |
| pickle_list          | 5.08 us                                                | 5.28 us: 1.04x slower                                      |
| unpickle             | 14.4 us                                                | 15.4 us: 1.07x slower                                      |
| pickle               | 10.7 us                                                | 12.0 us: 1.13x slower                                      |
| pickle_dict          | 29.6 us                                                | 34.7 us: 1.17x slower                                      |
| Geometric mean       | (ref)                                                  | 1.14x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.3 ms: 1.41x faster                                      |
| python_startup_no_site | 5.93 ms                                                | 8.87 ms: 1.50x slower                                      |
| Geometric mean         | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.2 ms: 1.46x faster                                      |
| django_template | 48.2 ms                                                | 34.7 ms: 1.39x faster                                      |
| genshi_text     | 31.8 ms                                                | 23.0 ms: 1.39x faster                                      |
| genshi_xml      | 66.0 ms                                                | 52.8 ms: 1.25x faster                                      |
| Geometric mean  | (ref)                                                  | 1.37x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 112 us: 4.87x faster                                       |
| generators               | 80.1 ms                                                | 30.3 ms: 2.65x faster                                      |
| deltablue                | 7.91 ms                                                | 3.24 ms: 2.44x faster                                      |
| logging_silent           | 190 ns                                                 | 97.7 ns: 1.94x faster                                      |
| raytrace                 | 507 ms                                                 | 265 ms: 1.91x faster                                       |
| chaos                    | 115 ms                                                 | 61.2 ms: 1.89x faster                                      |
| asyncio_tcp              | 922 ms                                                 | 501 ms: 1.84x faster                                       |
| pylint                   | 551 ms                                                 | 310 ms: 1.78x faster                                       |
| comprehensions           | 28.8 us                                                | 16.2 us: 1.77x faster                                      |
| crypto_pyaes             | 128 ms                                                 | 72.0 ms: 1.77x faster                                      |
| scimark_monte_carlo      | 118 ms                                                 | 67.2 ms: 1.76x faster                                      |
| richards_super           | 94.7 ms                                                | 54.1 ms: 1.75x faster                                      |
| go                       | 240 ms                                                 | 139 ms: 1.72x faster                                       |
| sqlglot_parse            | 2.17 ms                                                | 1.26 ms: 1.72x faster                                      |
| scimark_sor              | 220 ms                                                 | 129 ms: 1.71x faster                                       |
| hexiom                   | 10.4 ms                                                | 6.20 ms: 1.68x faster                                      |
| nbody                    | 154 ms                                                 | 92.1 ms: 1.67x faster                                      |
| richards                 | 79.3 ms                                                | 48.1 ms: 1.65x faster                                      |
| async_tree_none          | 728 ms                                                 | 444 ms: 1.64x faster                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.58 ms: 1.62x faster                                      |
| pickle_pure_python       | 484 us                                                 | 302 us: 1.61x faster                                       |
| scimark_lu               | 176 ms                                                 | 113 ms: 1.56x faster                                       |
| deepcopy_memo            | 58.5 us                                                | 37.9 us: 1.54x faster                                      |
| spectral_norm            | 170 ms                                                 | 111 ms: 1.53x faster                                       |
| coroutines               | 35.1 ms                                                | 23.0 ms: 1.53x faster                                      |
| unpickle_pure_python     | 331 us                                                 | 217 us: 1.53x faster                                       |
| async_tree_memoization   | 870 ms                                                 | 571 ms: 1.52x faster                                       |
| pyflate                  | 716 ms                                                 | 474 ms: 1.51x faster                                       |
| async_tree_io            | 1.77 sec                                               | 1.20 sec: 1.47x faster                                     |
| mako                     | 16.3 ms                                                | 11.2 ms: 1.46x faster                                      |
| regex_compile            | 188 ms                                                 | 132 ms: 1.43x faster                                       |
| tomli_loads              | 3.14 sec                                               | 2.20 sec: 1.43x faster                                     |
| logging_simple           | 8.30 us                                                | 5.83 us: 1.43x faster                                      |
| python_startup           | 14.6 ms                                                | 10.3 ms: 1.41x faster                                      |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 718 ms: 1.41x faster                                       |
| chameleon                | 9.68 ms                                                | 6.85 ms: 1.41x faster                                      |
| float                    | 117 ms                                                 | 83.1 ms: 1.41x faster                                      |
| tornado_http             | 136 ms                                                 | 97.1 ms: 1.40x faster                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.84 sec: 1.40x faster                                     |
| pprint_pformat           | 2.10 sec                                               | 1.51 sec: 1.39x faster                                     |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.64 ms: 1.39x faster                                      |
| logging_format           | 9.09 us                                                | 6.53 us: 1.39x faster                                      |
| pprint_safe_repr         | 1.02 sec                                               | 734 ms: 1.39x faster                                       |
| django_template          | 48.2 ms                                                | 34.7 ms: 1.39x faster                                      |
| genshi_text              | 31.8 ms                                                | 23.0 ms: 1.39x faster                                      |
| deepcopy                 | 479 us                                                 | 347 us: 1.38x faster                                       |
| deepcopy_reduce          | 4.17 us                                                | 3.06 us: 1.36x faster                                      |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.36x faster                                      |
| xml_etree_process        | 79.1 ms                                                | 59.3 ms: 1.33x faster                                      |
| thrift                   | 1.07 ms                                                | 807 us: 1.33x faster                                       |
| fannkuch                 | 532 ms                                                 | 401 ms: 1.33x faster                                       |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.32x faster                                       |
| html5lib                 | 88.9 ms                                                | 67.4 ms: 1.32x faster                                      |
| nqueens                  | 106 ms                                                 | 81.0 ms: 1.31x faster                                      |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                       |
| sympy_integrate          | 25.8 ms                                                | 19.9 ms: 1.30x faster                                      |
| scimark_fft              | 466 ms                                                 | 359 ms: 1.30x faster                                       |
| 2to3                     | 348 ms                                                 | 269 ms: 1.29x faster                                       |
| pycparser                | 1.58 sec                                               | 1.23 sec: 1.28x faster                                     |
| sqlglot_optimize         | 69.2 ms                                                | 54.2 ms: 1.28x faster                                      |
| sympy_str                | 346 ms                                                 | 274 ms: 1.26x faster                                       |
| dulwich_log              | 84.3 ms                                                | 67.0 ms: 1.26x faster                                      |
| genshi_xml               | 66.0 ms                                                | 52.8 ms: 1.25x faster                                      |
| docutils                 | 3.30 sec                                               | 2.65 sec: 1.24x faster                                     |
| aiohttp                  | 1.44 ms                                                | 1.17 ms: 1.22x faster                                      |
| sympy_expand             | 566 ms                                                 | 462 ms: 1.22x faster                                       |
| djangocms                | 38.4 us                                                | 31.5 us: 1.22x faster                                      |
| gunicorn                 | 1.53 ms                                                | 1.27 ms: 1.20x faster                                      |
| bench_thread_pool        | 986 us                                                 | 838 us: 1.18x faster                                       |
| xml_etree_generate       | 99.4 ms                                                | 86.9 ms: 1.14x faster                                      |
| regex_v8                 | 27.8 ms                                                | 24.4 ms: 1.14x faster                                      |
| json_loads               | 31.2 us                                                | 27.9 us: 1.12x faster                                      |
| meteor_contest           | 120 ms                                                 | 108 ms: 1.10x faster                                       |
| json                     | 5.69 ms                                                | 5.19 ms: 1.10x faster                                      |
| pathlib                  | 20.5 ms                                                | 18.7 ms: 1.09x faster                                      |
| mdp                      | 2.85 sec                                               | 2.61 sec: 1.09x faster                                     |
| xml_etree_iterparse      | 115 ms                                                 | 107 ms: 1.08x faster                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.51 ms: 1.07x faster                                      |
| sqlite_synth             | 3.02 us                                                | 2.87 us: 1.05x faster                                      |
| xml_etree_parse          | 168 ms                                                 | 160 ms: 1.05x faster                                       |
| unpickle_list            | 5.20 us                                                | 5.09 us: 1.02x faster                                      |
| gc_traversal             | 3.62 ms                                                | 3.55 ms: 1.02x faster                                      |
| regex_dna                | 227 ms                                                 | 224 ms: 1.01x faster                                       |
| bench_mp_pool            | 24.0 ms                                                | 23.8 ms: 1.01x faster                                      |
| pidigits                 | 191 ms                                                 | 189 ms: 1.01x faster                                       |
| asyncio_websockets       | 559 ms                                                 | 563 ms: 1.01x slower                                       |
| flaskblogging            | 8.58 ms                                                | 8.75 ms: 1.02x slower                                      |
| async_generators         | 444 ms                                                 | 459 ms: 1.03x slower                                       |
| pickle_list              | 5.08 us                                                | 5.28 us: 1.04x slower                                      |
| unpickle                 | 14.4 us                                                | 15.4 us: 1.07x slower                                      |
| pickle                   | 10.7 us                                                | 12.0 us: 1.13x slower                                      |
| telco                    | 7.27 ms                                                | 8.41 ms: 1.16x slower                                      |
| pickle_dict              | 29.6 us                                                | 34.7 us: 1.17x slower                                      |
| coverage                 | 79.4 ms                                                | 96.3 ms: 1.21x slower                                      |
| python_startup_no_site   | 5.93 ms                                                | 8.87 ms: 1.50x slower                                      |
| Geometric mean           | (ref)                                                  | 1.34x faster                                               |

Benchmark hidden because not significant (2): mypy2, regex_effbot
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.07x