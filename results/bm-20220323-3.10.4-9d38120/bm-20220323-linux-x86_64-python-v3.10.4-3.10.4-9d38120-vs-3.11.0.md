
# Results vs. 3.11.0

- fork: python
- ref: v3.10.4
- machine: linux-x86_64
- commit hash: 9d38120
- commit date: 2022-03-23
- overall geometric mean: 1.24x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 336 ms: 1.30x slower                                   |
| chameleon      | 6.47 ms                                                | 9.06 ms: 1.40x slower                                  |
| docutils       | 2.63 sec                                               | 3.17 sec: 1.21x slower                                 |
| html5lib       | 64.5 ms                                                | 85.9 ms: 1.33x slower                                  |
| tornado_http   | 96.3 ms                                                | 127 ms: 1.32x slower                                   |
| Geometric mean | (ref)                                                  | 1.31x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                   |
| float          | 77.2 ms                                                | 111 ms: 1.43x slower                                   |
| nbody          | 93.1 ms                                                | 142 ms: 1.52x slower                                   |
| Geometric mean | (ref)                                                  | 1.28x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.23 ms: 1.24x faster                                  |
| regex_dna      | 204 ms                                                 | 222 ms: 1.09x slower                                   |
| regex_v8       | 22.0 ms                                                | 25.0 ms: 1.14x slower                                  |
| regex_compile  | 138 ms                                                 | 177 ms: 1.28x slower                                   |
| Geometric mean | (ref)                                                  | 1.06x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_dict          | 31.1 us                                                | 27.3 us: 1.14x faster                                  |
| unpickle_list        | 4.91 us                                                | 4.82 us: 1.02x faster                                  |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                  |
| xml_etree_parse      | 158 ms                                                 | 163 ms: 1.03x slower                                   |
| unpickle             | 13.7 us                                                | 14.1 us: 1.03x slower                                  |
| xml_etree_iterparse  | 104 ms                                                 | 111 ms: 1.07x slower                                   |
| json_dumps           | 12.6 ms                                                | 13.5 ms: 1.08x slower                                  |
| json_loads           | 26.5 us                                                | 28.8 us: 1.09x slower                                  |
| pickle_list          | 4.11 us                                                | 4.56 us: 1.11x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 94.2 ms: 1.24x slower                                  |
| tomli_loads          | 2.22 sec                                               | 2.92 sec: 1.31x slower                                 |
| unpickle_pure_python | 228 us                                                 | 300 us: 1.32x slower                                   |
| xml_etree_process    | 53.9 ms                                                | 74.9 ms: 1.39x slower                                  |
| pickle_pure_python   | 306 us                                                 | 455 us: 1.49x slower                                   |
| Geometric mean       | (ref)                                                  | 1.13x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 6.01 ms                                                | 5.82 ms: 1.03x faster                                  |
| python_startup         | 8.52 ms                                                | 14.2 ms: 1.66x slower                                  |
| Geometric mean         | (ref)                                                  | 1.27x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 63.3 ms: 1.22x slower                                  |
| genshi_text     | 21.6 ms                                                | 30.3 ms: 1.41x slower                                  |
| django_template | 32.6 ms                                                | 45.9 ms: 1.41x slower                                  |
| mako            | 10.1 ms                                                | 14.8 ms: 1.46x slower                                  |
| Geometric mean  | (ref)                                                  | 1.37x slower                                           |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| coverage                 | 100 ms                                                 | 72.8 ms: 1.37x faster                                  |
| regex_effbot             | 3.99 ms                                                | 3.23 ms: 1.24x faster                                  |
| pickle_dict              | 31.1 us                                                | 27.3 us: 1.14x faster                                  |
| gc_traversal             | 4.02 ms                                                | 3.84 ms: 1.05x faster                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 3.01 sec: 1.04x faster                                 |
| pidigits                 | 198 ms                                                 | 190 ms: 1.04x faster                                   |
| python_startup_no_site   | 6.01 ms                                                | 5.82 ms: 1.03x faster                                  |
| unpickle_list            | 4.91 us                                                | 4.82 us: 1.02x faster                                  |
| asyncio_tcp              | 922 ms                                                 | 925 ms: 1.00x slower                                   |
| pickle                   | 10.1 us                                                | 10.3 us: 1.02x slower                                  |
| xml_etree_parse          | 158 ms                                                 | 163 ms: 1.03x slower                                   |
| unpickle                 | 13.7 us                                                | 14.1 us: 1.03x slower                                  |
| generators               | 73.5 ms                                                | 76.8 ms: 1.04x slower                                  |
| typing_runtime_protocols | 486 us                                                 | 510 us: 1.05x slower                                   |
| xml_etree_iterparse      | 104 ms                                                 | 111 ms: 1.07x slower                                   |
| json_dumps               | 12.6 ms                                                | 13.5 ms: 1.08x slower                                  |
| meteor_contest           | 107 ms                                                 | 115 ms: 1.08x slower                                   |
| mdp                      | 2.62 sec                                               | 2.82 sec: 1.08x slower                                 |
| regex_dna                | 204 ms                                                 | 222 ms: 1.09x slower                                   |
| json_loads               | 26.5 us                                                | 28.8 us: 1.09x slower                                  |
| json                     | 4.94 ms                                                | 5.42 ms: 1.10x slower                                  |
| pathlib                  | 18.2 ms                                                | 20.0 ms: 1.10x slower                                  |
| djangocms                | 32.4 us                                                | 35.9 us: 1.11x slower                                  |
| pickle_list              | 4.11 us                                                | 4.56 us: 1.11x slower                                  |
| sympy_sum                | 167 ms                                                 | 185 ms: 1.11x slower                                   |
| create_gc_cycles         | 1.49 ms                                                | 1.67 ms: 1.12x slower                                  |
| pylint                   | 465 ms                                                 | 525 ms: 1.13x slower                                   |
| sympy_str                | 290 ms                                                 | 328 ms: 1.13x slower                                   |
| regex_v8                 | 22.0 ms                                                | 25.0 ms: 1.14x slower                                  |
| sympy_expand             | 475 ms                                                 | 545 ms: 1.15x slower                                   |
| async_generators         | 368 ms                                                 | 425 ms: 1.15x slower                                   |
| bench_thread_pool        | 819 us                                                 | 947 us: 1.16x slower                                   |
| sympy_integrate          | 21.0 ms                                                | 24.3 ms: 1.16x slower                                  |
| flaskblogging            | 7.12 ms                                                | 8.27 ms: 1.16x slower                                  |
| sqlite_synth             | 2.52 us                                                | 2.93 us: 1.16x slower                                  |
| dask                     | 360 ms                                                 | 423 ms: 1.17x slower                                   |
| sqlalchemy_imperative    | 17.9 ms                                                | 21.2 ms: 1.18x slower                                  |
| dulwich_log              | 63.7 ms                                                | 75.9 ms: 1.19x slower                                  |
| comprehensions           | 22.4 us                                                | 26.8 us: 1.20x slower                                  |
| sqlalchemy_declarative   | 138 ms                                                 | 165 ms: 1.20x slower                                   |
| nqueens                  | 83.4 ms                                                | 100 ms: 1.20x slower                                   |
| docutils                 | 2.63 sec                                               | 3.17 sec: 1.21x slower                                 |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 5.45 ms: 1.21x slower                                  |
| genshi_xml               | 51.8 ms                                                | 63.3 ms: 1.22x slower                                  |
| sqlglot_optimize         | 53.1 ms                                                | 65.3 ms: 1.23x slower                                  |
| xml_etree_generate       | 76.2 ms                                                | 94.2 ms: 1.24x slower                                  |
| gunicorn                 | 1.18 ms                                                | 1.46 ms: 1.24x slower                                  |
| coroutines               | 25.5 ms                                                | 31.8 ms: 1.25x slower                                  |
| fannkuch                 | 388 ms                                                 | 486 ms: 1.25x slower                                   |
| sqlglot_normalize        | 108 ms                                                 | 135 ms: 1.25x slower                                   |
| aiohttp                  | 1.10 ms                                                | 1.38 ms: 1.26x slower                                  |
| pycparser                | 1.18 sec                                               | 1.50 sec: 1.27x slower                                 |
| regex_compile            | 138 ms                                                 | 177 ms: 1.28x slower                                   |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 951 ms: 1.29x slower                                   |
| scimark_fft              | 328 ms                                                 | 424 ms: 1.29x slower                                   |
| deepcopy                 | 342 us                                                 | 442 us: 1.29x slower                                   |
| 2to3                     | 259 ms                                                 | 336 ms: 1.30x slower                                   |
| deepcopy_reduce          | 2.94 us                                                | 3.82 us: 1.30x slower                                  |
| tomli_loads              | 2.22 sec                                               | 2.92 sec: 1.31x slower                                 |
| unpickle_pure_python     | 228 us                                                 | 300 us: 1.32x slower                                   |
| tornado_http             | 96.3 ms                                                | 127 ms: 1.32x slower                                   |
| html5lib                 | 64.5 ms                                                | 85.9 ms: 1.33x slower                                  |
| logging_format           | 6.68 us                                                | 8.91 us: 1.33x slower                                  |
| logging_simple           | 6.03 us                                                | 8.07 us: 1.34x slower                                  |
| pprint_safe_repr         | 701 ms                                                 | 955 ms: 1.36x slower                                   |
| async_tree_memoization   | 627 ms                                                 | 854 ms: 1.36x slower                                   |
| async_tree_none          | 526 ms                                                 | 717 ms: 1.36x slower                                   |
| pprint_pformat           | 1.46 sec                                               | 1.99 sec: 1.36x slower                                 |
| thrift                   | 756 us                                                 | 1.03 ms: 1.37x slower                                  |
| async_tree_io            | 1.30 sec                                               | 1.77 sec: 1.37x slower                                 |
| xml_etree_process        | 53.9 ms                                                | 74.9 ms: 1.39x slower                                  |
| chameleon                | 6.47 ms                                                | 9.06 ms: 1.40x slower                                  |
| genshi_text              | 21.6 ms                                                | 30.3 ms: 1.41x slower                                  |
| django_template          | 32.6 ms                                                | 45.9 ms: 1.41x slower                                  |
| deepcopy_memo            | 37.0 us                                                | 52.3 us: 1.41x slower                                  |
| float                    | 77.2 ms                                                | 111 ms: 1.43x slower                                   |
| sqlglot_transpile        | 1.70 ms                                                | 2.45 ms: 1.44x slower                                  |
| mako                     | 10.1 ms                                                | 14.8 ms: 1.46x slower                                  |
| sqlglot_parse            | 1.40 ms                                                | 2.06 ms: 1.47x slower                                  |
| scimark_lu               | 110 ms                                                 | 163 ms: 1.49x slower                                   |
| pickle_pure_python       | 306 us                                                 | 455 us: 1.49x slower                                   |
| hexiom                   | 6.37 ms                                                | 9.53 ms: 1.49x slower                                  |
| spectral_norm            | 100 ms                                                 | 150 ms: 1.50x slower                                   |
| unpack_sequence          | 43.1 ns                                                | 64.7 ns: 1.50x slower                                  |
| nbody                    | 93.1 ms                                                | 142 ms: 1.52x slower                                   |
| chaos                    | 69.2 ms                                                | 106 ms: 1.54x slower                                   |
| raytrace                 | 297 ms                                                 | 464 ms: 1.56x slower                                   |
| crypto_pyaes             | 74.7 ms                                                | 118 ms: 1.59x slower                                   |
| scimark_monte_carlo      | 68.1 ms                                                | 108 ms: 1.59x slower                                   |
| richards_super           | 56.8 ms                                                | 90.7 ms: 1.60x slower                                  |
| pyflate                  | 418 ms                                                 | 673 ms: 1.61x slower                                   |
| go                       | 140 ms                                                 | 229 ms: 1.64x slower                                   |
| richards                 | 45.7 ms                                                | 74.9 ms: 1.64x slower                                  |
| python_startup           | 8.52 ms                                                | 14.2 ms: 1.66x slower                                  |
| scimark_sor              | 118 ms                                                 | 197 ms: 1.67x slower                                   |
| logging_silent           | 101 ns                                                 | 175 ns: 1.73x slower                                   |
| deltablue                | 3.67 ms                                                | 7.42 ms: 2.02x slower                                  |
| Geometric mean           | (ref)                                                  | 1.24x slower                                           |

Benchmark hidden because not significant (3): telco, bench_mp_pool, mypy2
