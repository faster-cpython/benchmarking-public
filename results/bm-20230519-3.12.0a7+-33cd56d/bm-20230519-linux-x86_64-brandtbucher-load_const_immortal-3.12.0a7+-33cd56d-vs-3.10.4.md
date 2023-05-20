
# Results vs. 3.10.4

- fork: brandtbucher
- ref: load_const_immortal
- machine: linux-x86_64
- commit hash: 33cd56d
- commit date: 2023-05-19
- overall geometric mean: 1.28x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230519-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-33cd56d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 267 ms: 1.26x faster                                                        |
| docutils       | 3.17 sec                                               | 2.71 sec: 1.17x faster                                                      |
| tornado_http   | 127 ms                                                 | 98.8 ms: 1.29x faster                                                       |
| Geometric mean | (ref)                                                  | 1.24x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230519-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-33cd56d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.7 ms: 1.58x faster                                                       |
| float          | 111 ms                                                 | 80.3 ms: 1.38x faster                                                       |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230519-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-33cd56d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.22x faster                                                        |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                       |
| regex_dna      | 222 ms                                                 | 206 ms: 1.08x faster                                                        |
| regex_effbot   | 3.23 ms                                                | 3.60 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230519-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-33cd56d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 318 us: 1.43x faster                                                        |
| json_dumps           | 13.5 ms                                                | 9.82 ms: 1.38x faster                                                       |
| unpickle_pure_python | 300 us                                                 | 218 us: 1.38x faster                                                        |
| tomli_loads          | 2.92 sec                                               | 2.20 sec: 1.33x faster                                                      |
| xml_etree_process    | 74.9 ms                                                | 59.7 ms: 1.26x faster                                                       |
| json_loads           | 28.8 us                                                | 25.0 us: 1.15x faster                                                       |
| xml_etree_generate   | 94.2 ms                                                | 85.6 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.06x faster                                                        |
| pickle_list          | 4.56 us                                                | 4.68 us: 1.03x slower                                                       |
| unpickle             | 14.1 us                                                | 14.9 us: 1.06x slower                                                       |
| unpickle_list        | 4.82 us                                                | 5.13 us: 1.07x slower                                                       |
| pickle               | 10.3 us                                                | 11.0 us: 1.07x slower                                                       |
| pickle_dict          | 27.3 us                                                | 30.9 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230519-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-33cd56d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.33 ms: 1.52x faster                                                       |
| python_startup_no_site | 5.82 ms                                                | 6.78 ms: 1.17x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.14x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230519-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-33cd56d |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230519-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-33cd56d |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 140 us: 3.64x faster                                                        |
| generators               | 76.8 ms                                                | 30.8 ms: 2.49x faster                                                       |
| deltablue                | 7.42 ms                                                | 3.50 ms: 2.12x faster                                                       |
| richards_super           | 90.7 ms                                                | 49.9 ms: 1.82x faster                                                       |
| asyncio_tcp              | 925 ms                                                 | 514 ms: 1.80x faster                                                        |
| logging_silent           | 175 ns                                                 | 100 ns: 1.75x faster                                                        |
| richards                 | 74.9 ms                                                | 44.0 ms: 1.70x faster                                                       |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                      |
| go                       | 229 ms                                                 | 137 ms: 1.67x faster                                                        |
| chaos                    | 106 ms                                                 | 64.7 ms: 1.64x faster                                                       |
| scimark_sor              | 197 ms                                                 | 124 ms: 1.58x faster                                                        |
| nbody                    | 142 ms                                                 | 89.7 ms: 1.58x faster                                                       |
| raytrace                 | 464 ms                                                 | 296 ms: 1.56x faster                                                        |
| hexiom                   | 9.53 ms                                                | 6.10 ms: 1.56x faster                                                       |
| sqlglot_parse            | 2.06 ms                                                | 1.33 ms: 1.55x faster                                                       |
| async_tree_io            | 1.77 sec                                               | 1.16 sec: 1.53x faster                                                      |
| async_tree_none          | 717 ms                                                 | 469 ms: 1.53x faster                                                        |
| python_startup           | 14.2 ms                                                | 9.33 ms: 1.52x faster                                                       |
| scimark_monte_carlo      | 108 ms                                                 | 71.6 ms: 1.51x faster                                                       |
| pyflate                  | 673 ms                                                 | 451 ms: 1.49x faster                                                        |
| async_tree_memoization   | 854 ms                                                 | 573 ms: 1.49x faster                                                        |
| sqlglot_transpile        | 2.45 ms                                                | 1.65 ms: 1.49x faster                                                       |
| crypto_pyaes             | 118 ms                                                 | 79.8 ms: 1.48x faster                                                       |
| coroutines               | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                       |
| pickle_pure_python       | 455 us                                                 | 318 us: 1.43x faster                                                        |
| spectral_norm            | 150 ms                                                 | 105 ms: 1.43x faster                                                        |
| scimark_lu               | 163 ms                                                 | 115 ms: 1.42x faster                                                        |
| deepcopy_memo            | 52.3 us                                                | 37.6 us: 1.39x faster                                                       |
| mako                     | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                       |
| json_dumps               | 13.5 ms                                                | 9.82 ms: 1.38x faster                                                       |
| unpack_sequence          | 64.7 ns                                                | 47.0 ns: 1.38x faster                                                       |
| unpickle_pure_python     | 300 us                                                 | 218 us: 1.38x faster                                                        |
| float                    | 111 ms                                                 | 80.3 ms: 1.38x faster                                                       |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 709 ms: 1.34x faster                                                        |
| tomli_loads              | 2.92 sec                                               | 2.20 sec: 1.33x faster                                                      |
| pprint_pformat           | 1.99 sec                                               | 1.50 sec: 1.33x faster                                                      |
| pycparser                | 1.50 sec                                               | 1.14 sec: 1.32x faster                                                      |
| comprehensions           | 26.8 us                                                | 20.6 us: 1.30x faster                                                       |
| pprint_safe_repr         | 955 ms                                                 | 733 ms: 1.30x faster                                                        |
| tornado_http             | 127 ms                                                 | 98.8 ms: 1.29x faster                                                       |
| fannkuch                 | 486 ms                                                 | 381 ms: 1.27x faster                                                        |
| 2to3                     | 336 ms                                                 | 267 ms: 1.26x faster                                                        |
| xml_etree_process        | 74.9 ms                                                | 59.7 ms: 1.26x faster                                                       |
| logging_format           | 8.91 us                                                | 7.15 us: 1.25x faster                                                       |
| deepcopy                 | 442 us                                                 | 355 us: 1.24x faster                                                        |
| logging_simple           | 8.07 us                                                | 6.49 us: 1.24x faster                                                       |
| nqueens                  | 100 ms                                                 | 81.1 ms: 1.23x faster                                                       |
| sqlglot_normalize        | 135 ms                                                 | 110 ms: 1.23x faster                                                        |
| regex_compile            | 177 ms                                                 | 145 ms: 1.22x faster                                                        |
| deepcopy_reduce          | 3.82 us                                                | 3.15 us: 1.21x faster                                                       |
| sqlglot_optimize         | 65.3 ms                                                | 54.0 ms: 1.21x faster                                                       |
| scimark_fft              | 424 ms                                                 | 358 ms: 1.18x faster                                                        |
| docutils                 | 3.17 sec                                               | 2.71 sec: 1.17x faster                                                      |
| bench_thread_pool        | 947 us                                                 | 821 us: 1.15x faster                                                        |
| json_loads               | 28.8 us                                                | 25.0 us: 1.15x faster                                                       |
| regex_v8                 | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                       |
| sqlalchemy_declarative   | 165 ms                                                 | 144 ms: 1.14x faster                                                        |
| sqlalchemy_imperative    | 21.2 ms                                                | 18.6 ms: 1.14x faster                                                       |
| json                     | 5.42 ms                                                | 4.79 ms: 1.13x faster                                                       |
| dulwich_log              | 75.9 ms                                                | 67.8 ms: 1.12x faster                                                       |
| mdp                      | 2.82 sec                                               | 2.54 sec: 1.11x faster                                                      |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.11x faster                                                       |
| meteor_contest           | 115 ms                                                 | 104 ms: 1.10x faster                                                        |
| xml_etree_generate       | 94.2 ms                                                | 85.6 ms: 1.10x faster                                                       |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 5.01 ms: 1.09x faster                                                       |
| pathlib                  | 20.0 ms                                                | 18.4 ms: 1.09x faster                                                       |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                        |
| regex_dna                | 222 ms                                                 | 206 ms: 1.08x faster                                                        |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                                       |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.06x faster                                                        |
| gc_traversal             | 3.84 ms                                                | 3.84 ms: 1.00x faster                                                       |
| pickle_list              | 4.56 us                                                | 4.68 us: 1.03x slower                                                       |
| pidigits                 | 190 ms                                                 | 197 ms: 1.04x slower                                                        |
| unpickle                 | 14.1 us                                                | 14.9 us: 1.06x slower                                                       |
| async_generators         | 425 ms                                                 | 450 ms: 1.06x slower                                                        |
| telco                    | 6.54 ms                                                | 6.96 ms: 1.06x slower                                                       |
| unpickle_list            | 4.82 us                                                | 5.13 us: 1.07x slower                                                       |
| pickle                   | 10.3 us                                                | 11.0 us: 1.07x slower                                                       |
| regex_effbot             | 3.23 ms                                                | 3.60 ms: 1.12x slower                                                       |
| pickle_dict              | 27.3 us                                                | 30.9 us: 1.13x slower                                                       |
| python_startup_no_site   | 5.82 ms                                                | 6.78 ms: 1.17x slower                                                       |
| dask                     | 423 ms                                                 | 537 ms: 1.27x slower                                                        |
| coverage                 | 72.8 ms                                                | 95.4 ms: 1.31x slower                                                       |
| Geometric mean           | (ref)                                                  | 1.28x faster                                                                |

Benchmark hidden because not significant (2): bench_mp_pool, mypy2
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
