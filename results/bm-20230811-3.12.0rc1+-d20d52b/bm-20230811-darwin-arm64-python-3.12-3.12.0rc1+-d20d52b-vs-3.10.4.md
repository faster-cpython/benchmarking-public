
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: darwin-arm64
- commit hash: d20d52b
- commit date: 2023-08-11
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-darwin-arm64-python-3.12-3.12.0rc1+-d20d52b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 167 ms: 1.21x faster                                    |
| docutils       | 1.78 sec                                               | 1.47 sec: 1.21x faster                                  |
| tornado_http   | 91.9 ms                                                | 72.1 ms: 1.27x faster                                   |
| Geometric mean | (ref)                                                  | 1.23x faster                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-darwin-arm64-python-3.12-3.12.0rc1+-d20d52b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 69.0 ms: 1.37x faster                                   |
| float          | 72.3 ms                                                | 56.5 ms: 1.28x faster                                   |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                    |
| Geometric mean | (ref)                                                  | 1.21x faster                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-darwin-arm64-python-3.12-3.12.0rc1+-d20d52b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 75.5 ms: 1.28x faster                                   |
| regex_v8       | 17.5 ms                                                | 15.3 ms: 1.15x faster                                   |
| regex_dna      | 160 ms                                                 | 148 ms: 1.08x faster                                    |
| regex_effbot   | 2.45 ms                                                | 2.54 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-darwin-arm64-python-3.12-3.12.0rc1+-d20d52b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 189 us: 1.50x faster                                    |
| unpickle_pure_python | 203 us                                                 | 145 us: 1.40x faster                                    |
| json_dumps           | 8.38 ms                                                | 6.31 ms: 1.33x faster                                   |
| tomli_loads          | 1.76 sec                                               | 1.38 sec: 1.27x faster                                  |
| xml_etree_process    | 45.1 ms                                                | 38.7 ms: 1.16x faster                                   |
| unpickle             | 9.77 us                                                | 9.23 us: 1.06x faster                                   |
| pickle               | 7.36 us                                                | 7.39 us: 1.00x slower                                   |
| pickle_list          | 2.83 us                                                | 2.86 us: 1.01x slower                                   |
| pickle_dict          | 17.8 us                                                | 18.0 us: 1.01x slower                                   |
| xml_etree_generate   | 54.3 ms                                                | 55.7 ms: 1.03x slower                                   |
| xml_etree_parse      | 107 ms                                                 | 110 ms: 1.03x slower                                    |
| xml_etree_iterparse  | 72.6 ms                                                | 74.9 ms: 1.03x slower                                   |
| json_loads           | 16.9 us                                                | 17.6 us: 1.04x slower                                   |
| unpickle_list        | 2.66 us                                                | 3.28 us: 1.23x slower                                   |
| Geometric mean       | (ref)                                                  | 1.08x faster                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-darwin-arm64-python-3.12-3.12.0rc1+-d20d52b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 11.3 ms: 1.12x faster                                   |
| python_startup_no_site | 9.73 ms                                                | 9.14 ms: 1.06x faster                                   |
| Geometric mean         | (ref)                                                  | 1.09x faster                                            |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-darwin-arm64-python-3.12-3.12.0rc1+-d20d52b |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.61 ms: 1.38x faster                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230811-darwin-arm64-python-3.12-3.12.0rc1+-d20d52b |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 90.8 us: 3.79x faster                                   |
| deltablue                | 5.15 ms                                                | 2.40 ms: 2.14x faster                                   |
| richards_super           | 60.7 ms                                                | 34.0 ms: 1.78x faster                                   |
| logging_silent           | 119 ns                                                 | 68.0 ns: 1.75x faster                                   |
| go                       | 165 ms                                                 | 94.0 ms: 1.75x faster                                   |
| richards                 | 51.4 ms                                                | 30.3 ms: 1.70x faster                                   |
| scimark_monte_carlo      | 72.2 ms                                                | 43.3 ms: 1.67x faster                                   |
| sqlglot_parse            | 1.33 ms                                                | 822 us: 1.62x faster                                    |
| async_tree_memoization   | 493 ms                                                 | 307 ms: 1.61x faster                                    |
| chaos                    | 66.8 ms                                                | 41.8 ms: 1.60x faster                                   |
| raytrace                 | 328 ms                                                 | 207 ms: 1.59x faster                                    |
| async_tree_io            | 1.02 sec                                               | 654 ms: 1.56x faster                                    |
| async_tree_none          | 402 ms                                                 | 260 ms: 1.55x faster                                    |
| sqlglot_transpile        | 1.54 ms                                                | 1000 us: 1.54x faster                                   |
| scimark_lu               | 110 ms                                                 | 72.2 ms: 1.52x faster                                   |
| hexiom                   | 6.32 ms                                                | 4.19 ms: 1.51x faster                                   |
| pickle_pure_python       | 284 us                                                 | 189 us: 1.50x faster                                    |
| crypto_pyaes             | 78.0 ms                                                | 52.0 ms: 1.50x faster                                   |
| asyncio_tcp              | 673 ms                                                 | 449 ms: 1.50x faster                                    |
| scimark_sor              | 127 ms                                                 | 85.5 ms: 1.48x faster                                   |
| pyflate                  | 453 ms                                                 | 307 ms: 1.48x faster                                    |
| unpickle_pure_python     | 203 us                                                 | 145 us: 1.40x faster                                    |
| deepcopy_memo            | 34.5 us                                                | 24.8 us: 1.39x faster                                   |
| pycparser                | 915 ms                                                 | 664 ms: 1.38x faster                                    |
| mako                     | 10.5 ms                                                | 7.61 ms: 1.38x faster                                   |
| nbody                    | 94.1 ms                                                | 69.0 ms: 1.37x faster                                   |
| unpack_sequence          | 38.7 ns                                                | 28.5 ns: 1.36x faster                                   |
| json_dumps               | 8.38 ms                                                | 6.31 ms: 1.33x faster                                   |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.24 sec: 1.33x faster                                  |
| sqlalchemy_imperative    | 9.03 ms                                                | 6.87 ms: 1.31x faster                                   |
| logging_format           | 5.01 us                                                | 3.85 us: 1.30x faster                                   |
| logging_simple           | 4.63 us                                                | 3.57 us: 1.30x faster                                   |
| spectral_norm            | 96.4 ms                                                | 74.7 ms: 1.29x faster                                   |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 521 ms: 1.29x faster                                    |
| float                    | 72.3 ms                                                | 56.5 ms: 1.28x faster                                   |
| regex_compile            | 96.6 ms                                                | 75.5 ms: 1.28x faster                                   |
| tornado_http             | 91.9 ms                                                | 72.1 ms: 1.27x faster                                   |
| tomli_loads              | 1.76 sec                                               | 1.38 sec: 1.27x faster                                  |
| generators               | 32.9 ms                                                | 26.0 ms: 1.27x faster                                   |
| create_gc_cycles         | 876 us                                                 | 700 us: 1.25x faster                                    |
| pprint_pformat           | 1.24 sec                                               | 994 ms: 1.25x faster                                    |
| pprint_safe_repr         | 609 ms                                                 | 489 ms: 1.25x faster                                    |
| dulwich_log              | 37.1 ms                                                | 30.1 ms: 1.23x faster                                   |
| deepcopy                 | 278 us                                                 | 226 us: 1.23x faster                                    |
| 2to3                     | 202 ms                                                 | 167 ms: 1.21x faster                                    |
| docutils                 | 1.78 sec                                               | 1.47 sec: 1.21x faster                                  |
| fannkuch                 | 317 ms                                                 | 262 ms: 1.21x faster                                    |
| mypy2                    | 308 ms                                                 | 256 ms: 1.21x faster                                    |
| comprehensions           | 17.7 us                                                | 15.0 us: 1.17x faster                                   |
| xml_etree_process        | 45.1 ms                                                | 38.7 ms: 1.16x faster                                   |
| deepcopy_reduce          | 2.38 us                                                | 2.05 us: 1.16x faster                                   |
| scimark_fft              | 232 ms                                                 | 200 ms: 1.16x faster                                    |
| sqlalchemy_declarative   | 74.8 ms                                                | 64.5 ms: 1.16x faster                                   |
| coroutines               | 20.2 ms                                                | 17.4 ms: 1.16x faster                                   |
| regex_v8                 | 17.5 ms                                                | 15.3 ms: 1.15x faster                                   |
| nqueens                  | 68.1 ms                                                | 59.5 ms: 1.14x faster                                   |
| bench_thread_pool        | 548 us                                                 | 486 us: 1.13x faster                                    |
| sqlglot_optimize         | 38.0 ms                                                | 33.8 ms: 1.12x faster                                   |
| python_startup           | 12.6 ms                                                | 11.3 ms: 1.12x faster                                   |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.19 ms: 1.09x faster                                   |
| regex_dna                | 160 ms                                                 | 148 ms: 1.08x faster                                    |
| sqlglot_normalize        | 197 ms                                                 | 183 ms: 1.07x faster                                    |
| meteor_contest           | 78.6 ms                                                | 73.6 ms: 1.07x faster                                   |
| python_startup_no_site   | 9.73 ms                                                | 9.14 ms: 1.06x faster                                   |
| unpickle                 | 9.77 us                                                | 9.23 us: 1.06x faster                                   |
| json                     | 3.10 ms                                                | 2.97 ms: 1.04x faster                                   |
| mdp                      | 1.67 sec                                               | 1.62 sec: 1.03x faster                                  |
| pidigits                 | 282 ms                                                 | 281 ms: 1.00x faster                                    |
| pickle                   | 7.36 us                                                | 7.39 us: 1.00x slower                                   |
| pickle_list              | 2.83 us                                                | 2.86 us: 1.01x slower                                   |
| pickle_dict              | 17.8 us                                                | 18.0 us: 1.01x slower                                   |
| xml_etree_generate       | 54.3 ms                                                | 55.7 ms: 1.03x slower                                   |
| xml_etree_parse          | 107 ms                                                 | 110 ms: 1.03x slower                                    |
| xml_etree_iterparse      | 72.6 ms                                                | 74.9 ms: 1.03x slower                                   |
| telco                    | 3.68 ms                                                | 3.81 ms: 1.03x slower                                   |
| regex_effbot             | 2.45 ms                                                | 2.54 ms: 1.04x slower                                   |
| json_loads               | 16.9 us                                                | 17.6 us: 1.04x slower                                   |
| pathlib                  | 28.8 ms                                                | 30.5 ms: 1.06x slower                                   |
| sqlite_synth             | 1.47 us                                                | 1.61 us: 1.09x slower                                   |
| bench_mp_pool            | 41.0 ms                                                | 45.1 ms: 1.10x slower                                   |
| dask                     | 258 ms                                                 | 316 ms: 1.23x slower                                    |
| unpickle_list            | 2.66 us                                                | 3.28 us: 1.23x slower                                   |
| coverage                 | 40.8 ms                                                | 50.5 ms: 1.24x slower                                   |
| async_generators         | 233 ms                                                 | 306 ms: 1.31x slower                                    |
| Geometric mean           | (ref)                                                  | 1.24x faster                                            |

Benchmark hidden because not significant (1): gc_traversal
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.16x
