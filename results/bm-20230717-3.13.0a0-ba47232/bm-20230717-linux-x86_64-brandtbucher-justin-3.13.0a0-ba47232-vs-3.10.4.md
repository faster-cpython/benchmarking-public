
# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin
- machine: linux-x86_64
- commit hash: ba47232
- commit date: 2023-07-17
- overall geometric mean: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230717-linux-x86_64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.70 sec: 1.17x faster                                        |
| tornado_http   | 127 ms                                                 | 98.5 ms: 1.29x faster                                         |
| Geometric mean | (ref)                                                  | 1.23x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230717-linux-x86_64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 94.2 ms: 1.50x faster                                         |
| float          | 111 ms                                                 | 87.3 ms: 1.27x faster                                         |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                  | 1.22x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230717-linux-x86_64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 141 ms: 1.25x faster                                          |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                         |
| regex_dna      | 222 ms                                                 | 210 ms: 1.06x faster                                          |
| regex_effbot   | 3.23 ms                                                | 3.53 ms: 1.09x slower                                         |
| Geometric mean | (ref)                                                  | 1.08x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230717-linux-x86_64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 313 us: 1.46x faster                                          |
| unpickle_pure_python | 300 us                                                 | 216 us: 1.39x faster                                          |
| json_dumps           | 13.5 ms                                                | 9.85 ms: 1.37x faster                                         |
| xml_etree_process    | 74.9 ms                                                | 58.5 ms: 1.28x faster                                         |
| tomli_loads          | 2.92 sec                                               | 2.37 sec: 1.23x faster                                        |
| json_loads           | 28.8 us                                                | 25.3 us: 1.14x faster                                         |
| xml_etree_generate   | 94.2 ms                                                | 85.2 ms: 1.11x faster                                         |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.09x faster                                          |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.08x faster                                          |
| pickle_list          | 4.56 us                                                | 4.44 us: 1.03x faster                                         |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                         |
| unpickle_list        | 4.82 us                                                | 4.97 us: 1.03x slower                                         |
| unpickle             | 14.1 us                                                | 15.1 us: 1.07x slower                                         |
| pickle_dict          | 27.3 us                                                | 31.7 us: 1.16x slower                                         |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230717-linux-x86_64-brandtbucher-justin-3.13.0a0-ba47232 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.46 ms: 1.50x faster                                         |
| python_startup_no_site | 5.82 ms                                                | 6.88 ms: 1.18x slower                                         |
| Geometric mean         | (ref)                                                  | 1.12x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230717-linux-x86_64-brandtbucher-justin-3.13.0a0-ba47232 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 12.3 ms: 1.20x faster                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230717-linux-x86_64-brandtbucher-justin-3.13.0a0-ba47232 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 147 us: 3.48x faster                                          |
| generators               | 76.8 ms                                                | 28.8 ms: 2.67x faster                                         |
| deltablue                | 7.42 ms                                                | 3.56 ms: 2.09x faster                                         |
| asyncio_tcp              | 925 ms                                                 | 505 ms: 1.83x faster                                          |
| richards_super           | 90.7 ms                                                | 51.5 ms: 1.76x faster                                         |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                        |
| logging_silent           | 175 ns                                                 | 106 ns: 1.66x faster                                          |
| richards                 | 74.9 ms                                                | 45.2 ms: 1.66x faster                                         |
| chaos                    | 106 ms                                                 | 64.6 ms: 1.65x faster                                         |
| go                       | 229 ms                                                 | 141 ms: 1.63x faster                                          |
| scimark_sor              | 197 ms                                                 | 124 ms: 1.58x faster                                          |
| raytrace                 | 464 ms                                                 | 296 ms: 1.57x faster                                          |
| sqlglot_parse            | 2.06 ms                                                | 1.36 ms: 1.52x faster                                         |
| nbody                    | 142 ms                                                 | 94.2 ms: 1.50x faster                                         |
| python_startup           | 14.2 ms                                                | 9.46 ms: 1.50x faster                                         |
| scimark_monte_carlo      | 108 ms                                                 | 72.7 ms: 1.49x faster                                         |
| async_tree_io            | 1.77 sec                                               | 1.21 sec: 1.47x faster                                        |
| async_tree_none          | 717 ms                                                 | 492 ms: 1.46x faster                                          |
| sqlglot_transpile        | 2.45 ms                                                | 1.68 ms: 1.46x faster                                         |
| pickle_pure_python       | 455 us                                                 | 313 us: 1.46x faster                                          |
| hexiom                   | 9.53 ms                                                | 6.58 ms: 1.45x faster                                         |
| async_tree_memoization   | 854 ms                                                 | 598 ms: 1.43x faster                                          |
| coroutines               | 31.8 ms                                                | 22.4 ms: 1.42x faster                                         |
| pyflate                  | 673 ms                                                 | 476 ms: 1.41x faster                                          |
| unpack_sequence          | 64.7 ns                                                | 46.1 ns: 1.40x faster                                         |
| unpickle_pure_python     | 300 us                                                 | 216 us: 1.39x faster                                          |
| spectral_norm            | 150 ms                                                 | 108 ms: 1.39x faster                                          |
| json_dumps               | 13.5 ms                                                | 9.85 ms: 1.37x faster                                         |
| logging_format           | 8.91 us                                                | 6.55 us: 1.36x faster                                         |
| crypto_pyaes             | 118 ms                                                 | 87.2 ms: 1.36x faster                                         |
| logging_simple           | 8.07 us                                                | 6.05 us: 1.33x faster                                         |
| pprint_pformat           | 1.99 sec                                               | 1.49 sec: 1.33x faster                                        |
| pycparser                | 1.50 sec                                               | 1.13 sec: 1.33x faster                                        |
| pprint_safe_repr         | 955 ms                                                 | 731 ms: 1.31x faster                                          |
| tornado_http             | 127 ms                                                 | 98.5 ms: 1.29x faster                                         |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 736 ms: 1.29x faster                                          |
| xml_etree_process        | 74.9 ms                                                | 58.5 ms: 1.28x faster                                         |
| float                    | 111 ms                                                 | 87.3 ms: 1.27x faster                                         |
| sqlglot_normalize        | 135 ms                                                 | 107 ms: 1.26x faster                                          |
| mypy2                    | 428 ms                                                 | 341 ms: 1.26x faster                                          |
| deepcopy                 | 442 us                                                 | 352 us: 1.25x faster                                          |
| regex_compile            | 177 ms                                                 | 141 ms: 1.25x faster                                          |
| scimark_lu               | 163 ms                                                 | 131 ms: 1.25x faster                                          |
| tomli_loads              | 2.92 sec                                               | 2.37 sec: 1.23x faster                                        |
| sqlglot_optimize         | 65.3 ms                                                | 53.5 ms: 1.22x faster                                         |
| deepcopy_reduce          | 3.82 us                                                | 3.14 us: 1.22x faster                                         |
| mako                     | 14.8 ms                                                | 12.3 ms: 1.20x faster                                         |
| nqueens                  | 100 ms                                                 | 85.0 ms: 1.18x faster                                         |
| docutils                 | 3.17 sec                                               | 2.70 sec: 1.17x faster                                        |
| dulwich_log              | 75.9 ms                                                | 65.2 ms: 1.16x faster                                         |
| comprehensions           | 26.8 us                                                | 23.2 us: 1.16x faster                                         |
| bench_thread_pool        | 947 us                                                 | 829 us: 1.14x faster                                          |
| scimark_fft              | 424 ms                                                 | 372 ms: 1.14x faster                                          |
| json_loads               | 28.8 us                                                | 25.3 us: 1.14x faster                                         |
| json                     | 5.42 ms                                                | 4.77 ms: 1.13x faster                                         |
| create_gc_cycles         | 1.67 ms                                                | 1.48 ms: 1.13x faster                                         |
| regex_v8                 | 25.0 ms                                                | 22.4 ms: 1.12x faster                                         |
| fannkuch                 | 486 ms                                                 | 437 ms: 1.11x faster                                          |
| xml_etree_generate       | 94.2 ms                                                | 85.2 ms: 1.11x faster                                         |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.09x faster                                          |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.09x faster                                          |
| deepcopy_memo            | 52.3 us                                                | 48.6 us: 1.08x faster                                         |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.08x faster                                          |
| pathlib                  | 20.0 ms                                                | 18.7 ms: 1.07x faster                                         |
| sqlite_synth             | 2.93 us                                                | 2.75 us: 1.07x faster                                         |
| mdp                      | 2.82 sec                                               | 2.67 sec: 1.06x faster                                        |
| regex_dna                | 222 ms                                                 | 210 ms: 1.06x faster                                          |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 5.19 ms: 1.05x faster                                         |
| pickle_list              | 4.56 us                                                | 4.44 us: 1.03x faster                                         |
| bench_mp_pool            | 24.0 ms                                                | 24.0 ms: 1.00x slower                                         |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                         |
| unpickle_list            | 4.82 us                                                | 4.97 us: 1.03x slower                                         |
| pidigits                 | 190 ms                                                 | 198 ms: 1.04x slower                                          |
| telco                    | 6.54 ms                                                | 6.83 ms: 1.04x slower                                         |
| gc_traversal             | 3.84 ms                                                | 4.07 ms: 1.06x slower                                         |
| unpickle                 | 14.1 us                                                | 15.1 us: 1.07x slower                                         |
| async_generators         | 425 ms                                                 | 458 ms: 1.08x slower                                          |
| regex_effbot             | 3.23 ms                                                | 3.53 ms: 1.09x slower                                         |
| pickle_dict              | 27.3 us                                                | 31.7 us: 1.16x slower                                         |
| python_startup_no_site   | 5.82 ms                                                | 6.88 ms: 1.18x slower                                         |
| dask                     | 423 ms                                                 | 523 ms: 1.24x slower                                          |
| coverage                 | 72.8 ms                                                | 94.9 ms: 1.30x slower                                         |
| Geometric mean           | (ref)                                                  | 1.26x faster                                                  |
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
