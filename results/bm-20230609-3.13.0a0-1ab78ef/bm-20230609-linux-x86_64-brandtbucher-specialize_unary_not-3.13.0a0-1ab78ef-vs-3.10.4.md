
# Results vs. 3.10.4

- fork: brandtbucher
- ref: specialize_unary_not
- machine: linux-x86_64
- commit hash: 1ab78ef
- commit date: 2023-06-09
- overall geometric mean: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.74 sec: 1.16x faster                                                      |
| tornado_http   | 127 ms                                                 | 103 ms: 1.24x faster                                                        |
| Geometric mean | (ref)                                                  | 1.20x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.7 ms: 1.58x faster                                                       |
| float          | 111 ms                                                 | 81.5 ms: 1.36x faster                                                       |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 146 ms: 1.21x faster                                                        |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                       |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                                        |
| regex_effbot   | 3.23 ms                                                | 3.53 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 317 us: 1.44x faster                                                        |
| json_dumps           | 13.5 ms                                                | 9.84 ms: 1.38x faster                                                       |
| unpickle_pure_python | 300 us                                                 | 226 us: 1.33x faster                                                        |
| tomli_loads          | 2.92 sec                                               | 2.27 sec: 1.29x faster                                                      |
| xml_etree_process    | 74.9 ms                                                | 58.5 ms: 1.28x faster                                                       |
| json_loads           | 28.8 us                                                | 25.0 us: 1.15x faster                                                       |
| xml_etree_generate   | 94.2 ms                                                | 84.9 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.06x faster                                                        |
| unpickle_list        | 4.82 us                                                | 4.87 us: 1.01x slower                                                       |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                                       |
| pickle_list          | 4.56 us                                                | 4.75 us: 1.04x slower                                                       |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                                       |
| pickle_dict          | 27.3 us                                                | 32.1 us: 1.18x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.28 ms: 1.53x faster                                                       |
| python_startup_no_site | 5.82 ms                                                | 6.76 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.6 ms: 1.40x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230609-linux-x86_64-brandtbucher-specialize_unary_not-3.13.0a0-1ab78ef |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 143 us: 3.56x faster                                                        |
| generators               | 76.8 ms                                                | 30.8 ms: 2.50x faster                                                       |
| deltablue                | 7.42 ms                                                | 3.63 ms: 2.05x faster                                                       |
| asyncio_tcp              | 925 ms                                                 | 518 ms: 1.78x faster                                                        |
| richards_super           | 90.7 ms                                                | 51.4 ms: 1.76x faster                                                       |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                                      |
| go                       | 229 ms                                                 | 138 ms: 1.66x faster                                                        |
| richards                 | 74.9 ms                                                | 45.7 ms: 1.64x faster                                                       |
| chaos                    | 106 ms                                                 | 64.9 ms: 1.64x faster                                                       |
| logging_silent           | 175 ns                                                 | 108 ns: 1.62x faster                                                        |
| nbody                    | 142 ms                                                 | 89.7 ms: 1.58x faster                                                       |
| scimark_sor              | 197 ms                                                 | 126 ms: 1.56x faster                                                        |
| raytrace                 | 464 ms                                                 | 301 ms: 1.54x faster                                                        |
| python_startup           | 14.2 ms                                                | 9.28 ms: 1.53x faster                                                       |
| hexiom                   | 9.53 ms                                                | 6.34 ms: 1.50x faster                                                       |
| sqlglot_parse            | 2.06 ms                                                | 1.38 ms: 1.49x faster                                                       |
| crypto_pyaes             | 118 ms                                                 | 79.7 ms: 1.49x faster                                                       |
| pyflate                  | 673 ms                                                 | 454 ms: 1.48x faster                                                        |
| scimark_monte_carlo      | 108 ms                                                 | 74.5 ms: 1.45x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 1.23 sec: 1.45x faster                                                      |
| async_tree_none          | 717 ms                                                 | 496 ms: 1.45x faster                                                        |
| pickle_pure_python       | 455 us                                                 | 317 us: 1.44x faster                                                        |
| sqlglot_transpile        | 2.45 ms                                                | 1.71 ms: 1.43x faster                                                       |
| scimark_lu               | 163 ms                                                 | 115 ms: 1.42x faster                                                        |
| async_tree_memoization   | 854 ms                                                 | 600 ms: 1.42x faster                                                        |
| spectral_norm            | 150 ms                                                 | 107 ms: 1.40x faster                                                        |
| coroutines               | 31.8 ms                                                | 22.8 ms: 1.40x faster                                                       |
| mako                     | 14.8 ms                                                | 10.6 ms: 1.40x faster                                                       |
| json_dumps               | 13.5 ms                                                | 9.84 ms: 1.38x faster                                                       |
| float                    | 111 ms                                                 | 81.5 ms: 1.36x faster                                                       |
| deepcopy_memo            | 52.3 us                                                | 39.0 us: 1.34x faster                                                       |
| unpickle_pure_python     | 300 us                                                 | 226 us: 1.33x faster                                                        |
| unpack_sequence          | 64.7 ns                                                | 49.0 ns: 1.32x faster                                                       |
| pprint_pformat           | 1.99 sec                                               | 1.51 sec: 1.31x faster                                                      |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 735 ms: 1.29x faster                                                        |
| tomli_loads              | 2.92 sec                                               | 2.27 sec: 1.29x faster                                                      |
| comprehensions           | 26.8 us                                                | 20.8 us: 1.29x faster                                                       |
| pprint_safe_repr         | 955 ms                                                 | 744 ms: 1.28x faster                                                        |
| xml_etree_process        | 74.9 ms                                                | 58.5 ms: 1.28x faster                                                       |
| fannkuch                 | 486 ms                                                 | 389 ms: 1.25x faster                                                        |
| pycparser                | 1.50 sec                                               | 1.20 sec: 1.25x faster                                                      |
| tornado_http             | 127 ms                                                 | 103 ms: 1.24x faster                                                        |
| mypy2                    | 428 ms                                                 | 345 ms: 1.24x faster                                                        |
| logging_format           | 8.91 us                                                | 7.20 us: 1.24x faster                                                       |
| deepcopy                 | 442 us                                                 | 359 us: 1.23x faster                                                        |
| nqueens                  | 100 ms                                                 | 81.3 ms: 1.23x faster                                                       |
| logging_simple           | 8.07 us                                                | 6.56 us: 1.23x faster                                                       |
| regex_compile            | 177 ms                                                 | 146 ms: 1.21x faster                                                        |
| sqlglot_normalize        | 135 ms                                                 | 112 ms: 1.21x faster                                                        |
| scimark_fft              | 424 ms                                                 | 354 ms: 1.20x faster                                                        |
| deepcopy_reduce          | 3.82 us                                                | 3.22 us: 1.19x faster                                                       |
| sqlglot_optimize         | 65.3 ms                                                | 55.3 ms: 1.18x faster                                                       |
| docutils                 | 3.17 sec                                               | 2.74 sec: 1.16x faster                                                      |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.73 ms: 1.15x faster                                                       |
| regex_v8                 | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                       |
| json_loads               | 28.8 us                                                | 25.0 us: 1.15x faster                                                       |
| bench_thread_pool        | 947 us                                                 | 836 us: 1.13x faster                                                        |
| json                     | 5.42 ms                                                | 4.78 ms: 1.13x faster                                                       |
| create_gc_cycles         | 1.67 ms                                                | 1.50 ms: 1.12x faster                                                       |
| dulwich_log              | 75.9 ms                                                | 68.3 ms: 1.11x faster                                                       |
| mdp                      | 2.82 sec                                               | 2.54 sec: 1.11x faster                                                      |
| xml_etree_generate       | 94.2 ms                                                | 84.9 ms: 1.11x faster                                                       |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.08x faster                                                        |
| sqlite_synth             | 2.93 us                                                | 2.71 us: 1.08x faster                                                       |
| pathlib                  | 20.0 ms                                                | 18.5 ms: 1.08x faster                                                       |
| regex_dna                | 222 ms                                                 | 207 ms: 1.07x faster                                                        |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.07x faster                                                        |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.06x faster                                                        |
| unpickle_list            | 4.82 us                                                | 4.87 us: 1.01x slower                                                       |
| pickle                   | 10.3 us                                                | 10.6 us: 1.03x slower                                                       |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                                        |
| pickle_list              | 4.56 us                                                | 4.75 us: 1.04x slower                                                       |
| async_generators         | 425 ms                                                 | 448 ms: 1.05x slower                                                        |
| telco                    | 6.54 ms                                                | 6.89 ms: 1.05x slower                                                       |
| gc_traversal             | 3.84 ms                                                | 4.07 ms: 1.06x slower                                                       |
| unpickle                 | 14.1 us                                                | 15.0 us: 1.06x slower                                                       |
| regex_effbot             | 3.23 ms                                                | 3.53 ms: 1.09x slower                                                       |
| python_startup_no_site   | 5.82 ms                                                | 6.76 ms: 1.16x slower                                                       |
| pickle_dict              | 27.3 us                                                | 32.1 us: 1.18x slower                                                       |
| dask                     | 423 ms                                                 | 542 ms: 1.28x slower                                                        |
| coverage                 | 72.8 ms                                                | 95.0 ms: 1.31x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.27x faster                                                                |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
