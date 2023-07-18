
# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin
- machine: darwin-arm64
- commit hash: ba47232
- commit date: 2023-07-17
- overall geometric mean: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 1.78 sec                                               | 1.54 sec: 1.16x faster                                        |
| tornado_http   | 91.9 ms                                                | 71.5 ms: 1.29x faster                                         |
| Geometric mean | (ref)                                                  | 1.22x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 69.4 ms: 1.36x faster                                         |
| float          | 72.3 ms                                                | 57.6 ms: 1.26x faster                                         |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                          |
| Geometric mean | (ref)                                                  | 1.20x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 75.9 ms: 1.27x faster                                         |
| regex_v8       | 17.5 ms                                                | 15.9 ms: 1.10x faster                                         |
| regex_dna      | 160 ms                                                 | 150 ms: 1.07x faster                                          |
| regex_effbot   | 2.45 ms                                                | 2.56 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                  | 1.09x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 183 us: 1.55x faster                                          |
| unpickle_pure_python | 203 us                                                 | 143 us: 1.42x faster                                          |
| json_dumps           | 8.38 ms                                                | 6.44 ms: 1.30x faster                                         |
| xml_etree_process    | 45.1 ms                                                | 38.2 ms: 1.18x faster                                         |
| tomli_loads          | 1.76 sec                                               | 1.52 sec: 1.16x faster                                        |
| unpickle             | 9.77 us                                                | 9.31 us: 1.05x faster                                         |
| pickle               | 7.36 us                                                | 7.44 us: 1.01x slower                                         |
| pickle_list          | 2.83 us                                                | 2.88 us: 1.02x slower                                         |
| pickle_dict          | 17.8 us                                                | 18.1 us: 1.02x slower                                         |
| xml_etree_iterparse  | 72.6 ms                                                | 74.4 ms: 1.02x slower                                         |
| xml_etree_generate   | 54.3 ms                                                | 56.0 ms: 1.03x slower                                         |
| xml_etree_parse      | 107 ms                                                 | 111 ms: 1.03x slower                                          |
| json_loads           | 16.9 us                                                | 17.6 us: 1.04x slower                                         |
| unpickle_list        | 2.66 us                                                | 3.25 us: 1.22x slower                                         |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.7 ms: 1.01x slower                                         |
| python_startup_no_site | 9.73 ms                                                | 10.5 ms: 1.08x slower                                         |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mako      | 10.5 ms                                                | 8.10 ms: 1.29x faster                                         |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230717-darwin-arm64-brandtbucher-justin-3.13.0a0-ba47232 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 88.8 us: 3.87x faster                                         |
| deltablue                | 5.15 ms                                                | 2.50 ms: 2.06x faster                                         |
| richards_super           | 60.7 ms                                                | 33.5 ms: 1.81x faster                                         |
| logging_silent           | 119 ns                                                 | 65.8 ns: 1.81x faster                                         |
| richards                 | 51.4 ms                                                | 29.8 ms: 1.72x faster                                         |
| go                       | 165 ms                                                 | 105 ms: 1.57x faster                                          |
| asyncio_tcp              | 673 ms                                                 | 431 ms: 1.56x faster                                          |
| pickle_pure_python       | 284 us                                                 | 183 us: 1.55x faster                                          |
| async_tree_memoization   | 493 ms                                                 | 326 ms: 1.51x faster                                          |
| chaos                    | 66.8 ms                                                | 44.3 ms: 1.51x faster                                         |
| sqlglot_parse            | 1.33 ms                                                | 888 us: 1.50x faster                                          |
| scimark_lu               | 110 ms                                                 | 73.5 ms: 1.50x faster                                         |
| hexiom                   | 6.32 ms                                                | 4.23 ms: 1.50x faster                                         |
| crypto_pyaes             | 78.0 ms                                                | 53.2 ms: 1.47x faster                                         |
| scimark_monte_carlo      | 72.2 ms                                                | 49.4 ms: 1.46x faster                                         |
| async_tree_none          | 402 ms                                                 | 276 ms: 1.46x faster                                          |
| async_tree_io            | 1.02 sec                                               | 704 ms: 1.45x faster                                          |
| sqlglot_transpile        | 1.54 ms                                                | 1.07 ms: 1.44x faster                                         |
| unpack_sequence          | 38.7 ns                                                | 27.2 ns: 1.42x faster                                         |
| unpickle_pure_python     | 203 us                                                 | 143 us: 1.42x faster                                          |
| pycparser                | 915 ms                                                 | 664 ms: 1.38x faster                                          |
| scimark_sor              | 127 ms                                                 | 92.0 ms: 1.38x faster                                         |
| nbody                    | 94.1 ms                                                | 69.4 ms: 1.36x faster                                         |
| raytrace                 | 328 ms                                                 | 242 ms: 1.36x faster                                          |
| pyflate                  | 453 ms                                                 | 336 ms: 1.35x faster                                          |
| generators               | 32.9 ms                                                | 24.8 ms: 1.33x faster                                         |
| spectral_norm            | 96.4 ms                                                | 73.8 ms: 1.31x faster                                         |
| json_dumps               | 8.38 ms                                                | 6.44 ms: 1.30x faster                                         |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.27 sec: 1.30x faster                                        |
| mako                     | 10.5 ms                                                | 8.10 ms: 1.29x faster                                         |
| tornado_http             | 91.9 ms                                                | 71.5 ms: 1.29x faster                                         |
| regex_compile            | 96.6 ms                                                | 75.9 ms: 1.27x faster                                         |
| logging_format           | 5.01 us                                                | 3.95 us: 1.27x faster                                         |
| logging_simple           | 4.63 us                                                | 3.67 us: 1.26x faster                                         |
| create_gc_cycles         | 876 us                                                 | 696 us: 1.26x faster                                          |
| float                    | 72.3 ms                                                | 57.6 ms: 1.26x faster                                         |
| pprint_pformat           | 1.24 sec                                               | 989 ms: 1.25x faster                                          |
| pprint_safe_repr         | 609 ms                                                 | 488 ms: 1.25x faster                                          |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 541 ms: 1.24x faster                                          |
| deepcopy_memo            | 34.5 us                                                | 28.2 us: 1.22x faster                                         |
| dulwich_log              | 37.1 ms                                                | 30.4 ms: 1.22x faster                                         |
| deepcopy                 | 278 us                                                 | 228 us: 1.22x faster                                          |
| mypy2                    | 308 ms                                                 | 259 ms: 1.19x faster                                          |
| xml_etree_process        | 45.1 ms                                                | 38.2 ms: 1.18x faster                                         |
| coroutines               | 20.2 ms                                                | 17.2 ms: 1.18x faster                                         |
| deepcopy_reduce          | 2.38 us                                                | 2.05 us: 1.16x faster                                         |
| docutils                 | 1.78 sec                                               | 1.54 sec: 1.16x faster                                        |
| tomli_loads              | 1.76 sec                                               | 1.52 sec: 1.16x faster                                        |
| fannkuch                 | 317 ms                                                 | 279 ms: 1.14x faster                                          |
| bench_thread_pool        | 548 us                                                 | 484 us: 1.13x faster                                          |
| scimark_fft              | 232 ms                                                 | 205 ms: 1.13x faster                                          |
| nqueens                  | 68.1 ms                                                | 60.4 ms: 1.13x faster                                         |
| sqlglot_optimize         | 38.0 ms                                                | 34.0 ms: 1.12x faster                                         |
| regex_v8                 | 17.5 ms                                                | 15.9 ms: 1.10x faster                                         |
| comprehensions           | 17.7 us                                                | 16.1 us: 1.10x faster                                         |
| meteor_contest           | 78.6 ms                                                | 73.3 ms: 1.07x faster                                         |
| sqlglot_normalize        | 197 ms                                                 | 183 ms: 1.07x faster                                          |
| regex_dna                | 160 ms                                                 | 150 ms: 1.07x faster                                          |
| unpickle                 | 9.77 us                                                | 9.31 us: 1.05x faster                                         |
| json                     | 3.10 ms                                                | 3.00 ms: 1.03x faster                                         |
| mdp                      | 1.67 sec                                               | 1.64 sec: 1.01x faster                                        |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                          |
| python_startup           | 12.6 ms                                                | 12.7 ms: 1.01x slower                                         |
| pickle                   | 7.36 us                                                | 7.44 us: 1.01x slower                                         |
| pickle_list              | 2.83 us                                                | 2.88 us: 1.02x slower                                         |
| pickle_dict              | 17.8 us                                                | 18.1 us: 1.02x slower                                         |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.54 ms: 1.02x slower                                         |
| xml_etree_iterparse      | 72.6 ms                                                | 74.4 ms: 1.02x slower                                         |
| xml_etree_generate       | 54.3 ms                                                | 56.0 ms: 1.03x slower                                         |
| xml_etree_parse          | 107 ms                                                 | 111 ms: 1.03x slower                                          |
| json_loads               | 16.9 us                                                | 17.6 us: 1.04x slower                                         |
| telco                    | 3.68 ms                                                | 3.84 ms: 1.04x slower                                         |
| regex_effbot             | 2.45 ms                                                | 2.56 ms: 1.05x slower                                         |
| sqlite_synth             | 1.47 us                                                | 1.57 us: 1.07x slower                                         |
| python_startup_no_site   | 9.73 ms                                                | 10.5 ms: 1.08x slower                                         |
| bench_mp_pool            | 41.0 ms                                                | 47.3 ms: 1.15x slower                                         |
| pathlib                  | 28.8 ms                                                | 33.9 ms: 1.18x slower                                         |
| unpickle_list            | 2.66 us                                                | 3.25 us: 1.22x slower                                         |
| coverage                 | 40.8 ms                                                | 50.4 ms: 1.23x slower                                         |
| dask                     | 258 ms                                                 | 325 ms: 1.26x slower                                          |
| async_generators         | 233 ms                                                 | 307 ms: 1.31x slower                                          |
| Geometric mean           | (ref)                                                  | 1.21x faster                                                  |

Benchmark hidden because not significant (1): gc_traversal
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
