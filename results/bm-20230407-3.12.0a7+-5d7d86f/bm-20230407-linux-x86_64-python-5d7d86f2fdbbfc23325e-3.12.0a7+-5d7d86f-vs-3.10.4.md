
# Results vs. 3.10.4

- fork: python
- ref: 5d7d86f2fdbbfc23325e
- machine: linux-x86_64
- commit hash: 5d7d86f
- commit date: 2023-04-07
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                   |
| chameleon      | 9.06 ms                                                | 6.47 ms: 1.40x faster                                                  |
| docutils       | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                 |
| html5lib       | 85.9 ms                                                | 61.7 ms: 1.39x faster                                                  |
| tornado_http   | 127 ms                                                 | 94.1 ms: 1.35x faster                                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.8 ms: 1.59x faster                                                  |
| float          | 111 ms                                                 | 73.3 ms: 1.51x faster                                                  |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                                   |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                  |
| regex_dna      | 222 ms                                                 | 203 ms: 1.09x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.45 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 286 us: 1.59x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 199 us: 1.51x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.61 ms: 1.41x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 55.4 ms: 1.35x faster                                                  |
| json_loads           | 28.8 us                                                | 24.3 us: 1.18x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 80.0 ms: 1.18x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 99.9 ms: 1.12x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                   |
| pickle_list          | 4.56 us                                                | 4.46 us: 1.02x faster                                                  |
| unpickle             | 14.1 us                                                | 13.9 us: 1.02x faster                                                  |
| unpickle_list        | 4.82 us                                                | 4.99 us: 1.04x slower                                                  |
| pickle               | 10.3 us                                                | 10.8 us: 1.05x slower                                                  |
| pickle_dict          | 27.3 us                                                | 33.0 us: 1.21x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.84 ms: 1.60x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.53 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.1 ms: 1.46x faster                                                  |
| django_template | 45.9 ms                                                | 32.6 ms: 1.41x faster                                                  |
| genshi_text     | 30.3 ms                                                | 21.8 ms: 1.39x faster                                                  |
| genshi_xml      | 63.3 ms                                                | 48.3 ms: 1.31x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230407-linux-x86_64-python-5d7d86f2fdbbfc23325e-3.12.0a7+-5d7d86f |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.3 ms: 2.62x faster                                                  |
| deltablue               | 7.42 ms                                                | 3.22 ms: 2.30x faster                                                  |
| asyncio_tcp             | 925 ms                                                 | 503 ms: 1.84x faster                                                   |
| logging_silent          | 175 ns                                                 | 96.5 ns: 1.82x faster                                                  |
| scimark_sor             | 197 ms                                                 | 112 ms: 1.75x faster                                                   |
| richards                | 74.9 ms                                                | 43.8 ms: 1.71x faster                                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.22 ms: 1.69x faster                                                  |
| go                      | 229 ms                                                 | 139 ms: 1.66x faster                                                   |
| raytrace                | 464 ms                                                 | 281 ms: 1.65x faster                                                   |
| spectral_norm           | 150 ms                                                 | 91.2 ms: 1.64x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.50 ms: 1.63x faster                                                  |
| pyflate                 | 673 ms                                                 | 413 ms: 1.63x faster                                                   |
| scimark_monte_carlo     | 108 ms                                                 | 66.5 ms: 1.63x faster                                                  |
| crypto_pyaes            | 118 ms                                                 | 73.3 ms: 1.62x faster                                                  |
| chaos                   | 106 ms                                                 | 66.2 ms: 1.61x faster                                                  |
| python_startup          | 14.2 ms                                                | 8.84 ms: 1.60x faster                                                  |
| nbody                   | 142 ms                                                 | 88.8 ms: 1.59x faster                                                  |
| pickle_pure_python      | 455 us                                                 | 286 us: 1.59x faster                                                   |
| hexiom                  | 9.53 ms                                                | 5.99 ms: 1.59x faster                                                  |
| scimark_lu              | 163 ms                                                 | 105 ms: 1.55x faster                                                   |
| deepcopy_memo           | 52.3 us                                                | 34.0 us: 1.54x faster                                                  |
| unpickle_pure_python    | 300 us                                                 | 199 us: 1.51x faster                                                   |
| float                   | 111 ms                                                 | 73.3 ms: 1.51x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 43.6 ns: 1.48x faster                                                  |
| mako                    | 14.8 ms                                                | 10.1 ms: 1.46x faster                                                  |
| logging_simple          | 8.07 us                                                | 5.63 us: 1.43x faster                                                  |
| logging_format          | 8.91 us                                                | 6.23 us: 1.43x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.61 ms: 1.41x faster                                                  |
| scimark_fft             | 424 ms                                                 | 301 ms: 1.41x faster                                                   |
| django_template         | 45.9 ms                                                | 32.6 ms: 1.41x faster                                                  |
| async_tree_none         | 717 ms                                                 | 510 ms: 1.41x faster                                                   |
| chameleon               | 9.06 ms                                                | 6.47 ms: 1.40x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.42 sec: 1.40x faster                                                 |
| genshi_text             | 30.3 ms                                                | 21.8 ms: 1.39x faster                                                  |
| html5lib                | 85.9 ms                                                | 61.7 ms: 1.39x faster                                                  |
| coroutines              | 31.8 ms                                                | 22.9 ms: 1.39x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 1.28 sec: 1.39x faster                                                 |
| pprint_safe_repr        | 955 ms                                                 | 692 ms: 1.38x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 619 ms: 1.38x faster                                                   |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                  |
| deepcopy                | 442 us                                                 | 326 us: 1.36x faster                                                   |
| tornado_http            | 127 ms                                                 | 94.1 ms: 1.35x faster                                                  |
| xml_etree_process       | 74.9 ms                                                | 55.4 ms: 1.35x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.05 ms: 1.35x faster                                                  |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                   |
| gunicorn                | 1.46 ms                                                | 1.10 ms: 1.33x faster                                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 719 ms: 1.32x faster                                                   |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                                   |
| thrift                  | 1.03 ms                                                | 784 us: 1.32x faster                                                   |
| genshi_xml              | 63.3 ms                                                | 48.3 ms: 1.31x faster                                                  |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.31x faster                                                 |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.6 ms: 1.29x faster                                                  |
| fannkuch                | 486 ms                                                 | 377 ms: 1.29x faster                                                   |
| mypy2                   | 428 ms                                                 | 334 ms: 1.28x faster                                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.99 us: 1.28x faster                                                  |
| nqueens                 | 100 ms                                                 | 79.4 ms: 1.26x faster                                                  |
| docutils                | 3.17 sec                                               | 2.54 sec: 1.25x faster                                                 |
| comprehensions          | 26.8 us                                                | 21.8 us: 1.23x faster                                                  |
| dulwich_log             | 75.9 ms                                                | 63.0 ms: 1.21x faster                                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                                   |
| bench_thread_pool       | 947 us                                                 | 790 us: 1.20x faster                                                   |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                                  |
| sympy_expand            | 545 ms                                                 | 459 ms: 1.19x faster                                                   |
| json_loads              | 28.8 us                                                | 24.3 us: 1.18x faster                                                  |
| json                    | 5.42 ms                                                | 4.60 ms: 1.18x faster                                                  |
| xml_etree_generate      | 94.2 ms                                                | 80.0 ms: 1.18x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.0 ms: 1.17x faster                                                  |
| sympy_str               | 328 ms                                                 | 283 ms: 1.16x faster                                                   |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                                  |
| regex_v8                | 25.0 ms                                                | 22.3 ms: 1.12x faster                                                  |
| meteor_contest          | 115 ms                                                 | 102 ms: 1.12x faster                                                   |
| sympy_sum               | 185 ms                                                 | 165 ms: 1.12x faster                                                   |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                 | 99.9 ms: 1.12x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.54 sec: 1.11x faster                                                 |
| djangocms               | 35.9 us                                                | 32.4 us: 1.11x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                   |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                                  |
| regex_dna               | 222 ms                                                 | 203 ms: 1.09x faster                                                   |
| async_generators        | 425 ms                                                 | 415 ms: 1.02x faster                                                   |
| pickle_list             | 4.56 us                                                | 4.46 us: 1.02x faster                                                  |
| unpickle                | 14.1 us                                                | 13.9 us: 1.02x faster                                                  |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                   |
| unpickle_list           | 4.82 us                                                | 4.99 us: 1.04x slower                                                  |
| pickle                  | 10.3 us                                                | 10.8 us: 1.05x slower                                                  |
| gc_traversal            | 3.84 ms                                                | 4.07 ms: 1.06x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.45 ms: 1.07x slower                                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.53 ms: 1.12x slower                                                  |
| dask                    | 423 ms                                                 | 500 ms: 1.18x slower                                                   |
| pickle_dict             | 27.3 us                                                | 33.0 us: 1.21x slower                                                  |
| coverage                | 72.8 ms                                                | 95.9 ms: 1.32x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                           |

Benchmark hidden because not significant (2): telco, bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x
