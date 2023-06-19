
# Results vs. 3.10.4

- fork: python
- ref: 6baddd9fb25e03040c1c
- machine: linux-x86_64
- commit hash: 6baddd9
- commit date: 2023-06-18
- overall geometric mean: 1.28x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-linux-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 268 ms: 1.26x faster                                                   |
| docutils       | 3.17 sec                                               | 2.71 sec: 1.17x faster                                                 |
| tornado_http   | 127 ms                                                 | 99.1 ms: 1.29x faster                                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-linux-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.9 ms: 1.59x faster                                                  |
| float          | 111 ms                                                 | 79.6 ms: 1.39x faster                                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-linux-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 143 ms: 1.23x faster                                                   |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                  |
| regex_dna      | 222 ms                                                 | 211 ms: 1.05x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.66 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-linux-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 310 us: 1.47x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 215 us: 1.40x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.74 ms: 1.39x faster                                                  |
| tomli_loads          | 2.92 sec                                               | 2.18 sec: 1.34x faster                                                 |
| xml_etree_process    | 74.9 ms                                                | 58.7 ms: 1.28x faster                                                  |
| json_loads           | 28.8 us                                                | 25.0 us: 1.15x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 84.6 ms: 1.11x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                                   |
| unpickle_list        | 4.82 us                                                | 5.02 us: 1.04x slower                                                  |
| pickle               | 10.3 us                                                | 10.8 us: 1.05x slower                                                  |
| unpickle             | 14.1 us                                                | 15.2 us: 1.07x slower                                                  |
| pickle_dict          | 27.3 us                                                | 30.7 us: 1.13x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-linux-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.31 ms: 1.52x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.75 ms: 1.16x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-linux-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230618-linux-x86_64-python-6baddd9fb25e03040c1c-3.12.0b2+-6baddd9 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 145 us: 3.52x faster                                                   |
| generators               | 76.8 ms                                                | 32.2 ms: 2.38x faster                                                  |
| deltablue                | 7.42 ms                                                | 3.45 ms: 2.15x faster                                                  |
| richards_super           | 90.7 ms                                                | 49.5 ms: 1.83x faster                                                  |
| asyncio_tcp              | 925 ms                                                 | 512 ms: 1.81x faster                                                   |
| logging_silent           | 175 ns                                                 | 97.2 ns: 1.80x faster                                                  |
| richards                 | 74.9 ms                                                | 44.0 ms: 1.70x faster                                                  |
| chaos                    | 106 ms                                                 | 62.8 ms: 1.69x faster                                                  |
| go                       | 229 ms                                                 | 136 ms: 1.68x faster                                                   |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                 |
| scimark_sor              | 197 ms                                                 | 119 ms: 1.66x faster                                                   |
| nbody                    | 142 ms                                                 | 88.9 ms: 1.59x faster                                                  |
| raytrace                 | 464 ms                                                 | 292 ms: 1.59x faster                                                   |
| hexiom                   | 9.53 ms                                                | 6.06 ms: 1.57x faster                                                  |
| sqlglot_parse            | 2.06 ms                                                | 1.33 ms: 1.55x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 1.15 sec: 1.54x faster                                                 |
| crypto_pyaes             | 118 ms                                                 | 77.3 ms: 1.53x faster                                                  |
| async_tree_none          | 717 ms                                                 | 468 ms: 1.53x faster                                                   |
| scimark_monte_carlo      | 108 ms                                                 | 71.0 ms: 1.53x faster                                                  |
| pyflate                  | 673 ms                                                 | 442 ms: 1.52x faster                                                   |
| python_startup           | 14.2 ms                                                | 9.31 ms: 1.52x faster                                                  |
| async_tree_memoization   | 854 ms                                                 | 573 ms: 1.49x faster                                                   |
| sqlglot_transpile        | 2.45 ms                                                | 1.64 ms: 1.49x faster                                                  |
| pickle_pure_python       | 455 us                                                 | 310 us: 1.47x faster                                                   |
| scimark_lu               | 163 ms                                                 | 113 ms: 1.45x faster                                                   |
| coroutines               | 31.8 ms                                                | 22.0 ms: 1.44x faster                                                  |
| spectral_norm            | 150 ms                                                 | 106 ms: 1.42x faster                                                   |
| unpickle_pure_python     | 300 us                                                 | 215 us: 1.40x faster                                                   |
| deepcopy_memo            | 52.3 us                                                | 37.5 us: 1.39x faster                                                  |
| json_dumps               | 13.5 ms                                                | 9.74 ms: 1.39x faster                                                  |
| float                    | 111 ms                                                 | 79.6 ms: 1.39x faster                                                  |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                  |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 708 ms: 1.34x faster                                                   |
| tomli_loads              | 2.92 sec                                               | 2.18 sec: 1.34x faster                                                 |
| pycparser                | 1.50 sec                                               | 1.14 sec: 1.31x faster                                                 |
| pprint_pformat           | 1.99 sec                                               | 1.52 sec: 1.31x faster                                                 |
| comprehensions           | 26.8 us                                                | 20.7 us: 1.29x faster                                                  |
| pprint_safe_repr         | 955 ms                                                 | 739 ms: 1.29x faster                                                   |
| logging_format           | 8.91 us                                                | 6.92 us: 1.29x faster                                                  |
| tornado_http             | 127 ms                                                 | 99.1 ms: 1.29x faster                                                  |
| fannkuch                 | 486 ms                                                 | 379 ms: 1.28x faster                                                   |
| logging_simple           | 8.07 us                                                | 6.31 us: 1.28x faster                                                  |
| xml_etree_process        | 74.9 ms                                                | 58.7 ms: 1.28x faster                                                  |
| 2to3                     | 336 ms                                                 | 268 ms: 1.26x faster                                                   |
| nqueens                  | 100 ms                                                 | 79.7 ms: 1.25x faster                                                  |
| sqlglot_normalize        | 135 ms                                                 | 108 ms: 1.25x faster                                                   |
| deepcopy                 | 442 us                                                 | 355 us: 1.25x faster                                                   |
| regex_compile            | 177 ms                                                 | 143 ms: 1.23x faster                                                   |
| sqlglot_optimize         | 65.3 ms                                                | 53.6 ms: 1.22x faster                                                  |
| deepcopy_reduce          | 3.82 us                                                | 3.14 us: 1.22x faster                                                  |
| unpack_sequence          | 64.7 ns                                                | 54.8 ns: 1.18x faster                                                  |
| scimark_fft              | 424 ms                                                 | 361 ms: 1.17x faster                                                   |
| docutils                 | 3.17 sec                                               | 2.71 sec: 1.17x faster                                                 |
| json_loads               | 28.8 us                                                | 25.0 us: 1.15x faster                                                  |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.76 ms: 1.15x faster                                                  |
| sqlalchemy_declarative   | 165 ms                                                 | 144 ms: 1.14x faster                                                   |
| bench_thread_pool        | 947 us                                                 | 828 us: 1.14x faster                                                   |
| sqlalchemy_imperative    | 21.2 ms                                                | 18.5 ms: 1.14x faster                                                  |
| json                     | 5.42 ms                                                | 4.76 ms: 1.14x faster                                                  |
| regex_v8                 | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                  |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.11x faster                                                  |
| dulwich_log              | 75.9 ms                                                | 68.1 ms: 1.11x faster                                                  |
| xml_etree_generate       | 94.2 ms                                                | 84.6 ms: 1.11x faster                                                  |
| pathlib                  | 20.0 ms                                                | 18.1 ms: 1.11x faster                                                  |
| mdp                      | 2.82 sec                                               | 2.55 sec: 1.11x faster                                                 |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.09x faster                                                   |
| gc_traversal             | 3.84 ms                                                | 3.55 ms: 1.08x faster                                                  |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                   |
| sqlite_synth             | 2.93 us                                                | 2.73 us: 1.07x faster                                                  |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                                   |
| regex_dna                | 222 ms                                                 | 211 ms: 1.05x faster                                                   |
| async_generators         | 425 ms                                                 | 439 ms: 1.03x slower                                                   |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| unpickle_list            | 4.82 us                                                | 5.02 us: 1.04x slower                                                  |
| pickle                   | 10.3 us                                                | 10.8 us: 1.05x slower                                                  |
| telco                    | 6.54 ms                                                | 6.93 ms: 1.06x slower                                                  |
| unpickle                 | 14.1 us                                                | 15.2 us: 1.07x slower                                                  |
| pickle_dict              | 27.3 us                                                | 30.7 us: 1.13x slower                                                  |
| regex_effbot             | 3.23 ms                                                | 3.66 ms: 1.13x slower                                                  |
| python_startup_no_site   | 5.82 ms                                                | 6.75 ms: 1.16x slower                                                  |
| dask                     | 423 ms                                                 | 534 ms: 1.26x slower                                                   |
| coverage                 | 72.8 ms                                                | 95.0 ms: 1.30x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.28x faster                                                           |

Benchmark hidden because not significant (3): bench_mp_pool, pickle_list, mypy2
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
