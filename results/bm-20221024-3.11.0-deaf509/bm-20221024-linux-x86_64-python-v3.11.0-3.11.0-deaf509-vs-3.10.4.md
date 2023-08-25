
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0
- machine: linux-x86_64
- commit hash: deaf509
- commit date: 2022-10-24
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 259 ms: 1.30x faster                                   |
| chameleon      | 9.06 ms                                                | 6.47 ms: 1.40x faster                                  |
| docutils       | 3.17 sec                                               | 2.63 sec: 1.21x faster                                 |
| html5lib       | 85.9 ms                                                | 64.5 ms: 1.33x faster                                  |
| tornado_http   | 127 ms                                                 | 96.3 ms: 1.32x faster                                  |
| Geometric mean | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 93.1 ms: 1.52x faster                                  |
| float          | 111 ms                                                 | 77.2 ms: 1.43x faster                                  |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 138 ms: 1.28x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                  |
| regex_dna      | 222 ms                                                 | 204 ms: 1.09x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.99 ms: 1.24x slower                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 306 us: 1.49x faster                                   |
| xml_etree_process    | 74.9 ms                                                | 53.9 ms: 1.39x faster                                  |
| unpickle_pure_python | 300 us                                                 | 228 us: 1.32x faster                                   |
| tomli_loads          | 2.92 sec                                               | 2.22 sec: 1.31x faster                                 |
| xml_etree_generate   | 94.2 ms                                                | 76.2 ms: 1.24x faster                                  |
| pickle_list          | 4.56 us                                                | 4.11 us: 1.11x faster                                  |
| json_loads           | 28.8 us                                                | 26.5 us: 1.09x faster                                  |
| json_dumps           | 13.5 ms                                                | 12.6 ms: 1.08x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                   |
| unpickle             | 14.1 us                                                | 13.7 us: 1.03x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 158 ms: 1.03x faster                                   |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                  |
| unpickle_list        | 4.82 us                                                | 4.91 us: 1.02x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.1 us: 1.14x slower                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.52 ms: 1.66x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.01 ms: 1.03x slower                                  |
| Geometric mean         | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.1 ms: 1.46x faster                                  |
| django_template | 45.9 ms                                                | 32.6 ms: 1.41x faster                                  |
| genshi_text     | 30.3 ms                                                | 21.6 ms: 1.41x faster                                  |
| genshi_xml      | 63.3 ms                                                | 51.8 ms: 1.22x faster                                  |
| Geometric mean  | (ref)                                                  | 1.37x faster                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue                | 7.42 ms                                                | 3.67 ms: 2.02x faster                                  |
| logging_silent           | 175 ns                                                 | 101 ns: 1.73x faster                                   |
| scimark_sor              | 197 ms                                                 | 118 ms: 1.67x faster                                   |
| python_startup           | 14.2 ms                                                | 8.52 ms: 1.66x faster                                  |
| richards                 | 74.9 ms                                                | 45.7 ms: 1.64x faster                                  |
| go                       | 229 ms                                                 | 140 ms: 1.64x faster                                   |
| pyflate                  | 673 ms                                                 | 418 ms: 1.61x faster                                   |
| richards_super           | 90.7 ms                                                | 56.8 ms: 1.60x faster                                  |
| scimark_monte_carlo      | 108 ms                                                 | 68.1 ms: 1.59x faster                                  |
| crypto_pyaes             | 118 ms                                                 | 74.7 ms: 1.59x faster                                  |
| raytrace                 | 464 ms                                                 | 297 ms: 1.56x faster                                   |
| chaos                    | 106 ms                                                 | 69.2 ms: 1.54x faster                                  |
| nbody                    | 142 ms                                                 | 93.1 ms: 1.52x faster                                  |
| unpack_sequence          | 64.7 ns                                                | 43.1 ns: 1.50x faster                                  |
| spectral_norm            | 150 ms                                                 | 100 ms: 1.50x faster                                   |
| hexiom                   | 9.53 ms                                                | 6.37 ms: 1.49x faster                                  |
| pickle_pure_python       | 455 us                                                 | 306 us: 1.49x faster                                   |
| scimark_lu               | 163 ms                                                 | 110 ms: 1.49x faster                                   |
| sqlglot_parse            | 2.06 ms                                                | 1.40 ms: 1.47x faster                                  |
| mako                     | 14.8 ms                                                | 10.1 ms: 1.46x faster                                  |
| sqlglot_transpile        | 2.45 ms                                                | 1.70 ms: 1.44x faster                                  |
| float                    | 111 ms                                                 | 77.2 ms: 1.43x faster                                  |
| deepcopy_memo            | 52.3 us                                                | 37.0 us: 1.41x faster                                  |
| django_template          | 45.9 ms                                                | 32.6 ms: 1.41x faster                                  |
| genshi_text              | 30.3 ms                                                | 21.6 ms: 1.41x faster                                  |
| chameleon                | 9.06 ms                                                | 6.47 ms: 1.40x faster                                  |
| xml_etree_process        | 74.9 ms                                                | 53.9 ms: 1.39x faster                                  |
| async_tree_io            | 1.77 sec                                               | 1.30 sec: 1.37x faster                                 |
| thrift                   | 1.03 ms                                                | 756 us: 1.37x faster                                   |
| pprint_pformat           | 1.99 sec                                               | 1.46 sec: 1.36x faster                                 |
| async_tree_none          | 717 ms                                                 | 526 ms: 1.36x faster                                   |
| async_tree_memoization   | 854 ms                                                 | 627 ms: 1.36x faster                                   |
| pprint_safe_repr         | 955 ms                                                 | 701 ms: 1.36x faster                                   |
| logging_simple           | 8.07 us                                                | 6.03 us: 1.34x faster                                  |
| logging_format           | 8.91 us                                                | 6.68 us: 1.33x faster                                  |
| html5lib                 | 85.9 ms                                                | 64.5 ms: 1.33x faster                                  |
| tornado_http             | 127 ms                                                 | 96.3 ms: 1.32x faster                                  |
| unpickle_pure_python     | 300 us                                                 | 228 us: 1.32x faster                                   |
| tomli_loads              | 2.92 sec                                               | 2.22 sec: 1.31x faster                                 |
| deepcopy_reduce          | 3.82 us                                                | 2.94 us: 1.30x faster                                  |
| 2to3                     | 336 ms                                                 | 259 ms: 1.30x faster                                   |
| deepcopy                 | 442 us                                                 | 342 us: 1.29x faster                                   |
| scimark_fft              | 424 ms                                                 | 328 ms: 1.29x faster                                   |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 739 ms: 1.29x faster                                   |
| regex_compile            | 177 ms                                                 | 138 ms: 1.28x faster                                   |
| pycparser                | 1.50 sec                                               | 1.18 sec: 1.27x faster                                 |
| aiohttp                  | 1.38 ms                                                | 1.10 ms: 1.26x faster                                  |
| sqlglot_normalize        | 135 ms                                                 | 108 ms: 1.25x faster                                   |
| fannkuch                 | 486 ms                                                 | 388 ms: 1.25x faster                                   |
| coroutines               | 31.8 ms                                                | 25.5 ms: 1.25x faster                                  |
| gunicorn                 | 1.46 ms                                                | 1.18 ms: 1.24x faster                                  |
| xml_etree_generate       | 94.2 ms                                                | 76.2 ms: 1.24x faster                                  |
| sqlglot_optimize         | 65.3 ms                                                | 53.1 ms: 1.23x faster                                  |
| genshi_xml               | 63.3 ms                                                | 51.8 ms: 1.22x faster                                  |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.50 ms: 1.21x faster                                  |
| docutils                 | 3.17 sec                                               | 2.63 sec: 1.21x faster                                 |
| nqueens                  | 100 ms                                                 | 83.4 ms: 1.20x faster                                  |
| sqlalchemy_declarative   | 165 ms                                                 | 138 ms: 1.20x faster                                   |
| comprehensions           | 26.8 us                                                | 22.4 us: 1.20x faster                                  |
| dulwich_log              | 75.9 ms                                                | 63.7 ms: 1.19x faster                                  |
| sqlalchemy_imperative    | 21.2 ms                                                | 17.9 ms: 1.18x faster                                  |
| dask                     | 423 ms                                                 | 360 ms: 1.17x faster                                   |
| sqlite_synth             | 2.93 us                                                | 2.52 us: 1.16x faster                                  |
| flaskblogging            | 8.27 ms                                                | 7.12 ms: 1.16x faster                                  |
| sympy_integrate          | 24.3 ms                                                | 21.0 ms: 1.16x faster                                  |
| bench_thread_pool        | 947 us                                                 | 819 us: 1.16x faster                                   |
| async_generators         | 425 ms                                                 | 368 ms: 1.15x faster                                   |
| sympy_expand             | 545 ms                                                 | 475 ms: 1.15x faster                                   |
| regex_v8                 | 25.0 ms                                                | 22.0 ms: 1.14x faster                                  |
| sympy_str                | 328 ms                                                 | 290 ms: 1.13x faster                                   |
| pylint                   | 525 ms                                                 | 465 ms: 1.13x faster                                   |
| create_gc_cycles         | 1.67 ms                                                | 1.49 ms: 1.12x faster                                  |
| sympy_sum                | 185 ms                                                 | 167 ms: 1.11x faster                                   |
| pickle_list              | 4.56 us                                                | 4.11 us: 1.11x faster                                  |
| djangocms                | 35.9 us                                                | 32.4 us: 1.11x faster                                  |
| pathlib                  | 20.0 ms                                                | 18.2 ms: 1.10x faster                                  |
| json                     | 5.42 ms                                                | 4.94 ms: 1.10x faster                                  |
| json_loads               | 28.8 us                                                | 26.5 us: 1.09x faster                                  |
| regex_dna                | 222 ms                                                 | 204 ms: 1.09x faster                                   |
| mdp                      | 2.82 sec                                               | 2.62 sec: 1.08x faster                                 |
| meteor_contest           | 115 ms                                                 | 107 ms: 1.08x faster                                   |
| json_dumps               | 13.5 ms                                                | 12.6 ms: 1.08x faster                                  |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.07x faster                                   |
| typing_runtime_protocols | 510 us                                                 | 486 us: 1.05x faster                                   |
| generators               | 76.8 ms                                                | 73.5 ms: 1.04x faster                                  |
| unpickle                 | 14.1 us                                                | 13.7 us: 1.03x faster                                  |
| xml_etree_parse          | 163 ms                                                 | 158 ms: 1.03x faster                                   |
| pickle                   | 10.3 us                                                | 10.1 us: 1.02x faster                                  |
| asyncio_tcp              | 925 ms                                                 | 922 ms: 1.00x faster                                   |
| unpickle_list            | 4.82 us                                                | 4.91 us: 1.02x slower                                  |
| python_startup_no_site   | 5.82 ms                                                | 6.01 ms: 1.03x slower                                  |
| pidigits                 | 190 ms                                                 | 198 ms: 1.04x slower                                   |
| asyncio_tcp_ssl          | 3.01 sec                                               | 3.14 sec: 1.04x slower                                 |
| gc_traversal             | 3.84 ms                                                | 4.02 ms: 1.05x slower                                  |
| pickle_dict              | 27.3 us                                                | 31.1 us: 1.14x slower                                  |
| regex_effbot             | 3.23 ms                                                | 3.99 ms: 1.24x slower                                  |
| coverage                 | 72.8 ms                                                | 100 ms: 1.37x slower                                   |
| Geometric mean           | (ref)                                                  | 1.24x faster                                           |

Benchmark hidden because not significant (3): mypy2, bench_mp_pool, telco


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x
