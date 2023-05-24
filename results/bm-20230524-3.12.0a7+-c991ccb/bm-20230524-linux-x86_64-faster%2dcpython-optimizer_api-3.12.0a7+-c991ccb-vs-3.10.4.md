
# Results vs. 3.10.4

- fork: faster-cpython
- ref: optimizer_api
- machine: linux-x86_64
- commit hash: c991ccb
- commit date: 2023-05-24
- overall geometric mean: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230524-linux-x86_64-faster%2dcpython-optimizer_api-3.12.0a7+-c991ccb |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 271 ms: 1.24x faster                                                      |
| docutils       | 3.17 sec                                               | 2.74 sec: 1.16x faster                                                    |
| tornado_http   | 127 ms                                                 | 99.4 ms: 1.28x faster                                                     |
| Geometric mean | (ref)                                                  | 1.23x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230524-linux-x86_64-faster%2dcpython-optimizer_api-3.12.0a7+-c991ccb |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 91.4 ms: 1.55x faster                                                     |
| float          | 111 ms                                                 | 82.0 ms: 1.35x faster                                                     |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.26x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230524-linux-x86_64-faster%2dcpython-optimizer_api-3.12.0a7+-c991ccb |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.22x faster                                                      |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                     |
| regex_dna      | 222 ms                                                 | 210 ms: 1.06x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.83 ms: 1.18x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230524-linux-x86_64-faster%2dcpython-optimizer_api-3.12.0a7+-c991ccb |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 315 us: 1.45x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 217 us: 1.38x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.82 ms: 1.38x faster                                                     |
| tomli_loads          | 2.92 sec                                               | 2.21 sec: 1.32x faster                                                    |
| xml_etree_process    | 74.9 ms                                                | 59.3 ms: 1.26x faster                                                     |
| json_loads           | 28.8 us                                                | 24.7 us: 1.17x faster                                                     |
| xml_etree_generate   | 94.2 ms                                                | 85.7 ms: 1.10x faster                                                     |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                      |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                                      |
| pickle_list          | 4.56 us                                                | 4.63 us: 1.02x slower                                                     |
| unpickle             | 14.1 us                                                | 14.8 us: 1.04x slower                                                     |
| pickle               | 10.3 us                                                | 10.8 us: 1.05x slower                                                     |
| unpickle_list        | 4.82 us                                                | 5.09 us: 1.06x slower                                                     |
| pickle_dict          | 27.3 us                                                | 32.6 us: 1.19x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230524-linux-x86_64-faster%2dcpython-optimizer_api-3.12.0a7+-c991ccb |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.34 ms: 1.52x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.79 ms: 1.17x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.14x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230524-linux-x86_64-faster%2dcpython-optimizer_api-3.12.0a7+-c991ccb |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.9 ms: 1.35x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230524-linux-x86_64-faster%2dcpython-optimizer_api-3.12.0a7+-c991ccb |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 141 us: 3.61x faster                                                      |
| generators               | 76.8 ms                                                | 32.1 ms: 2.39x faster                                                     |
| deltablue                | 7.42 ms                                                | 3.49 ms: 2.13x faster                                                     |
| asyncio_tcp              | 925 ms                                                 | 513 ms: 1.80x faster                                                      |
| richards_super           | 90.7 ms                                                | 50.7 ms: 1.79x faster                                                     |
| logging_silent           | 175 ns                                                 | 99.8 ns: 1.75x faster                                                     |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                    |
| richards                 | 74.9 ms                                                | 44.8 ms: 1.67x faster                                                     |
| go                       | 229 ms                                                 | 138 ms: 1.67x faster                                                      |
| chaos                    | 106 ms                                                 | 64.8 ms: 1.64x faster                                                     |
| scimark_sor              | 197 ms                                                 | 125 ms: 1.57x faster                                                      |
| raytrace                 | 464 ms                                                 | 298 ms: 1.56x faster                                                      |
| nbody                    | 142 ms                                                 | 91.4 ms: 1.55x faster                                                     |
| hexiom                   | 9.53 ms                                                | 6.17 ms: 1.54x faster                                                     |
| async_tree_none          | 717 ms                                                 | 466 ms: 1.54x faster                                                      |
| sqlglot_parse            | 2.06 ms                                                | 1.34 ms: 1.54x faster                                                     |
| async_tree_io            | 1.77 sec                                               | 1.17 sec: 1.52x faster                                                    |
| crypto_pyaes             | 118 ms                                                 | 78.1 ms: 1.52x faster                                                     |
| pyflate                  | 673 ms                                                 | 444 ms: 1.52x faster                                                      |
| python_startup           | 14.2 ms                                                | 9.34 ms: 1.52x faster                                                     |
| async_tree_memoization   | 854 ms                                                 | 569 ms: 1.50x faster                                                      |
| scimark_monte_carlo      | 108 ms                                                 | 72.3 ms: 1.50x faster                                                     |
| sqlglot_transpile        | 2.45 ms                                                | 1.66 ms: 1.48x faster                                                     |
| pickle_pure_python       | 455 us                                                 | 315 us: 1.45x faster                                                      |
| scimark_lu               | 163 ms                                                 | 113 ms: 1.45x faster                                                      |
| spectral_norm            | 150 ms                                                 | 106 ms: 1.42x faster                                                      |
| coroutines               | 31.8 ms                                                | 22.6 ms: 1.41x faster                                                     |
| unpickle_pure_python     | 300 us                                                 | 217 us: 1.38x faster                                                      |
| json_dumps               | 13.5 ms                                                | 9.82 ms: 1.38x faster                                                     |
| deepcopy_memo            | 52.3 us                                                | 38.4 us: 1.36x faster                                                     |
| mako                     | 14.8 ms                                                | 10.9 ms: 1.35x faster                                                     |
| float                    | 111 ms                                                 | 82.0 ms: 1.35x faster                                                     |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 707 ms: 1.35x faster                                                      |
| tomli_loads              | 2.92 sec                                               | 2.21 sec: 1.32x faster                                                    |
| pprint_pformat           | 1.99 sec                                               | 1.51 sec: 1.31x faster                                                    |
| pprint_safe_repr         | 955 ms                                                 | 741 ms: 1.29x faster                                                      |
| comprehensions           | 26.8 us                                                | 20.9 us: 1.28x faster                                                     |
| tornado_http             | 127 ms                                                 | 99.4 ms: 1.28x faster                                                     |
| logging_simple           | 8.07 us                                                | 6.33 us: 1.27x faster                                                     |
| logging_format           | 8.91 us                                                | 7.01 us: 1.27x faster                                                     |
| xml_etree_process        | 74.9 ms                                                | 59.3 ms: 1.26x faster                                                     |
| pycparser                | 1.50 sec                                               | 1.20 sec: 1.26x faster                                                    |
| fannkuch                 | 486 ms                                                 | 388 ms: 1.25x faster                                                      |
| 2to3                     | 336 ms                                                 | 271 ms: 1.24x faster                                                      |
| deepcopy                 | 442 us                                                 | 358 us: 1.23x faster                                                      |
| sqlglot_normalize        | 135 ms                                                 | 110 ms: 1.23x faster                                                      |
| regex_compile            | 177 ms                                                 | 145 ms: 1.22x faster                                                      |
| deepcopy_reduce          | 3.82 us                                                | 3.14 us: 1.22x faster                                                     |
| nqueens                  | 100 ms                                                 | 82.6 ms: 1.21x faster                                                     |
| sqlglot_optimize         | 65.3 ms                                                | 54.1 ms: 1.21x faster                                                     |
| scimark_fft              | 424 ms                                                 | 356 ms: 1.19x faster                                                      |
| json_loads               | 28.8 us                                                | 24.7 us: 1.17x faster                                                     |
| docutils                 | 3.17 sec                                               | 2.74 sec: 1.16x faster                                                    |
| bench_thread_pool        | 947 us                                                 | 828 us: 1.14x faster                                                      |
| sqlalchemy_imperative    | 21.2 ms                                                | 18.7 ms: 1.13x faster                                                     |
| json                     | 5.42 ms                                                | 4.79 ms: 1.13x faster                                                     |
| sqlalchemy_declarative   | 165 ms                                                 | 147 ms: 1.13x faster                                                      |
| regex_v8                 | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                     |
| dulwich_log              | 75.9 ms                                                | 68.2 ms: 1.11x faster                                                     |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.11x faster                                                     |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.94 ms: 1.10x faster                                                     |
| xml_etree_generate       | 94.2 ms                                                | 85.7 ms: 1.10x faster                                                     |
| unpack_sequence          | 64.7 ns                                                | 59.7 ns: 1.09x faster                                                     |
| pathlib                  | 20.0 ms                                                | 18.5 ms: 1.08x faster                                                     |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.08x faster                                                      |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                      |
| sqlite_synth             | 2.93 us                                                | 2.73 us: 1.07x faster                                                     |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                                      |
| mdp                      | 2.82 sec                                               | 2.67 sec: 1.06x faster                                                    |
| regex_dna                | 222 ms                                                 | 210 ms: 1.06x faster                                                      |
| gc_traversal             | 3.84 ms                                                | 3.82 ms: 1.00x faster                                                     |
| pickle_list              | 4.56 us                                                | 4.63 us: 1.02x slower                                                     |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                                      |
| unpickle                 | 14.1 us                                                | 14.8 us: 1.04x slower                                                     |
| telco                    | 6.54 ms                                                | 6.83 ms: 1.04x slower                                                     |
| pickle                   | 10.3 us                                                | 10.8 us: 1.05x slower                                                     |
| unpickle_list            | 4.82 us                                                | 5.09 us: 1.06x slower                                                     |
| async_generators         | 425 ms                                                 | 452 ms: 1.06x slower                                                      |
| python_startup_no_site   | 5.82 ms                                                | 6.79 ms: 1.17x slower                                                     |
| regex_effbot             | 3.23 ms                                                | 3.83 ms: 1.18x slower                                                     |
| pickle_dict              | 27.3 us                                                | 32.6 us: 1.19x slower                                                     |
| dask                     | 423 ms                                                 | 539 ms: 1.27x slower                                                      |
| coverage                 | 72.8 ms                                                | 96.7 ms: 1.33x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.27x faster                                                              |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
