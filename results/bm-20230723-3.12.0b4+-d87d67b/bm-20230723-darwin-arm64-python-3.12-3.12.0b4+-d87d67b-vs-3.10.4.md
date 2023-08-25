
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: darwin-arm64
- commit hash: d87d67b
- commit date: 2023-07-23
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230723-darwin-arm64-python-3.12-3.12.0b4+-d87d67b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 168 ms: 1.20x faster                                   |
| docutils       | 1.78 sec                                               | 1.51 sec: 1.18x faster                                 |
| tornado_http   | 91.9 ms                                                | 70.3 ms: 1.31x faster                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230723-darwin-arm64-python-3.12-3.12.0b4+-d87d67b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 69.6 ms: 1.35x faster                                  |
| float          | 72.3 ms                                                | 56.8 ms: 1.27x faster                                  |
| Geometric mean | (ref)                                                  | 1.20x faster                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230723-darwin-arm64-python-3.12-3.12.0b4+-d87d67b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 75.9 ms: 1.27x faster                                  |
| regex_v8       | 17.5 ms                                                | 15.8 ms: 1.11x faster                                  |
| regex_dna      | 160 ms                                                 | 151 ms: 1.06x faster                                   |
| regex_effbot   | 2.45 ms                                                | 2.58 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230723-darwin-arm64-python-3.12-3.12.0b4+-d87d67b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 191 us: 1.48x faster                                   |
| unpickle_pure_python | 203 us                                                 | 146 us: 1.39x faster                                   |
| json_dumps           | 8.38 ms                                                | 6.35 ms: 1.32x faster                                  |
| tomli_loads          | 1.76 sec                                               | 1.39 sec: 1.27x faster                                 |
| xml_etree_process    | 45.1 ms                                                | 39.0 ms: 1.16x faster                                  |
| unpickle             | 9.77 us                                                | 9.27 us: 1.05x faster                                  |
| pickle_list          | 2.83 us                                                | 2.81 us: 1.01x faster                                  |
| pickle               | 7.36 us                                                | 7.39 us: 1.00x slower                                  |
| pickle_dict          | 17.8 us                                                | 17.9 us: 1.01x slower                                  |
| xml_etree_parse      | 107 ms                                                 | 110 ms: 1.02x slower                                   |
| xml_etree_iterparse  | 72.6 ms                                                | 75.1 ms: 1.03x slower                                  |
| xml_etree_generate   | 54.3 ms                                                | 56.1 ms: 1.03x slower                                  |
| json_loads           | 16.9 us                                                | 17.5 us: 1.04x slower                                  |
| unpickle_list        | 2.66 us                                                | 3.16 us: 1.19x slower                                  |
| Geometric mean       | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230723-darwin-arm64-python-3.12-3.12.0b4+-d87d67b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 10.9 ms: 1.15x faster                                  |
| python_startup_no_site | 9.73 ms                                                | 8.80 ms: 1.10x faster                                  |
| Geometric mean         | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230723-darwin-arm64-python-3.12-3.12.0b4+-d87d67b |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.59 ms: 1.38x faster                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230723-darwin-arm64-python-3.12-3.12.0b4+-d87d67b |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 90.6 us: 3.80x faster                                  |
| deltablue                | 5.15 ms                                                | 2.42 ms: 2.13x faster                                  |
| richards_super           | 60.7 ms                                                | 34.0 ms: 1.79x faster                                  |
| go                       | 165 ms                                                 | 94.6 ms: 1.74x faster                                  |
| logging_silent           | 119 ns                                                 | 68.6 ns: 1.74x faster                                  |
| richards                 | 51.4 ms                                                | 30.3 ms: 1.70x faster                                  |
| scimark_monte_carlo      | 72.2 ms                                                | 43.3 ms: 1.67x faster                                  |
| sqlglot_parse            | 1.33 ms                                                | 833 us: 1.60x faster                                   |
| chaos                    | 66.8 ms                                                | 42.0 ms: 1.59x faster                                  |
| async_tree_memoization   | 493 ms                                                 | 311 ms: 1.58x faster                                   |
| raytrace                 | 328 ms                                                 | 207 ms: 1.58x faster                                   |
| sqlglot_transpile        | 1.54 ms                                                | 1.00 ms: 1.53x faster                                  |
| async_tree_io            | 1.02 sec                                               | 665 ms: 1.53x faster                                   |
| async_tree_none          | 402 ms                                                 | 265 ms: 1.52x faster                                   |
| crypto_pyaes             | 78.0 ms                                                | 51.6 ms: 1.51x faster                                  |
| scimark_lu               | 110 ms                                                 | 72.8 ms: 1.51x faster                                  |
| hexiom                   | 6.32 ms                                                | 4.23 ms: 1.49x faster                                  |
| pickle_pure_python       | 284 us                                                 | 191 us: 1.48x faster                                   |
| scimark_sor              | 127 ms                                                 | 85.7 ms: 1.48x faster                                  |
| pyflate                  | 453 ms                                                 | 309 ms: 1.47x faster                                   |
| asyncio_tcp              | 673 ms                                                 | 459 ms: 1.46x faster                                   |
| unpickle_pure_python     | 203 us                                                 | 146 us: 1.39x faster                                   |
| mako                     | 10.5 ms                                                | 7.59 ms: 1.38x faster                                  |
| deepcopy_memo            | 34.5 us                                                | 25.1 us: 1.38x faster                                  |
| pycparser                | 915 ms                                                 | 671 ms: 1.36x faster                                   |
| nbody                    | 94.1 ms                                                | 69.6 ms: 1.35x faster                                  |
| unpack_sequence          | 38.7 ns                                                | 28.7 ns: 1.35x faster                                  |
| json_dumps               | 8.38 ms                                                | 6.35 ms: 1.32x faster                                  |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.25 sec: 1.31x faster                                 |
| tornado_http             | 91.9 ms                                                | 70.3 ms: 1.31x faster                                  |
| logging_format           | 5.01 us                                                | 3.86 us: 1.30x faster                                  |
| logging_simple           | 4.63 us                                                | 3.58 us: 1.29x faster                                  |
| spectral_norm            | 96.4 ms                                                | 74.6 ms: 1.29x faster                                  |
| sqlalchemy_imperative    | 9.03 ms                                                | 7.00 ms: 1.29x faster                                  |
| regex_compile            | 96.6 ms                                                | 75.9 ms: 1.27x faster                                  |
| float                    | 72.3 ms                                                | 56.8 ms: 1.27x faster                                  |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 527 ms: 1.27x faster                                   |
| tomli_loads              | 1.76 sec                                               | 1.39 sec: 1.27x faster                                 |
| create_gc_cycles         | 876 us                                                 | 704 us: 1.24x faster                                   |
| generators               | 32.9 ms                                                | 26.5 ms: 1.24x faster                                  |
| pprint_pformat           | 1.24 sec                                               | 1.00 sec: 1.24x faster                                 |
| pprint_safe_repr         | 609 ms                                                 | 493 ms: 1.23x faster                                   |
| dulwich_log              | 37.1 ms                                                | 30.1 ms: 1.23x faster                                  |
| deepcopy                 | 278 us                                                 | 227 us: 1.22x faster                                   |
| 2to3                     | 202 ms                                                 | 168 ms: 1.20x faster                                   |
| fannkuch                 | 317 ms                                                 | 265 ms: 1.20x faster                                   |
| mypy2                    | 308 ms                                                 | 259 ms: 1.19x faster                                   |
| docutils                 | 1.78 sec                                               | 1.51 sec: 1.18x faster                                 |
| comprehensions           | 17.7 us                                                | 15.1 us: 1.17x faster                                  |
| scimark_fft              | 232 ms                                                 | 200 ms: 1.16x faster                                   |
| xml_etree_process        | 45.1 ms                                                | 39.0 ms: 1.16x faster                                  |
| deepcopy_reduce          | 2.38 us                                                | 2.07 us: 1.15x faster                                  |
| sqlalchemy_declarative   | 74.8 ms                                                | 64.9 ms: 1.15x faster                                  |
| python_startup           | 12.6 ms                                                | 10.9 ms: 1.15x faster                                  |
| coroutines               | 20.2 ms                                                | 17.6 ms: 1.15x faster                                  |
| bench_thread_pool        | 548 us                                                 | 485 us: 1.13x faster                                   |
| nqueens                  | 68.1 ms                                                | 60.4 ms: 1.13x faster                                  |
| sqlglot_optimize         | 38.0 ms                                                | 34.1 ms: 1.12x faster                                  |
| regex_v8                 | 17.5 ms                                                | 15.8 ms: 1.11x faster                                  |
| python_startup_no_site   | 9.73 ms                                                | 8.80 ms: 1.10x faster                                  |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.15 ms: 1.10x faster                                  |
| sqlglot_normalize        | 197 ms                                                 | 184 ms: 1.07x faster                                   |
| meteor_contest           | 78.6 ms                                                | 74.4 ms: 1.06x faster                                  |
| regex_dna                | 160 ms                                                 | 151 ms: 1.06x faster                                   |
| unpickle                 | 9.77 us                                                | 9.27 us: 1.05x faster                                  |
| mdp                      | 1.67 sec                                               | 1.62 sec: 1.03x faster                                 |
| json                     | 3.10 ms                                                | 3.03 ms: 1.02x faster                                  |
| pickle_list              | 2.83 us                                                | 2.81 us: 1.01x faster                                  |
| gc_traversal             | 2.40 ms                                                | 2.40 ms: 1.00x slower                                  |
| pickle                   | 7.36 us                                                | 7.39 us: 1.00x slower                                  |
| telco                    | 3.68 ms                                                | 3.71 ms: 1.01x slower                                  |
| pickle_dict              | 17.8 us                                                | 17.9 us: 1.01x slower                                  |
| xml_etree_parse          | 107 ms                                                 | 110 ms: 1.02x slower                                   |
| xml_etree_iterparse      | 72.6 ms                                                | 75.1 ms: 1.03x slower                                  |
| xml_etree_generate       | 54.3 ms                                                | 56.1 ms: 1.03x slower                                  |
| json_loads               | 16.9 us                                                | 17.5 us: 1.04x slower                                  |
| regex_effbot             | 2.45 ms                                                | 2.58 ms: 1.06x slower                                  |
| bench_mp_pool            | 41.0 ms                                                | 44.9 ms: 1.09x slower                                  |
| sqlite_synth             | 1.47 us                                                | 1.61 us: 1.10x slower                                  |
| pathlib                  | 28.8 ms                                                | 34.0 ms: 1.18x slower                                  |
| unpickle_list            | 2.66 us                                                | 3.16 us: 1.19x slower                                  |
| coverage                 | 40.8 ms                                                | 50.4 ms: 1.23x slower                                  |
| dask                     | 258 ms                                                 | 318 ms: 1.24x slower                                   |
| async_generators         | 233 ms                                                 | 307 ms: 1.32x slower                                   |
| Geometric mean           | (ref)                                                  | 1.23x faster                                           |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.16x
