
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: eaff9c3
- commit date: 2023-06-03
- overall geometric mean: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-darwin-arm64-python-main-3.13.0a0-eaff9c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.78 sec                                               | 1.51 sec: 1.18x faster                                |
| tornado_http   | 91.9 ms                                                | 70.5 ms: 1.30x faster                                 |
| Geometric mean | (ref)                                                  | 1.24x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-darwin-arm64-python-main-3.13.0a0-eaff9c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 94.1 ms                                                | 69.0 ms: 1.37x faster                                 |
| float          | 72.3 ms                                                | 57.0 ms: 1.27x faster                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                  |
| Geometric mean | (ref)                                                  | 1.20x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-darwin-arm64-python-main-3.13.0a0-eaff9c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 75.7 ms: 1.28x faster                                 |
| regex_v8       | 17.5 ms                                                | 15.9 ms: 1.10x faster                                 |
| regex_dna      | 160 ms                                                 | 150 ms: 1.07x faster                                  |
| regex_effbot   | 2.45 ms                                                | 2.61 ms: 1.07x slower                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-darwin-arm64-python-main-3.13.0a0-eaff9c3 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 187 us: 1.51x faster                                  |
| unpickle_pure_python | 203 us                                                 | 143 us: 1.42x faster                                  |
| json_dumps           | 8.38 ms                                                | 6.40 ms: 1.31x faster                                 |
| tomli_loads          | 1.76 sec                                               | 1.38 sec: 1.28x faster                                |
| xml_etree_process    | 45.1 ms                                                | 38.7 ms: 1.16x faster                                 |
| unpickle             | 9.77 us                                                | 9.32 us: 1.05x faster                                 |
| pickle               | 7.36 us                                                | 7.42 us: 1.01x slower                                 |
| pickle_dict          | 17.8 us                                                | 17.9 us: 1.01x slower                                 |
| xml_etree_parse      | 107 ms                                                 | 110 ms: 1.02x slower                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 74.4 ms: 1.02x slower                                 |
| xml_etree_generate   | 54.3 ms                                                | 56.1 ms: 1.03x slower                                 |
| json_loads           | 16.9 us                                                | 17.6 us: 1.04x slower                                 |
| unpickle_list        | 2.66 us                                                | 3.16 us: 1.19x slower                                 |
| Geometric mean       | (ref)                                                  | 1.09x faster                                          |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-darwin-arm64-python-main-3.13.0a0-eaff9c3 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 11.0 ms: 1.14x faster                                 |
| python_startup_no_site | 9.73 ms                                                | 8.97 ms: 1.08x faster                                 |
| Geometric mean         | (ref)                                                  | 1.11x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-darwin-arm64-python-main-3.13.0a0-eaff9c3 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.55 ms: 1.39x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230603-darwin-arm64-python-main-3.13.0a0-eaff9c3 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 90.8 us: 3.79x faster                                 |
| deltablue                | 5.15 ms                                                | 2.39 ms: 2.16x faster                                 |
| richards_super           | 60.7 ms                                                | 33.2 ms: 1.83x faster                                 |
| logging_silent           | 119 ns                                                 | 66.9 ns: 1.78x faster                                 |
| go                       | 165 ms                                                 | 94.4 ms: 1.75x faster                                 |
| richards                 | 51.4 ms                                                | 29.8 ms: 1.72x faster                                 |
| scimark_monte_carlo      | 72.2 ms                                                | 43.4 ms: 1.66x faster                                 |
| sqlglot_parse            | 1.33 ms                                                | 821 us: 1.62x faster                                  |
| chaos                    | 66.8 ms                                                | 41.5 ms: 1.61x faster                                 |
| raytrace                 | 328 ms                                                 | 207 ms: 1.59x faster                                  |
| sqlglot_transpile        | 1.54 ms                                                | 993 us: 1.55x faster                                  |
| async_tree_memoization   | 493 ms                                                 | 325 ms: 1.51x faster                                  |
| pickle_pure_python       | 284 us                                                 | 187 us: 1.51x faster                                  |
| hexiom                   | 6.32 ms                                                | 4.20 ms: 1.50x faster                                 |
| crypto_pyaes             | 78.0 ms                                                | 51.9 ms: 1.50x faster                                 |
| scimark_sor              | 127 ms                                                 | 85.6 ms: 1.48x faster                                 |
| scimark_lu               | 110 ms                                                 | 74.7 ms: 1.47x faster                                 |
| async_tree_io            | 1.02 sec                                               | 695 ms: 1.47x faster                                  |
| async_tree_none          | 402 ms                                                 | 278 ms: 1.44x faster                                  |
| pyflate                  | 453 ms                                                 | 316 ms: 1.43x faster                                  |
| asyncio_tcp              | 673 ms                                                 | 470 ms: 1.43x faster                                  |
| unpickle_pure_python     | 203 us                                                 | 143 us: 1.42x faster                                  |
| mako                     | 10.5 ms                                                | 7.55 ms: 1.39x faster                                 |
| deepcopy_memo            | 34.5 us                                                | 25.1 us: 1.37x faster                                 |
| nbody                    | 94.1 ms                                                | 69.0 ms: 1.37x faster                                 |
| pycparser                | 915 ms                                                 | 671 ms: 1.36x faster                                  |
| unpack_sequence          | 38.7 ns                                                | 28.9 ns: 1.34x faster                                 |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.25 sec: 1.32x faster                                |
| json_dumps               | 8.38 ms                                                | 6.40 ms: 1.31x faster                                 |
| tornado_http             | 91.9 ms                                                | 70.5 ms: 1.30x faster                                 |
| logging_format           | 5.01 us                                                | 3.86 us: 1.30x faster                                 |
| logging_simple           | 4.63 us                                                | 3.57 us: 1.30x faster                                 |
| spectral_norm            | 96.4 ms                                                | 74.7 ms: 1.29x faster                                 |
| tomli_loads              | 1.76 sec                                               | 1.38 sec: 1.28x faster                                |
| regex_compile            | 96.6 ms                                                | 75.7 ms: 1.28x faster                                 |
| float                    | 72.3 ms                                                | 57.0 ms: 1.27x faster                                 |
| create_gc_cycles         | 876 us                                                 | 696 us: 1.26x faster                                  |
| generators               | 32.9 ms                                                | 26.2 ms: 1.26x faster                                 |
| pprint_pformat           | 1.24 sec                                               | 995 ms: 1.25x faster                                  |
| pprint_safe_repr         | 609 ms                                                 | 489 ms: 1.24x faster                                  |
| dulwich_log              | 37.1 ms                                                | 29.8 ms: 1.24x faster                                 |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 542 ms: 1.24x faster                                  |
| fannkuch                 | 317 ms                                                 | 260 ms: 1.22x faster                                  |
| deepcopy                 | 278 us                                                 | 230 us: 1.21x faster                                  |
| mypy2                    | 308 ms                                                 | 258 ms: 1.19x faster                                  |
| docutils                 | 1.78 sec                                               | 1.51 sec: 1.18x faster                                |
| comprehensions           | 17.7 us                                                | 15.0 us: 1.18x faster                                 |
| xml_etree_process        | 45.1 ms                                                | 38.7 ms: 1.16x faster                                 |
| coroutines               | 20.2 ms                                                | 17.5 ms: 1.16x faster                                 |
| scimark_fft              | 232 ms                                                 | 201 ms: 1.15x faster                                  |
| deepcopy_reduce          | 2.38 us                                                | 2.07 us: 1.15x faster                                 |
| python_startup           | 12.6 ms                                                | 11.0 ms: 1.14x faster                                 |
| bench_thread_pool        | 548 us                                                 | 482 us: 1.14x faster                                  |
| nqueens                  | 68.1 ms                                                | 60.5 ms: 1.13x faster                                 |
| sqlglot_optimize         | 38.0 ms                                                | 34.1 ms: 1.11x faster                                 |
| regex_v8                 | 17.5 ms                                                | 15.9 ms: 1.10x faster                                 |
| python_startup_no_site   | 9.73 ms                                                | 8.97 ms: 1.08x faster                                 |
| meteor_contest           | 78.6 ms                                                | 73.5 ms: 1.07x faster                                 |
| sqlglot_normalize        | 197 ms                                                 | 184 ms: 1.07x faster                                  |
| regex_dna                | 160 ms                                                 | 150 ms: 1.07x faster                                  |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.27 ms: 1.06x faster                                 |
| unpickle                 | 9.77 us                                                | 9.32 us: 1.05x faster                                 |
| json                     | 3.10 ms                                                | 2.99 ms: 1.04x faster                                 |
| mdp                      | 1.67 sec                                               | 1.63 sec: 1.03x faster                                |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                  |
| pickle                   | 7.36 us                                                | 7.42 us: 1.01x slower                                 |
| pickle_dict              | 17.8 us                                                | 17.9 us: 1.01x slower                                 |
| telco                    | 3.68 ms                                                | 3.72 ms: 1.01x slower                                 |
| xml_etree_parse          | 107 ms                                                 | 110 ms: 1.02x slower                                  |
| xml_etree_iterparse      | 72.6 ms                                                | 74.4 ms: 1.02x slower                                 |
| xml_etree_generate       | 54.3 ms                                                | 56.1 ms: 1.03x slower                                 |
| json_loads               | 16.9 us                                                | 17.6 us: 1.04x slower                                 |
| sqlite_synth             | 1.47 us                                                | 1.57 us: 1.06x slower                                 |
| regex_effbot             | 2.45 ms                                                | 2.61 ms: 1.07x slower                                 |
| bench_mp_pool            | 41.0 ms                                                | 44.7 ms: 1.09x slower                                 |
| pathlib                  | 28.8 ms                                                | 32.4 ms: 1.12x slower                                 |
| unpickle_list            | 2.66 us                                                | 3.16 us: 1.19x slower                                 |
| coverage                 | 40.8 ms                                                | 50.8 ms: 1.24x slower                                 |
| async_generators         | 233 ms                                                 | 310 ms: 1.33x slower                                  |
| Geometric mean           | (ref)                                                  | 1.24x faster                                          |

Benchmark hidden because not significant (2): gc_traversal, pickle_list
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
