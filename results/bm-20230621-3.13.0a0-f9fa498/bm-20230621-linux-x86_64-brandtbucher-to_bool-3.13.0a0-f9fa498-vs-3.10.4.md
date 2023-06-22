
# Results vs. 3.10.4

- fork: brandtbucher
- ref: to_bool
- machine: linux-x86_64
- commit hash: f9fa498
- commit date: 2023-06-21
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.66 sec: 1.19x faster                                         |
| tornado_http   | 127 ms                                                 | 96.3 ms: 1.32x faster                                          |
| Geometric mean | (ref)                                                  | 1.26x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.3 ms: 1.60x faster                                          |
| float          | 111 ms                                                 | 79.8 ms: 1.39x faster                                          |
| pidigits       | 190 ms                                                 | 196 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                  | 1.29x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                           |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                          |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                           |
| regex_effbot   | 3.23 ms                                                | 3.50 ms: 1.08x slower                                          |
| Geometric mean | (ref)                                                  | 1.11x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 301 us: 1.51x faster                                           |
| unpickle_pure_python | 300 us                                                 | 209 us: 1.43x faster                                           |
| json_dumps           | 13.5 ms                                                | 9.91 ms: 1.37x faster                                          |
| tomli_loads          | 2.92 sec                                               | 2.24 sec: 1.30x faster                                         |
| xml_etree_process    | 74.9 ms                                                | 58.4 ms: 1.28x faster                                          |
| json_loads           | 28.8 us                                                | 25.2 us: 1.14x faster                                          |
| xml_etree_generate   | 94.2 ms                                                | 84.4 ms: 1.12x faster                                          |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                           |
| xml_etree_parse      | 163 ms                                                 | 156 ms: 1.04x faster                                           |
| unpickle_list        | 4.82 us                                                | 4.90 us: 1.02x slower                                          |
| pickle_list          | 4.56 us                                                | 4.67 us: 1.02x slower                                          |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                          |
| unpickle             | 14.1 us                                                | 14.9 us: 1.05x slower                                          |
| pickle_dict          | 27.3 us                                                | 32.0 us: 1.17x slower                                          |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.19 ms: 1.54x faster                                          |
| python_startup_no_site | 5.82 ms                                                | 6.67 ms: 1.15x slower                                          |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498 |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.6 ms: 1.39x faster                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230621-linux-x86_64-brandtbucher-to_bool-3.13.0a0-f9fa498 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 148 us: 3.45x faster                                           |
| generators               | 76.8 ms                                                | 29.1 ms: 2.64x faster                                          |
| deltablue                | 7.42 ms                                                | 3.29 ms: 2.25x faster                                          |
| asyncio_tcp              | 925 ms                                                 | 508 ms: 1.82x faster                                           |
| logging_silent           | 175 ns                                                 | 99.5 ns: 1.76x faster                                          |
| richards_super           | 90.7 ms                                                | 52.4 ms: 1.73x faster                                          |
| chaos                    | 106 ms                                                 | 62.2 ms: 1.71x faster                                          |
| scimark_sor              | 197 ms                                                 | 116 ms: 1.69x faster                                           |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.80 sec: 1.67x faster                                         |
| go                       | 229 ms                                                 | 137 ms: 1.67x faster                                           |
| richards                 | 74.9 ms                                                | 46.1 ms: 1.62x faster                                          |
| hexiom                   | 9.53 ms                                                | 5.90 ms: 1.61x faster                                          |
| nbody                    | 142 ms                                                 | 88.3 ms: 1.60x faster                                          |
| raytrace                 | 464 ms                                                 | 294 ms: 1.58x faster                                           |
| sqlglot_parse            | 2.06 ms                                                | 1.32 ms: 1.56x faster                                          |
| python_startup           | 14.2 ms                                                | 9.19 ms: 1.54x faster                                          |
| crypto_pyaes             | 118 ms                                                 | 77.3 ms: 1.53x faster                                          |
| pyflate                  | 673 ms                                                 | 441 ms: 1.53x faster                                           |
| pickle_pure_python       | 455 us                                                 | 301 us: 1.51x faster                                           |
| scimark_monte_carlo      | 108 ms                                                 | 71.5 ms: 1.51x faster                                          |
| scimark_lu               | 163 ms                                                 | 109 ms: 1.50x faster                                           |
| sqlglot_transpile        | 2.45 ms                                                | 1.64 ms: 1.49x faster                                          |
| async_tree_none          | 717 ms                                                 | 487 ms: 1.47x faster                                           |
| async_tree_io            | 1.77 sec                                               | 1.21 sec: 1.47x faster                                         |
| async_tree_memoization   | 854 ms                                                 | 592 ms: 1.44x faster                                           |
| spectral_norm            | 150 ms                                                 | 104 ms: 1.44x faster                                           |
| coroutines               | 31.8 ms                                                | 22.1 ms: 1.44x faster                                          |
| unpickle_pure_python     | 300 us                                                 | 209 us: 1.43x faster                                           |
| unpack_sequence          | 64.7 ns                                                | 45.8 ns: 1.41x faster                                          |
| deepcopy_memo            | 52.3 us                                                | 37.2 us: 1.41x faster                                          |
| mako                     | 14.8 ms                                                | 10.6 ms: 1.39x faster                                          |
| logging_format           | 8.91 us                                                | 6.41 us: 1.39x faster                                          |
| float                    | 111 ms                                                 | 79.8 ms: 1.39x faster                                          |
| logging_simple           | 8.07 us                                                | 5.85 us: 1.38x faster                                          |
| json_dumps               | 13.5 ms                                                | 9.91 ms: 1.37x faster                                          |
| pprint_pformat           | 1.99 sec                                               | 1.48 sec: 1.34x faster                                         |
| pprint_safe_repr         | 955 ms                                                 | 719 ms: 1.33x faster                                           |
| tornado_http             | 127 ms                                                 | 96.3 ms: 1.32x faster                                          |
| comprehensions           | 26.8 us                                                | 20.3 us: 1.32x faster                                          |
| regex_compile            | 177 ms                                                 | 135 ms: 1.31x faster                                           |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 728 ms: 1.31x faster                                           |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.30x faster                                         |
| tomli_loads              | 2.92 sec                                               | 2.24 sec: 1.30x faster                                         |
| xml_etree_process        | 74.9 ms                                                | 58.4 ms: 1.28x faster                                          |
| fannkuch                 | 486 ms                                                 | 380 ms: 1.28x faster                                           |
| mypy2                    | 428 ms                                                 | 335 ms: 1.28x faster                                           |
| deepcopy                 | 442 us                                                 | 346 us: 1.28x faster                                           |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.27x faster                                           |
| deepcopy_reduce          | 3.82 us                                                | 3.10 us: 1.24x faster                                          |
| sqlglot_optimize         | 65.3 ms                                                | 53.1 ms: 1.23x faster                                          |
| scimark_fft              | 424 ms                                                 | 346 ms: 1.22x faster                                           |
| nqueens                  | 100 ms                                                 | 82.3 ms: 1.22x faster                                          |
| docutils                 | 3.17 sec                                               | 2.66 sec: 1.19x faster                                         |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.60 ms: 1.19x faster                                          |
| bench_thread_pool        | 947 us                                                 | 819 us: 1.16x faster                                           |
| dulwich_log              | 75.9 ms                                                | 65.7 ms: 1.16x faster                                          |
| regex_v8                 | 25.0 ms                                                | 21.8 ms: 1.15x faster                                          |
| json_loads               | 28.8 us                                                | 25.2 us: 1.14x faster                                          |
| json                     | 5.42 ms                                                | 4.79 ms: 1.13x faster                                          |
| xml_etree_generate       | 94.2 ms                                                | 84.4 ms: 1.12x faster                                          |
| mdp                      | 2.82 sec                                               | 2.53 sec: 1.11x faster                                         |
| create_gc_cycles         | 1.67 ms                                                | 1.51 ms: 1.11x faster                                          |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.09x faster                                           |
| xml_etree_iterparse      | 111 ms                                                 | 104 ms: 1.07x faster                                           |
| regex_dna                | 222 ms                                                 | 207 ms: 1.07x faster                                           |
| sqlite_synth             | 2.93 us                                                | 2.77 us: 1.06x faster                                          |
| pathlib                  | 20.0 ms                                                | 19.2 ms: 1.04x faster                                          |
| xml_etree_parse          | 163 ms                                                 | 156 ms: 1.04x faster                                           |
| gc_traversal             | 3.84 ms                                                | 3.82 ms: 1.01x faster                                          |
| unpickle_list            | 4.82 us                                                | 4.90 us: 1.02x slower                                          |
| pickle_list              | 4.56 us                                                | 4.67 us: 1.02x slower                                          |
| pidigits                 | 190 ms                                                 | 196 ms: 1.03x slower                                           |
| telco                    | 6.54 ms                                                | 6.80 ms: 1.04x slower                                          |
| pickle                   | 10.3 us                                                | 10.7 us: 1.04x slower                                          |
| unpickle                 | 14.1 us                                                | 14.9 us: 1.05x slower                                          |
| async_generators         | 425 ms                                                 | 451 ms: 1.06x slower                                           |
| regex_effbot             | 3.23 ms                                                | 3.50 ms: 1.08x slower                                          |
| python_startup_no_site   | 5.82 ms                                                | 6.67 ms: 1.15x slower                                          |
| pickle_dict              | 27.3 us                                                | 32.0 us: 1.17x slower                                          |
| dask                     | 423 ms                                                 | 521 ms: 1.23x slower                                           |
| coverage                 | 72.8 ms                                                | 92.6 ms: 1.27x slower                                          |
| Geometric mean           | (ref)                                                  | 1.30x faster                                                   |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
