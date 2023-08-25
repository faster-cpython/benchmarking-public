
# Results vs. 3.10.4

- fork: python
- ref: ca066bdbed85094a9c4d
- machine: linux-x86_64
- commit hash: ca066bd
- commit date: 2023-03-09
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.33x faster                                                   |
| chameleon      | 9.06 ms                                                | 6.36 ms: 1.42x faster                                                  |
| docutils       | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                 |
| html5lib       | 85.9 ms                                                | 62.1 ms: 1.38x faster                                                  |
| tornado_http   | 127 ms                                                 | 95.1 ms: 1.34x faster                                                  |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 93.1 ms: 1.52x faster                                                  |
| float          | 111 ms                                                 | 74.3 ms: 1.49x faster                                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.15x faster                                                  |
| regex_dna      | 222 ms                                                 | 205 ms: 1.08x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.56 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 286 us: 1.59x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 204 us: 1.47x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.62 ms: 1.41x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 55.7 ms: 1.35x faster                                                  |
| json_loads           | 28.8 us                                                | 24.4 us: 1.18x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 80.9 ms: 1.16x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 101 ms: 1.11x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                   |
| pickle_list          | 4.56 us                                                | 4.16 us: 1.10x faster                                                  |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                                  |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                  |
| unpickle_list        | 4.82 us                                                | 4.97 us: 1.03x slower                                                  |
| pickle_dict          | 27.3 us                                                | 31.0 us: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.01 ms: 1.57x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.54 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.95 ms: 1.48x faster                                                  |
| genshi_text     | 30.3 ms                                                | 21.5 ms: 1.41x faster                                                  |
| django_template | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                  |
| genshi_xml      | 63.3 ms                                                | 48.0 ms: 1.32x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-python-ca066bdbed85094a9c4d-3.12.0a6+-ca066bd |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.6 ms: 2.51x faster                                                  |
| deltablue               | 7.42 ms                                                | 3.27 ms: 2.27x faster                                                  |
| logging_silent          | 175 ns                                                 | 93.6 ns: 1.87x faster                                                  |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                                   |
| asyncio_tcp             | 925 ms                                                 | 507 ms: 1.82x faster                                                   |
| richards                | 74.9 ms                                                | 43.6 ms: 1.72x faster                                                  |
| pyflate                 | 673 ms                                                 | 407 ms: 1.65x faster                                                   |
| go                      | 229 ms                                                 | 140 ms: 1.64x faster                                                   |
| raytrace                | 464 ms                                                 | 288 ms: 1.61x faster                                                   |
| crypto_pyaes            | 118 ms                                                 | 74.2 ms: 1.60x faster                                                  |
| pickle_pure_python      | 455 us                                                 | 286 us: 1.59x faster                                                   |
| spectral_norm           | 150 ms                                                 | 94.3 ms: 1.59x faster                                                  |
| scimark_monte_carlo     | 108 ms                                                 | 68.3 ms: 1.58x faster                                                  |
| python_startup          | 14.2 ms                                                | 9.01 ms: 1.57x faster                                                  |
| chaos                   | 106 ms                                                 | 68.7 ms: 1.55x faster                                                  |
| nbody                   | 142 ms                                                 | 93.1 ms: 1.52x faster                                                  |
| hexiom                  | 9.53 ms                                                | 6.26 ms: 1.52x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 43.0 ns: 1.50x faster                                                  |
| deepcopy_memo           | 52.3 us                                                | 35.0 us: 1.49x faster                                                  |
| float                   | 111 ms                                                 | 74.3 ms: 1.49x faster                                                  |
| mako                    | 14.8 ms                                                | 9.95 ms: 1.48x faster                                                  |
| unpickle_pure_python    | 300 us                                                 | 204 us: 1.47x faster                                                   |
| scimark_lu              | 163 ms                                                 | 113 ms: 1.45x faster                                                   |
| sqlglot_parse           | 2.06 ms                                                | 1.44 ms: 1.43x faster                                                  |
| chameleon               | 9.06 ms                                                | 6.36 ms: 1.42x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                                 |
| sqlglot_transpile       | 2.45 ms                                                | 1.73 ms: 1.41x faster                                                  |
| genshi_text             | 30.3 ms                                                | 21.5 ms: 1.41x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.62 ms: 1.41x faster                                                  |
| pprint_safe_repr        | 955 ms                                                 | 686 ms: 1.39x faster                                                   |
| django_template         | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                  |
| html5lib                | 85.9 ms                                                | 62.1 ms: 1.38x faster                                                  |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                  |
| scimark_fft             | 424 ms                                                 | 309 ms: 1.37x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.37x faster                                                 |
| async_tree_none         | 717 ms                                                 | 524 ms: 1.37x faster                                                   |
| logging_format          | 8.91 us                                                | 6.56 us: 1.36x faster                                                  |
| fannkuch                | 486 ms                                                 | 359 ms: 1.35x faster                                                   |
| coroutines              | 31.8 ms                                                | 23.5 ms: 1.35x faster                                                  |
| logging_simple          | 8.07 us                                                | 5.96 us: 1.35x faster                                                  |
| xml_etree_process       | 74.9 ms                                                | 55.7 ms: 1.35x faster                                                  |
| tornado_http            | 127 ms                                                 | 95.1 ms: 1.34x faster                                                  |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                                  |
| 2to3                    | 336 ms                                                 | 252 ms: 1.33x faster                                                   |
| pycparser               | 1.50 sec                                               | 1.13 sec: 1.33x faster                                                 |
| thrift                  | 1.03 ms                                                | 778 us: 1.33x faster                                                   |
| genshi_xml              | 63.3 ms                                                | 48.0 ms: 1.32x faster                                                  |
| regex_compile           | 177 ms                                                 | 135 ms: 1.31x faster                                                   |
| deepcopy                | 442 us                                                 | 337 us: 1.31x faster                                                   |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 657 ms: 1.30x faster                                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 741 ms: 1.28x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                                  |
| mypy2                   | 428 ms                                                 | 335 ms: 1.28x faster                                                   |
| deepcopy_reduce         | 3.82 us                                                | 3.01 us: 1.27x faster                                                  |
| nqueens                 | 100 ms                                                 | 80.2 ms: 1.25x faster                                                  |
| docutils                | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.55 ms: 1.20x faster                                                  |
| bench_thread_pool       | 947 us                                                 | 791 us: 1.20x faster                                                   |
| sqlalchemy_declarative  | 165 ms                                                 | 139 ms: 1.19x faster                                                   |
| dulwich_log             | 75.9 ms                                                | 63.7 ms: 1.19x faster                                                  |
| json_loads              | 28.8 us                                                | 24.4 us: 1.18x faster                                                  |
| sympy_expand            | 545 ms                                                 | 462 ms: 1.18x faster                                                   |
| sympy_integrate         | 24.3 ms                                                | 20.6 ms: 1.18x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.0 ms: 1.18x faster                                                  |
| json                    | 5.42 ms                                                | 4.63 ms: 1.17x faster                                                  |
| xml_etree_generate      | 94.2 ms                                                | 80.9 ms: 1.16x faster                                                  |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.15x faster                                                  |
| sympy_str               | 328 ms                                                 | 287 ms: 1.14x faster                                                   |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                  |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                  |
| comprehensions          | 26.8 us                                                | 23.9 us: 1.12x faster                                                  |
| sqlite_synth            | 2.93 us                                                | 2.63 us: 1.12x faster                                                  |
| djangocms               | 35.9 us                                                | 32.3 us: 1.11x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                 | 101 ms: 1.11x faster                                                   |
| sympy_sum               | 185 ms                                                 | 167 ms: 1.11x faster                                                   |
| mdp                     | 2.82 sec                                               | 2.55 sec: 1.11x faster                                                 |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                   |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.10x faster                                                   |
| pickle_list             | 4.56 us                                                | 4.16 us: 1.10x faster                                                  |
| gc_traversal            | 3.84 ms                                                | 3.55 ms: 1.08x faster                                                  |
| regex_dna               | 222 ms                                                 | 205 ms: 1.08x faster                                                   |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                                  |
| async_generators        | 425 ms                                                 | 413 ms: 1.03x faster                                                   |
| telco                   | 6.54 ms                                                | 6.50 ms: 1.01x faster                                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                   |
| pickle                  | 10.3 us                                                | 10.5 us: 1.02x slower                                                  |
| unpickle_list           | 4.82 us                                                | 4.97 us: 1.03x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.56 ms: 1.10x slower                                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.54 ms: 1.12x slower                                                  |
| pickle_dict             | 27.3 us                                                | 31.0 us: 1.14x slower                                                  |
| dask                    | 423 ms                                                 | 509 ms: 1.20x slower                                                   |
| coverage                | 72.8 ms                                                | 94.5 ms: 1.30x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.24x
