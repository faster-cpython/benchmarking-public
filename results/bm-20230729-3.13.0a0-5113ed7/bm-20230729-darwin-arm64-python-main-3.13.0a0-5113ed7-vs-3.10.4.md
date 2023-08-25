
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 5113ed7
- commit date: 2023-07-29
- overall geometric mean: 1.17x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-darwin-arm64-python-main-3.13.0a0-5113ed7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 1.78 sec                                               | 1.56 sec: 1.15x faster                                |
| tornado_http   | 91.9 ms                                                | 72.9 ms: 1.26x faster                                 |
| Geometric mean | (ref)                                                  | 1.20x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-darwin-arm64-python-main-3.13.0a0-5113ed7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 94.1 ms                                                | 72.8 ms: 1.29x faster                                 |
| float          | 72.3 ms                                                | 60.4 ms: 1.20x faster                                 |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-darwin-arm64-python-main-3.13.0a0-5113ed7 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 81.5 ms: 1.19x faster                                 |
| regex_v8       | 17.5 ms                                                | 15.7 ms: 1.12x faster                                 |
| regex_dna      | 160 ms                                                 | 149 ms: 1.07x faster                                  |
| regex_effbot   | 2.45 ms                                                | 2.56 ms: 1.05x slower                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-darwin-arm64-python-main-3.13.0a0-5113ed7 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 205 us: 1.38x faster                                  |
| json_dumps           | 8.38 ms                                                | 6.61 ms: 1.27x faster                                 |
| unpickle_pure_python | 203 us                                                 | 166 us: 1.22x faster                                  |
| xml_etree_process    | 45.1 ms                                                | 41.5 ms: 1.09x faster                                 |
| tomli_loads          | 1.76 sec                                               | 1.67 sec: 1.06x faster                                |
| unpickle             | 9.77 us                                                | 9.30 us: 1.05x faster                                 |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                 |
| xml_etree_parse      | 107 ms                                                 | 110 ms: 1.02x slower                                  |
| pickle_list          | 2.83 us                                                | 2.91 us: 1.03x slower                                 |
| json_loads           | 16.9 us                                                | 17.6 us: 1.04x slower                                 |
| xml_etree_iterparse  | 72.6 ms                                                | 77.1 ms: 1.06x slower                                 |
| xml_etree_generate   | 54.3 ms                                                | 59.2 ms: 1.09x slower                                 |
| unpickle_list        | 2.66 us                                                | 3.15 us: 1.18x slower                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                          |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-darwin-arm64-python-main-3.13.0a0-5113ed7 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 10.3 ms: 1.23x faster                                 |
| python_startup_no_site | 9.73 ms                                                | 8.22 ms: 1.18x faster                                 |
| Geometric mean         | (ref)                                                  | 1.20x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-darwin-arm64-python-main-3.13.0a0-5113ed7 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.82 ms: 1.34x faster                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-darwin-arm64-python-main-3.13.0a0-5113ed7 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 96.4 us: 3.57x faster                                 |
| deltablue                | 5.15 ms                                                | 2.91 ms: 1.77x faster                                 |
| asyncio_tcp              | 673 ms                                                 | 407 ms: 1.65x faster                                  |
| crypto_pyaes             | 78.0 ms                                                | 48.7 ms: 1.60x faster                                 |
| chaos                    | 66.8 ms                                                | 43.3 ms: 1.54x faster                                 |
| async_tree_memoization   | 493 ms                                                 | 324 ms: 1.52x faster                                  |
| async_tree_io            | 1.02 sec                                               | 685 ms: 1.49x faster                                  |
| logging_silent           | 119 ns                                                 | 80.6 ns: 1.48x faster                                 |
| richards_super           | 60.7 ms                                                | 41.2 ms: 1.47x faster                                 |
| async_tree_none          | 402 ms                                                 | 274 ms: 1.47x faster                                  |
| sqlglot_parse            | 1.33 ms                                                | 931 us: 1.43x faster                                  |
| raytrace                 | 328 ms                                                 | 230 ms: 1.43x faster                                  |
| scimark_lu               | 110 ms                                                 | 77.8 ms: 1.41x faster                                 |
| pickle_pure_python       | 284 us                                                 | 205 us: 1.38x faster                                  |
| sqlglot_transpile        | 1.54 ms                                                | 1.11 ms: 1.38x faster                                 |
| unpack_sequence          | 38.7 ns                                                | 28.2 ns: 1.37x faster                                 |
| richards                 | 51.4 ms                                                | 37.6 ms: 1.37x faster                                 |
| go                       | 165 ms                                                 | 122 ms: 1.35x faster                                  |
| mako                     | 10.5 ms                                                | 7.82 ms: 1.34x faster                                 |
| scimark_monte_carlo      | 72.2 ms                                                | 54.5 ms: 1.33x faster                                 |
| hexiom                   | 6.32 ms                                                | 4.78 ms: 1.32x faster                                 |
| nbody                    | 94.1 ms                                                | 72.8 ms: 1.29x faster                                 |
| pycparser                | 915 ms                                                 | 711 ms: 1.29x faster                                  |
| json_dumps               | 8.38 ms                                                | 6.61 ms: 1.27x faster                                 |
| spectral_norm            | 96.4 ms                                                | 76.1 ms: 1.27x faster                                 |
| create_gc_cycles         | 876 us                                                 | 693 us: 1.26x faster                                  |
| tornado_http             | 91.9 ms                                                | 72.9 ms: 1.26x faster                                 |
| deepcopy_memo            | 34.5 us                                                | 27.4 us: 1.26x faster                                 |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 537 ms: 1.25x faster                                  |
| pyflate                  | 453 ms                                                 | 365 ms: 1.24x faster                                  |
| python_startup           | 12.6 ms                                                | 10.3 ms: 1.23x faster                                 |
| unpickle_pure_python     | 203 us                                                 | 166 us: 1.22x faster                                  |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.36 sec: 1.21x faster                                |
| float                    | 72.3 ms                                                | 60.4 ms: 1.20x faster                                 |
| logging_format           | 5.01 us                                                | 4.21 us: 1.19x faster                                 |
| regex_compile            | 96.6 ms                                                | 81.5 ms: 1.19x faster                                 |
| logging_simple           | 4.63 us                                                | 3.91 us: 1.18x faster                                 |
| python_startup_no_site   | 9.73 ms                                                | 8.22 ms: 1.18x faster                                 |
| generators               | 32.9 ms                                                | 28.0 ms: 1.18x faster                                 |
| mypy2                    | 308 ms                                                 | 263 ms: 1.17x faster                                  |
| dulwich_log              | 37.1 ms                                                | 31.7 ms: 1.17x faster                                 |
| pprint_safe_repr         | 609 ms                                                 | 531 ms: 1.15x faster                                  |
| deepcopy                 | 278 us                                                 | 242 us: 1.15x faster                                  |
| docutils                 | 1.78 sec                                               | 1.56 sec: 1.15x faster                                |
| pprint_pformat           | 1.24 sec                                               | 1.08 sec: 1.15x faster                                |
| scimark_fft              | 232 ms                                                 | 206 ms: 1.13x faster                                  |
| regex_v8                 | 17.5 ms                                                | 15.7 ms: 1.12x faster                                 |
| deepcopy_reduce          | 2.38 us                                                | 2.15 us: 1.11x faster                                 |
| fannkuch                 | 317 ms                                                 | 290 ms: 1.09x faster                                  |
| xml_etree_process        | 45.1 ms                                                | 41.5 ms: 1.09x faster                                 |
| bench_thread_pool        | 548 us                                                 | 507 us: 1.08x faster                                  |
| regex_dna                | 160 ms                                                 | 149 ms: 1.07x faster                                  |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.24 ms: 1.07x faster                                 |
| nqueens                  | 68.1 ms                                                | 63.5 ms: 1.07x faster                                 |
| tomli_loads              | 1.76 sec                                               | 1.67 sec: 1.06x faster                                |
| sqlglot_optimize         | 38.0 ms                                                | 35.9 ms: 1.06x faster                                 |
| scimark_sor              | 127 ms                                                 | 120 ms: 1.06x faster                                  |
| comprehensions           | 17.7 us                                                | 16.8 us: 1.05x faster                                 |
| unpickle                 | 9.77 us                                                | 9.30 us: 1.05x faster                                 |
| coroutines               | 20.2 ms                                                | 19.4 ms: 1.04x faster                                 |
| json                     | 3.10 ms                                                | 3.00 ms: 1.03x faster                                 |
| meteor_contest           | 78.6 ms                                                | 77.3 ms: 1.02x faster                                 |
| sqlglot_normalize        | 197 ms                                                 | 194 ms: 1.01x faster                                  |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                  |
| mdp                      | 1.67 sec                                               | 1.69 sec: 1.01x slower                                |
| pickle_dict              | 17.8 us                                                | 18.0 us: 1.01x slower                                 |
| xml_etree_parse          | 107 ms                                                 | 110 ms: 1.02x slower                                  |
| pickle_list              | 2.83 us                                                | 2.91 us: 1.03x slower                                 |
| pathlib                  | 28.8 ms                                                | 29.8 ms: 1.03x slower                                 |
| json_loads               | 16.9 us                                                | 17.6 us: 1.04x slower                                 |
| regex_effbot             | 2.45 ms                                                | 2.56 ms: 1.05x slower                                 |
| xml_etree_iterparse      | 72.6 ms                                                | 77.1 ms: 1.06x slower                                 |
| bench_mp_pool            | 41.0 ms                                                | 44.2 ms: 1.08x slower                                 |
| xml_etree_generate       | 54.3 ms                                                | 59.2 ms: 1.09x slower                                 |
| sqlite_synth             | 1.47 us                                                | 1.61 us: 1.09x slower                                 |
| unpickle_list            | 2.66 us                                                | 3.15 us: 1.18x slower                                 |
| telco                    | 3.68 ms                                                | 4.58 ms: 1.24x slower                                 |
| coverage                 | 40.8 ms                                                | 51.8 ms: 1.27x slower                                 |
| dask                     | 258 ms                                                 | 342 ms: 1.33x slower                                  |
| async_generators         | 233 ms                                                 | 316 ms: 1.36x slower                                  |
| Geometric mean           | (ref)                                                  | 1.17x faster                                          |

Benchmark hidden because not significant (2): pickle, gc_traversal
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.09x
