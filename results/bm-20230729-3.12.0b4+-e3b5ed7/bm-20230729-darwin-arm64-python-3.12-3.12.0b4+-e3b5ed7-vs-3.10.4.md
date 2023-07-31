
# Results vs. 3.10.4

- fork: python
- ref: 3.12
- machine: darwin-arm64
- commit hash: e3b5ed7
- commit date: 2023-07-29
- overall geometric mean: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-darwin-arm64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 167 ms: 1.21x faster                                   |
| docutils       | 1.78 sec                                               | 1.50 sec: 1.19x faster                                 |
| tornado_http   | 91.9 ms                                                | 70.8 ms: 1.30x faster                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-darwin-arm64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 69.0 ms: 1.37x faster                                  |
| float          | 72.3 ms                                                | 56.3 ms: 1.28x faster                                  |
| Geometric mean | (ref)                                                  | 1.21x faster                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-darwin-arm64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 75.6 ms: 1.28x faster                                  |
| regex_v8       | 17.5 ms                                                | 15.8 ms: 1.11x faster                                  |
| regex_dna      | 160 ms                                                 | 150 ms: 1.07x faster                                   |
| regex_effbot   | 2.45 ms                                                | 2.57 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-darwin-arm64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 189 us: 1.50x faster                                   |
| unpickle_pure_python | 203 us                                                 | 145 us: 1.40x faster                                   |
| json_dumps           | 8.38 ms                                                | 6.32 ms: 1.33x faster                                  |
| tomli_loads          | 1.76 sec                                               | 1.39 sec: 1.27x faster                                 |
| xml_etree_process    | 45.1 ms                                                | 38.7 ms: 1.16x faster                                  |
| unpickle             | 9.77 us                                                | 9.27 us: 1.05x faster                                  |
| pickle_dict          | 17.8 us                                                | 17.9 us: 1.01x slower                                  |
| pickle_list          | 2.83 us                                                | 2.89 us: 1.02x slower                                  |
| xml_etree_iterparse  | 72.6 ms                                                | 74.4 ms: 1.02x slower                                  |
| xml_etree_parse      | 107 ms                                                 | 110 ms: 1.03x slower                                   |
| xml_etree_generate   | 54.3 ms                                                | 56.0 ms: 1.03x slower                                  |
| json_loads           | 16.9 us                                                | 17.5 us: 1.04x slower                                  |
| unpickle_list        | 2.66 us                                                | 3.27 us: 1.23x slower                                  |
| Geometric mean       | (ref)                                                  | 1.08x faster                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-darwin-arm64-python-3.12-3.12.0b4+-e3b5ed7 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 10.5 ms: 1.20x faster                                  |
| python_startup_no_site | 9.73 ms                                                | 8.42 ms: 1.15x faster                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-darwin-arm64-python-3.12-3.12.0b4+-e3b5ed7 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.61 ms: 1.38x faster                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230729-darwin-arm64-python-3.12-3.12.0b4+-e3b5ed7 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 90.7 us: 3.79x faster                                  |
| deltablue                | 5.15 ms                                                | 2.40 ms: 2.14x faster                                  |
| richards_super           | 60.7 ms                                                | 34.0 ms: 1.79x faster                                  |
| logging_silent           | 119 ns                                                 | 67.9 ns: 1.75x faster                                  |
| go                       | 165 ms                                                 | 94.0 ms: 1.75x faster                                  |
| richards                 | 51.4 ms                                                | 30.3 ms: 1.70x faster                                  |
| scimark_monte_carlo      | 72.2 ms                                                | 43.4 ms: 1.67x faster                                  |
| sqlglot_parse            | 1.33 ms                                                | 827 us: 1.61x faster                                   |
| async_tree_memoization   | 493 ms                                                 | 306 ms: 1.61x faster                                   |
| chaos                    | 66.8 ms                                                | 41.7 ms: 1.60x faster                                  |
| raytrace                 | 328 ms                                                 | 206 ms: 1.59x faster                                   |
| async_tree_io            | 1.02 sec                                               | 651 ms: 1.57x faster                                   |
| async_tree_none          | 402 ms                                                 | 260 ms: 1.55x faster                                   |
| sqlglot_transpile        | 1.54 ms                                                | 1000 us: 1.54x faster                                  |
| asyncio_tcp              | 673 ms                                                 | 440 ms: 1.53x faster                                   |
| scimark_lu               | 110 ms                                                 | 72.2 ms: 1.52x faster                                  |
| crypto_pyaes             | 78.0 ms                                                | 51.5 ms: 1.51x faster                                  |
| hexiom                   | 6.32 ms                                                | 4.19 ms: 1.51x faster                                  |
| pickle_pure_python       | 284 us                                                 | 189 us: 1.50x faster                                   |
| scimark_sor              | 127 ms                                                 | 85.4 ms: 1.48x faster                                  |
| pyflate                  | 453 ms                                                 | 307 ms: 1.48x faster                                   |
| unpickle_pure_python     | 203 us                                                 | 145 us: 1.40x faster                                   |
| deepcopy_memo            | 34.5 us                                                | 24.7 us: 1.39x faster                                  |
| mako                     | 10.5 ms                                                | 7.61 ms: 1.38x faster                                  |
| pycparser                | 915 ms                                                 | 666 ms: 1.37x faster                                   |
| nbody                    | 94.1 ms                                                | 69.0 ms: 1.37x faster                                  |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.23 sec: 1.33x faster                                 |
| unpack_sequence          | 38.7 ns                                                | 29.1 ns: 1.33x faster                                  |
| json_dumps               | 8.38 ms                                                | 6.32 ms: 1.33x faster                                  |
| sqlalchemy_imperative    | 9.03 ms                                                | 6.92 ms: 1.31x faster                                  |
| logging_format           | 5.01 us                                                | 3.84 us: 1.30x faster                                  |
| logging_simple           | 4.63 us                                                | 3.56 us: 1.30x faster                                  |
| tornado_http             | 91.9 ms                                                | 70.8 ms: 1.30x faster                                  |
| spectral_norm            | 96.4 ms                                                | 74.6 ms: 1.29x faster                                  |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 520 ms: 1.29x faster                                   |
| float                    | 72.3 ms                                                | 56.3 ms: 1.28x faster                                  |
| regex_compile            | 96.6 ms                                                | 75.6 ms: 1.28x faster                                  |
| tomli_loads              | 1.76 sec                                               | 1.39 sec: 1.27x faster                                 |
| generators               | 32.9 ms                                                | 26.0 ms: 1.27x faster                                  |
| create_gc_cycles         | 876 us                                                 | 701 us: 1.25x faster                                   |
| deepcopy                 | 278 us                                                 | 224 us: 1.24x faster                                   |
| dulwich_log              | 37.1 ms                                                | 30.0 ms: 1.24x faster                                  |
| pprint_pformat           | 1.24 sec                                               | 1.02 sec: 1.22x faster                                 |
| pprint_safe_repr         | 609 ms                                                 | 502 ms: 1.21x faster                                   |
| 2to3                     | 202 ms                                                 | 167 ms: 1.21x faster                                   |
| mypy2                    | 308 ms                                                 | 255 ms: 1.21x faster                                   |
| python_startup           | 12.6 ms                                                | 10.5 ms: 1.20x faster                                  |
| fannkuch                 | 317 ms                                                 | 266 ms: 1.19x faster                                   |
| docutils                 | 1.78 sec                                               | 1.50 sec: 1.19x faster                                 |
| comprehensions           | 17.7 us                                                | 15.0 us: 1.17x faster                                  |
| deepcopy_reduce          | 2.38 us                                                | 2.04 us: 1.17x faster                                  |
| xml_etree_process        | 45.1 ms                                                | 38.7 ms: 1.16x faster                                  |
| scimark_fft              | 232 ms                                                 | 200 ms: 1.16x faster                                   |
| coroutines               | 20.2 ms                                                | 17.4 ms: 1.16x faster                                  |
| sqlalchemy_declarative   | 74.8 ms                                                | 64.5 ms: 1.16x faster                                  |
| python_startup_no_site   | 9.73 ms                                                | 8.42 ms: 1.15x faster                                  |
| nqueens                  | 68.1 ms                                                | 59.4 ms: 1.15x faster                                  |
| bench_thread_pool        | 548 us                                                 | 485 us: 1.13x faster                                   |
| sqlglot_optimize         | 38.0 ms                                                | 33.9 ms: 1.12x faster                                  |
| regex_v8                 | 17.5 ms                                                | 15.8 ms: 1.11x faster                                  |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.16 ms: 1.10x faster                                  |
| sqlglot_normalize        | 197 ms                                                 | 184 ms: 1.07x faster                                   |
| regex_dna                | 160 ms                                                 | 150 ms: 1.07x faster                                   |
| meteor_contest           | 78.6 ms                                                | 73.8 ms: 1.07x faster                                  |
| unpickle                 | 9.77 us                                                | 9.27 us: 1.05x faster                                  |
| json                     | 3.10 ms                                                | 2.97 ms: 1.04x faster                                  |
| mdp                      | 1.67 sec                                               | 1.62 sec: 1.03x faster                                 |
| pickle_dict              | 17.8 us                                                | 17.9 us: 1.01x slower                                  |
| telco                    | 3.68 ms                                                | 3.71 ms: 1.01x slower                                  |
| pickle_list              | 2.83 us                                                | 2.89 us: 1.02x slower                                  |
| xml_etree_iterparse      | 72.6 ms                                                | 74.4 ms: 1.02x slower                                  |
| xml_etree_parse          | 107 ms                                                 | 110 ms: 1.03x slower                                   |
| xml_etree_generate       | 54.3 ms                                                | 56.0 ms: 1.03x slower                                  |
| json_loads               | 16.9 us                                                | 17.5 us: 1.04x slower                                  |
| regex_effbot             | 2.45 ms                                                | 2.57 ms: 1.05x slower                                  |
| bench_mp_pool            | 41.0 ms                                                | 44.4 ms: 1.08x slower                                  |
| sqlite_synth             | 1.47 us                                                | 1.61 us: 1.09x slower                                  |
| dask                     | 258 ms                                                 | 316 ms: 1.23x slower                                   |
| unpickle_list            | 2.66 us                                                | 3.27 us: 1.23x slower                                  |
| coverage                 | 40.8 ms                                                | 50.7 ms: 1.24x slower                                  |
| async_generators         | 233 ms                                                 | 306 ms: 1.31x slower                                   |
| Geometric mean           | (ref)                                                  | 1.24x faster                                           |

Benchmark hidden because not significant (4): gc_traversal, pidigits, pickle, pathlib
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
