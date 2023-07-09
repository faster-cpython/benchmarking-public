
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: darwin-arm64
- commit hash: 60ade0c
- commit date: 2023-07-08
- overall geometric mean: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-darwin-arm64-python-3.12-3.12.0b3+-60ade0c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 169 ms: 1.20x faster                                   |
| docutils       | 1.78 sec                                               | 1.52 sec: 1.17x faster                                 |
| tornado_http   | 91.9 ms                                                | 70.4 ms: 1.31x faster                                  |
| Geometric mean | (ref)                                                  | 1.22x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-darwin-arm64-python-3.12-3.12.0b3+-60ade0c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 68.5 ms: 1.37x faster                                  |
| float          | 72.3 ms                                                | 57.3 ms: 1.26x faster                                  |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.20x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-darwin-arm64-python-3.12-3.12.0b3+-60ade0c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 76.3 ms: 1.27x faster                                  |
| regex_v8       | 17.5 ms                                                | 15.9 ms: 1.10x faster                                  |
| regex_dna      | 160 ms                                                 | 150 ms: 1.07x faster                                   |
| regex_effbot   | 2.45 ms                                                | 2.58 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-darwin-arm64-python-3.12-3.12.0b3+-60ade0c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 192 us: 1.48x faster                                   |
| unpickle_pure_python | 203 us                                                 | 147 us: 1.38x faster                                   |
| json_dumps           | 8.38 ms                                                | 6.31 ms: 1.33x faster                                  |
| tomli_loads          | 1.76 sec                                               | 1.39 sec: 1.27x faster                                 |
| xml_etree_process    | 45.1 ms                                                | 39.1 ms: 1.15x faster                                  |
| unpickle             | 9.77 us                                                | 9.32 us: 1.05x faster                                  |
| pickle_dict          | 17.8 us                                                | 17.9 us: 1.00x slower                                  |
| pickle_list          | 2.83 us                                                | 2.85 us: 1.01x slower                                  |
| xml_etree_parse      | 107 ms                                                 | 111 ms: 1.03x slower                                   |
| xml_etree_generate   | 54.3 ms                                                | 56.3 ms: 1.04x slower                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 75.4 ms: 1.04x slower                                  |
| json_loads           | 16.9 us                                                | 17.6 us: 1.04x slower                                  |
| unpickle_list        | 2.66 us                                                | 3.19 us: 1.20x slower                                  |
| Geometric mean       | (ref)                                                  | 1.08x faster                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-darwin-arm64-python-3.12-3.12.0b3+-60ade0c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 11.8 ms: 1.07x faster                                  |
| python_startup_no_site | 9.73 ms                                                | 9.60 ms: 1.01x faster                                  |
| Geometric mean         | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-darwin-arm64-python-3.12-3.12.0b3+-60ade0c |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.59 ms: 1.38x faster                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230708-darwin-arm64-python-3.12-3.12.0b3+-60ade0c |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 91.6 us: 3.75x faster                                  |
| deltablue                | 5.15 ms                                                | 2.42 ms: 2.13x faster                                  |
| richards_super           | 60.7 ms                                                | 34.1 ms: 1.78x faster                                  |
| go                       | 165 ms                                                 | 94.1 ms: 1.75x faster                                  |
| logging_silent           | 119 ns                                                 | 69.1 ns: 1.72x faster                                  |
| richards                 | 51.4 ms                                                | 30.4 ms: 1.69x faster                                  |
| scimark_monte_carlo      | 72.2 ms                                                | 43.2 ms: 1.67x faster                                  |
| sqlglot_parse            | 1.33 ms                                                | 827 us: 1.61x faster                                   |
| chaos                    | 66.8 ms                                                | 42.0 ms: 1.59x faster                                  |
| raytrace                 | 328 ms                                                 | 207 ms: 1.58x faster                                   |
| async_tree_memoization   | 493 ms                                                 | 312 ms: 1.58x faster                                   |
| sqlglot_transpile        | 1.54 ms                                                | 1.00 ms: 1.53x faster                                  |
| async_tree_io            | 1.02 sec                                               | 667 ms: 1.53x faster                                   |
| async_tree_none          | 402 ms                                                 | 266 ms: 1.51x faster                                   |
| scimark_lu               | 110 ms                                                 | 72.8 ms: 1.51x faster                                  |
| crypto_pyaes             | 78.0 ms                                                | 51.6 ms: 1.51x faster                                  |
| hexiom                   | 6.32 ms                                                | 4.23 ms: 1.49x faster                                  |
| pickle_pure_python       | 284 us                                                 | 192 us: 1.48x faster                                   |
| scimark_sor              | 127 ms                                                 | 85.8 ms: 1.48x faster                                  |
| pyflate                  | 453 ms                                                 | 309 ms: 1.47x faster                                   |
| asyncio_tcp              | 673 ms                                                 | 482 ms: 1.40x faster                                   |
| unpickle_pure_python     | 203 us                                                 | 147 us: 1.38x faster                                   |
| deepcopy_memo            | 34.5 us                                                | 25.0 us: 1.38x faster                                  |
| mako                     | 10.5 ms                                                | 7.59 ms: 1.38x faster                                  |
| nbody                    | 94.1 ms                                                | 68.5 ms: 1.37x faster                                  |
| pycparser                | 915 ms                                                 | 673 ms: 1.36x faster                                   |
| unpack_sequence          | 38.7 ns                                                | 28.7 ns: 1.35x faster                                  |
| json_dumps               | 8.38 ms                                                | 6.31 ms: 1.33x faster                                  |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.26 sec: 1.31x faster                                 |
| sqlalchemy_imperative    | 9.03 ms                                                | 6.91 ms: 1.31x faster                                  |
| tornado_http             | 91.9 ms                                                | 70.4 ms: 1.31x faster                                  |
| logging_format           | 5.01 us                                                | 3.86 us: 1.30x faster                                  |
| spectral_norm            | 96.4 ms                                                | 74.6 ms: 1.29x faster                                  |
| logging_simple           | 4.63 us                                                | 3.58 us: 1.29x faster                                  |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 528 ms: 1.27x faster                                   |
| tomli_loads              | 1.76 sec                                               | 1.39 sec: 1.27x faster                                 |
| regex_compile            | 96.6 ms                                                | 76.3 ms: 1.27x faster                                  |
| float                    | 72.3 ms                                                | 57.3 ms: 1.26x faster                                  |
| pprint_pformat           | 1.24 sec                                               | 995 ms: 1.25x faster                                   |
| create_gc_cycles         | 876 us                                                 | 704 us: 1.24x faster                                   |
| generators               | 32.9 ms                                                | 26.5 ms: 1.24x faster                                  |
| pprint_safe_repr         | 609 ms                                                 | 492 ms: 1.24x faster                                   |
| dulwich_log              | 37.1 ms                                                | 30.0 ms: 1.24x faster                                  |
| deepcopy                 | 278 us                                                 | 228 us: 1.22x faster                                   |
| 2to3                     | 202 ms                                                 | 169 ms: 1.20x faster                                   |
| fannkuch                 | 317 ms                                                 | 266 ms: 1.19x faster                                   |
| mypy2                    | 308 ms                                                 | 259 ms: 1.19x faster                                   |
| comprehensions           | 17.7 us                                                | 15.1 us: 1.17x faster                                  |
| docutils                 | 1.78 sec                                               | 1.52 sec: 1.17x faster                                 |
| deepcopy_reduce          | 2.38 us                                                | 2.06 us: 1.15x faster                                  |
| scimark_fft              | 232 ms                                                 | 201 ms: 1.15x faster                                   |
| xml_etree_process        | 45.1 ms                                                | 39.1 ms: 1.15x faster                                  |
| coroutines               | 20.2 ms                                                | 17.6 ms: 1.15x faster                                  |
| sqlalchemy_declarative   | 74.8 ms                                                | 65.5 ms: 1.14x faster                                  |
| bench_thread_pool        | 548 us                                                 | 484 us: 1.13x faster                                   |
| nqueens                  | 68.1 ms                                                | 60.2 ms: 1.13x faster                                  |
| sqlglot_optimize         | 38.0 ms                                                | 34.3 ms: 1.11x faster                                  |
| regex_v8                 | 17.5 ms                                                | 15.9 ms: 1.10x faster                                  |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.17 ms: 1.10x faster                                  |
| python_startup           | 12.6 ms                                                | 11.8 ms: 1.07x faster                                  |
| regex_dna                | 160 ms                                                 | 150 ms: 1.07x faster                                   |
| sqlglot_normalize        | 197 ms                                                 | 185 ms: 1.06x faster                                   |
| meteor_contest           | 78.6 ms                                                | 74.3 ms: 1.06x faster                                  |
| unpickle                 | 9.77 us                                                | 9.32 us: 1.05x faster                                  |
| json                     | 3.10 ms                                                | 2.99 ms: 1.04x faster                                  |
| mdp                      | 1.67 sec                                               | 1.63 sec: 1.02x faster                                 |
| python_startup_no_site   | 9.73 ms                                                | 9.60 ms: 1.01x faster                                  |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x faster                                   |
| gc_traversal             | 2.40 ms                                                | 2.41 ms: 1.00x slower                                  |
| pickle_dict              | 17.8 us                                                | 17.9 us: 1.00x slower                                  |
| telco                    | 3.68 ms                                                | 3.70 ms: 1.01x slower                                  |
| pickle_list              | 2.83 us                                                | 2.85 us: 1.01x slower                                  |
| xml_etree_parse          | 107 ms                                                 | 111 ms: 1.03x slower                                   |
| xml_etree_generate       | 54.3 ms                                                | 56.3 ms: 1.04x slower                                  |
| xml_etree_iterparse      | 72.6 ms                                                | 75.4 ms: 1.04x slower                                  |
| json_loads               | 16.9 us                                                | 17.6 us: 1.04x slower                                  |
| regex_effbot             | 2.45 ms                                                | 2.58 ms: 1.05x slower                                  |
| sqlite_synth             | 1.47 us                                                | 1.62 us: 1.10x slower                                  |
| bench_mp_pool            | 41.0 ms                                                | 45.6 ms: 1.11x slower                                  |
| pathlib                  | 28.8 ms                                                | 33.5 ms: 1.16x slower                                  |
| unpickle_list            | 2.66 us                                                | 3.19 us: 1.20x slower                                  |
| coverage                 | 40.8 ms                                                | 50.5 ms: 1.24x slower                                  |
| dask                     | 258 ms                                                 | 320 ms: 1.24x slower                                   |
| async_generators         | 233 ms                                                 | 308 ms: 1.32x slower                                   |
| Geometric mean           | (ref)                                                  | 1.23x faster                                           |

Benchmark hidden because not significant (1): pickle
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
