# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a1
- machine: linux-x86_64
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 0.64x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 276 ms: 1.26x faster                                       |
| chameleon      | 9.68 ms                                                | 7.13 ms: 1.36x faster                                      |
| docutils       | 3.30 sec                                               | 2.71 sec: 1.22x faster                                     |
| html5lib       | 88.9 ms                                                | 67.3 ms: 1.32x faster                                      |
| tornado_http   | 136 ms                                                 | 99.1 ms: 1.38x faster                                      |
| Geometric mean | (ref)                                                  | 1.31x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 728 ms                                                 | 446 ms: 1.63x faster                                       |
| async_tree_memoization  | 870 ms                                                 | 572 ms: 1.52x faster                                       |
| async_tree_io           | 1.77 sec                                               | 1.21 sec: 1.46x faster                                     |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 726 ms: 1.40x faster                                       |
| Geometric mean          | (ref)                                                  | 1.50x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 154 ms                                                 | 95.7 ms: 1.61x faster                                      |
| float          | 117 ms                                                 | 83.4 ms: 1.40x faster                                      |
| pidigits       | 191 ms                                                 | 190 ms: 1.00x faster                                       |
| Geometric mean | (ref)                                                  | 1.31x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 142 ms: 1.33x faster                                       |
| regex_v8       | 27.8 ms                                                | 25.3 ms: 1.10x faster                                      |
| regex_dna      | 227 ms                                                 | 209 ms: 1.08x faster                                       |
| regex_effbot   | 3.63 ms                                                | 3.56 ms: 1.02x faster                                      |
| Geometric mean | (ref)                                                  | 1.13x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 307 us: 1.58x faster                                       |
| unpickle_pure_python | 331 us                                                 | 226 us: 1.46x faster                                       |
| tomli_loads          | 3.14 sec                                               | 2.25 sec: 1.40x faster                                     |
| json_dumps           | 14.2 ms                                                | 10.5 ms: 1.35x faster                                      |
| xml_etree_process    | 79.1 ms                                                | 60.5 ms: 1.31x faster                                      |
| xml_etree_generate   | 99.4 ms                                                | 87.7 ms: 1.13x faster                                      |
| json_loads           | 31.2 us                                                | 27.9 us: 1.12x faster                                      |
| xml_etree_iterparse  | 115 ms                                                 | 107 ms: 1.08x faster                                       |
| xml_etree_parse      | 168 ms                                                 | 160 ms: 1.05x faster                                       |
| unpickle_list        | 5.20 us                                                | 5.08 us: 1.02x faster                                      |
| pickle_list          | 5.08 us                                                | 5.21 us: 1.03x slower                                      |
| unpickle             | 14.4 us                                                | 14.9 us: 1.04x slower                                      |
| pickle               | 10.7 us                                                | 11.7 us: 1.09x slower                                      |
| pickle_dict          | 29.6 us                                                | 35.4 us: 1.20x slower                                      |
| Geometric mean       | (ref)                                                  | 1.14x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 10.4 ms: 1.40x faster                                      |
| python_startup_no_site | 5.93 ms                                                | 7.05 ms: 1.19x slower                                      |
| Geometric mean         | (ref)                                                  | 1.09x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 16.3 ms                                                | 11.7 ms: 1.39x faster                                      |
| django_template | 48.2 ms                                                | 34.7 ms: 1.39x faster                                      |
| genshi_text     | 31.8 ms                                                | 23.1 ms: 1.38x faster                                      |
| genshi_xml      | 66.0 ms                                                | 52.0 ms: 1.27x faster                                      |
| Geometric mean  | (ref)                                                  | 1.36x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 153 us: 3.55x faster                                       |
| generators               | 80.1 ms                                                | 29.5 ms: 2.71x faster                                      |
| deltablue                | 7.91 ms                                                | 3.40 ms: 2.33x faster                                      |
| asyncio_tcp              | 922 ms                                                 | 498 ms: 1.85x faster                                       |
| chaos                    | 115 ms                                                 | 64.0 ms: 1.80x faster                                      |
| raytrace                 | 507 ms                                                 | 285 ms: 1.78x faster                                       |
| logging_silent           | 190 ns                                                 | 109 ns: 1.75x faster                                       |
| scimark_sor              | 220 ms                                                 | 127 ms: 1.73x faster                                       |
| crypto_pyaes             | 128 ms                                                 | 75.1 ms: 1.70x faster                                      |
| richards_super           | 94.7 ms                                                | 56.0 ms: 1.69x faster                                      |
| pylint                   | 551 ms                                                 | 328 ms: 1.68x faster                                       |
| scimark_monte_carlo      | 118 ms                                                 | 70.2 ms: 1.68x faster                                      |
| sqlglot_parse            | 2.17 ms                                                | 1.31 ms: 1.66x faster                                      |
| go                       | 240 ms                                                 | 146 ms: 1.64x faster                                       |
| async_tree_none          | 728 ms                                                 | 446 ms: 1.63x faster                                       |
| hexiom                   | 10.4 ms                                                | 6.40 ms: 1.62x faster                                      |
| nbody                    | 154 ms                                                 | 95.7 ms: 1.61x faster                                      |
| richards                 | 79.3 ms                                                | 49.9 ms: 1.59x faster                                      |
| pickle_pure_python       | 484 us                                                 | 307 us: 1.58x faster                                       |
| sqlglot_transpile        | 2.57 ms                                                | 1.63 ms: 1.58x faster                                      |
| async_tree_memoization   | 870 ms                                                 | 572 ms: 1.52x faster                                       |
| scimark_lu               | 176 ms                                                 | 117 ms: 1.50x faster                                       |
| pyflate                  | 716 ms                                                 | 482 ms: 1.49x faster                                       |
| coroutines               | 35.1 ms                                                | 23.7 ms: 1.48x faster                                      |
| deepcopy_memo            | 58.5 us                                                | 39.6 us: 1.48x faster                                      |
| unpickle_pure_python     | 331 us                                                 | 226 us: 1.46x faster                                       |
| async_tree_io            | 1.77 sec                                               | 1.21 sec: 1.46x faster                                     |
| spectral_norm            | 170 ms                                                 | 116 ms: 1.46x faster                                       |
| float                    | 117 ms                                                 | 83.4 ms: 1.40x faster                                      |
| python_startup           | 14.6 ms                                                | 10.4 ms: 1.40x faster                                      |
| asyncio_tcp_ssl          | 2.57 sec                                               | 1.83 sec: 1.40x faster                                     |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 726 ms: 1.40x faster                                       |
| tomli_loads              | 3.14 sec                                               | 2.25 sec: 1.40x faster                                     |
| mako                     | 16.3 ms                                                | 11.7 ms: 1.39x faster                                      |
| django_template          | 48.2 ms                                                | 34.7 ms: 1.39x faster                                      |
| genshi_text              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                      |
| logging_simple           | 8.30 us                                                | 6.02 us: 1.38x faster                                      |
| tornado_http             | 136 ms                                                 | 99.1 ms: 1.38x faster                                      |
| pprint_pformat           | 2.10 sec                                               | 1.54 sec: 1.36x faster                                     |
| chameleon                | 9.68 ms                                                | 7.13 ms: 1.36x faster                                      |
| logging_format           | 9.09 us                                                | 6.71 us: 1.35x faster                                      |
| pprint_safe_repr         | 1.02 sec                                               | 752 ms: 1.35x faster                                       |
| json_dumps               | 14.2 ms                                                | 10.5 ms: 1.35x faster                                      |
| comprehensions           | 28.8 us                                                | 21.5 us: 1.34x faster                                      |
| deepcopy                 | 479 us                                                 | 361 us: 1.33x faster                                       |
| regex_compile            | 188 ms                                                 | 142 ms: 1.33x faster                                       |
| sqlglot_normalize        | 143 ms                                                 | 108 ms: 1.32x faster                                       |
| html5lib                 | 88.9 ms                                                | 67.3 ms: 1.32x faster                                      |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.93 ms: 1.31x faster                                      |
| xml_etree_process        | 79.1 ms                                                | 60.5 ms: 1.31x faster                                      |
| nqueens                  | 106 ms                                                 | 81.0 ms: 1.31x faster                                      |
| deepcopy_reduce          | 4.17 us                                                | 3.20 us: 1.30x faster                                      |
| genshi_xml               | 66.0 ms                                                | 52.0 ms: 1.27x faster                                      |
| sqlglot_optimize         | 69.2 ms                                                | 54.5 ms: 1.27x faster                                      |
| pycparser                | 1.58 sec                                               | 1.24 sec: 1.27x faster                                     |
| fannkuch                 | 532 ms                                                 | 420 ms: 1.27x faster                                       |
| 2to3                     | 348 ms                                                 | 276 ms: 1.26x faster                                       |
| sympy_integrate          | 25.8 ms                                                | 20.8 ms: 1.24x faster                                      |
| scimark_fft              | 466 ms                                                 | 375 ms: 1.24x faster                                       |
| dulwich_log              | 84.3 ms                                                | 68.5 ms: 1.23x faster                                      |
| sympy_sum                | 196 ms                                                 | 160 ms: 1.23x faster                                       |
| aiohttp                  | 1.44 ms                                                | 1.18 ms: 1.22x faster                                      |
| sympy_expand             | 566 ms                                                 | 463 ms: 1.22x faster                                       |
| docutils                 | 3.30 sec                                               | 2.71 sec: 1.22x faster                                     |
| sympy_str                | 346 ms                                                 | 286 ms: 1.21x faster                                       |
| gunicorn                 | 1.53 ms                                                | 1.27 ms: 1.20x faster                                      |
| bench_thread_pool        | 986 us                                                 | 833 us: 1.18x faster                                       |
| xml_etree_generate       | 99.4 ms                                                | 87.7 ms: 1.13x faster                                      |
| json_loads               | 31.2 us                                                | 27.9 us: 1.12x faster                                      |
| mdp                      | 2.85 sec                                               | 2.58 sec: 1.10x faster                                     |
| regex_v8                 | 27.8 ms                                                | 25.3 ms: 1.10x faster                                      |
| regex_dna                | 227 ms                                                 | 209 ms: 1.08x faster                                       |
| meteor_contest           | 120 ms                                                 | 111 ms: 1.08x faster                                       |
| json                     | 5.69 ms                                                | 5.27 ms: 1.08x faster                                      |
| xml_etree_iterparse      | 115 ms                                                 | 107 ms: 1.08x faster                                       |
| create_gc_cycles         | 1.62 ms                                                | 1.50 ms: 1.08x faster                                      |
| xml_etree_parse          | 168 ms                                                 | 160 ms: 1.05x faster                                       |
| pathlib                  | 20.5 ms                                                | 19.6 ms: 1.05x faster                                      |
| unpickle_list            | 5.20 us                                                | 5.08 us: 1.02x faster                                      |
| regex_effbot             | 3.63 ms                                                | 3.56 ms: 1.02x faster                                      |
| bench_mp_pool            | 24.0 ms                                                | 23.9 ms: 1.01x faster                                      |
| pidigits                 | 191 ms                                                 | 190 ms: 1.00x faster                                       |
| asyncio_websockets       | 559 ms                                                 | 563 ms: 1.01x slower                                       |
| flaskblogging            | 8.58 ms                                                | 8.77 ms: 1.02x slower                                      |
| pickle_list              | 5.08 us                                                | 5.21 us: 1.03x slower                                      |
| sqlite_synth             | 3.02 us                                                | 3.11 us: 1.03x slower                                      |
| unpickle                 | 14.4 us                                                | 14.9 us: 1.04x slower                                      |
| async_generators         | 444 ms                                                 | 472 ms: 1.06x slower                                       |
| pickle                   | 10.7 us                                                | 11.7 us: 1.09x slower                                      |
| gc_traversal             | 3.62 ms                                                | 4.15 ms: 1.15x slower                                      |
| telco                    | 7.27 ms                                                | 8.41 ms: 1.16x slower                                      |
| python_startup_no_site   | 5.93 ms                                                | 7.05 ms: 1.19x slower                                      |
| pickle_dict              | 29.6 us                                                | 35.4 us: 1.20x slower                                      |
| dask                     | 441 ms                                                 | 544 ms: 1.23x slower                                       |
| thrift                   | 1.07 ms                                                | 9.24 ms: 8.62x slower                                      |
| coverage                 | 79.4 ms                                                | 700 ms: 8.81x slower                                       |
| Geometric mean           | (ref)                                                  | 1.24x faster                                               |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: djangocms, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (4) of results/bm-20231013-3.13.0a1-ad056f0-NOGIL/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 0.64x