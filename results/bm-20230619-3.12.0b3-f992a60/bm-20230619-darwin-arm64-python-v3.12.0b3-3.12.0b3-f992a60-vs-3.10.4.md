
# Results vs. 3.10.4

- fork: python
- ref: v3.12.0b3
- machine: darwin-arm64
- commit hash: f992a60
- commit date: 2023-06-19
- overall geometric mean: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-darwin-arm64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 170 ms: 1.19x faster                                       |
| docutils       | 1.78 sec                                               | 1.52 sec: 1.17x faster                                     |
| tornado_http   | 91.9 ms                                                | 70.6 ms: 1.30x faster                                      |
| Geometric mean | (ref)                                                  | 1.22x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-darwin-arm64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 68.8 ms: 1.37x faster                                      |
| float          | 72.3 ms                                                | 56.9 ms: 1.27x faster                                      |
| Geometric mean | (ref)                                                  | 1.20x faster                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-darwin-arm64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 76.2 ms: 1.27x faster                                      |
| regex_v8       | 17.5 ms                                                | 16.3 ms: 1.08x faster                                      |
| regex_dna      | 160 ms                                                 | 156 ms: 1.02x faster                                       |
| regex_effbot   | 2.45 ms                                                | 2.79 ms: 1.14x slower                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-darwin-arm64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 284 us                                                 | 191 us: 1.49x faster                                       |
| unpickle_pure_python | 203 us                                                 | 147 us: 1.39x faster                                       |
| json_dumps           | 8.38 ms                                                | 6.31 ms: 1.33x faster                                      |
| tomli_loads          | 1.76 sec                                               | 1.40 sec: 1.26x faster                                     |
| xml_etree_process    | 45.1 ms                                                | 39.1 ms: 1.15x faster                                      |
| unpickle             | 9.77 us                                                | 9.24 us: 1.06x faster                                      |
| pickle_list          | 2.83 us                                                | 2.86 us: 1.01x slower                                      |
| pickle               | 7.36 us                                                | 7.43 us: 1.01x slower                                      |
| xml_etree_parse      | 107 ms                                                 | 110 ms: 1.03x slower                                       |
| xml_etree_iterparse  | 72.6 ms                                                | 74.9 ms: 1.03x slower                                      |
| pickle_dict          | 17.8 us                                                | 18.5 us: 1.04x slower                                      |
| xml_etree_generate   | 54.3 ms                                                | 56.5 ms: 1.04x slower                                      |
| json_loads           | 16.9 us                                                | 17.6 us: 1.04x slower                                      |
| unpickle_list        | 2.66 us                                                | 3.23 us: 1.21x slower                                      |
| Geometric mean       | (ref)                                                  | 1.08x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-darwin-arm64-python-v3.12.0b3-3.12.0b3-f992a60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.2 ms: 1.04x faster                                      |
| python_startup_no_site | 9.73 ms                                                | 9.95 ms: 1.02x slower                                      |
| Geometric mean         | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-darwin-arm64-python-v3.12.0b3-3.12.0b3-f992a60 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 10.5 ms                                                | 7.56 ms: 1.39x faster                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230619-darwin-arm64-python-v3.12.0b3-3.12.0b3-f992a60 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 344 us                                                 | 90.9 us: 3.79x faster                                      |
| deltablue                | 5.15 ms                                                | 2.42 ms: 2.13x faster                                      |
| richards_super           | 60.7 ms                                                | 34.0 ms: 1.79x faster                                      |
| go                       | 165 ms                                                 | 94.2 ms: 1.75x faster                                      |
| logging_silent           | 119 ns                                                 | 69.3 ns: 1.72x faster                                      |
| richards                 | 51.4 ms                                                | 30.3 ms: 1.70x faster                                      |
| scimark_monte_carlo      | 72.2 ms                                                | 43.4 ms: 1.66x faster                                      |
| mypy2                    | 308 ms                                                 | 191 ms: 1.61x faster                                       |
| sqlglot_parse            | 1.33 ms                                                | 830 us: 1.60x faster                                       |
| chaos                    | 66.8 ms                                                | 41.8 ms: 1.60x faster                                      |
| async_tree_memoization   | 493 ms                                                 | 311 ms: 1.58x faster                                       |
| raytrace                 | 328 ms                                                 | 208 ms: 1.58x faster                                       |
| async_tree_io            | 1.02 sec                                               | 665 ms: 1.53x faster                                       |
| sqlglot_transpile        | 1.54 ms                                                | 1.00 ms: 1.53x faster                                      |
| scimark_lu               | 110 ms                                                 | 72.6 ms: 1.51x faster                                      |
| async_tree_none          | 402 ms                                                 | 266 ms: 1.51x faster                                       |
| asyncio_tcp              | 673 ms                                                 | 445 ms: 1.51x faster                                       |
| crypto_pyaes             | 78.0 ms                                                | 51.9 ms: 1.50x faster                                      |
| hexiom                   | 6.32 ms                                                | 4.24 ms: 1.49x faster                                      |
| pickle_pure_python       | 284 us                                                 | 191 us: 1.49x faster                                       |
| scimark_sor              | 127 ms                                                 | 85.8 ms: 1.48x faster                                      |
| pyflate                  | 453 ms                                                 | 310 ms: 1.47x faster                                       |
| mako                     | 10.5 ms                                                | 7.56 ms: 1.39x faster                                      |
| unpickle_pure_python     | 203 us                                                 | 147 us: 1.39x faster                                       |
| deepcopy_memo            | 34.5 us                                                | 25.0 us: 1.38x faster                                      |
| nbody                    | 94.1 ms                                                | 68.8 ms: 1.37x faster                                      |
| pycparser                | 915 ms                                                 | 675 ms: 1.36x faster                                       |
| json_dumps               | 8.38 ms                                                | 6.31 ms: 1.33x faster                                      |
| unpack_sequence          | 38.7 ns                                                | 29.3 ns: 1.32x faster                                      |
| asyncio_tcp_ssl          | 1.64 sec                                               | 1.25 sec: 1.31x faster                                     |
| tornado_http             | 91.9 ms                                                | 70.6 ms: 1.30x faster                                      |
| sqlalchemy_imperative    | 9.03 ms                                                | 6.94 ms: 1.30x faster                                      |
| spectral_norm            | 96.4 ms                                                | 74.7 ms: 1.29x faster                                      |
| logging_format           | 5.01 us                                                | 3.91 us: 1.28x faster                                      |
| logging_simple           | 4.63 us                                                | 3.62 us: 1.28x faster                                      |
| async_tree_cpu_io_mixed  | 670 ms                                                 | 527 ms: 1.27x faster                                       |
| float                    | 72.3 ms                                                | 56.9 ms: 1.27x faster                                      |
| regex_compile            | 96.6 ms                                                | 76.2 ms: 1.27x faster                                      |
| tomli_loads              | 1.76 sec                                               | 1.40 sec: 1.26x faster                                     |
| create_gc_cycles         | 876 us                                                 | 705 us: 1.24x faster                                       |
| generators               | 32.9 ms                                                | 26.6 ms: 1.24x faster                                      |
| dulwich_log              | 37.1 ms                                                | 30.0 ms: 1.23x faster                                      |
| deepcopy                 | 278 us                                                 | 228 us: 1.22x faster                                       |
| pprint_safe_repr         | 609 ms                                                 | 503 ms: 1.21x faster                                       |
| pprint_pformat           | 1.24 sec                                               | 1.03 sec: 1.21x faster                                     |
| fannkuch                 | 317 ms                                                 | 265 ms: 1.20x faster                                       |
| 2to3                     | 202 ms                                                 | 170 ms: 1.19x faster                                       |
| docutils                 | 1.78 sec                                               | 1.52 sec: 1.17x faster                                     |
| comprehensions           | 17.7 us                                                | 15.1 us: 1.17x faster                                      |
| scimark_fft              | 232 ms                                                 | 201 ms: 1.15x faster                                       |
| xml_etree_process        | 45.1 ms                                                | 39.1 ms: 1.15x faster                                      |
| sqlalchemy_declarative   | 74.8 ms                                                | 65.5 ms: 1.14x faster                                      |
| deepcopy_reduce          | 2.38 us                                                | 2.10 us: 1.14x faster                                      |
| bench_thread_pool        | 548 us                                                 | 484 us: 1.13x faster                                       |
| coroutines               | 20.2 ms                                                | 17.9 ms: 1.13x faster                                      |
| nqueens                  | 68.1 ms                                                | 60.7 ms: 1.12x faster                                      |
| sqlglot_optimize         | 38.0 ms                                                | 34.3 ms: 1.11x faster                                      |
| scimark_sparse_mat_mult  | 3.47 ms                                                | 3.19 ms: 1.09x faster                                      |
| regex_v8                 | 17.5 ms                                                | 16.3 ms: 1.08x faster                                      |
| unpickle                 | 9.77 us                                                | 9.24 us: 1.06x faster                                      |
| meteor_contest           | 78.6 ms                                                | 74.5 ms: 1.06x faster                                      |
| sqlglot_normalize        | 197 ms                                                 | 186 ms: 1.05x faster                                       |
| python_startup           | 12.6 ms                                                | 12.2 ms: 1.04x faster                                      |
| regex_dna                | 160 ms                                                 | 156 ms: 1.02x faster                                       |
| json                     | 3.10 ms                                                | 3.02 ms: 1.02x faster                                      |
| mdp                      | 1.67 sec                                               | 1.64 sec: 1.02x faster                                     |
| gc_traversal             | 2.40 ms                                                | 2.40 ms: 1.00x slower                                      |
| pickle_list              | 2.83 us                                                | 2.86 us: 1.01x slower                                      |
| pickle                   | 7.36 us                                                | 7.43 us: 1.01x slower                                      |
| telco                    | 3.68 ms                                                | 3.73 ms: 1.01x slower                                      |
| python_startup_no_site   | 9.73 ms                                                | 9.95 ms: 1.02x slower                                      |
| xml_etree_parse          | 107 ms                                                 | 110 ms: 1.03x slower                                       |
| xml_etree_iterparse      | 72.6 ms                                                | 74.9 ms: 1.03x slower                                      |
| pickle_dict              | 17.8 us                                                | 18.5 us: 1.04x slower                                      |
| xml_etree_generate       | 54.3 ms                                                | 56.5 ms: 1.04x slower                                      |
| json_loads               | 16.9 us                                                | 17.6 us: 1.04x slower                                      |
| sqlite_synth             | 1.47 us                                                | 1.63 us: 1.11x slower                                      |
| bench_mp_pool            | 41.0 ms                                                | 46.4 ms: 1.13x slower                                      |
| regex_effbot             | 2.45 ms                                                | 2.79 ms: 1.14x slower                                      |
| pathlib                  | 28.8 ms                                                | 33.1 ms: 1.15x slower                                      |
| unpickle_list            | 2.66 us                                                | 3.23 us: 1.21x slower                                      |
| coverage                 | 40.8 ms                                                | 50.5 ms: 1.24x slower                                      |
| dask                     | 258 ms                                                 | 321 ms: 1.24x slower                                       |
| async_generators         | 233 ms                                                 | 309 ms: 1.33x slower                                       |
| Geometric mean           | (ref)                                                  | 1.23x faster                                               |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
