
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 30a306c
- commit date: 2023-03-25
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-python-main-3.12.0a6+-30a306c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 254 ms: 1.32x faster                                   |
| chameleon      | 9.06 ms                                                | 6.54 ms: 1.39x faster                                  |
| docutils       | 3.17 sec                                               | 2.56 sec: 1.24x faster                                 |
| html5lib       | 85.9 ms                                                | 62.0 ms: 1.39x faster                                  |
| tornado_http   | 127 ms                                                 | 91.2 ms: 1.40x faster                                  |
| Geometric mean | (ref)                                                  | 1.34x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-python-main-3.12.0a6+-30a306c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.5 ms: 1.58x faster                                  |
| float          | 111 ms                                                 | 73.8 ms: 1.50x faster                                  |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.34x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-python-main-3.12.0a6+-30a306c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                  |
| regex_dna      | 222 ms                                                 | 204 ms: 1.09x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.45 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-python-main-3.12.0a6+-30a306c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 287 us: 1.58x faster                                   |
| unpickle_pure_python | 300 us                                                 | 200 us: 1.50x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.58 ms: 1.41x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 56.0 ms: 1.34x faster                                  |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 81.7 ms: 1.15x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 101 ms: 1.11x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                  |
| pickle_list          | 4.56 us                                                | 4.35 us: 1.05x faster                                  |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                  |
| unpickle_list        | 4.82 us                                                | 4.96 us: 1.03x slower                                  |
| pickle_dict          | 27.3 us                                                | 32.3 us: 1.18x slower                                  |
| Geometric mean       | (ref)                                                  | 1.16x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-python-main-3.12.0a6+-30a306c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.86 ms: 1.60x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.54 ms: 1.12x slower                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-python-main-3.12.0a6+-30a306c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.82 ms: 1.50x faster                                  |
| genshi_text     | 30.3 ms                                                | 21.3 ms: 1.43x faster                                  |
| django_template | 45.9 ms                                                | 33.5 ms: 1.37x faster                                  |
| genshi_xml      | 63.3 ms                                                | 48.3 ms: 1.31x faster                                  |
| Geometric mean  | (ref)                                                  | 1.40x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230325-linux-x86_64-python-main-3.12.0a6+-30a306c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.6 ms: 2.59x faster                                  |
| deltablue               | 7.42 ms                                                | 3.21 ms: 2.31x faster                                  |
| asyncio_tcp             | 925 ms                                                 | 504 ms: 1.84x faster                                   |
| logging_silent          | 175 ns                                                 | 97.6 ns: 1.79x faster                                  |
| scimark_sor             | 197 ms                                                 | 112 ms: 1.75x faster                                   |
| richards                | 74.9 ms                                                | 44.0 ms: 1.70x faster                                  |
| go                      | 229 ms                                                 | 137 ms: 1.68x faster                                   |
| spectral_norm           | 150 ms                                                 | 90.9 ms: 1.65x faster                                  |
| pyflate                 | 673 ms                                                 | 410 ms: 1.64x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 65.9 ms: 1.64x faster                                  |
| raytrace                | 464 ms                                                 | 282 ms: 1.64x faster                                   |
| crypto_pyaes            | 118 ms                                                 | 73.2 ms: 1.62x faster                                  |
| chaos                   | 106 ms                                                 | 65.8 ms: 1.62x faster                                  |
| python_startup          | 14.2 ms                                                | 8.86 ms: 1.60x faster                                  |
| hexiom                  | 9.53 ms                                                | 5.99 ms: 1.59x faster                                  |
| pickle_pure_python      | 455 us                                                 | 287 us: 1.58x faster                                   |
| nbody                   | 142 ms                                                 | 89.5 ms: 1.58x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 34.1 us: 1.54x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 42.1 ns: 1.54x faster                                  |
| mako                    | 14.8 ms                                                | 9.82 ms: 1.50x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 200 us: 1.50x faster                                   |
| float                   | 111 ms                                                 | 73.8 ms: 1.50x faster                                  |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.49x faster                                   |
| sqlglot_parse           | 2.06 ms                                                | 1.42 ms: 1.44x faster                                  |
| genshi_text             | 30.3 ms                                                | 21.3 ms: 1.43x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.72 ms: 1.43x faster                                  |
| json_dumps              | 13.5 ms                                                | 9.58 ms: 1.41x faster                                  |
| logging_format          | 8.91 us                                                | 6.32 us: 1.41x faster                                  |
| logging_simple          | 8.07 us                                                | 5.74 us: 1.41x faster                                  |
| tornado_http            | 127 ms                                                 | 91.2 ms: 1.40x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.42 sec: 1.40x faster                                 |
| scimark_fft             | 424 ms                                                 | 305 ms: 1.39x faster                                   |
| html5lib                | 85.9 ms                                                | 62.0 ms: 1.39x faster                                  |
| chameleon               | 9.06 ms                                                | 6.54 ms: 1.39x faster                                  |
| coroutines              | 31.8 ms                                                | 23.0 ms: 1.38x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 692 ms: 1.38x faster                                   |
| async_tree_none         | 717 ms                                                 | 520 ms: 1.38x faster                                   |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                  |
| django_template         | 45.9 ms                                                | 33.5 ms: 1.37x faster                                  |
| async_tree_io           | 1.77 sec                                               | 1.30 sec: 1.37x faster                                 |
| deepcopy                | 442 us                                                 | 328 us: 1.35x faster                                   |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 56.0 ms: 1.34x faster                                  |
| async_tree_memoization  | 854 ms                                                 | 643 ms: 1.33x faster                                   |
| 2to3                    | 336 ms                                                 | 254 ms: 1.32x faster                                   |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.14 ms: 1.32x faster                                  |
| genshi_xml              | 63.3 ms                                                | 48.3 ms: 1.31x faster                                  |
| thrift                  | 1.03 ms                                                | 795 us: 1.30x faster                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 734 ms: 1.30x faster                                   |
| fannkuch                | 486 ms                                                 | 375 ms: 1.29x faster                                   |
| mypy2                   | 428 ms                                                 | 333 ms: 1.29x faster                                   |
| pycparser               | 1.50 sec                                               | 1.18 sec: 1.28x faster                                 |
| deepcopy_reduce         | 3.82 us                                                | 3.00 us: 1.28x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.28x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 51.3 ms: 1.28x faster                                  |
| docutils                | 3.17 sec                                               | 2.56 sec: 1.24x faster                                 |
| nqueens                 | 100 ms                                                 | 82.5 ms: 1.21x faster                                  |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 138 ms: 1.20x faster                                   |
| bench_thread_pool       | 947 us                                                 | 790 us: 1.20x faster                                   |
| dulwich_log             | 75.9 ms                                                | 63.7 ms: 1.19x faster                                  |
| sympy_integrate         | 24.3 ms                                                | 20.5 ms: 1.18x faster                                  |
| json                    | 5.42 ms                                                | 4.59 ms: 1.18x faster                                  |
| sympy_expand            | 545 ms                                                 | 463 ms: 1.18x faster                                   |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.0 ms: 1.18x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 81.7 ms: 1.15x faster                                  |
| sympy_str               | 328 ms                                                 | 285 ms: 1.15x faster                                   |
| comprehensions          | 26.8 us                                                | 23.5 us: 1.14x faster                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                  |
| djangocms               | 35.9 us                                                | 32.0 us: 1.12x faster                                  |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                  |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                  |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                   |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                   |
| mdp                     | 2.82 sec                                               | 2.55 sec: 1.11x faster                                 |
| sqlite_synth            | 2.93 us                                                | 2.65 us: 1.11x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 101 ms: 1.11x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                   |
| regex_dna               | 222 ms                                                 | 204 ms: 1.09x faster                                   |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                  |
| pickle_list             | 4.56 us                                                | 4.35 us: 1.05x faster                                  |
| async_generators        | 425 ms                                                 | 409 ms: 1.04x faster                                   |
| telco                   | 6.54 ms                                                | 6.44 ms: 1.02x faster                                  |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                   |
| pickle                  | 10.3 us                                                | 10.4 us: 1.01x slower                                  |
| gc_traversal            | 3.84 ms                                                | 3.93 ms: 1.02x slower                                  |
| unpickle_list           | 4.82 us                                                | 4.96 us: 1.03x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.45 ms: 1.07x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.54 ms: 1.12x slower                                  |
| pickle_dict             | 27.3 us                                                | 32.3 us: 1.18x slower                                  |
| dask                    | 423 ms                                                 | 514 ms: 1.22x slower                                   |
| coverage                | 72.8 ms                                                | 97.6 ms: 1.34x slower                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x
